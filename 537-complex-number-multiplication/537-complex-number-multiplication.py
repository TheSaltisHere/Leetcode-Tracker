class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1_list=num1.split("+")
        num2_list=num2.split("+")
        real1=int(num1_list[0])
        real2=int(num2_list[0])
        imag1=int(num1_list[1][:len(num1_list[1])-1])
        imag2=int(num2_list[1][:len(num2_list[1])-1])
        real=real1*real2-imag1*imag2
        imag=real1*imag2+real2*imag1
        return(str(real)+"+"+str(imag)+"i")


