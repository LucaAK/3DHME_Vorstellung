print("Lukas Keller")

class LukasKeller:
    def __init__(self):
        self.stack = []
        self.input_string = ""
        self.index = 0
        self.state = "start"

    def parse(self, input_string):
        self.input_string = input_string
        self.index = 0
        self.state = "start"
        self.stack = []
        return self._parse()

    def _parse(self):
        while True:
            if self.state == "start":
                if self.index < len(self.input_string):
                    char = self.input_string[self.index]
                    if char == "(":
                        self.stack.append(char)
                        self.index += 1
                    elif char == ")":
                        if not self.stack or self.stack[-1] != "(":
                            return False
                        else:
                            self.stack.pop()
                            self.index += 1
                    else:
                        return False
                else:
                    if not self.stack:
                        return True
                    else:
                        return False