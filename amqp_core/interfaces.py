"""
Base classes for the library's implementations of stateful AMQP objects

The AMQP spec defines channels as the conduit for communicating and negotiating connections
with brokers, so a ChannelWriter interface is provided for wrapper classes to implement

Christian Fitzpatrick
"""
import enum


class STATES(enum.Enum):
    """Connection/channel states"""

    CLOSED = 0
    CLOSING = 1
    OPEN = 2
    OPENING = 3


class ChannelWriter:
    """Interface providing methods that map to AMQP commands through RPC transport

    :param channel: AMQP channel
    """

    def __init__(self, channel):
        self.channel = channel

    def _exec_rpc(self, command_frame):
        """Execute the backing RPC call for the AMQP command encapsulated by the frame"""


class AMQPClass(ChannelWriter):
    """Base class for each of the AMQP classes in its command architecture
    Provides AMQP class instances with channel write capabilities

    :param channel: AMQP channel
    """

    def __init__(self, channel, name):
        super().__init__(channel)
        self.name = name


class AMQPStatefulInstance:
    """Base instance for an AMQP class that carries connection/channel oriented state"""

    def __init__(self):
        self._state = STATES.CLOSED


class AMQPChannel(AMQPStatefulInstance):
    """Base class of an AMQP channel"""

    def __init__(self):
        super().__init__()
