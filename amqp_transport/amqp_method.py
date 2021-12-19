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
