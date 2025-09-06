def enc(plaintext):
    return "".join(
        chr((ord(c) - (base := ord('A') if c.isupper() else ord('a')) + i) % 26 + base) 
        if c.isalpha() else c
        for i, c in enumerate(plaintext)
    )

print(enc("Flag"))
#output: a_up4qr_kaiaf0_bujktaz_qm_su4ux_cpbq_ETZ_rhrudm

