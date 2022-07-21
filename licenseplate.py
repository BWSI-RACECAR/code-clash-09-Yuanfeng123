"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #9 - License Plate (licenseplate.py)


Author: Wonjun Lee

Difficulty Level: 5/10

Prompt: Jon was speeding on the highway with his RACECAR, and the highway camera has taken a picture 
of the RACECAR’s number plate. However, some characters on the plate are blurry. Please write a function 
that returns the number of possible combinations of the number plate. The number plate for his RACECAR
consists of 7 distinct characters, starting with 3 distinct alphabets and ending with 4 distinct numbers. 
The input will be passed as a string and any blurred characters will be written as ‘.’

Test Cases: 
Input: “ABC123.” ; Output: 7
Input: “.ON0123” ; Output: 24
Input: “.BC.234” ; Output: 168
"""

from re import T


class Solution:
    def licensePlate(self,str):
        # type str: string
        # return: int
        
        # TODO: Write code below to return an int with the solution to the prompt
        alphabetPart = str[0:3]
        numPart = str[3:]
        c1 = alphabetPart.count(".")
        c2 = numPart.count(".")
        t1 = 1
        t = 0
        for i in range(c1):
            t1 *= 26-t
            t+=1
        t2 = 1
        t = 0
        for i in range(c2):
            t2 *= 10 - t
            t += 1
        return t1*t2


        # if "." in alphabetPart: 
        #     c1 = alphabetPart.count(".")
        #     if "." in numPart:
        #         c2 = numPart.count(".")
        #         return (26 - (len(alphabetPart) - c1)) * (10 - (len(numPart) - c2))
        #     else:
        #         return 26 - (len(alphabetPart) - c1)
        # elif "." in numPart:
        #     c1 = numPart.count(".")
        #     if "." in alphabetPart:
        #         c2 = alphabetPart.count(".")
        #         return (26 - (len(alphabetPart) - c1)) * (10 - (len(numPart) - c2))
        #     else:
        #         return 10 - (len(numPart) - c1)

def main():
    string1 = input()
    tc1 = Solution()
    ans = tc1.licensePlate(string1)
    print(ans)

if __name__ == "__main__":
    main()