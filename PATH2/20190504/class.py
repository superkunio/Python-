class asvdw ():
    def __init__(self,p,j,k):
        self.a = p+j
        self.p = p
        self.j = j
        self.k = k

    def sum(self):
        print(self.p+self.j+self.k)




def main():
    k = asvdw(1,2,3)

    k.sum()

    print(k.a)

if __name__ == '__main__':
    main()