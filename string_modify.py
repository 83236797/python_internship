


name = "my  name is VAISHNAVI"
print(name.lower())
name="satape"
print(name.upper())
name="LALALALALALALLALA"
print(name.lower())
name = '''                                                   this string containg whitespaces 
                               but why i dont know so that  i am removing it using strip() method'''
print(name.strip())
paragraph = " hey how are you, are you doing a wrong code, oops you must be replaced by using replace() method"
print(paragraph.replace("h", "o"))
team = "hello, team, pranav, gourav, snehal, vaishnavi, pratiksha, ganesh, we must split by any operator"


team_list = team.split(",")
print(team_list)
#['hello', ' team', ' pranav', ' gourav', ' snehal', ' vaishnavi', ' pratiksha', ' ganesh', ' we must split by any operator'] 
#must split by any operator
print(type(team_list))
#print(type(team))
print(team.split("."))
#print(type(team))

#team_list= team.split(",") te array dakhavte 

#concatenation of string

str1 = "Pranali"
str2 = "satape"
result= str1+str2
print (result)

space =" "
result = str1 + space + str2
print(result)

#string format method
name = "my name is Pranali, and i am {} years old, i like {}, my school is {}"
print(name.format(17, "dog","gpp")) #argument pass karu shakto

#name. sagle lihine te 
print(name.capitalize())
#string method assingment

#bool
print(bool()) #blank is always false
print(bool("is this true")) #
print(bool(1234))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
print(bool(False))
print(bool(None))




