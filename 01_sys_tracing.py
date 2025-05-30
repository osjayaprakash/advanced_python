import sys

def trace_calls(frame, event, arg):
    if event == 'call':
        func_name = frame.f_code.co_name
        arg_names = frame.f_code.co_varnames[:frame.f_code.co_argcount]
        args = [frame.f_locals[name] for name in arg_names]
        print(f"Call: {func_name}({', '.join(repr(arg) for arg in args)})")
    return trace_calls

def my_function(x):
    if x:
        return my_function(x[:-1])  +x[-1]
    return 0

def main():
    sys.settrace(trace_calls)
    result = my_function([5,3,4,5])
    print(f"Result: {result}")
    sys.settrace(None) # Disable tracing

if __name__ == "__main__":
    main()

local _expected output = '''
Call: my_function([5, 3, 4, 5])
Call: my_function([5, 3, 4])
Call: my_function([5, 3])
Call: my_function([5])
Call: my_function([])
Result: 17
'''
