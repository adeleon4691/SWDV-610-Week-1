#Write a short Python function, is_multiple(n, m),
#that takes two integer values and returns True is n is a multiple of m,
#that is, n = mi for some integer i, and False otherwise.

m=int(input("Enter a number: "))
n=int(input("Enter a number to see if is a multiple: "))

def is_multiple(n,m):
    
    if n%m==0:
        print("True")
    else:
        print("False")
        
is_multiple(n,m)