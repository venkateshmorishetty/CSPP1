'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    string = input()
    count = len(string)
    i = 0
    res = ''
    while i < count:
        if string[i] in ("!", "@", "#", "$", "%", "^", "&", "*"):
            res += " "
        else:
            res += string[i]
        i = i+1
    print(res)
if __name__ == "__main__":
    main()
