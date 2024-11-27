import sys

def decode_unsigned_varint(hex_string):
    """Decode an unsigned varint from a hexadecimal string."""
    if hex_string.startswith("0x") or hex_string.startswith("0X"):
        hex_string = hex_string[2:]  # Remove the "0x" prefix
    else:
        raise ValueError("Hexadecimal input must start with '0x'.")
    
    bytes_data = bytes.fromhex(hex_string)
    result = 0
    shift = 0

    for i, byte in enumerate(bytes_data):
        # Extract the lower 7 bits and add to the result
        value = byte & 0x7F
        result |= value << shift

        # Check the MSB to determine if more bytes follow
        if not (byte & 0x80):
            break

        shift += 7

        # Safety check to avoid infinite loops on malformed input
        if shift >= 64:  # Maximum 64 bits supported
            raise ValueError(f"Varint too long at byte index {i}")

    return result


def decode_signed_varint_32_from_unsigned(unsigned_value):
    """
    Decode a signed 32-bit varint from an unsigned 32-bit varint.
    This assumes the value has been truncated to 32 bits after decoding as an unsigned varint.
    """
    # Truncate to 32 bits
    truncated_value = unsigned_value & 0xFFFFFFFF

    # Interpret as a signed 32-bit value
    if truncated_value & (1 << 31):  # Check if the MSB is set
        signed_value = truncated_value - (1 << 32)  # Convert to negative in two's complement
    else:
        signed_value = truncated_value

    return signed_value


def encode_unsigned_varint(value):
    """Encode an unsigned integer into varint hexadecimal format."""
    result = bytearray()
    while value > 0x7F:
        result.append((value & 0x7F) | 0x80)
        value >>= 7
    result.append(value & 0x7F)
    return result.hex().upper()


def main():
    # Check for command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python script.py <0xHEX or unsigned varint>")
        sys.exit(1)

    input_value = sys.argv[1]

    try:
        # Check if the input is numeric
        if input_value.isdigit():
            # Assume the input is an unsigned varint value
            unsigned_value = int(input_value)
            print(f"Unsigned Varint Input: {unsigned_value}")

            # Encode to hexadecimal
            encoded_hex = encode_unsigned_varint(unsigned_value)
            print(f"Encoded Hexadecimal: 0x{encoded_hex}")

            # Decode as signed varint
            signed_value = decode_signed_varint_32_from_unsigned(unsigned_value)
            print(f"Decoded Signed Varint (32-bit): {signed_value}")

        elif input_value.startswith("0x") or input_value.startswith("0X"):
            # Decode as hexadecimal input
            print(f"Hexadecimal Input: {input_value}")
            unsigned_value = decode_unsigned_varint(input_value)
            signed_value = decode_signed_varint_32_from_unsigned(unsigned_value)
            print(f"Decoded Unsigned Varint: {unsigned_value}")
            print(f"Decoded Signed Varint (32-bit): {signed_value}")

        else:
            print("Error: Hexadecimal inputs must start with '0x' or input must be an unsigned varint.")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
