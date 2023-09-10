def caesar(s, k, decode = False):
  if decode:
    k= 26-k
  return ''.join([chr((ord(i) - 65 + k) % 26 + 65) for i in s.upper() if ord(i) >= 65 and ord(i) <= 98 ])

txt = 'The quick brown fox jumped over the lazy dogs"
keyw = 11
print('Plain text:', txt)
print('Encrypted:', caesar(txt, keyw))
print('Decrypted:, caesar(caesar(txt, keyw), keyw, decode = True))
