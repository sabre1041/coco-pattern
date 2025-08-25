#!/usr/bin/env python3

import gzip
import sys


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 gzipper.py <file_to_gzip> <gzipped_file_name>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        # Read the input file
        with open(input_file, "rb") as f_in:
            data = f_in.read()

        # Compress and write to output file
        with gzip.open(output_file, "wb") as f_out:
            f_out.write(data)

        print(f"Successfully compressed '{input_file}' to '{output_file}'")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
