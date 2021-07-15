#Moumita Rahman Rimjhim
#15 July 2021

F_Name=input("First Name: ")
M_Name=input("Middle Name: ")
L_Name=input("Last Name: ")
Full_Name=f"{F_Name} {M_Name} {L_Name}"

#Using \n & \t
print(Full_Name)
print(F_Name,"\n",M_Name,"\t",L_Name)
print("\n Moumita \n\t Rahman \t Rimjhim \n")

#Left Strip
Name="     Rahman     "
n=Name.lstrip()
print("Moumita",n,"Rimjhim")

#Right Strip
n=Name.rstrip()
print("Moumita",n,"Rimjhim")

#Strip
n=Name.strip()
print("Moumita",n,"Rimjhim")
