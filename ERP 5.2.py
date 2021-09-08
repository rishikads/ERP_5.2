professors={}
for i in range(2019, 2022):
  print("year "+ str(i))
  year=i
  N=int(input("Enter the number of students "))
  a_F1=int(input("Number of Available Professors "))
  a_F2=int(input("Number of Associate Professors "))
  a_F3=int(input("Number of Assistant professors "))
  r_F1=1/9*((N/15))
  r_F2=2/9*((N/15))
  r_F3=6/9*((N/15))
  r_F1=round(r_F1)
  r_F2=round(r_F2)
  r_F3=round(r_F3)
  print("Number of professors required in " + str(i) + "=" + str(r_F1))
  print("Number of Associate professors required in " + str(i)+ "=" + str(r_F2))
  print("Number of Assistant professors required in " + str(i)+ "=" + str(r_F3))
  professors[i]={}
  professors[i]['Students']=N
  professors[i]['Available_professors']=a_F1
  professors[i]['Available_associate_professors']=a_F2
  professors[i]['Available_assistant_professors']=a_F3
  professors[i]['Required_professors']=r_F1
  professors[i]['Required_associate_professors']=r_F2
  professors[i]['Required_assistant_professors']=r_F3
  print(" ")
avg_a_F1=(professors[2019]['Available_professors']+professors[2020]['Available_professors']+professors[2021]['Available_professors'])/3
avg_a_F2=(professors[2019]['Available_associate_professors']+professors[2020]['Available_associate_professors']+professors[2021]['Available_associate_professors'])/3
avg_a_F3=(professors[2019]['Available_assistant_professors']+professors[2020]['Available_assistant_professors']+professors[2021]['Available_assistant_professors'])/3
avg_r_F1=(professors[2019]['Required_professors']+professors[2020]['Required_professors']+professors[2021]['Required_professors'])/3
avg_r_F2=(professors[2019]['Required_associate_professors']+professors[2020]['Required_associate_professors']+professors[2021]['Required_associate_professors'])/3
avg_r_F3=(professors[2019]['Required_assistant_professors']+professors[2020]['Required_assistant_professors']+professors[2021]['Required_assistant_professors'])/3
avg_a_F1=round(avg_a_F1)
avg_a_F2=round(avg_a_F2)
avg_a_F3=round(avg_a_F3)
avg_r_F1=round(avg_r_F1)
avg_r_F2=round(avg_r_F2)
avg_r_F3=round(avg_r_F3)
print("Average available professors="+str(avg_a_F1))
print("Average available associate professors="+str(avg_a_F2))
print("Average available assistant professors="+str(avg_a_F3))
print("Average required assistant professors="+str(avg_r_F1))
print("Average required assistant professors="+str(avg_r_F2))
print("Average required assistant professors="+str(avg_r_F3))
professors['avg']={}
professors['avg']['Average_available_professors']=avg_a_F1
professors['avg']['Average_available_assistant_professors']=avg_a_F2
professors['avg']['Average_available_associate_professors']=avg_a_F3
professors['avg']['Average_required_professors']=avg_r_F1
professors['avg']['Average_required_assistant_professors']=avg_r_F2
professors['avg']['Average_required_assosiate_professors']=avg_r_F3

if avg_a_F1==avg_a_F2==0:
    CRD=0
else:
    CRD=((avg_a_F1/avg_r_F1)+((avg_a_F2*0.6)/avg_r_F2)+((avg_a_F3*0.4)/avg_r_F3))*12.5
if CRD>25:
    CRD=25
professors['CRD']=CRD
print("Cadre Ratio Marks "+str(CRD))
print(professors)






