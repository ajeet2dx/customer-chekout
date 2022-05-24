def checkout_time(customers: list, cash_registers: int):
    if cash_registers == 1:
        print (sum(customers))
    elif len(customers) <= cash_registers:
        print (max(customers))

    registers = {}
    for i in range(cash_registers):
        registers[i] = customers.pop(0)

    iterations = 0
    while any(registers.values()):
        for r in registers.copy():

            registers[r] -= 1
            if registers[r] <= 0:
                try:
                    registers[r] = customers.pop(0)
                except IndexError:
                    registers[r] = 0

        iterations += 1

    return iterations

def main():
    checkout_time(customers=[5,1,3] , cash_registers=1)

if __name__ == '__main__':
    main()


