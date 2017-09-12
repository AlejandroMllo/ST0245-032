# Taller 8
#
# Presentado por:
#       Juan Pablo Vidal C.
#       Alejandro Murillo G.
#

print("Presentado por:\n\tJuan Pablo Vidal C.\n\tAlejandro Murillo G.")

# --- Stack ----------------------------------------------------------

stack = []
stack.append(1)
stack.append(2)
stack.append(3)

stack2 = []
while len(stack) > 0:
    stack2.append(stack.pop())

print("\n--- Punto 1 ---")
print(stack2)

# --- Queue ----------------------------------------------------------

from collections import deque

queue = deque([])
queue.append("Juan")
queue.append("Maria")
queue.append("Pedro")

print("\n--- Punto 2 ---")
while len(queue) > 0:
    print("Atendiendo a: " + queue.popleft())

# --- Punto 3 --------------------------------------------------------

stackCalculator = []

operations = str(input("Ingrese la cadena (dentro de comillas) de operaciones en Notacion Polaca: "))

for c in operations:
    stackCalculator.append(c)

while len(stackCalculator) > 0:
    b = stackCalculator.pop()
    a = stackCalculator.pop()
    operation = str(a) + stackCalculator.pop() + str(b)
    stackCalculator.append(eval(operation))
    if (len(stackCalculator) == 1):
        print(stackCalculator.pop())
