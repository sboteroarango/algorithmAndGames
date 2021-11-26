
def byte_entero(byte_):
  byteEnBits = list(map(int,str(byte_)))
  valorEnteroPrimero = 128
  entero = 0
  for bit in byteEnBits:
    if bit == 1:
      entero += valorEnteroPrimero
    valorEnteroPrimero = valorEnteroPrimero/2
  return entero
def entero_byte(entero):
  byteEnLista = []
  byte = ''
  while entero > 0 :
    byteEnLista.append(entero%2)
    entero = int(entero / 2)
  for bit in byteEnLista:
    byte += str(bit)
  return(byteEnLista)
print(byte_entero(11111111))
print(entero_byte(255))
