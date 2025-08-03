from app import Calculator
import pytest


def test_normal_expression():
    calc = Calculator("5++375*45+2")
    tokenized = calc.tokeninator()
    assert tokenized == ["5", "++", "375", "*", "45", "+", "2"]

def test_ending_operator():
    calc = Calculator("5++375*45+2+")
    with pytest.raises(ValueError):
        calc.tokeninator()

def test_end_point():
    calc = Calculator("5++375*45+2.")
    tokenized = calc.tokeninator()
    assert tokenized == ["5", "++", "375", "*", "45", "+", "2."]


def test_normal_combine():
    calc  = Calculator("")
    calc.expression_as_list = ["5", "++", "375", "*", "45", "+", "2"]
    combined = calc.symbol_combiner_inator()
    assert combined == ["5", "+", "375", "*", "45", "+", "2"]

def test_start_combine():
    calc = Calculator("")
    calc.expression_as_list = ["---", "5", "++", "375", "*", "45", "+", "2"]
    combined = calc.symbol_combiner_inator()
    assert combined == ["-", "5", "+", "375", "*", "45", "+", "2"]

def test_minus_to_plus():
    calc = Calculator("")
    calc.expression_as_list = ["----", "5", "++", "375", "*", "45", "+", "2"]
    combined = calc.symbol_combiner_inator()
    assert combined == ["+", "5", "+", "375", "*", "45", "+", "2"]

def test_multiplication_error():
    calc = Calculator("")
    token = "***"
    with pytest.raises(ValueError):
        calc.MD_error_intor(token)

def test_combine_first():
    calc = Calculator("")
    calc.expression_as_list = ["+", "5"]
    combined = calc.AS_starter_combiner_inator()
    assert combined == ["+5"]

def test_starting_MD():
    calc = Calculator("")
    calc.expression_as_list = ["/", "5", "+", "375", "*", "45", "+", "2"]
    with pytest.raises(ValueError):
        calc.MD_starter_error_inator()

def test_number_conversion():
    calc = Calculator("")
    calc.expression_as_list = ["+", "5", "/", "5.0"]
    changed = calc.pynum_convertor_inator()
    assert changed == [5, "/", 5.0]

def test_normal_MD_processing():
    calc = Calculator("")
    calc.expression_as_list = [5, "*", 6, "/", 4]
    solution = calc.MD_solve_processing_inator()
    assert solution == [7.5]
    
def test_normal_calculation():
    calc = Calculator("5++375*45+2")
    solution = calc.calculation_inator()
    assert solution == 16882

def test_decimal_calculation():
    calc = Calculator("4/5")
    solution = calc.calculation_inator()
    assert solution == 0.8

def test_no_math_calculation():
    calc = Calculator("500")
    solution = calc.calculation_inator()
    assert solution == 500

def test_normal_shortend_num():
    calc = Calculator("")
    shortend_num = calc.solution_large_number_shortener_inator(10000000000)
    assert shortend_num == (1, 10, True)

def test_long_shortend_num():
    calc = Calculator("")
    shortend_num = calc.solution_large_number_shortener_inator(1000000000000000000000000)
    assert shortend_num == (1, 24, True)

def test_normal_long_decimal():
    calc = Calculator("")
    rounded_num = calc.long_decimal_round_inator(10000.666666)
    assert rounded_num == 10000.66667


def test_long_after_point():
    calc = Calculator("")
    rounded_num = calc.long_decimal_round_inator(1.6666666666)
    assert rounded_num == 1.666666667

def test_long_after_point_to_whole():
    calc = Calculator("")
    rounded_num = calc.long_decimal_round_inator(1.99999999999)
    assert rounded_num == 2

    
def test_long_num_formatted():
    calc = Calculator("")
    formatted_solution = calc.formatting_long_number(123456789111222333)
    assert formatted_solution == (1.234567891, 17, True)

def test_no_format_num():
    calc = Calculator("")
    formatted_solution = calc.formatting_long_number(500)
    assert formatted_solution == (500, None, False)

def test_long_decimal_num():
    calc = Calculator("")
    formatted_solution = calc.formatting_long_number(5000.78998785)
    assert formatted_solution == (5000.789988, None, False)