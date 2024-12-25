def crc(data, gen_poly):
    """
    Calculates the CRC checksum for the given data and generator polynomial.

    Args:
        data: The input data as a binary string.
        gen_poly: The generator polynomial as a binary string.

    Returns:
        The CRC checksum as a binary string.
    """

    padded_data = data + '0' * (len(gen_poly) - 1)
    check_value = padded_data[:len(gen_poly)]

    for _ in range(len(data)):
        if check_value[0] == '1':
            check_value = xor(check_value, gen_poly)
        check_value = check_value[1:] + (padded_data[len(gen_poly) + _] if len(gen_poly) + _ < len(padded_data) else '0')

    return check_value[1:]


def xor(a, b):
    """
    Performs bitwise XOR operation on two binary strings.

    Args:
        a: The first binary string.
        b: The second binary string.

    Returns:
        The result of XOR operation as a binary string.
    """
    return ''.join('0' if x == y else '1' for x, y in zip(a, b))


if __name__ == "__main__":
    data = input("Enter data: ")
    gen_poly = input("Enter generator polynomial: ")

    # Calculate CRC
    crc_value = crc(data, gen_poly)
    print("CRC:", crc_value)

    # Transmit data with CRC
    transmitted_data = data + crc_value
    print("Transmitted Data:", transmitted_data)

    # Receive data
    received_data = input("Enter received data: ")

    # Check for errors
    remainder = crc(received_data, gen_poly)
    print("No Error" if remainder == '0' * (len(gen_poly) - 1) else "Error detected")