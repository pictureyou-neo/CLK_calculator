# Import area
import sys
from print_functions import print_error, print_error_oorange, print_delimiter, print_intro, print_step1, print_step2, print_step3, print_step4, print_calculation
from print_functions import W, R, G, O, B, P

# Global variable
device = 0

# Function definition

def check_device(mcu) :
    if mcu == 2 or mcu == 4 :
        return True
    else :
        return False

def check_target_sys_clk_src(src) :
    if src=="xosc" or src=="irc" or src=="pll0" or src=="pll1" :
        return True
    else :
        print_error()

def check_range(src, value) :
    # range check based on source
    if src == 'xosc' :
        min = 4000000
        max = 40000000
    elif src == "pll0_phi" :
        min = 10000000
        max = 100000000
    elif src == "sysclk" :
        min = 16000000
        max = 180000000

    if (min <= value) & (value <= max) :
        return True
    else :
        return False

# Class definition



# Main
if __name__ == "__main__":

    # Intro
    print_intro()

    # Step1 : receive device info
    print_step1()
    device = input("What is your device? : ")
    device = int(device)
    result = check_device(device)
    if result == False : print_error()
    print("MCU = " + B, "Chorus", device, "M", W + "", "\n")

    # Step2 : receive target system clock source
    print_step2()
    target_sysclk_src = input("Target system clock source? : ")
    check_target_sys_clk_src(target_sysclk_src)
    print("Target system clock source : " + B , target_sysclk_src, W + "", "\n")

    # Step3 : receive target system clock
    print_step3()
    target_sysclk = input("Target system clock? (in Mhz) : ")
    target_sysclk = int(target_sysclk) * 1000000
    result = check_range("sysclk", target_sysclk)
    if result == False: print_error_oorange()
    print("Target system clock :" + B, target_sysclk, W + 'Mhz', "\n")

    # Step4 : receive clk source for pll 0
    print_step4()
    clk_source = input("What is your clock source for pll_0 ? : ")
    if clk_source == "xosc" :
        ref_freq = input("What is your xosc frequency? (in Mhz) : ")
        ref_freq = int(ref_freq) * 1000000
        print("Ref clock freq :" + B ,ref_freq, W + 'Mhz')
        result = check_range("xosc", ref_freq)
    elif clk_source == "irc" :
        ref_freq = 16000000
        print("Ref clock freq :" + B ,ref_freq, W + 'Mhz')
    else :
        print_error()
    if result == False: print_error_oorange()

    # pll_0 auto calculation





