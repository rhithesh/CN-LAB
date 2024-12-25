import time
import random

def leaky_bucket(packets, bucket_size, output_rate):
    remaining = 0  # Bytes remaining in the bucket

    for packet in packets:
        if packet > bucket_size:
            print(f"Packet of size {packet} bytes exceeds bucket capacity ({bucket_size} bytes) - REJECTED")
        elif packet + remaining > bucket_size:
            print(f"Bucket capacity exceeded with packet size {packet} bytes - REJECTED")
        else:
            remaining += packet
            print(f"\nPacket of size {packet} bytes added to bucket")
            print(f"Bytes in bucket: {remaining}")

            # Transmit data from the bucket
            while remaining > 0:
                time.sleep(1)  # Simulate time for transmission
                if remaining <= output_rate:
                    print(f"Transmitting {remaining} bytes")
                    remaining = 0
                else:
                    print(f"Transmitting {output_rate} bytes")
                    remaining -= output_rate
                print(f"Bytes remaining in bucket: {remaining}")

if __name__ == "__main__":
    # Generate random packet sizes
    packets = [random.randint(1, 100) for _ in range(5)]
    print(f"Generated packets: {packets}")

    # Get bucket size and output rate from the user
    bucket_size = int(input("Enter bucket size: "))
    output_rate = int(input("Enter output rate: "))

    # Simulate leaky bucket
    leaky_bucket(packets, bucket_size, output_rate)
