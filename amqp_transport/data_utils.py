"""Encoding/decoding utilities for AMQP types

Christian Fitzpatrick
"""
import struct
from typing import List
from datetime import datetime

DataBuffer = List[bytes]

# The procedures for encoding resemble C-style I/O syscalls
# Parameters: The data to encode and the buffer to write the result to
# On success, return the number of bytes written to the buffer (including the tag type char)
# TODO: On failure, raise an appropriate exception


def encode_shortstr(data: str, buffer: DataBuffer) -> int:
    """Encode an AMQP short string and write the result to a buffer

    :param data: The data to encode into a shortstr
    :param buffer: The buffer to write the encoded data into

    @FromSpec 4.2.5.3:
    length   -> 8-bit unsigned int
    contents -> [0 - 255] octets of UTF-8 data
    """
    encoded_contents = data.encode("utf-8")
    content_len = len(encoded_contents)

    # Check the length constraint
    if content_len > 255:
        return -1

    # Build the wire-level representation of a shortstr
    encoded_len = struct.pack("B", content_len)
    encoded_shortstr = encoded_len + encoded_contents

    # Write the shortstr representation to the buffer
    buffer.append(encoded_shortstr)
    return len(encoded_contents) + 1


def decode_shortstr(data: bytes):
    """Decode a byte stream into an AMQP short string"""
    len_shortstr = struct.unpack_from("B", data, 0)[0]
    shortstr_content = data[1 : len_shortstr + 1]
    decoded_content = shortstr_content.decode("utf-8")
    return decoded_content


def encode_longstr(data: str, buffer: DataBuffer) -> int:
    """Encode an AMQP long string and write to buffer

    returns the number of bytes written, including the type tag char
    """
    encoded_contents = data.encode("utf-8")
    conten_len = len(encoded_contents)
    encoded_len = struct.pack("I", conten_len)
    encoded_longstr = encoded_len + encoded_contents
    buffer.append(encoded_longstr)
    return len(encoded_contents) + 1


def decode_longstr(data: bytes):
    """Decode a byte stream into an AMQP long string"""
    len_longstr = struct.unpack_from("I", data, 0)[0]
    longstr_content = data[4 : len_longstr + 4]
    decoded_content = longstr_content.decode("utf-8")
    return decoded_content


def encode_bool(data, buffer: DataBuffer) -> int:
    """Encode an AMQP boolean"""
    encoded = struct.pack(">cB", b"t", int(data))
    buffer.append(encoded)
    return 2


def decode_bool(data: bytes):
    """Decode an AMQP boolean"""
    decoded = struct.unpack(">cB", data)[1]
    return bool(decoded)


def encode_timestamp(data, buffer: DataBuffer) -> int:
    """Encode an AMQP timestamp

    POSIX timestamps represented as 64-bit long long uints
    Accuracy to the second, as per the integer cast
    """
    encoded = struct.pack(">cQ", b"T", int(data))
    buffer.append(encoded)
    return 9


def decode_timestamp(data: bytes):
    """Decode a byte stream into a timestamp"""
    as_int = struct.unpack(">cQ", data)[1]
    decoded = datetime.fromtimestamp(as_int)
    return decoded


def encode_octet(data: int, buffer: DataBuffer):
    """Encode an AMQP octet

    NOTE:
    Spec  doesn't provide a format specifier, so `o` was chosen
    """
    encoded = struct.pack(">cB", data)
    buffer.append(encoded)
    return 2


def decode_octet(data: bytes):
    """Decode a byte stream into an AMQP octet"""
    decoded = struct.unpack(">cB", data)[1]
    return decoded


def encode_short_uint(data: int, buffer: DataBuffer) -> int:
    """Encode an AMQP short unsigned int"""
    encoded = struct.pack(">cH", b"u", data)
    buffer.append(encoded)
    return 3


def decode_short_uint(data: bytes):
    """Decode a byte stream into an AMQP short unsigned int"""
    decoded = struct.unpack(">cH", data)[1]
    return decoded


def encode_long_uint(data: int, buffer: DataBuffer) -> int:
    "Encode an AMQP long unsigned int" ""
    encoded = struct.pack(">cI", b"i", data)
    buffer.append(encoded)
    return 5


def decode_long_uint(data: bytes):
    """Decode a byte stream into an AMQP long unsigned int"""
    decoded = struct.unpack(">cI", data)[1]
    return decoded


def encode_long_long_uint(data: int, buffer: DataBuffer) -> int:
    """Encode an AMQP long long unsigned int"""
    encoded = struct.pack(">cQ", b"l", data)
    buffer.append(encoded)
    return 9


def decode_long_long_uint(data: bytes):
    """Decode a byte stream into an AMQP long long unsigned int"""
    decoded = struct.unpack(">cQ", data)[1]
    return decoded


def encode_none(buffer: DataBuffer) -> int:
    """Encodes a Python None instance into an empty AMQP field"""
    encoded = struct.pack(">c", b"V")
    buffer.append(encoded)
    return 1


def type_tag(data: bytes) -> str:
    """Grab the type tag from an encoded AMQP instance"""
    return struct.unpack_from(">c", data, 0)[0]
