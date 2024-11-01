"""# LOGIC GATE PROBLEM
Research other types of gates that exist (such as NAND, NOR, and XOR). Add them to the circuit hierarchy. How much additional coding did you need to do?

The most simple arithmetic circuit is known as the half adder. Research the simple half-adder circuit. Implement this circuit.

Now extend that circuit and implement an 8-bit full adder."""

class LogicGate:
    def __init__(self, lbl):
        self.name = lbl
        self.output = None

    def get_label(self):
        return self.name

    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output


class BinaryGate(LogicGate):

    def __init__(self, lbl):
        super(BinaryGate, self).__init__(lbl)
        self.pin_a = None
        self.pin_b = None

    #Programmatically set value
    def set_a(self,a):
        self.pin_a = a
    def set_b(self,b):
        self.pin_b = b
    #Grab values from the user
    def set_pin_a(self, value):
        self.pin_a = value

    def set_pin_b(self, value):
        self.pin_b = value

    # Call to set both pins with provided data
    def set_pins(self, value_a, value_b):
        self.pin_a = value_a
        self.pin_b = value_b

    def set_next_pin(self, source):
        if self.pin_a == None:
            self.pin_a = source
        else:
            if self.pin_b == None:
                self.pin_b = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")
    
    def get_pin_a(self):
        return self.pin_a
    
    def get_pin_b(self):
        return self.pin_b


class ANDGate(BinaryGate):

    def __init__(self, lbl):
        BinaryGate.__init__(self, lbl)

    def perform_gate_logic(self):
        assert self.pin_a != None and self.pin_b != None
        return(self.pin_a and self.pin_b)

class ORGate(BinaryGate):

    def __init__(self, lbl):
        BinaryGate.__init__(self, lbl)

    def perform_gate_logic(self):
        assert self.pin_a != None and self.pin_b != None
        if self.pin_a == 1 or self.pin_b == 1:
            return 1
        else:
            return 0

class XORGate(BinaryGate): 
    def __init__(self, lbl):
        BinaryGate.__init__(self, lbl)
    def perform_gate_logic(self):
        assert self.pin_a != None and self.pin_b != None
        return((self.pin_a or self.pin_b) and     not(self.pin_a and self.pin_b))  

class UnaryGate(LogicGate):

    def __init__(self, lbl):
        LogicGate.__init__(self, lbl)

        self.pin = None

    def set_pin(self, value):
        self.pin = value

    def get_pin(self):
        return self.pin
            

    def set_next_pin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class NOTGate(UnaryGate):

    def __init__(self, lbl):
        UnaryGate.__init__(self, lbl)

    def perform_gate_logic(self):
        if self.get_pin():
            return 0
        else:
            return 1


class NANDGate(ANDGate):
    
    def perform_gate_logic(self):
        if super().perform_gate_logic() == 1:
            return 0
        else:
            return 1  

class NORGate(ORGate):
    def perform_gate_logic(self):
        if super().perform_gate_logic() == 1:
            return 0
        else:
            return 1

class Connector:

    def __init__(self, fgate, tgate):
        self.from_gate = fgate
        self.to_gate = tgate

        tgate.set_next_pin(fgate.get_output())

    def get_from(self):
        return self.from_gate

    def get_to(self):
        return self.to_gate



g1 = ANDGate("G1")
g2 = ANDGate("G2")
g3 = ORGate("G3")
g4 = NOTGate("G4")
# c1 = Connector(g1, g3)
# c2 = Connector(g2, g3)
def main():
    g1 = ANDGate("G1")
    g2 = ANDGate("G2")
    g3 = ORGate("G3")
    g4 = NOTGate("G4")

    g1.set_pins(1, 1)
    g2.set_pins(0, 1)
    g3.set_pins(g1.get_output(), g2.get_output())
    g4.set_pin(g3.get_output())

    print(g4.get_output())

if __name__ == "__main__":
    main()


