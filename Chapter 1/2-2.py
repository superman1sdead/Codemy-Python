a = int(input("Masukkan bilangan :"))

dig0 = (a//10000)
dig1 = (a //1000)% 10
dig2 = (a //100) % 10
dig3 = (a //10) % 10
dig4 = a % 10

print (dig0*dig1 * dig2 * dig3 * dig4)