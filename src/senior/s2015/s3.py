number_of_gates = int(input())
number_of_planes = int(input())
planes = []
gates = []

for _ in range(number_of_planes):
    planes.append(int(input()))

for _ in range(number_of_gates):
    gates.append(False)

planes_docked = 0
for plane in planes:
    if not gates[plane - 1]:
        gates[plane - 1] = True
        planes_docked += 1
    else:
        # max gate is not available, look at smaller gate
        can_dock = False
        gate_number = plane - 2
        while gate_number > -1:
            if not gates[gate_number]:
                gates[gate_number] = True
                can_dock = True
                planes_docked += 1
                break
            gate_number -= 1
        if not can_dock:
            break

print(planes_docked)

