# Bitcoin Script Interpreter
 # 
 # Preconditions: String input with OP_*
 # 
 # Postconditions: Return value boolean

bitcoin_stack = []  # Python List to simulate a Bitcoin script stack

stack_progression = {} # Python Dict to simulate the progression at each stage of the Bitcoin script stack

def script_arguments_parse(opcodes_string):
    '''Parse the string, spaces separating'''
    args_list = opcodes_string.split(' OP_')
    args_list[0] = args_list[0].replace('OP_', '')
    print(args_list)
    return args_list

def script_runner(opcodes_list):
    return_bool = True
    for script_element in opcodes_list:
        print(script_element)
        print(bitcoin_stack)
        if script_element == 'ADD':
            ## call the op_add() function here, etc.
            return_bool = op_add()
        elif script_element == 'EQUAL':
            return_bool = op_equal()
        elif script_element == 'SUB':
            return_bool = op_sub()
        elif script_element.isnumeric():
            ## If it's not a function, and it's a numeric string, and push to the stack
            ## TIL: https://www.pythonpool.com/python-check-if-string-is-integer/
            print('Not an opcode')
            bitcoin_stack.append(script_element)
            print(bitcoin_stack)
        else:
            return_bool = "ERROR: That's not right."
    stack_results = bitcoin_stack
    stack_clear()
    return [return_bool, stack_results]

def op_add():
    '''Add the previous two arguments, remove them both from the stack, push the sum to the stack, return bool'''
    print('op_add running now')
    # Error Checking: make sure that there are even two previous values at all!
    print ('Length of the list bitcoin_stack is currently: ', len(bitcoin_stack))
    if len(bitcoin_stack) < 2:
        print('ERROR: op_add() says that the bitcoin_stack is less than 2. Returning False.')
        return False

    # Error Checking: make sure that the two previous values are integers
    back_two = bitcoin_stack[len(bitcoin_stack)-2]
    back_one = bitcoin_stack[len(bitcoin_stack)-1]
#    if not back_one.isnumeric() or not back_two.isnumeric():
#        print('ERROR: Both of the previous two elements were not integers')
#        return False
    sum = int(bitcoin_stack[len(bitcoin_stack)-2]) + int(bitcoin_stack[len(bitcoin_stack)-1])
    print('"Popping" the following element off of the stack: ', bitcoin_stack.pop())
    print('"Popping" the following element off of the stack: ', bitcoin_stack.pop())
    bitcoin_stack.append(sum)
    return True

def op_sub():
    '''Subtract the second argument from the previous, push the sum to the stack, return bool'''
    print('op_sub running now')
    difference = int(bitcoin_stack[len(bitcoin_stack)-2]) - int(bitcoin_stack[len(bitcoin_stack)-1])
    print('Popping ', bitcoin_stack.pop())
    print('Popping ', bitcoin_stack.pop())
    bitcoin_stack.append(difference)
    return difference

def op_equal(): 
    '''Evaluate whether the two arguments are equal, push 1 to the stack if equal, push zero to the stack if not, return a bool'''
    print ('op_equal running now')
    return_bool = -1
    print ('Before comparing for op_equal(), the stack is as follows: ', bitcoin_stack)
    if int(bitcoin_stack[len(bitcoin_stack)-2]) == int(bitcoin_stack[len(bitcoin_stack)-1]):
        print('Popping ', bitcoin_stack.pop())
        print('Popping ', bitcoin_stack.pop())
        bitcoin_stack.append(1)
        print(bitcoin_stack)
        return_bool = True
    elif int(bitcoin_stack[len(bitcoin_stack)-2]) != int(bitcoin_stack[len(bitcoin_stack)-1]):
        print ('op_equal() - Looks like these guys are not equal: ', int(bitcoin_stack[len(bitcoin_stack)-2]), int(bitcoin_stack[len(bitcoin_stack)-1]))
        print('Popping ', bitcoin_stack.pop())
        print('Popping ', bitcoin_stack.pop())
        bitcoin_stack.append(0)
        print(bitcoin_stack)
        return_bool = False
    else: 
        print('Something went wrong...')
        return_bool = 'SOMETHING IS WRONG'
    return_bool = is_top_zero(bitcoin_stack)
    return return_bool


def stack_clear():
    global bitcoin_stack 
    bitcoin_stack = []  # Simulate clearing a Bitcoin script stack
    return bitcoin_stack

def is_top_zero(stack_to_check):
    return_bool = -1
    top_stack_element_value = bitcoin_stack[-1:][0]
    print('The top_stack_element is ', top_stack_element_value)
    if top_stack_element_value == 0:
        return_bool = False
    elif isinstance(top_stack_element_value, int):
        return_bool = True
    else: print('top of the stack element is not an integer')
    return return_bool

def stackit(script_string):
    parsed_arguments = script_arguments_parse(script_string)
    result = script_runner(parsed_arguments)
    return result

def update_stack_progression(summary='OP', stack):
    print('Adding', stack, 'to stack progression, with summary', summary)
    stack_progression[summary] = stack
    

if __name__ == '__main__':
    
    parsed_arguments = script_arguments_parse('OP_1 OP_2 OP_3 OP_5 OP_1 OP_8 OP_16 OP_ADD OP_ADD')
    
    script_runner(parsed_arguments)
    
    print(bitcoin_stack)
    
