from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

class Calculator:
    def __init__(self, raw_expression):
        self.raw_expression_str = raw_expression
        
        self.numbers_str = "0123456789"
        self.operator_str = "+-*/"
        self.point_str = "."
        
        self.expression_as_list = []
        
        self.number_before = False
        self.operator_before = False
        
        self.number = ""
        self.operator = ""
        self.addition, self.subtraction, self.multiplication, self.division = self.operator_str 
    
    
    def number_creator_inator(self):
        if self.number_before == False:
            if self.operator:
                self.expression_as_list.append(self.operator)
                self.operator = ""
                        
            self.number_before = True
            self.operator_before = False 

   
    def operator_creator_inator(self):
        if self.operator_before == False:
            if self.number:
                self.expression_as_list.append(self.number)
                self.number = ""
                    
            self.operator_before = True
            self.number_before = False
    
    def last_number_adder_inator(self):
        if self.number:
            self.expression_as_list.append(self.number)
            
        elif self.operator:
            raise ValueError("Expression can't end on operator")
    
    def tokeninator(self):
        for char in self.raw_expression_str:
            
            if char in self.numbers_str + self.point_str:
                self.number_creator_inator()
                self.number += char
            
            elif char in self.operator_str:
                self.operator_creator_inator()
                self.operator += char
            
            else:
                raise ValueError("Expression contains none math character")
            
        self.last_number_adder_inator()
    
        return self.expression_as_list

   
    def MD_error_intor(self, token):
        if (self.multiplication in token or self.division in token) and len(token) > 1:
            raise ValueError("Division and multiplication operators need to stand alone")
    
    def subtraction_counter_inator(self, token):
        subtraction_count = 0
                        
        for symbol in token:
            if symbol == self.subtraction:
                subtraction_count += 1
            
        return subtraction_count
    
    def subtraction_count_processor_inator(self, subtraction_count):  
        if subtraction_count % 2 == 0:
            new_char = "+"
            
        elif subtraction_count % 2 == 1:
            new_char = "-"
        
        return new_char
    
    def AS_combine_process_inator(self, token):
        if self.subtraction in token:
            subtraction_count = self.subtraction_counter_inator(token)
            return self.subtraction_count_processor_inator(subtraction_count)
                        
        elif self.addition in token:
            return "+"
        
        return token
         
    def symbol_combiner_inator(self):
        
        for i, token in enumerate(self.expression_as_list):
            if any(op in token for op in self.operator_str):
                self.MD_error_intor(token)
                
                if len(token) > 1:
                    self.expression_as_list[i] = self.AS_combine_process_inator(token) 
                     
        return self.expression_as_list
                                                                                                  
    
    def MD_starter_error_inator(self):
        if self.expression_as_list[0] in (self.multiplication, self.division):
            raise ValueError("Expression can't start with division or multiplication operators")
    
    def AS_starter_combiner_inator(self):
        if self.expression_as_list[0] in (self.addition, self.subtraction):
            new_first_char = self.expression_as_list[0] + self.expression_as_list[1]
            self.expression_as_list[0:2] = [new_first_char]
        
        return self.expression_as_list
    
    def pynum_convertor_inator(self):
        self.MD_starter_error_inator()
        self.AS_starter_combiner_inator()
        
        for i, token in enumerate(self.expression_as_list):
            
            try:
                if self.point_str in token:
                    converted_num = float(token)
                    
                    if converted_num.is_integer():
                        converted_num = int(converted_num)
                    
                else:
                    converted_num = int(token)
                    
                self.expression_as_list[i] = converted_num
                
            except ValueError:
                continue
            
        return self.expression_as_list
    
    def solution_passer(self, solution, position):
        self.expression_as_list[position - 1 : position + 2] = [solution]
    
    def MD_solve_processing_inator(self):
        i = 0
        
        while i < len(self.expression_as_list):
            token = self.expression_as_list[i]
            
            if token == self.multiplication:
                solution = self.expression_as_list[i - 1] * self.expression_as_list[i + 1]
                self.solution_passer(solution, i)
                i = 0
            
            elif token == self.division:
                if self.expression_as_list[i + 1] != 0:
                    solution = self.expression_as_list[i - 1] / self.expression_as_list[i + 1]
                    self.solution_passer(solution, i)
                    i = 0
                else:
                    raise ZeroDivisionError
            i += 1
                
        return self.expression_as_list
        
    def AS_solve_processing_inator(self):
        i = 0
        
        while i < len(self.expression_as_list):
            token = self.expression_as_list[i]
            
            if token == self.addition:
                solution = self.expression_as_list[i - 1] + self.expression_as_list[i + 1]
                self.solution_passer(solution, i)
                i = 0
                
            elif token == self.subtraction:
                solution = self.expression_as_list[i - 1] - self.expression_as_list[i + 1]
                self.solution_passer(solution, i)
                i = 0
                
            i += 1
            
    def calculation_inator(self):
        self.tokeninator()
        
        self.symbol_combiner_inator()
        
        self.pynum_convertor_inator()
        
        self.MD_solve_processing_inator()
        self.AS_solve_processing_inator()
        
        calculated_number = self.expression_as_list[0]
        
        return calculated_number
    
    
    def get_decimal_length_inator(self, number):
            float_len = len(str(number)) - 1
            return float_len
    
    def last_digit_round_inator(self, number):
        decimal_numbers = str(number).split(".")[1]
        round_number = len(decimal_numbers) - 1
        return round(number, round_number)
    
    
    def long_decimal_round_inator(self, calculated_number):
        rounded_num = calculated_number
        
        if isinstance(calculated_number, float):
            float_len = self.get_decimal_length_inator(calculated_number)
            
            if float_len > 10:
                shortend_float_str = str(calculated_number)[:12]
                rounded_num = self.last_digit_round_inator(float(shortend_float_str))
                
        return rounded_num
                         
    def solution_large_number_shortener_inator(self, number):
        truncated_num = int(number)
        truncated_num_len = len(str(truncated_num))
        was_long_num_shortend = False
        squring_num = None
        fitted_num = number
        
        if truncated_num_len > 10:
            squring_num = truncated_num_len - 1
            shortening_num = 10 ** squring_num
            
            fitted_num = number / shortening_num
            was_long_num_shortend = True
            
        return fitted_num, squring_num, was_long_num_shortend
    
    def formatting_long_number(self, calculated_number):
        fitted_num, squring_num, was_long_num_shortend = self.solution_large_number_shortener_inator(calculated_number)
        rounded_num = self.long_decimal_round_inator(fitted_num)
        
        return rounded_num, squring_num, was_long_num_shortend                          
                       
                                                         
@app.route("/", methods=["GET", "POST"])
def calculation():
    data = request.get_json()
    expression = data.get("expression")
    print(data)
    
    calc_expression = Calculator(expression)
    try:
        solution = calc_expression.calculation_inator()
        formatted_solution, squring_num, was_long_num_shortend = calc_expression.formatting_long_number(solution)
    except ValueError as e:
        return jsonify({"error": True, "message": "Syntax ERROR"}), 400
    
    except ZeroDivisionError:
        return jsonify({"error": True, "message": "Zero Division ERROR"}), 400
    
    return jsonify({
        "solution": formatted_solution,
        "squaringNum": squring_num,
        "wasShortend": was_long_num_shortend
    })
    
  
if __name__ == "__main__":
    app.run(debug=True) 