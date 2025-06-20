def shrink(s):
    print(s[:8])

def enlarge(s):
    print(s + 'z' * (8 -len(s)))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        exit() 

    for arg in sys.argv) ==1:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)