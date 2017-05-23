def print_call_func():
    print('call func')

def execute_another_function( func ):
    func()

execute_another_function(print_call_func)

def test ():
    return 'test'

print(type(test()))


print('----------------------------')



def return_print_function (msg):
    def print_msg (msg2):
        print(msg)
    
    return print_msg

f1 = return_print_function('이걸 출력해 주세요')

execute_another_function(f1('test'))

print('----------------------------')

