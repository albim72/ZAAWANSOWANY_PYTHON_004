#przykład 1

num = [67,8,9,-1,0,34,55,100,-99,35,67,99,2,8,12]

kr = [(9,3),(6,90),(45,3)]

numparz = list(filter(lambda x:x%2==0,num))
print(numparz)

cube = list(map(lambda x:x**3,num))
print(cube)

def multifive(n):
    return n*5

five = list(map(multifive,num))

print(five)

def multifiveplus(n):
    return n[0]*5+n[1]

dwa = list(map(multifiveplus,kr))
print(dwa)

#przykład 2

def witaj(imie):
    return f"Miło Cię widzieć {imie}"

def konkurs(imie,punkty):
    return f"Uczestnik konkursu: {imie}, liczba punktów: {punkty}"

def kierowca(imie,dosw,prawo_j=True,kraj="PL"):
    return f"kierowca: {imie}, dośwkadczenie: {dosw} lat, prawo jazdy: {prawo_j}"

def osoba(funkcja,*args,**kwargs):
    return funkcja(*args,**kwargs)

print(osoba(witaj,"Olaf"))
print(osoba(konkurs,"Ala",55))
print(osoba(kierowca,"Tomek",6))
print(osoba(kierowca,"Jan",7,False))
print(osoba(kierowca,"Tomek",6,kraj="GB"))
