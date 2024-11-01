import pytest
from logic_gates.gates import (
    ANDGate, 
    ORGate, 
    NOTGate, 
    XORGate,
    NANDGate,
    NORGate
)

class TestLogicGates:
    def test_and_gate(self):
        gate = ANDGate("TestAND")
        gate.set_pins(1, 1)
        assert gate.get_output() == 1

        gate.set_pins(1, 0)
        assert gate.get_output() == 0

    def test_or_gate(self):
        gate = ORGate("TestOR")
        gate.set_pins(0, 1)
        assert gate.get_output() == 1

        gate.set_pins(0, 0)
        assert gate.get_output() == 0

    def test_not_gate(self):
        gate = NOTGate("TestNOT")
        gate.set_pin(1)
        assert gate.get_output() == 0

        gate.set_pin(0)
        assert gate.get_output() == 1

    def test_xor_gate(self):
        gate = XORGate("TestXOR")
        gate.set_pins(1, 0)
        assert gate.get_output() == 1

        gate.set_pins(1, 1)
        assert gate.get_output() == 0

    def test_nand_gate(self):
        gate = NANDGate("TestNAND")
        gate.set_pins(1, 1)
        assert gate.get_output() == 0

        gate.set_pins(1, 0)
        assert gate.get_output() == 1

    def test_nor_gate(self):
        gate = NORGate("TestNOR")
        gate.set_pins(0, 0)
        assert gate.get_output() == 1

        gate.set_pins(1, 0)
        assert gate.get_output() == 0

    def test_unset_pins(self):
        gate = ANDGate("TestAND")
        with pytest.raises(AssertionError):
            gate.get_output()