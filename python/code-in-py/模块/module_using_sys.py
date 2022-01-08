import sys#sys 模块module

print('The command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is',sys.path,'\n')

