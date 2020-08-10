# Import area

# Function definition
def check_range(src, value) :
    # range check based on source
    if src == 'xosc' :
        min = 8000000
        max = 40000000
    elif src == "pll0_phi" :
        min = 10000000
        max = 100000000

    if (min <= value) & (value <= max) :
        return True
    else :
        return False


# Class definition

# Main
if __name__ == "__main__":
    target_sysclk = input("System clock? : ")
    result = check_range("xosc", 20000000)
    print(result)



