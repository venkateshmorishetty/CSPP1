'''Guess My Number Exercise'''

def main():
    '''guessing number'''
    print("guess a no")
    mid = 50
    high = 100
    low = 0
    inp = 'l'
    while mid >= 0.01:
        print(mid)
        inp = input()
        if inp == 'h':
            high = mid
            mid = (high+low)//2
        elif inp == 'l':
            low = mid
            mid = (high+low)//2
    print("your guess number is:", mid)
if __name__ == "__main__":
    main()
