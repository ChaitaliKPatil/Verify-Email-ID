from re import*
#regular expression object
pattern=compile('(^|\s)[a-z0-9-_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')
#beginning a function definition by requesting user input and attempt to match that with the pattern
def get_address():
    address=input('Enter Your Email Address: ')
    is_valid=pattern.match(address)
    # add indented statements to display an appropriate message describing whether the attempt succeeded
    if is_valid:
        print('Valid Address: ',is_valid.group())
    else:
        print('Invalid Address! Please Retry...\n')
get_address()
