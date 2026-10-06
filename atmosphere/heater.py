power = 0
previous_state = ''

def get_power(thermal_state):
    values = {
        "heat_bleed": 9,
        "clear": 5,
        "dust_storm": 3,
        "dest_veil": 0
    }

    return float(values.get(thermal_state, 0)) 

while True:
    thermal_state = self.thermal_state()
    
    if not previous_state == thermal_state:
        power = get_power(thermal_state)
        self.set_power(power)
        previous_state = thermal_state

    
    # self.set_power(power)
    # efficiency = self.efficiency()
    # thermal_state = self.thermal_state()
    # if efficiency < 100:
    #     power += 1
    
    # print(f"Efficiency: {efficiency} -- Power {power} -- Thermal State {thermal_state}")
