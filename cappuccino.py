#!/usr/bin/env python3
"""
Cappuccino Code - A Simple Programming Language
A lightweight, easy-to-learn programming language for beginners
"""

import sys
import re
import os

class CappuccinoInterpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {}
        
    def run(self, code):
        lines = code.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            # Skip empty lines and comments
            if not line or line.startswith('//'):
                i += 1
                continue
            
            # Handle function definitions
            if line.startswith('func '):
                func_name, func_body, lines_consumed = self.parse_function(lines[i:])
                self.functions[func_name] = func_body
                i += lines_consumed
                continue
            
            # Handle loops
            if line.startswith('repeat '):
                loop_body, lines_consumed = self.parse_block(lines[i:])
                times = self.evaluate(line.split('repeat')[1].split('{')[0].strip())
                for _ in range(int(times)):
                    for body_line in loop_body:
                        if body_line.strip():
                            self.execute_line(body_line)
                i += lines_consumed
                continue
            
            # Handle if statements
            if line.startswith('if '):
                condition = line.split('if')[1].split('{')[0].strip()
                if_body, lines_consumed = self.parse_block(lines[i:])
                if self.evaluate_condition(condition):
                    for body_line in if_body:
                        if body_line.strip():
                            self.execute_line(body_line)
                i += lines_consumed
                continue
            
            self.execute_line(line)
            i += 1
    
    def parse_block(self, lines):
        """Parse a block of code inside { }"""
        body_lines = []
        i = 1
        brace_count = 1
        
        while i < len(lines) and brace_count > 0:
            line = lines[i]
            if '{' in line:
                brace_count += line.count('{')
            if '}' in line:
                brace_count -= line.count('}')
            
            if brace_count > 0:
                body_lines.append(line)
            i += 1
        
        return body_lines, i
    
    def parse_function(self, lines):
        # Parse: func name(params) { body }
        first_line = lines[0].strip()
        match = re.match(r'func\s+(\w+)\s*\((.*?)\)\s*{', first_line)
        if not match:
            raise SyntaxError(f"Invalid function definition: {first_line}")
        
        func_name = match.group(1)
        params = [p.strip() for p in match.group(2).split(',') if p.strip()]
        
        body_lines, lines_consumed = self.parse_block(lines)
        
        return func_name, {'params': params, 'body': body_lines}, lines_consumed
    
    def evaluate_condition(self, condition):
        """Evaluate a condition like 'x == 5' or 'name is Alice'"""
        condition = condition.strip()
        
        # Handle 'is' comparison
        if ' is ' in condition:
            left, right = condition.split(' is ', 1)
            left_val = self.evaluate(left.strip())
            right_val = self.evaluate(right.strip())
            return str(left_val) == str(right_val)
        
        # Handle 'not' comparison
        if ' not ' in condition:
            left, right = condition.split(' not ', 1)
            left_val = self.evaluate(left.strip())
            right_val = self.evaluate(right.strip())
            return str(left_val) != str(right_val)
        
        # Handle numeric comparisons
        for op in ['>=', '<=', '>', '<', '==', '!=']:
            if op in condition:
                left, right = condition.split(op, 1)
                left_val = self.evaluate(left.strip())
                right_val = self.evaluate(right.strip())
                
                try:
                    left_val = float(left_val)
                    right_val = float(right_val)
                except:
                    pass
                
                if op == '==':
                    return left_val == right_val
                elif op == '!=':
                    return left_val != right_val
                elif op == '>':
                    return left_val > right_val
                elif op == '<':
                    return left_val < right_val
                elif op == '>=':
                    return left_val >= right_val
                elif op == '<=':
                    return left_val <= right_val
        
        # Just evaluate as truthy
        return bool(self.evaluate(condition))
    
    def execute_line(self, line):
        # say "text" - print text
        if line.startswith('say '):
            self.cmd_say(line[4:])
        
        # ask "prompt" -> variable - get input
        elif ' = ask ' in line:
            var_name = line.split('=')[0].strip()
            prompt = line.split('ask')[1].strip()
            self.cmd_ask(var_name, prompt)
        
        # wait seconds - pause execution
        elif line.startswith('wait '):
            import time
            seconds = self.evaluate(line[5:].strip())
            time.sleep(float(seconds))
        
        # clear - clear screen
        elif line == 'clear':
            os.system('cls' if os.name == 'nt' else 'clear')
        
        # random min max -> variable
        elif ' = random ' in line:
            import random
            var_name = line.split('=')[0].strip()
            range_part = line.split('random')[1].strip()
            parts = range_part.split()
            min_val = int(self.evaluate(parts[0]))
            max_val = int(self.evaluate(parts[1]))
            self.variables[var_name] = random.randint(min_val, max_val)
        
        # variable = value - assignment
        elif '=' in line and not any(op in line for op in ['==', '!=', '<=', '>=']):
            parts = line.split('=', 1)
            var_name = parts[0].strip()
            value = self.evaluate(parts[1].strip())
            self.variables[var_name] = value
        
        # Function call
        elif '(' in line and ')' in line:
            self.call_function(line)
    
    def cmd_say(self, text):
        # Remove quotes if present
        text = text.strip()
        if (text.startswith('"') and text.endswith('"')) or (text.startswith("'") and text.endswith("'")):
            text = text[1:-1]
        else:
            # It's a variable or expression
            text = str(self.evaluate(text))
        print(text)
    
    def cmd_ask(self, var_name, prompt):
        prompt = prompt.strip()
        if (prompt.startswith('"') and prompt.endswith('"')) or (prompt.startswith("'") and prompt.endswith("'")):
            prompt = prompt[1:-1]
        user_input = input(prompt)
        
        # Try to convert to number if possible
        try:
            if '.' in user_input:
                self.variables[var_name] = float(user_input)
            else:
                self.variables[var_name] = int(user_input)
        except ValueError:
            self.variables[var_name] = user_input
    
    def evaluate(self, expr):
        expr = expr.strip()
        
        # String literal
        if (expr.startswith('"') and expr.endswith('"')) or (expr.startswith("'") and expr.endswith("'")):
            return expr[1:-1]
        
        # Number
        try:
            if '.' in expr:
                return float(expr)
            return int(expr)
        except ValueError:
            pass
        
        # Variable
        if expr in self.variables:
            return self.variables[expr]
        
        # Math expression with variables
        try:
            # Replace variables in expression
            eval_expr = expr
            for var, val in self.variables.items():
                # Use word boundaries to avoid replacing partial matches
                eval_expr = re.sub(r'\b' + re.escape(var) + r'\b', str(val), eval_expr)
            return eval(eval_expr)
        except:
            return expr
    
    def call_function(self, line):
        match = re.match(r'(\w+)\s*\((.*?)\)', line)
        if match:
            func_name = match.group(1)
            args = [self.evaluate(arg.strip()) for arg in match.group(2).split(',') if arg.strip()]
            
            if func_name in self.functions:
                func = self.functions[func_name]
                # Save current variables
                old_vars = self.variables.copy()
                
                # Set parameters
                for param, arg in zip(func['params'], args):
                    self.variables[param] = arg
                
                # Execute function body
                for body_line in func['body']:
                    if body_line.strip():
                        self.execute_line(body_line)
                
                # Restore variables
                self.variables = old_vars

def main():
    if len(sys.argv) < 2:
        print("☕ Cappuccino Code Interpreter")
        print("Usage: cap <filename.capu>")
        print("\nOr run in REPL mode:")
        print("Enter code line by line, type 'run' to execute, 'exit' to quit\n")
        
        interpreter = CappuccinoInterpreter()
        code_buffer = []
        
        while True:
            try:
                line = input(">>> " if not code_buffer else "... ")
                if line.strip() == 'exit':
                    break
                elif line.strip() == 'run':
                    interpreter.run('\n'.join(code_buffer))
                    code_buffer = []
                else:
                    code_buffer.append(line)
            except KeyboardInterrupt:
                print("\n\nExiting...")
                break
            except Exception as e:
                print(f"Error: {e}")
                code_buffer = []
    else:
        filename = sys.argv[1]
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                code = f.read()
            
            interpreter = CappuccinoInterpreter()
            interpreter.run(code)
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found")
        except Exception as e:
            print(f"Error: {e}")
            import traceback
            traceback.print_exc()

if __name__ == '__main__':
    main()
