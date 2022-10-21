import re

#Generates base query
def genQuery(uName, password):
   print(f"SELECT * FROM users WHERE username='{uName}' and password='{password}';\n")

#generates queries with weak mitigation techniques
def genQueryWeak(uName, password):
   print("BASE QUERY")
   print(f"SELECT * FROM users WHERE username='{uName}' and password='{password}';")
   print("WEAK MITIGATION QUERY")
   #!!!sanitize both name and password before building query
   cleanUname = sanitizeString(uName)
   cleanPassword = sanitizeString(password)
   print(f"SELECT * FROM users WHERE username='{cleanUname}' and password='{cleanPassword}';\n")

#generates queries with strong mitigation techniques
def genQueryStrong(uName, password):
   print("BASE QUERY")
   print(f"SELECT * FROM users WHERE username='{uName}' and password='{password}';")
   print("STRONG MITIGATION QUERY")
   #reducing strings to lower and sanitizing the string
   str.lower(uName)
   #by changing the way the query is setup and only getting the information needed 
   #closes a lot of holes as well as allowing passowrds to be more complex
   print(f"SELECT password FROM users WHERE username='{sanitizeString(uName)}';\n")

#sanitize string following rule "username and the password consist of letters, numbers, and underscores"
def sanitizeString(string):
   cleanString = re.sub(r'[^a-zA-Z0-9_]', '', string)
   return cleanString

#run valid test cases  !!! need everyone in team to create 1 set for each test set per instructions !!!
def testValid(queryGen):
   validTests = [["]Austin", "pass123"],
   ["FrEd", "SuperSecure"],
   ["Brad", "CrayCray"],
   ["Daniel", "passpass321"],
   ["Spencer", "123456789"]]
   print("----  VALID TESTS    ----\n")
   for validTest in validTests:
      queryGen(validTest[0], validTest[1])
   print("--------------------\n")

#run tautology test cases
def testTautology(queryGen):
   tautologyTests = [["test", "' or 1=1 --"],
   ["test", "' or 1=1 --"],
   ["test", "' or 1=1 --"],
   ["test", "' or 1=1 --"],
   ["test", "' or 1=1 --"]]
   print("----  TAUTOLOGY TESTS    ----\n")
   for tautologyTest in tautologyTests:
      queryGen(tautologyTest[0], tautologyTest[1])
   print("--------------------\n")

#run union test cases
def testUnion(queryGen):
   unionTests = [["test", "' UNION SELECT * from secrets --"],
   ["test", "' union select * from secrets --"],
   ["test", "' union select * from secrets --"],
   ["test", "' union select * from secrets --"],
   ["test", "' union select * from secrets --"]]
   print("----  UNION TESTS    ----\n")
   for unionTest in unionTests:
      queryGen(unionTest[0], unionTest[1])
   print("--------------------\n")

#run additional statement test cases
def testAddState(queryGen):
   addStatementTests = [["test", "'; delete * from users where ''='"],
   ["test", "'; delete * from users where ''='"],
   ["test", "'; delete * from users where ''='"],
   ["test", "'; delete * from users where ''='"],
   ["test", "'; delete * from users where ''='"]]
   print("----  ADD STATEMENT TESTS    ----\n")
   for addStatmentTest in addStatementTests:
      queryGen(addStatmentTest[0], addStatmentTest[1])
   print("--------------------\n")

#run comment test cases
def testComment(queryGen):
   commentTests = [["test ' --", ""],
   ["test ' --", ""],
   ["test ' --", ""],
   ["test ' --", ""],
   ["test ' --", ""]]
   print("----  COMMENT TESTS    ----\n")
   for commentTest in commentTests:
      queryGen(commentTest[0], commentTest[1])
   print("--------------------\n")

#manual test option
def manual_test():
   username = input("What Username would you like use? ")
   password = input("What Password would you like to use? ")
   while(True):
      san = input("What type of Sanitizer would you like to use? Strong or Weak (s/w)")
      if san.lower() =="strong" or san.lower() =="s":
         genQueryStrong(username, password)
         break
      elif san.lower() =="weak" or san.lower() =="w":
         genQueryWeak(username, password)
         break
      else:
         print("Invalid input")
         continue
    
#run tests through query generator
def run_Tests(queryGen):
   testValid(queryGen)
   testTautology(queryGen)
   testUnion(queryGen)
   testAddState(queryGen)
   testComment(queryGen)

#basic menu function
def menu():
   while (True):
      print("Types of tests:")
      print("\t 1: Base Query Results")
      print("\t 2: Weak Mitigation Results")
      print("\t 3: Strong Mitigation Results")
      print("\t 4: Manual Input")
      test_type = int(input("Type which test to run: "))
      if test_type == 1:
         run_Tests(genQuery)
      elif test_type == 2:
         run_Tests(genQueryWeak)
      elif test_type == 3:
         run_Tests(genQueryStrong)
      elif test_type == 4:
         manual_test
      else:
         print("Invalid input\n")
         continue

#program run point
menu()