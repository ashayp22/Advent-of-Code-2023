class Tracker:
    def __init__(self):
        self.low = 0
        self.high = 0
        self.queue = []

    def track(self, is_high: bool):
        self.high += 1 if is_high else 0
        self.low += 0 if is_high else 1

    def print(self):
        print(f"High: {self.high}")
        print(f"Low: {self.low}")
        print(f"Answer: {self.low*self.high}")

    def add_pulse_task(self, module, is_high: bool, sender: str):
        self.queue.append((module, is_high, sender))

    def eval(self):
        while len(self.queue) > 0:
            module, is_high, sender = self.queue.pop(0)
            # print(f"{sender} {'-high->' if is_high else '-low->'} {module.name}")
            module.pulse(is_high, sender)

class Module:
    def __init__(self, name, outputs, tracker: Tracker):
        self.name = name
        self.outputs = outputs
        self.tracker = tracker

    def pulse(self, is_high: bool, sender: str):
        self.tracker.track(is_high)

    def add_pulse_task(self, module, is_high: bool, sender: str):
        self.tracker.add_pulse_task(module, is_high, sender)

    def add_outputs(self, outputs):
        self.outputs = outputs

    def add_input(self, input_name):
        pass

class Broadcaster(Module):
    def __init__(self, outputs: list[Module], tracker: Tracker):
        super().__init__("broadcaster", outputs, tracker)

    def pulse(self, is_high: bool, sender: str):
        super().pulse(is_high, sender)

        for output in self.outputs:
            self.add_pulse_task(output, is_high, self.name)

class FlipFlop(Module):
    def __init__(self, name: str, outputs: list[Module], tracker: Tracker):
        super().__init__(name, outputs, tracker)
        self.on = False

    def pulse(self, is_high: bool, sender: str):
        super().pulse(is_high, sender)

        if not is_high:
            # If it was off, it turns on and sends a high pulse
            self.on = not self.on

            for output in self.outputs:
                self.add_pulse_task(output, self.on, self.name)

class Conjunction(Module):
    def __init__(self, name: str, inputs: list[str], outputs: list[Module], tracker: Tracker):
        super().__init__(name, outputs, tracker)
        self.input_is_high_pulse = {}

        for input in inputs:
            self.input_is_high_pulse[input] = False

    def all_high_inputs(self):
        for input in self.input_is_high_pulse:
            if not self.input_is_high_pulse[input]:
                # Found a low input
                return False
        return True

    def add_input(self, input_name):
        self.input_is_high_pulse[input_name] = False

    def pulse(self, is_high: bool, sender: str):
        super().pulse(is_high, sender)

        self.input_is_high_pulse[sender] = is_high
        send_high_pulse = not self.all_high_inputs()

        for output in self.outputs:
            self.add_pulse_task(output, send_high_pulse, self.name)

class Untyped(Module):
    def __init__(self, name: str, tracker: Tracker):
        super().__init__(name, [], tracker)
        self.name = name

    def pulse(self, is_high: bool, sender: str):
        super().pulse(is_high, sender)

file1 = open('input1.txt', 'r')
Lines = file1.readlines()

all_modules = {}
tracker = Tracker()

# Create modules
for line in Lines:
    if line[-1] == "\n":
        # Remove new line character
        line = line[0:-1]

    if "broadcaster" in line:
        # Broadcaster
        all_modules["broadcaster"] = Broadcaster([], tracker)
    elif line[0] == "%":
        # Flip-flop
        line = line[1:]
        name = line.split(" -> ")[0]
        all_modules[name] = FlipFlop(name, [], tracker)
    else:
        # Conjunction
        line = line[1:]
        name = line.split(" -> ")[0]
        all_modules[name] = Conjunction(name, [], [], tracker)

def getModule(name):
    if name not in all_modules:
        all_modules[name] = Untyped(name, tracker)
    return all_modules[name]

# Assign inputs and outputs for each module
for line in Lines:
    if line[-1] == "\n":
        # Remove new line character
        line = line[0:-1]

    if "broadcaster" in line:
        outputs = line.split(" -> ")[1].split(", ")

        module_outputs = [getModule(name) for name in outputs]

        all_modules["broadcaster"].add_outputs(module_outputs)

        for output in module_outputs:
            output.add_input("broadcaster")
    else:
        # Flip-flop or conjunction
        line = line[1:]
        name = line.split(" -> ")[0]
        outputs = line.split(" -> ")[1].split(", ")

        module_outputs = [getModule(name) for name in outputs]

        all_modules[name].add_outputs(module_outputs)

        for output in module_outputs:
            output.add_input(name)

for _ in range(1000):
    tracker.add_pulse_task(all_modules["broadcaster"], False, "button")
    tracker.eval()

tracker.print()