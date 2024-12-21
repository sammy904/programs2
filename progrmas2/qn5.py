a = float(input("Enter marks for Subject 1: "))
b = float(input("Enter marks for Subject 2: "))
c = float(input("Enter marks for Subject 3: "))
d = float(input("Enter marks for Subject 4: "))
total_marks = a + b + c + d
percentage = (total_marks / 400) * 100
if percentage > 70:
  print("distinction")
elif percentage > 60:
  print("First")
elif percentage > 40:
  print("pass")
else:
  print("fail")