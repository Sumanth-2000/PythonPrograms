'''Eligibility for following companies based on
Skill Set
Projects
companies:
Evry
TCS
Infosys
zoho'''
skillset=str(input("Enter your skill: "))
projects=int(input("Enter the number of projects: "))
if skillset=="java" or  "c" and projects>=3:
    print("U can get job in Evry")
elif skillset=="java" or "python" and projects>=4:
    print("U can get job in Infosys")
elif skillset=="python" or  "c" and projects>=2:
    print("U can get job in TCS")
elif skillset=="cpp" or  "c" and projects>=3:
    print("U can get job in Zoho")
else:
    print("U can't get job in any of these companies")
