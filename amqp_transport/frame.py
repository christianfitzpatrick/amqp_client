"""
AMQP frames and related marshaling/unmarshaling utilities


Christian Fitzpatrick
"""

import enum
import abc
import struct

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


class Frame:
    """Base class for all AMQP frame types

    :param frame_type: AMQP defined contant for frame type
    :param channel_number: the channel the frame belongs to
    """

    def __init__(self, frame_type: FrameType, channel_number: int):
        self.frame_type = frame_type
        self.channel_number = channel_number

    def _marshal(self, encoded_payload):
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

        header = struct.pack(">BHI", self.frame_type, self.channel_number, payload_size)

        return header + payload + FRAME_END_BYTE

    @abc.abstractmethod
    def encode_payload(self):
        """Encode the payload of the particular frame type

        MUST be implemented for EACH frame type
        """

        raise NotImplementedError
