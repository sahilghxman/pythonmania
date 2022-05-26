import time
import pickle
def dumper():
    m = open('bookmart.dat','ab')
    g=[]
    h=[]
    lis = ['Book number', 'Author name','Book name','Price']
    for i in lis:
        ent = input(i)
        g.append(ent)
    h.append(g)
    x = []
    x = pickle.dump(g,m)

    m.close()
def loader():
    z =  open('bookmart.dat','rb')
    for i in range(2):
        print(pickle.load(z))

    print()
    z.close()

def main():
    def body():

        print('Welcome to the program')
        time.sleep(2.5)
        print('What can I do you for?')
        time.sleep(1)
        print('You must press 0 to add enteries to the file')
        time.sleep(1)
        print('You must press 1 to search some specific author or book')

        time.sleep(1.5)
    deed = input('HERE   >>')

    if deed == str(1):
        loader()
    elif deed == str(0):
        dumper()
    else:
        print('Do you not understand what 0 or 1 is?/?')
        time.sleep(3)
        print('Bbye')
        quit()
main()
