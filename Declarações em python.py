#If, elif e else

a=[10,9,8,4,5,7,9,10,5]

if a[3] >= 6:
    print('Aprovado!')

elif a[3] >= 5:
    print('Recuperação!')

else:
    print('Reprovado!')

# For

l = [1,2,3,4,5,6,7]

print(l)

for num in l:
    if num % 2 == 0:
        print(num,'é par.')
    else:
        print(num,'é impar')

sum_ = 0

for num in l:
    sum_ += num
print(sum_)

string = 'Essa é uma string!'

for tchuale in string:
    print(tchuale)

tup = (1,2,3,4,5)

for t in tup:
    print(t)

z = [(1,2),(2,3),(3,4)]

(t1, t2) = z[0]

for (t1,t2) in z:
    print(t1*t2)

d = {'k1':1, 'k2':2, 'k3':3}

for (key,valor) in d.items():
    print(key, ':',valor)
    