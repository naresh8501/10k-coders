''' Problem sovling questions Assignment-2

1->Check even or odd
->Determine whether a number is even or odd. Explanation: A number is even if it is divisible by 2. Otherwise, its odd.
->input=6 '''
# a=6
# if a%2==0:
#     print('Even Number')
# else:
#     print('Odd Number') 
# OUTPUT=Even Number

'''
2->Divisible by 5 but not by 10
->Check if a number is divisible by 5 but not by 10. Explanation: Use modulo (%) to check if the number % 5 == 0 and number % 10 != 0
->Input=25'''
# b=25
# if b%5==0 & b%10!=10:
#     print('Satisfy')
# OUTPUT=Satisfy

'''
3->Biggest among two numbers
->Find the biggest number among two. Explanation: Use comparison operators (>) to check which number is greater
->Input=A,B=4,7'''
# A=4
# B=7
# if A>B:
#     print('Biggest is :',A)
# else:
#     print('Biggest is:',B)
# OUTPUT=Biggest is:7

'''
4->Smallest among two numbers
->Find the smallest number among two. Explanation: Use comparison operators (<) to find the smaller value
->Input=A,B=4,7'''
# A=4
# B=7
# if A<B:
#     print('Smallest is:',A)
# else:
#     print('Smallest is:',B)
# OUTPUT=Smallest is:4

'''
5->Divisible by 2, 3, and 6
->Check if a number is divisible by 2, 3, and 6. Explanation: If a number is divisible by both 2 and 3, it is also divisible by 6
->Input=18'''
# a=18
# if a%2==0 & a%3==0 :
#     print('Satisfy')
# OUTPUT=Satisfy

'''
6->Voting Eligibility
>Check if a person is eligible to vote (age >= 18). Explanation: A person is eligible to vote if their age is 18 or above
->Input=19'''
# age=19
# if age>=18:
#     print('Eligible to vote')
# OUTPUT=Eligible to vote


'''7->Student Pass/Fail Based on All Subjects >= 35
->Check if a student passed all subjects (maths, physics, chemistry). Explanation: Student passes only if marks in all subjects are 35 or more
->Input=Maths,Physics,Chemistry=40,36,30'''
# Maths=40
# Physics=36
# Chemistry=30
# if Maths>=35 and Physics>=35 and Chemistry>=35:
#     print('Pass')
# else:
#     print('Fail')
# OUTPUT=Fail

'''8->Check if a student passed all subjects (maths, physics, chemistry). Explanation: Student passes only if marks in all subjects are 35 or more
->Check if the student passed any two out of three subjects. Explanation: Use a counter or logical conditions to verify two subjects >= 35
->Input=Maths=20,Physics=38,Chemistry=25'''
# M=20
# P=38
# C=25
# if M>=35 or P>=35 or C>=35:
#     print('Pass')
# OUTPUT=Pass

'''9->Student Pass if Passed Any Two Subjects
->Check if the student passed any two out of three subjects. Explanation: Use a counter or logical conditions to verify two subjects >= 35
->Input: Maths = 40, Physics = 20, Chemistry = 36 '''
# m=40
# p=20
# c=36
# if (m>35 and p>=35) or (p>35 and c>=35) or (c>35 and m>=35):
#     print('Pass')
# OUTPUT=Pass
    
'''10->Biggest Among Three Numbers
->Find the biggest number among three. Explanation: Compare each pair of numbers using if-else conditions
->Input=A = 7, B = 4, C = 9 '''
# A=7
# B=4
# C=9
# if A>B and A>C:
#     print('Biggest is :',A)
# elif B>A and B>C:
#     print('Biggest is:',B)
# else:
#     print('Biggest is:',C)
# OUTPUT=Biggest is:9

'''11->Smallest Among Three Numbers
->Find the smallest number among three. Explanation: Use comparison logic to determine the minimum value
->Input:-A = 7, B = 4, C = 9 '''
# A=7
# B=4
# C=9
# if A<B and A<C:
#     print('Smallest is:',A)
# elif B<A and B<C:
#     print('Smallest is :',B)
# else:
#     print('Smallest is:',C)
# OUTPUT=Smallest is:4


'''12. Perfect Square or Not
->Check if a number is a perfect square. Explanation: A number is a perfect square if the square of its square root equals the number
->Number = 49 '''
# Number=49
# B=Number**0.5
# if int(B)**2==Number:
#     print('Square number')
# OUTPUT=Square number

'''13. Cars Required for Members (Max 5 per car)
->Calculate how many cars are needed for a given number of people
->Members = 17 '''
# Members=17
# if Members%5==0:
#     print('Cars needed:',Members//5)
# else:
#     print('Cars needed:',(Members//5)+1)
# OUTPUT=Cars needed:4

'''14. Second Biggest Among Three Numbers
->Find the second largest number among three inputs. Explanation: Use sorting or nested conditions to find the second largest value
->Input:A=10,B=25,C=18 '''
# A=10
# B=25
# C=18
# if (A>B and A<C) or (A<B and A>C):
#     print('Second biggest:',A)
# elif (B>A and B<C) or (B<A and B>C):
#     print('second biggest is:',B)
# else:
#     print('second biggest is:',C)
# OUTPUT=second biggest is:18

'''15. Leap Year or Not
->Check if a given year is a leap year
->Input: Year = 2024 '''
# Year=2024
# if (Year%400==0) or (Year%4==0 and Year%100!=0):
#     print('Leap year')
# else:
#     print('Not a leap year')
# OUTPUT=Leap year

#                           ----------***---------