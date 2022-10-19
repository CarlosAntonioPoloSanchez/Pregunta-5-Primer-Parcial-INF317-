from multiprocessing import Pool

def palindromo(n):
    return n[::-1]

if __name__ == '__main__':
    print("ingrese una palabra")
    a=input()

    x=(Pool().map(palindromo,[a]))
    print(x[0]==a)

