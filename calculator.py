# Import area
import sys
from print_functions import *
from random import*

# Global variable
Mhz = 1000000
device = 0
result_pll0_phi0 = []
cnt_pass = 0
cnt_fail = 0
cnt_fail_pll0_vco = 0
sysclk = 0
ref_freq_xosc = 0
target_sysclk = 0
target_pll0 = 0
target_pll1 = 0
frcdiv = 0

# Function definition

def check_device(mcu) :
    global sysclk
    if mcu == 2 or mcu == 4 :
        if mcu == 2 :
            sysclk = 120
        elif mcu == 4 :
            sysclk = 180
        else :
            print_error()
        return True
    else :
        return False

def check_target_sys_clk_src(src) :
    global target_sysclk, target_pll0, target_pll1
    if src=="xosc" or src=="irc" :
        return True
    elif src=="pll0":
        target_sysclk = target_pll0
        return True
    elif src=="pll1":
        target_sysclk = target_pll1
    else :
        print_error()

def check_range(src, value) :
    # range check based on source
    if src == 'xosc' :
        min = 8 * Mhz       # Pll0 input range min.
        max = 40 * Mhz      # XOSC input range max.
    elif src == "pll0_VCO":
        min = 600 * Mhz
        max = 1400 * Mhz
    elif src == "pll0_phi0" :
        min = 4.762 * Mhz   # pll0_phi0 output range min.
        max = 400 * Mhz     # pll0_phi0 output range max.
    elif src == "pll0_phi1":
        min = 20 * Mhz      # pll0_phi1 output range min.
        max = 175 * Mhz     # pll0_phi1 output range max.
    elif src == "pll1_input" :
        min = 37.5 * Mhz    # pll1 input range min.
        max = 87.5 * Mhz    # pll1 input range max.
    elif src == "pll1_VCO":
        min = 600 * Mhz
        max = 1400 * Mhz
    elif src == "pll1_output":
        min = 4.762 * Mhz   # pll1 output range min.
        max = sysclk * Mhz  # pll0_phi0 output range max.
    elif src == "sysclk" :
        min = 16 * Mhz      # IRC freq.
        max = sysclk * Mhz  # Sys max freq.
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
                pll0_phi0 = ref_pll0 * (cnt_mfd / (cnt_prediv * cnt_rfdphi))
                # PASS
                if pll0_phi0 == target :
                    # Check VCO range
                    pll0_vco = (ref_pll0 * cnt_mfd * 2) / cnt_prediv
                    result = check_range("pll0_VCO", pll0_vco)
                    if result == True :
                        # print result
                        # print("PASS :", pll0_phi0, cnt_mfd, cnt_prediv, cnt_rfdphi)
                        # save result
                        global result_pll0_phi0
                        result_pll0_phi0.append([pll0_phi0, cnt_mfd, cnt_prediv, cnt_rfdphi])
                        global cnt_pass
                        cnt_pass += 1
                    else :
                        global cnt_fail_pll0_vco
                        cnt_fail_pll0_vco += 1
                # FAIL
                else :
                    # print("FAIL : ",pll0_phi0, cnt_mfd, cnt_prediv, cnt_rfdphi)
                    global cnt_fail
                    cnt_fail += 1
                    continue;

    print("Total Calculation iteration : ", cnt_pass + cnt_fail_pll0_vco +cnt_fail)
    print("PASS case : " + B , cnt_pass)
    print(W + "FAIL(VCO) case : ", cnt_fail_pll0_vco)
    print("FAIL(SYS) case : ", cnt_fail, "\n")

def calc_pll1(ref_pll1, target) :
    global frcdiv

    pll1_phi = ref_pll1 * ((cnt_mfd + frcdiv/2^12) / (2 * cnt_rfdphi))

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

    # Step2 : receive clk source for pll 0
    print_step2()
    clk_source = input("What is your clock source for pll_0 ? : ")
    if clk_source == "xosc" or clk_source == "d":
        ref_freq_pll0 = input("What is your xosc frequency? (in Mhz) : ")
        ref_freq_pll0 = int(ref_freq_pll0) * Mhz
        ref_freq_xosc = ref_freq_pll0
        result = check_range("xosc", ref_freq_pll0)
    elif clk_source == "irc" :
        ref_freq_pll0 = 16 * Mhz
    else :
        print_error()
    if result == False: print_error_oorange()
    target_pll0 = input("Target PLL0 clock? (in Mhz) : ")
    target_pll0 = int(target_pll0) * Mhz
    print("Ref clock freq :" + B, ref_freq_pll0, W + 'hz')
    print("PLL0 target    :" + B, target_pll0, W + 'hz', "\n")

    # Step3 : receive clk soruce for pll 1
    print_step3()
    clk_source = input("What is your clock source for pll_1 ? : ")
    if clk_source == "xosc" :
        ref_freq_pll1 = ref_freq_xosc
    elif clk_source == "pll0_phi1" or clk_source == "d" :
        ref_freq_pll1 = target_pll0
    else :
        print_error()
    if result == False: print_error_oorange()
    target_pll1 = input("Target PLL1 clock? (in Mhz) : ")
    target_pll1 = int(target_pll1) * Mhz
    print("Ref clock freq :" + B, ref_freq_pll1, W + 'hz')
    print("PLL0 target    :" + B, target_pll1, W + 'hz', "\n")

    # Step4 : receive target system clock source
    print_step4()
    target_sysclk_src = input("Target system clock source? : ")
    if target_sysclk_src == "d" :
        target_sysclk_src = "pll1"
    check_target_sys_clk_src(target_sysclk_src)
    print("Target system clock source : " + B , target_sysclk_src, W + "", "\n")

    # Step5 : receive target system clock
    print_step5()
    # target_sysclk = input("Target system clock? (in Mhz) : ")
    # target_sysclk = int(target_sysclk) * Mhz
    result = check_range("sysclk", target_sysclk)
    if result == False: print_error_oorange()
    print("Target system clock :" + B, target_sysclk, W + 'hz', "\n")

    # Step6 : calculation
    print_step6()
    if target_sysclk_src == "xosc":
        print("No need to calculate PLL")
    elif target_sysclk_src == "irc":
        print("No need to calculate PLL")
    elif target_sysclk_src == "pll0":
        calc_pll0(ref_freq_pll0, target_sysclk)
        #calc_pll1(ref_freq_pll1, target_pll1)
    elif target_sysclk_src == "pll1":
        calc_pll0(ref_freq_pll0, target_pll0)
        #calc_pll1(ref_freq_pll1, target_sysclk)
    else :
        print_error()




    # calc_pll0(ref_freq_pll0, target_sysclk)
    # print("Total Calculation iteration : ", cnt_pass + cnt_fail_pll0_vco +cnt_fail)
    # print("PASS case : " + B , cnt_pass)
    # print(W + "FAIL(VCO) case : ", cnt_fail_pll0_vco)
    # print("FAIL(SYS) case : ", cnt_fail, "\n")

    # Step7 : Result
    print_step7()
    select_result_view = input("How do you want to see the result? : ")
    len_result_pll0_phi0 = result_pll0_phi0.__len__() # calculate the number of PASS
    if select_result_view == "s" :
        suggestion = randint(1, len_result_pll0_phi0) # pick a number with random
        print("[ Target system clock ] =" + B, int(target_sysclk/Mhz), W + 'Mhz')
        print_result_pll0(suggestion,result_pll0_phi0[suggestion][1],result_pll0_phi0[suggestion][2],result_pll0_phi0[suggestion][3])
    elif select_result_view =="a" :
        print("[ Target system clock ] =" + B, int(target_sysclk/Mhz), W + 'Mhz')
        for cnt in range(0, len_result_pll0_phi0):
            print_result_pll0(cnt+1, result_pll0_phi0[cnt][1], result_pll0_phi0[cnt][2], result_pll0_phi0[cnt][3])
    else :
        print_error()





