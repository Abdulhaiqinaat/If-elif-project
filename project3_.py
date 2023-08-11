'''You are applying for a scholarship. In order to qualify, you need to have at least a 3.0 GPA and a
1100 SAT score. Write a program that determines if the user qualifies for the scholarship or not.
Sample Program Run #1
What is your SAT score?
1140
What is your GPA?
3.7
Great, you qualify for the scholarship!'''

gpa=float(input("Enter your GPA= "))
if 3.0<=gpa<=3.5:
    print("Great, you will get a wii for your good grades! ")
elif 3.5<gpa<=3.8:
    print("Great, you will get a Kinect for your good grades!.")
elif gpa>3.8:
    print("Great, you will get a playstation for your good grades! ")
else:
    print("Sorry, you do not get a game system")