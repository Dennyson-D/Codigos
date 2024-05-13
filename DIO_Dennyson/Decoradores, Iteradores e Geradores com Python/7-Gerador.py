def gerador(numeros = list[int]):
    for num in numeros:    
        yield num * 2

for i in gerador(numeros  = [1,2,3,4,5,6,7]):
    print(i)