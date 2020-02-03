ini_dict = {"Kaushal":"RI","Neha":"Thalildar","Avinash":"VAO"}
print("initial dictionary : ", str(ini_dict))
inv_dict = {v: k for k, v in ini_dict.items()}
print("inverse mapped dictionary : ", str(inv_dict))