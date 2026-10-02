atmosphere = get_component("atmosphere")

while True:    
    oxygen = self.set_intake(atmosphere.get_co2() / 10)

    if not oxygen.status == "ok":
        print(oxygen.message)

    if self.waste() > 50: 
        dump_waste = self.dump_waste()

        if not dump_waste.status == "ok":
            print(dump_waste.message)