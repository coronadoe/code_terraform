import random

code = [0] * 6
trash = [set() for _ in code]

lock = self.contract.lock

def get_code(code) -> list:
    return lock.intercept(code)


def get_random_key(excluded) -> int:
    while True:
        number = random.randint(0, 99)

        if number not in excluded:
            break

    return number


while True:
    result = get_code(code)

    if all(result):
        print(code)
        break
    
    for index, valid in enumerate(result):
        if not valid:
            trash[index].add(code[index])
            key = get_random_key(trash[index])
            code[index] = key
        

transmitter = get_component("transmitter")
transmitter.connect("earth")
transmitter.transmit(self.contract.id, code)