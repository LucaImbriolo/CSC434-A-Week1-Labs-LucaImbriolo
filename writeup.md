# Buffer Overflow Handout – CSC434 (Week 1)

## Task 1 – Vulnerable “string-like copy” calls

The handout shows examples where input is copied into a fixed-size buffer without enforcing the buffer size.  
This is what causes a **stack buffer overflow**.

### Example 1 (Stack buffer overflow section)

```c
char name[100];
read(0, name, 0x100);
```

This is vulnerable because the buffer is **100 bytes**, but the program reads **0x100 bytes (256 bytes)**.  
That extra data can overwrite nearby stack values like the `secret` variable and even the saved return address.

### Example 2 (ROP section)

```c
char echo[100];
read(0, echo, 1000);
```

This is vulnerable because 1000 bytes can overflow the 100-byte buffer, leading to stack corruption.

---

## Task 2 – Bytes needed to reach the saved return address

The stack layout is typically:

- Local buffer
- Other local variables
- Saved frame pointer (EBP/RBP)
- Saved return address (EIP/RIP)

In the handout example, the payload offset is:

- 100 bytes for `name`
- 4 bytes for `secret`
- 4 bytes for saved EBP

So:

**100 + 4 + 4 = 108 bytes**

This means the return address overwrite begins at **108 bytes**.

---

## Task 3 – Python payload generator script

I wrote a Python script that generates a payload file in the same structure as the handout’s demonstration:

- Padding up to the return address
- Placeholder overwrite bytes

Example command:

```bash
python3 payload.py --offset 108 --arch 32 --out payload.bin
```

This produces a binary payload file and prints output to show completeness.

---

## Task 4 – How the payload executes + mitigations

### How stack smashing works

1. Program reads more bytes than the buffer can hold.
2. Overflow overwrites adjacent stack data.
3. Eventually the saved return address is overwritten.
4. When the function returns, execution jumps to the attacker-controlled address.

### Developer mitigations

- Input bounds checking / safer functions
- Stack canaries
- ASLR (address randomization)
- NX / DEP (non-executable stack)
- Compiler hardening (PIE, RELRO, etc.)

---
