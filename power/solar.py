clock = get_component('clock')

while True:
    sun_elevation = clock.get_elevation()
    tilt = self.set_tilt(90 - sun_elevation)

    if not tilt.status == "ok":
        print(tilt.message)