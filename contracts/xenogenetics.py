result = []

c = self.contract
alien_samples = c.samples
earth_samples = c.earth_ref

for alien_sample in alien_samples:
    if alien_sample not in earth_samples:
        result.append(alien_sample)


transmitter = get_component('transmitter')
transmitter.connect('earth')
transmitter.transmit(c.id, result)
