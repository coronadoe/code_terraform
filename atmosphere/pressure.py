while True:
    low = self.next_window_low()
    high = self.next_window_high()
    gauge = self.gauge()

    if low < gauge < high:
        self.sync()