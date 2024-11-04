import pytest
from logic_gates.gates import (
    LogicGate, BinaryGate, UnaryGate,
    ANDGate, ORGate, NOTGate, NANDGate, NORGate, XORGate
)

class TestLogicGates:
    def test_and_gate(self):
        gate = ANDGate("AND1")
        test_cases = [
            (0, 0, 0),
            (0, 1, 0),
            (1, 0, 0),
            (1, 1, 1)
        ]
        for a, b, expected in test_cases:
            gate.set_pins(a, b)
            assert gate.get_output() == expected

    def test_or_gate(self):
        gate = ORGate("OR1")
        test_cases = [
            (0, 0, 0),
            (0, 1, 1),
            (1, 0, 1),
            (1, 1, 1)
        ]
        for a, b, expected in test_cases:
            gate.set_pins(a, b)
            assert gate.get_output() == expected

    def test_not_gate(self):
        gate = NOTGate("NOT1")
        test_cases = [
            (0, 1),
            (1, 0)
        ]
        for input_val, expected in test_cases:
            gate.set_pin(input_val)
            assert gate.get_output() == expected

    def test_nand_gate(self):
        gate = NANDGate("NAND1")
        test_cases = [
            (0, 0, 1),
            (0, 1, 1),
            (1, 0, 1),
            (1, 1, 0)
        ]
        for a, b, expected in test_cases:
            gate.set_pins(a, b)
            assert gate.get_output() == expected

    def test_nor_gate(self):
        gate = NORGate("NOR1")
        test_cases = [
            (0, 0, 1),
            (0, 1, 0),
            (1, 0, 0),
            (1, 1, 0)
        ]
        for a, b, expected in test_cases:
            gate.set_pins(a, b)
            assert gate.get_output() == expected

    def test_xor_gate(self):
        gate = XORGate("XOR1")
        test_cases = [
            (0, 0, 0),
            (0, 1, 1),
            (1, 0, 1),
            (1, 1, 0)
        ]
        for a, b, expected in test_cases:
            gate.set_pins(a, b)
            assert gate.get_output() == expected

    def test_connector(self):
        and_gate = ANDGate("AND1")
        not_gate = NOTGate("NOT1")
        and_gate.set_pins(1, 1)
        not_gate.set_pin(and_gate.get_output())
        assert not_gate.get_output() == 0

    def test_invalid_pin_assignment(self):
        gate = ANDGate("AND1")
        with pytest.raises(AssertionError):
            gate.get_output()

    def test_gate_labels(self):
        gate = ANDGate("TestGate")
        assert gate.get_label() == "TestGate"