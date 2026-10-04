for letter in "ABCDEFGH":
    for number in range(1, 25):
        section = f"{letter}{number}"
        result = self.scan(section)
        
        if result.status == 'ok':
            print(f"{section}: " + result.name)
        else:
            print(f"{section}: " + result.message)
