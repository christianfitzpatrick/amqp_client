"""
Mappings for AMQP class methods

Christian Fitzpatrick
"""
import abc
import struct


class AMQPMethod:
    """Base object for AMQP methods to be mapped onto and wrapped by a middleware API"""

    def __init__(self, class_id, method_id):
        self.class_id = class_id
        self.method_id = method_id

    #  0          2           4
    #  +----------+-----------+-------------- - -
    #  | class-id | method-id | arguments...
    #  +----------+-----------+-------------- - -
    #     short      short    ...

    def _pack(self, encoded_args):
        """Pack the fully encoded method data and args into a method frame payload"""
        encoded_class_id = struct.pack(">H", self.class_id)
        encoded_method_id = struct.pack(">H", self.method_id)
        return encoded_class_id + encoded_method_id + encoded_args

    @abc.abstractmethod
    def encode(self):
        """Encode the method data and arguments"""

        raise NotImplementedError


class ConnectionStart(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 10, 10)

    def encode(self):
        pass

class ConnectionStartOk(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 10, 11)

    def encode(self):
        pass

class ConnectionSecure(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 10, 20)

    def encode(self):
        pass

class ConnectionSecureOk(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 10, 21)

    def encode(self):
        pass

class ConnectionTune(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 10, 30)

    def encode(self):
        pass

class ConnectionTuneOk(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 10, 31)

    def encode(self):
        pass

class ConnectionOpen(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 10, 40)

    def encode(self):
        pass

class ConnectionOpenOk(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 10, 41)

    def encode(self):
        pass

class ConnectionClose(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 10, 50)

    def encode(self):
        pass

class ConnectionCloseOk(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 10, 51)

    def encode(self):
        pass

class ConnectionBlocked(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 10, 60)

    def encode(self):
        pass

class ConnectionUnblocked(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 10, 61)

    def encode(self):
        pass

class ConnectionUpdateSecret(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 10, 70)

    def encode(self):
        pass

class ConnectionUpdateSecretOk(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 10, 71)

    def encode(self):
        pass

class ChannelOpen(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 20, 10)

    def encode(self):
        pass

class ChannelOpenOk(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 20, 11)

    def encode(self):
        pass

class ChannelFlow(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 20, 20)

    def encode(self):
        pass

class ChannelFlowOk(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 20, 21)

    def encode(self):
        pass

class ChannelClose(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 20, 40)

    def encode(self):
        pass

class ChannelCloseOk(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 20, 41)

    def encode(self):
        pass

class AccessRequest(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 30, 10)

    def encode(self):
        pass

class AccessRequestOk(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 30, 11)

    def encode(self):
        pass

class ExchangeDeclare(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 40, 10)

    def encode(self):
        pass

class ExchangeDeclareOk(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 40, 11)

    def encode(self):
        pass

class ExchangeDelete(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 40, 20)

    def encode(self):
        pass

class ExchangeDeleteOk(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 40, 21)

    def encode(self):
        pass

class ExchangeBind(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 40, 30)

    def encode(self):
        pass

class ExchangeBindOk(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 40, 31)

    def encode(self):
        pass

class ExchangeUnbind(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 40, 40)

    def encode(self):
        pass

class ExchangeUnbindOk(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 40, 51)

    def encode(self):
        pass

class QueueDeclare(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 50, 10)

    def encode(self):
        pass

class QueueDeclareOk(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 50, 11)

    def encode(self):
        pass

class QueueBind(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 50, 20)

    def encode(self):
        pass

class QueueBindOk(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 50, 21)

    def encode(self):
        pass

class QueuePurge(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 50, 30)

    def encode(self):
        pass

class QueuePurgeOk(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 50, 31)

    def encode(self):
        pass

class QueueDelete(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 50, 40)

    def encode(self):
        pass

class QueueDeleteOk(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 50, 41)

    def encode(self):
        pass

class QueueUnbind(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 50, 50)

    def encode(self):
        pass

class QueueUnbindOk(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 50, 51)

    def encode(self):
        pass

class BasicQos(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 60, 10)

    def encode(self):
        pass

class BasicQosOk(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 60, 11)

    def encode(self):
        pass

class BasicConsume(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 60, 20)

    def encode(self):
        pass

class BasicConsumeOk(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 60, 21)

    def encode(self):
        pass

class BasicCancel(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 60, 30)

    def encode(self):
        pass

class BasicCancelOk(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 60, 31)

    def encode(self):
        pass

class BasicPublish(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 60, 40)

    def encode(self):
        pass

class BasicReturn(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 60, 50)

    def encode(self):
        pass

class BasicDeliver(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 60, 60)

    def encode(self):
        pass

class BasicGet(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 60, 70)

    def encode(self):
        pass

class BasicGetOk(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 60, 71)

    def encode(self):
        pass

class BasicGetEmpty(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 60, 72)

    def encode(self):
        pass

class BasicAck(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 60, 80)

    def encode(self):
        pass

class BasicReject(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 60, 90)

    def encode(self):
        pass

class BasicRecoverAsync(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 60, 100)

    def encode(self):
        pass

class BasicRecover(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 60, 110)

    def encode(self):
        pass

class BasicRecoverOk(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 60, 111)

    def encode(self):
        pass

class BasicNack(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 60, 120)

    def encode(self):
        pass

class TxSelect(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 90, 10)

    def encode(self):
        pass

class TxSelectOk(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 90, 11)

    def encode(self):
        pass

class TxCommit(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 90, 20)

    def encode(self):
        pass

class TxCommitOk(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 90, 21)

    def encode(self):
        pass

class TxRollback(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 90, 30)

    def encode(self):
        pass

class TxRollbackOk(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 90, 31)

    def encode(self):
        pass

class ConfirmSelect(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 85, 10)

    def encode(self):
        pass

class ConfirmSelectOk(AMQPMethod):
    def __init__(self):
        AMQPMethod.__init__(self, 85, 11)

    def encode(self):
        pass
