#!/usr/bin/env python3
"""
CSC434 Buffer Overflow Handout – Payload Generator (Week 1)
"""

import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--offset", type=int, default=108,
                        help="Number of bytes to reach saved return address (handout example uses 108)")
    parser.add_argument("--arch", choices=["32", "64"], default="32",
                        help="Architecture width for overwrite size")
    parser.add_argument("--out", default="payload.bin",
                        help="Output payload filename")

    args = parser.parse_args()

    padding = b"A" * args.offset

    if args.arch == "32":
        overwrite = b"BBBB"   # 4-byte placeholder overwrite
    else:
        overwrite = b"B" * 8  # 8-byte placeholder overwrite

    payload_data = padding + overwrite

    out_path = Path(args.out)
    out_path.write_bytes(payload_data)

    print(f"[+] Payload written to {out_path}")
    print(f"[+] Total bytes: {len(payload_data)}")
    print(f"[+] Offset used: {args.offset}")

if __name__ == "__main__":
    main()
