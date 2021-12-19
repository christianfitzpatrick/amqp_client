"""
AMQP frames and related marshaling/unmarshaling utilities


Christian Fitzpatrick
"""

import enum
import abc
import struct
from amqp_transport.amqp_method import AMQPMethod

# For AMQP version 0-9-1, ONLY
PROTOCOL_HEADER_FRAME = b"AMQP" + struct.pack("BBBB", 0, 0, 9, 1)


# AMQP defined end-byte marker for frames
FRAME_END_BYTE = bytes(206)


class FrameType(enum.Enum):
    """AMQP defined constants for frame types"""

    FRAME_METHOD = 1
    FRAME_HEADER = 2
    FRAME_BODY = 3
    FRAME_HEARTBEAT = 8

    def __eq__(self, other) -> bool:
        return self.value == other


class Frame:
    """Base class for all AMQP frame types

    :param frame_type: AMQP defined contant for frame type
    :param channel_number: the channel the frame belongs to
    """

    def __init__(self, frame_type: FrameType, channel_number: int):
        self.frame_type = frame_type
        self.channel_number = channel_number

    def _pack(self, encoded_payload):
        """Pack the fully encoded frame data into a wire-level format for RPC transmission

        The encoding of the payload is implemented by each specific frame type instance

        :param encoded_payload: the encoded payload contents for the frame
        """

        payload = b"".join(encoded_payload)
        payload_size = len(payload)

        # [-------- FRAME HEADER --------]
        #
        # 0      1         3             7                  size+7 size+8
        # +------+---------+-------------+  +------------+  +-----------+
        # | type | channel |     size    |  |  payload   |  | frame-end |
        # +------+---------+-------------+  +------------+  +-----------+
        # octet   short         long         size octets       octet

        header = struct.pack(">BHL", self.frame_type, self.channel_number, payload_size)

        return header + payload + FRAME_END_BYTE

    @abc.abstractmethod
    def marshal(self):
        """Encode the payload of the particular frame type, completing the marshaling process

        MUST be implemented for EACH frame type
        """

        raise NotImplementedError


class MethodFrame(Frame):
    """AMQP method frame"""

    def __init__(self, channel_number: int, method: AMQPMethod):
        Frame.__init__(self, FrameType.FRAME_METHOD, channel_number)
        self.method = method

    def marshal(self):
        body = self.method.encode()
        return self._pack(body)


def is_protocol_header(bytes_read: bytes):
    """Check if a a byte stream is an AMQP protocol header frame

    :param bytes_read: data read from a socket
    """
    _bytes = struct.unpack("ccccBBBB", bytes_read)
    return b"AMQP" == b"".join(list(_bytes)[:4])


def parse_frame_header(data):
    """Parse the components of a generic frame header
    :param data: raw frame header data (7 bytes)

    :returns: (frame_type, frame_channel, payload_size)
    """
    return struct.unpack(">BHL", data)


def read_frame(socket_data: bytes):
    """Build an AMQP frame from raw socket data

    :param socket_data: contents of raw socket read

    @FromSpec: 2.3.5 Frame Details
    Consider implementing a read-ahead buffering to reduce syscall overhead
    """
    if is_protocol_header(socket_data):
        return PROTOCOL_HEADER_FRAME

    frame_total_size = len(socket_data)

    # "Magic number": sizeof(octet + short + long)
    frame_header_size = 7
    frame_header = socket_data[0:frame_header_size]

    # Build the frame header
    frame_type, frame_channel, payload_size = parse_frame_header(frame_header)

    # Extract frame payload
    payload = socket_data[frame_header_size : frame_total_size - 1]

    # Match on frame type and build out a frame of corresponding type
    match frame_type:
        case FrameType.FRAME_METHOD:
            class_id, method_id = struct.unpack(">HH", payload[0:4])
            method = AMQPMethod(class_id, method_id)

        case FrameType.FRAME_HEADER:
            pass
        case FrameType.FRAME_BODY:
            pass
        case FrameType.FRAME_HEARTBEAT:
            pass
