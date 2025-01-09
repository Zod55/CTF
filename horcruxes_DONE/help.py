import re


def calculate_exp(text):
    # Use regex to find all numbers with optional + or - sign
    exp_values = re.findall(r'[+-]?\d+', text)
    
    # Convert strings to integers and sum only the EXP values
    total_exp = sum(int(value) for value in exp_values)
    
    # Print individual EXP values (Python 2 style)
    print("\nIndividual EXP values:")
    for value in exp_values:
        print("%12s" % value)  # Use % formatting for Python 2 compatibility
    print("-" * 20)
    print("Total EXP:  %12d" % total_exp)  # Format total EXP as integer
    
    return ((total_exp + 2**31) % 2**32) - 2**31 




if __name__ == "__main__":
 print("Enter your text (press Ctrl+D on Unix/Linux or Ctrl+Z on Windows followed by Enter when done):")
 user_input = []
 try:
     while True:
         line = input()
         user_input.append(line)
 except EOFError:
     text = '\n'.join(user_input)
     calculate_exp(text)
