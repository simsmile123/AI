

def elvis(n):
    if(n<= 3): print(n+1)
    else: 
        elvis(n-3)
        print('>>')


def main():
   print(elvis(11))
if __name__ == '__main__': main()