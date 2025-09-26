import flexhash

hex_header1 = '00800020448ba2f03e7f5c198a5a1268db90606e199be89f762bfe4a5226cee4b14449a2ed7d6f6334fe360558453a1deb2f7158510c5b03edc44a756d4ab32050cb99cac162d6689887001e8aaaaae2'
hex_header = '00800020d3d8a70beca9a7c1fcf4b233a02d23df622aee47f3699b7193c9ef827efe076147199e4b2412829a6c03ef89775e7f24697e34652745bb47b5ca77483c11ba5368d678ae1e00a17e270100a0'
hex_header = '008000206107fe7e82efc993719b69f347ee2a62df232da033b2f4fcc1a7a9ec0ba7d8d34cbccf4ea383f0022aab3de32ea3e0ec0cedde9c335525a846369dbc405b77b4ae78d6687ea1001ed2291b00'
hex_header = '008000200ba7d8d3c1a7a9ec33b2f4fcdf232da047ee2a62719b69f382efc9936107fe7e0dd3f482ecf66ee025f3de1e9b2281d602779e9dc5ecc88651753d20680ced3aae78d6687ea1001ea0000127'
header = bytes.fromhex(hex_header)   # <-- raw 80 bytes

digest = flexhash.hash(header)       # real Flex output (32 bytes)

print('digest (raw hex):', digest.hex())
print('digest reversed (common display):', digest[::-1].hex())
print('digest int (big-endian):', int(digest[::-1].hex(), 16))

# miner-style words
hash_words = [format(int.from_bytes(digest[i:i+4], 'little'), '08x') for i in range(0, 32, 4)]
print('Hash[ 7: 0]:', ' '.join(hash_words[::-1]))