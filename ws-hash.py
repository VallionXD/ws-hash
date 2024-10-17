# ws-hash.py - vallionxd 2024
def ws256(message):
    K = [
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
        0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
        0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
        0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
        0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
        0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
        0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
        0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
        0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
        0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
        0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
        0x19b4c79b, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
        0x391c0cb3, 0x4ed8aa11, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
        0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
    ]

    H = [
        0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
        0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
    ]

    bytes = message.encode('utf-8')
    original_byte_length = len(bytes)
    original_bit_length = original_byte_length * 8

    padded_length = ((original_byte_length + 1 + 8) // 64 + 1) * 64
    padded_bytes = bytearray(padded_length)
    padded_bytes[:original_byte_length] = bytes
    padded_bytes[original_byte_length] = 0x80

    padded_bytes[-8:] = original_bit_length.to_bytes(8, byteorder='big')

    for offset in range(0, padded_length, 64):
        chunk = padded_bytes[offset:offset + 64]
        W = [0] * 64

        for i in range(16):
            W[i] = (chunk[i * 4] << 24) | (chunk[i * 4 + 1] << 16) | (chunk[i * 4 + 2] << 8) | chunk[i * 4 + 3]

        for i in range(16, 64):
            s0 = ((W[i - 15] >> 7) | (W[i - 15] << (32 - 7))) ^ ((W[i - 15] >> 18) | (W[i - 15] << (32 - 18))) ^ (W[i - 15] >> 3)
            s1 = ((W[i - 2] >> 17) | (W[i - 2] << (32 - 17))) ^ ((W[i - 2] >> 19) | (W[i - 2] << (32 - 19))) ^ (W[i - 2] >> 10)
            W[i] = (W[i - 16] + s0 + W[i - 7] + s1) & 0xFFFFFFFF

        a, b, c, d, e, f, g, h = H

        for i in range(64):
            S1 = ((e >> 6) | (e << (32 - 6))) ^ ((e >> 11) | (e << (32 - 11))) ^ ((e >> 25) | (e << (32 - 25)))
            ch = (e & f) ^ (~e & g)
            temp1 = (h + S1 + ch + K[i] + W[i]) & 0xFFFFFFFF
            S0 = ((a >> 2) | (a << (32 - 2))) ^ ((a >> 13) | (a << (32 - 13))) ^ ((a >> 22) | (a << (32 - 22)))
            maj = (a & b) ^ (a & c) ^ (b & c)
            temp2 = (S0 + maj) & 0xFFFFFFFF

            h = g
            g = f
            f = e
            e = (d + temp1) & 0xFFFFFFFF
            d = c
            c = b
            b = a
            a = (temp1 + temp2) & 0xFFFFFFFF

        H[0] = (H[0] + a) & 0xFFFFFFFF
        H[1] = (H[1] + b) & 0xFFFFFFFF
        H[2] = (H[2] + c) & 0xFFFFFFFF
        H[3] = (H[3] + d) & 0xFFFFFFFF
        H[4] = (H[4] + e) & 0xFFFFFFFF
        H[5] = (H[5] + f) & 0xFFFFFFFF
        H[6] = (H[6] + g) & 0xFFFFFFFF
        H[7] = (H[7] + h) & 0xFFFFFFFF

    hash_value = bytearray(32)
    for i in range(8):
        hash_value[i * 4:i * 4 + 4] = H[i].to_bytes(4, byteorder='big')

    return hash_value.hex()

def ws512(message):
    K = [
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
        0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
        0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
        0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
        0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
        0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
        0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
        0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
        0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
        0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
        0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
        0x19b4c79b, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
        0x391c0cb3, 0x4ed8aa11, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
        0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
    ] * 2  

    H = [
        0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
        0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
    ] * 2  

    bytes = message.encode('utf-8')
    original_byte_length = len(bytes)
    original_bit_length = original_byte_length * 8

    padded_length = ((original_byte_length + 1 + 16) // 128 + 1) * 128
    padded_bytes = bytearray(padded_length)
    padded_bytes[:original_byte_length] = bytes
    padded_bytes[original_byte_length] = 0x80

    padded_bytes[-16:] = original_bit_length.to_bytes(16, byteorder='big')

    for offset in range(0, padded_length, 128):
        chunk = padded_bytes[offset:offset + 128]
        W = [0] * 128

        for i in range(32):
            W[i] = (chunk[i * 4] << 24) | (chunk[i * 4 + 1] << 16) | (chunk[i * 4 + 2] << 8) | chunk[i * 4 + 3]

        for i in range(32, 128):
            s0 = ((W[i - 15] >> 7) | (W[i - 15] << (32 - 7))) ^ ((W[i - 15] >> 18) | (W[i - 15] << (32 - 18))) ^ (W[i - 15] >> 3)
            s1 = ((W[i - 2] >> 17) | (W[i - 2] << (32 - 17))) ^ ((W[i - 2] >> 19) | (W[i - 2] << (32 - 19))) ^ (W[i - 2] >> 10)
            W[i] = (W[i - 16] + s0 + W[i - 7] + s1) & 0xFFFFFFFF

        a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p = H

        for i in range(128):
            S1 = ((e >> 6) | (e << (32 - 6))) ^ ((e >> 11) | (e << (32 - 11))) ^ ((e >> 25) | (e << (32 - 25)))
            ch = (e & f) ^ (~e & g)
            temp1 = (h + S1 + ch + K[i] + W[i]) & 0xFFFFFFFF
            S0 = ((a >> 2) | (a << (32 - 2))) ^ ((a >> 13) | (a << (32 - 13))) ^ ((a >> 22) | (a << (32 - 22)))
            maj = (a & b) ^ (a & c) ^ (b & c)
            temp2 = (S0 + maj) & 0xFFFFFFFF

            h = g
            g = f
            f = e
            e = (d + temp1) & 0xFFFFFFFF
            d = c
            c = b
            b = a
            a = (temp1 + temp2) & 0xFFFFFFFF

        H[0] = (H[0] + a) & 0xFFFFFFFF
        H[1] = (H[1] + b) & 0xFFFFFFFF
        H[2] = (H[2] + c) & 0xFFFFFFFF
        H[3] = (H[3] + d) & 0xFFFFFFFF
        H[4] = (H[4] + e) & 0xFFFFFFFF
        H[5] = (H[5] + f) & 0xFFFFFFFF
        H[6] = (H[6] + g) & 0xFFFFFFFF
        H[7] = (H[7] + h) & 0xFFFFFFFF
        H[8] = (H[8] + i) & 0xFFFFFFFF
        H[9] = (H[9] + j) & 0xFFFFFFFF
        H[10] = (H[10] + k) & 0xFFFFFFFF
        H[11] = (H[11] + l) & 0xFFFFFFFF
        H[12] = (H[12] + m) & 0xFFFFFFFF
        H[13] = (H[13] + n) & 0xFFFFFFFF
        H[14] = (H[14] + o) & 0xFFFFFFFF
        H[15] = (H[15] + p) & 0xFFFFFFFF

    hash_value = bytearray(64)
    for i in range(16):
        hash_value[i * 4:i * 4 + 4] = H[i].to_bytes(4, byteorder='big')

    return hash_value.hex()
