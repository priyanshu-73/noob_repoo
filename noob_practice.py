# lex_auth_01269438070259712046

def count_names(name_list):
    count1 = 0
    count2 = 0
    a='at'
    for z in name_list:
        if a==z[-2:]:
            count1+=1
    print("_at -> ", count1)
    for i in name_list:
        if a in i:
            count2+=1
    print("%at% -> ", count2)





# Provide different names in the list and test your program
name_list = ["at","dats"]
count_names(name_list)