import sys

# Console color
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple

# print function definition
def print_error() :
    print(R + "ERROR : Re-run the program" + W)
    sys.exit(1)

def print_error_oorange() :
    print(R + "ERROR : CLK OUT OF RANGE!" + W)
    sys.exit(1)

def print_delimiter() :
    print(G + "###################################################" + W)

def print_intro() :
    print_delimiter()
    print(G + "############" + P, "PLL calculator ver 0.1", G + "###############" + W)
    print_delimiter()
    print("\r")

def print_step1() :
    print_delimiter()
    print(G + "Step1 : Device select" + W)
    print(G + "        CH2M = 2, CH4M = 4" + W)
    print_delimiter()

def print_step2():
    print_delimiter()
    print(G + "Step2 : Select pll 0 clock source" + W)
    print(G + "        irc,   xosc" + W)
    print(P + "             (default)" + W)
    print_delimiter()

def print_step3():
    print_delimiter()
    print(G + "Step3 : Select pll 1 clock source" + W)
    print(G + "        xosc,  pll0_phi1" + W)
    print(P + "               (default)" + W)
    print_delimiter()

def print_step4() :
    print_delimiter()
    print(G + "Step4 : Select system clock source" + W)
    print(G + "        irc,   xosc,   pll0,   pll1" + W)
    print(P + "                             (default)" + W)
    print_delimiter()

def print_step5() :
    print_delimiter()
    print(G + "Step5 : Specify target system clock" + W)
    print(G + "        CH2M = max. 120Mhz, CH4M = max. 180Mhz" + W)
    print_delimiter()

def print_step6() :
    print_delimiter()
    print(G + "Step6 : Calculation" + W)
    print_delimiter()

def print_step7() :
    print_delimiter()
    print(G + "Step7 : Result" + W)
    print(G + "        Suggestion (random) = s" + W)
    print(G + "        See all available   = a" + W)
    print_delimiter()

def print_result_pll0(num, mfd, prediv, rfdphi ) :
    print("[ PLL0 :",num,"th ] =>  MFD :"+B, mfd, W+"  PREDIV :"+B, prediv, W+"  RFDPHI"+B, rfdphi, W+"")

def print_result_pll1(num, mfd, prediv, rfdphi ) :
    print("[ PLL1 :",num,"th ] =>  MFD :"+B, mfd, W+"  PREDIV :"+B, prediv, W+"  RFDPHI"+B, rfdphi, W+"")
