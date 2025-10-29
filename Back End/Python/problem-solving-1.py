# Interview-Style Programming Questions: Basic Math and Logic
# Asssignment 1

#  Q1.Calculate the area of a square
# input: 5
side=20
print("Area of square:",side*side) 
# Output: Area of square: 400 

# Q4.Calculate the perimeter of a square
# Input: Side=4
side=4
print('Perimeter of square',4*side)
# Output:Perimeter of square 16

# Q2.Calculate the area of a rectangle
# Input: length=6 Breadth=4
length=20
breadth=30
print('Area of rectangle:',length*breadth)
# Output:Area of rectangle: 600

# Q5.Calculate the perimeter of a rectangle
# Input:Length=5 breadth=3
length=5
breadth=3
print('Perimeter of rectangle:',2*(length+breadth))
# Output:Perimeter of rectangle: 16


# Q3.Area of triangle
base=30
height=50
print('Area of triangle:',1/2*base*height)
# Output:Area of triangle: 750.0

# Q6.Calculate the perimeter of a triangle
# Input:side1=5 side2=6 side3=7
side2=6
side1=5
side3=7
print('Perimeter of triangle:',side1+side2+side3)
# Output:Perimeter of triangle: 18

# Q7.Break the total amount into denominations
# Input: Amount=3700
Amount=3700
Thousands=3700//1000
c=Amount%1000
Hundreds=c//500
Remaining_amount=c%500
print('Thousands are:',Thousands,'Hundreds are:',Hundreds,'Remaining amount:',Remaining_amount)
# Output:- Thousands are: 3 Hundreds are: 1 Remaining amount: 200


# Q8.Convert total seconds into hours, minutes, and seconds
# Input:Total_seconds=3672
Total_seconds=3672
Hours=Total_seconds//(60*60)
Minutes=Total_seconds//(60*60)
Seconds=Total_seconds%60
print('Hours:',Hours,'Minutes:',Minutes,'Seconds:',Seconds)


# Q9.Calculate the sum of marks in 3 subjects
# Input:Maths=85 Physiscs=90 Chemistry=88
Maths=85
Physics=90
Chemistry=88
Sum=Maths+Physics+Chemistry
print('Sum of all subjects:',Sum)
# Output:Sum of all subjects: 263

# Q10.Calculate the average of marks in 3 subjects
# Input:Maths=85 Physics=90 Chemistry=88
Maths=85
Physics=90
Chemistry=88
Sum=Maths+Chemistry+Physics
Average=Sum/3
print('Average marks:',Average)
# output:Average marks: 87.66666666666667