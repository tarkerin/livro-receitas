a = int(input('Entre com a sua primeira nota'))
while a > 10:
    a = int(input('Entre com a sua primeira nota novamente.'))

b = int(input('Entre com a sua segunda nota'))
while b > 10:
    b = int(input('Entre com a sua segunda nota novamente.'))

c = int(input('Entre com a sua terceira nota'))
while c > 10:
    c = int(input('Entre com a sua terceira nota novamente.'))

d = int(input('Entre com a sua quarta nota'))
while d > 10:
    d = int(input('Entre com a sua quarta nota novamente.'))

media = (a + b + c + d / 4)
print ('media: {}'.format(media))






# a = int(input('Entre com a sua primeira nota: '))
# b = int(input('Entre com a sua segunda nota: '))
# c = int(input('Entre com a sua terceira nota: '))
# d = int(input('Entre com a sua quarta nota: '))
# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#      print('media: {}'.format(media))
# else:
#      print('foi informado alguma nota errada. Favor colocar as notas certas.')
#      media = (port + ing) / 2