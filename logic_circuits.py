"""# LOGIC GATE PROBLEM
Research other types of gates that exist (such as NAND, NOR, and XOR). Add them to the circuit hierarchy. How much additional coding did you need to do?

The most simple arithmetic circuit is known as the half adder. Research the simple half-adder circuit. Implement this circuit.

Now extend that circuit and implement an 8-bit full adder."""

"""
Enhanced implementation of logic gates and arithmetic circuits.
Includes half-adder and 8-bit full adder implementations.
"""

"""
Enhanced implementation of logic gates and arithmetic circuits.
Includes half-adder and 8-bit full adder implementations.
"""

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
        super().__init__(lbl)
        self.pin_a = None
        self.pin_b = None

    def set_a(self, a):
        self.pin_a = a

    def set_b(self, b):
        self.pin_b = b

    def set_pin_a(self, value):
        self.pin_a = value

    def set_pin_b(self, value):
        self.pin_b = value

    def set_pins(self, value_a, value_b):
        self.pin_a = value_a
        self.pin_b = value_b

    def set_next_pin(self, source):
        if self.pin_a is None:
            self.pin_a = source
        elif self.pin_b is None:
            self.pin_b = source
        else:
            raise ValueError("Cannot Connect: NO EMPTY PINS on this gate")

    def get_pin_a(self):
        return self.pin_a

    def get_pin_b(self):
        return self.pin_b

class UnaryGate(LogicGate):
    def __init__(self, lbl):
        super().__init__(lbl)
        self.pin = None

    def set_pin(self, value):
        self.pin = value

    def get_pin(self):
        return self.pin

    def set_next_pin(self, source):
        if self.pin is None:
            self.pin = source
        else:
            raise ValueError("Cannot Connect: NO EMPTY PINS on this gate")

# Basic Gates
class ANDGate(BinaryGate):
    def perform_gate_logic(self):
        return int(bool(self.pin_a) and bool(self.pin_b))

class ORGate(BinaryGate):
    def perform_gate_logic(self):
        return int(bool(self.pin_a) or bool(self.pin_b))

class NOTGate(UnaryGate):
    def perform_gate_logic(self):
        return int(not bool(self.pin))

class XORGate(BinaryGate):
    def perform_gate_logic(self):
        return int(bool(self.pin_a) != bool(self.pin_b))

class NANDGate(BinaryGate):
    def perform_gate_logic(self):
        return int(not (bool(self.pin_a) and bool(self.pin_b)))

class NORGate(BinaryGate):
    def perform_gate_logic(self):
        return int(not (bool(self.pin_a) or bool(self.pin_b)))

# Connector
class Connector:
    def __init__(self, fgate, tgate):
        self.from_gate = fgate
        self.to_gate = tgate
        tgate.set_next_pin(fgate.get_output())

# Half Adder
class HalfAdder:
    def __init__(self):
        self.xor_gate = XORGate("XOR")
        self.and_gate = ANDGate("AND")
        
    def compute(self, a, b):
        self.xor_gate.set_pins(a, b)
        self.and_gate.set_pins(a, b)
        
        sum_bit = self.xor_gate.get_output()
        carry_bit = self.and_gate.get_output()
        
        return sum_bit, carry_bit

# Full Adder
class FullAdder:
    def __init__(self):
        self.ha1 = HalfAdder()
        self.ha2 = HalfAdder()
        self.or_gate = ORGate("OR")
        
    def compute(self, a, b, cin):
        sum1, carry1 = self.ha1.compute(a, b)
        sum2, carry2 = self.ha2.compute(sum1, cin)
        
        self.or_gate.set_pins(carry1, carry2)
        carry_out = self.or_gate.get_output()
        
        return sum2, carry_out

# 8-bit Full Adder
class EightBitFullAdder:
    def __init__(self):
        self.adders = [FullAdder() for _ in range(8)]
    
    def compute(self, a, b):
        """
        Compute sum of two 8-bit numbers.
        a, b: lists of 8 bits each (LSB first)
        Returns: tuple (sum_bits, carry_out)
        """
        if len(a) != 8 or len(b) != 8:
            raise ValueError("Inputs must be 8 bits each")
            
        carry = 0
        sum_bits = []
        
        for i in range(8):
            sum_bit, carry = self.adders[i].compute(a[i], b[i], carry)
            sum_bits.append(sum_bit)
            
        return sum_bits, carry

def binary_to_decimal(binary_list):
    """Convert binary list to decimal number"""
    return sum(bit * (2 ** i) for i, bit in enumerate(binary_list))

def decimal_to_binary(decimal, bits=8):
    """Convert decimal to binary list with specified number of bits"""
    binary = []
    for _ in range(bits):
        binary.append(decimal & 1)
        decimal >>= 1
    return binary