stroka = "In the hole in the ground there lived a hobbit"

fin = stroka.find("h",0)
fin2 = stroka.find("h",-8)

res = stroka[:fin] + stroka[fin2:]

print(res)
