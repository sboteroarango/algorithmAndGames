def bytes_entero(byte_):
  byteEnBits = list(map(int,str(byte_)))
  valorEnteroPrimero = 128
  entero = 0
  for bit in byteEnBits:
    if bit == 1:
      entero += valorEnteroPrimero
    valorEnteroPrimero = valorEnteroPrimero/2
  return entero
bytes_entero(11111111)
