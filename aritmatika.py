   
import math   

print("Kalkulator sederhana persamaan akar kuadrat")
a = float(input("masukkan nilai a: "))
b = float(input("masukkan nilai b: "))
c = float(input("masukkan nilai c: "))

def find_roots(a, b, c):
  ans_2 = ((-b) - math.sqrt(b**2 - 4*a*c))/2*a 
  ans = ((-b) + math.sqrt(b**2 - 4*a*c))/2*a
  return ans_2, ans

  
print("hasil x1 dan x2 = ", find_roots(a, b, c));
