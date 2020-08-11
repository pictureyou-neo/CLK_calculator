# Import area
import sys
from print_functions import *
from random import*

# Global variable
device = 0
result_pll0_phi = []
cnt_pass = 0
cnt_fail = 0

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
    else :
        print_error()

    if (min <= value) & (value <= max) :
        return True
    else :
        return False

def calc_pll0(ref_pll0, target) :

    for cnt_prediv in range(1, 9) :
        for cnt_rfdphi in range(1, 65) :
            for cnt_mfd in range(8, 129) :
                pll0_phi = ref_pll0 * (cnt_mfd / (cnt_prediv * cnt_rfdphi))
                # PASS
                if pll0_phi == target :
                    # print result
                    # print("PASS :", pll0_phi, cnt_mfd, cnt_prediv, cnt_rfdphi)
                    # save result
                    global result_pll0_phi
                    result_pll0_phi.append([pll0_phi, cnt_mfd, cnt_prediv, cnt_rfdphi])
                    global cnt_pass
                    cnt_pass += 1
                # FAIL
                else :
                    # print("FAIL : ",pll0_phi, cnt_mfd, cnt_prediv, cnt_rfdphi)
                    global cnt_fail
                    cnt_fail += 1
                    continue;

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
    print("Target system clock :" + B, target_sysclk, W + 'hz', "\n")

    # Step4 : receive clk source for pll 0
    print_step4()
    clk_source = input("What is your clock source for pll_0 ? : ")
    if clk_source == "xosc" :
        ref_freq = input("What is your xosc frequency? (in Mhz) : ")
        ref_freq = int(ref_freq) * 1000000
        print("Ref clock freq :" + B ,ref_freq, W + 'hz', "\n")
        result = check_range("xosc", ref_freq)
    elif clk_source == "irc" :
        ref_freq = 16000000
        print("Ref clock freq :" + B ,ref_freq, W + 'hz', "\n")
    else :
        print_error()
    if result == False: print_error_oorange()

    # Step5 : calculation
    print_step5()
    calc_pll0(ref_freq, target_sysclk)
    print("Total Calculation iteration : ", cnt_fail+cnt_pass)
    print("PASS case : " + B , cnt_pass)
    print(W + "FAIL case : ", cnt_fail, "\n")

    # Step6 : Result
    print_step6()
    select_result_view = input("How do you want to see the result? : ")
    len_result_pll0_phi = result_pll0_phi.__len__() # calculate the number of PASS
    if select_result_view == "s" :
        suggestion = randint(1, len_result_pll0_phi) # pick a number with random
        print("[ Target system clock ] =" + B, int(target_sysclk/1000000), W + 'Mhz')
        print_result(suggestion,result_pll0_phi[suggestion][1],result_pll0_phi[suggestion][2],result_pll0_phi[suggestion][3])
    elif select_result_view =="a" :
        print("[ Target system clock ] =" + B, int(target_sysclk/1000000), W + 'Mhz')
        for cnt in range(0, len_result_pll0_phi):
            print_result(cnt+1, result_pll0_phi[cnt][1], result_pll0_phi[cnt][2], result_pll0_phi[cnt][3])
    else :
        print_error()





