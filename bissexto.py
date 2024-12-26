print('='*30)
print('       vamos testar  se  o ano é bissexto')
n=int(input(' digite o ano : '))
if n % 4 ==0:
    if n % 100 ==0:
        if n % 400==0:
            print(f' {n}  è ano bissexto')
        else:
            print(f' {n} não é ano bissexto')
    else:
        print(f'{n} é  ano bissexto')
else:
    print(f' {n} não é bissexto')


    #logica ano bissexto -> divisivel por 4 não diviivel por 100  fim / caso for divisivel por 100 tem que ser divisivel por 400 tambem