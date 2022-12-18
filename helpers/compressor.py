#
# Compressor using LZ77 algorithm
#
# Author: David A. Mahrous | @x3non_c0der (Github)
# Date: 2022-12-10 03:20:14
#
# Path: helpers\compressor.py

import logging
from typing import List, Tuple

def compress(payload: str, max_offset: int = 2047, max_length: int = 31, path: str = None):
    # Create the input
    input_array = str(payload[:])

    # Create a string of the characters which have been passed
    window = ""

    ## Store output in this list
    output = []

    # Loop through the input string
    while input_array != "":
        length, offset = best_length_offset(window, input_array, max_length, max_offset)
        output.append((offset, length, input_array[0]))
        window += input_array[:length]
        input_array = input_array[length:]


    if path is not None:
        with open (path, "wb") as f:
            # Convert to bytes
            f.write(to_bytes(output))

    return output

def decompress(path) -> str:
    input_array: List[Tuple[int, int, str]] = None
    output = ""

    try:
        with open(path, "rb") as f:
            input_array = from_bytes(bytearray(f.read()))
    except FileNotFoundError:
        raise
    except Exception:
        raise

    for value in input_array:
        offset, length, char = value

        if length == 0:
            if char is not None:
                output += char
        else:
            if offset == 0:
                if char is not None:
                    output += char
                    length -= 1
                    offset = 1
            start_index = len(output) - offset
            for i in range(length):
                output += output[start_index + i]

    return output

def to_bytes(compressed_representation: [(int, int, str)], offset_bits: int = 11, length_bits: int = 5,) -> bytearray:
    # Create a bytearray to store the output
    output = bytearray()

    offset_length_bytes = int((offset_bits + length_bits) / 8)

    for value in compressed_representation:
        offset, length, char = value

        offset_length_value = (offset << length_bits) + length

        for count in range(offset_length_bytes):
            output.append((offset_length_value >> (8 * (offset_length_bytes - count - 1))) & (0b11111111))

        if char is not None:
            if offset == 0:
                output.append(ord(char))
        else:
            output.append(0)

    return output

def from_bytes(compressed_bytes: bytearray, offset_bits: int = 11, length_bits: int = 5,) -> [(int, int, str)]:
    offset_length_bytes = int((offset_bits + length_bits) / 8)

    output = []

    while len(compressed_bytes) > 0:
        offset_length_value = 0
        for _ in range(offset_length_bytes):
            offset_length_value = (offset_length_value * 256) + int(compressed_bytes.pop(0))

        offset = offset_length_value >> length_bits
        length = offset_length_value & ((2 ** length_bits) - 1)

        if offset > 0:
            char_out = None
        else:
            # Get the next character and convert to an ascii character
            char_out = str(chr(compressed_bytes.pop(0)))

        output.append((offset, length, char_out))

    return output

def best_length_offset(window: str, input_string: str, max_length: int = 15, max_offset: int = 4095) -> (int, int):
    if max_offset < len(window):
        cut_window = window[-max_offset:]
    else:
        cut_window = window

    # Return (0, 0) if the string provided is empty
    if input_string is None or input_string == "":
        return (0, 0)

    # Initialise result parameters - best case so far
    length, offset = (1, 0)

    # This should also catch the empty window case
    if input_string[0] not in cut_window:
        best_length = repeating_length_from_start(input_string[0], input_string[1:])
        return (min((length + best_length), max_length), offset)

    # Best length now zero to allow occurrences to take priority
    length = 0

    # Loop through the window
    for index in range(1, (len(cut_window) + 1)):

        # Get the character at this offset
        char = cut_window[-index]
        if char == input_string[0]:
            # Get the length of the match
            found_offset = index

            # Collect any further strings which can be found
            found_length = repeating_length_from_start(cut_window[-index:], input_string)

            # If the length is greater than the current best, update the best
            if found_length > length:
                length = found_length
                offset = found_offset

    # Return the best length and offset
    return (min(length, max_length), offset)


def repeating_length_from_start(window: str, input_string: str) -> int:
    # Return 0 if the string provided is empty or the window is empty
    if window == "" or input_string == "":
        return 0
    elif window[0] == input_string[0]:
        return 1 + repeating_length_from_start(window[1:] + input_string[0], input_string[1:])
    else:
        return 0
