class ODE:
    def __init__(self, f, final_time, initial_time, initial_value, steps=10_000):
        self.steps = steps
        self.final_time = final_time
        self.initial_time = initial_time
        self.initial_value = initial_value
        self.f = f

    def solve_runge_kutta(self):
        """
        Given dy/dt = f(t,y), and y(initial_time) = initial_output

        @return: ts, ys -- array of inputs and estimated outputs of y at that input
        """
        delta = (self.final_time - self.initial_time) / self.steps

        ts = [self.initial_time]
        ys = [self.initial_value]

        for s in range(self.steps):
            k1 = self.f(ts[-1], ys[-1])
            k2 = self.f(ts[-1] + delta / 2, ys[-1] + delta * k1 / 2)
            k3 = self.f(ts[-1] + delta / 2, ys[-1] + delta * k2 / 2)
            k4 = self.f(ts[-1] + delta, ys[-1] + delta * k3)

            ts.append(ts[-1] + delta)
            ys.append(ys[-1] + (delta / 6) * (k1 + 2 * k2 + 2 * k3 + k4))

        return ts, ys
