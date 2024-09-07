# def gcf(n, m):
#     l = min(n, m)
#     lst =[]

#     for i in range(1, l+1):
#         if n % i == m % i == 0:
#             lst.append(i)
            
#     return max(lst)

# if __name__ == "__main__":
#     n, m = map(int, input("Enter two numbers: ").split())
#     print(f"GCF: {gcf(n, m)}")
#     print(f"LCM: {int(n*m/gcf(n, m))}")

x = 4
y = 8

def gcd(x, y):
    return (x * y) // lcm(x, y)

# def gcd(x, y):
#     while y:      
#         x, y = y, x % y
#         print(x, y)
#     return x

# def lcm(x, y):
#     return x * y / gcd(x, y)

def lcm(a, b):
  t = a % b
  if t == 0: return a
  return a * lcm(b, t) // t

print(gcd(x, y))
print(lcm(x, y))