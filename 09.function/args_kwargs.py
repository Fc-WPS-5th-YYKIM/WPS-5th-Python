def print_args(*args):
    print(args)


def print_kwargs(**kwargs):
    print(kwargs)

print_args('python', 'ruby', 'java')
print_args(language='python', ide='pycharm')

print_kwargs(language='python', ide='pycharm')
print_kwargs('python', 'ruby', 'java')

