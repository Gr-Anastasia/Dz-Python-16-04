stroka = "In the hole in the ground there lived a hobbit"

fin = stroka.find("h")
fin2 = stroka.find("h",-6)

res = stroka[:fin] + stroka[fin2:]

print(res)
