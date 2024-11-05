"""
Test suite for logic gates and arithmetic circuits.
Run with: pytest test_logic_circuits.py
"""
import pytest
from logic_circuits import (
    ANDGate, ORGate, NOTGate, XORGate, NANDGate, NORGate,
    HalfAdder, FullAdder, EightBitFullAdder,
    binary_to_decimal, decimal_to_binary
)

# Test basic gates
@pytest.mark.parametrize("gate_class,inputs,expected", [
    (ANDGate, [(0,0), (0,1), (1,0), (1,1)], [0,0,0,1]),
    (ORGate, [(0,0), (0,1), (1,0), (1,1)], [0,1,1,1]),
    (NANDGate, [(0,0), (0,1), (1,0), (1,1)], [1,1,1,0]),
    (NORGate, [(0,0), (0,1), (1,0), (1,1)], [1,0,0,0]),
    (XORGate, [(0,0), (0,1), (1,0), (1,1)], [0,1,1,0]),
])
def test_binary_gates(gate_class, inputs, expected):
    gate = gate_class("TEST")
    for (a, b), exp in zip(inputs, expected):
        gate.set_pins(a, b)
        assert gate.get_output() == exp

def test_not_gate():
    gate = NOTGate("NOT")
    gate.set_pin(0)
    assert gate.get_output() == 1
    gate.set_pin(1)
    assert gate.get_output() == 0

# Test Half Adder
def test_half_adder():
    ha = HalfAdder()
    test_cases = [
        ((0, 0), (0, 0)),  # a=0, b=0 -> sum=0, carry=0
        ((0, 1), (1, 0)),  # a=0, b=1 -> sum=1, carry=0
        ((1, 0), (1, 0)),  # a=1, b=0 -> sum=1, carry=0
        ((1, 1), (0, 1)),  # a=1, b=1 -> sum=0, carry=1
    ]
    
    for (a, b), (exp_sum, exp_carry) in test_cases:
        sum_bit, carry_bit = ha.compute(a, b)
        assert (sum_bit, carry_bit) == (exp_sum, exp_carry)

# Test Full Adder
def test_full_adder():
    fa = FullAdder()
    test_cases = [
        ((0, 0, 0), (0, 0)),  # a=0, b=0, cin=0 -> sum=0, cout=0
        ((0, 0, 1), (1, 0)),  # a=0, b=0, cin=1 -> sum=1, cout=0
        ((0, 1, 0), (1, 0)),  # a=0, b=1, cin=0 -> sum=1, cout=0
        ((0, 1, 1), (0, 1)),  # a=0, b=1, cin=1 -> sum=0, cout=1
        ((1, 0, 0), (1, 0)),  # a=1, b=0, cin=0 -> sum=1, cout=0
        ((1, 0, 1), (0, 1)),  # a=1, b=0, cin=1 -> sum=0, cout=1
        ((1, 1, 0), (0, 1)),  # a=1, b=1, cin=0 -> sum=0, cout=1
        ((1, 1, 1), (1, 1)),  # a=1, b=1, cin=1 -> sum=1, cout=1
    ]
    
    for (a, b, cin), (exp_sum, exp_carry) in test_cases:
        sum_bit, carry_bit = fa.compute(a, b, cin)
        assert (sum_bit, carry_bit) == (exp_sum, exp_carry)

# Test 8-bit Full Adder
def test_eight_bit_adder():
    adder = EightBitFullAdder()
    
    test_cases = [
        (0, 0),      # 0 + 0 = 0
        (15, 15),    # 15 + 15 = 30
        (255, 1),    # 255 + 1 = 256 (overflow)
        (100, 100),  # 100 + 100 = 200
    ]
    
    for num1, num2 in test_cases:
        bin1 = decimal_to_binary(num1)
        bin2 = decimal_to_binary(num2)
        
        sum_bits, carry = adder.compute(bin1, bin2)
        result = binary_to_decimal(sum_bits)
        
        expected = (num1 + num2) % 256  # 8-bit result wraps around
        assert result == expected
        assert carry == (1 if num1 + num2 > 255 else 0)

# Test binary conversion utilities
def test_binary_conversion():
    test_numbers = [0, 1, 15, 100, 255]
    
    for num in test_numbers:
        binary = decimal_to_binary(num)
        assert len(binary) == 8
        assert binary_to_decimal(binary) == num