import sys
p = 83
q = 103
n = p*q
fn = (p-1)*(q-1)
d=7
e=0
while((d*e)%fn!=1):
	e+=1
m=35
#print("p",p," q",q," n",n," fn",fn," d",d," e",e)
#print("m",m," mn",mn)
def encode(message):
	return (int(message)**d)%n
	
def decode(chiper):
	return (int(chiper)**e)%n
	
p = 'Privatni klic je (n={},d={})'.format(n,d)
print(p)
v = 'Verejny klic je (n={},e={})'.format(n,e)
print(v)

while(True):
	i = input('Zadejte zpravu mensi nez {}   '.format(n))
	encoded = encode(int(i))
	print('Zakodovana zprava "{}"'.format(encode(i)))
	print('Odkodovana zprava "{}"'.format(decode(encoded)))


