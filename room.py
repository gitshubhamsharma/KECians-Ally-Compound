import json

def room_check(num,arr,dept):
  """
  It checks whether the Compound can be booked if it does not lie in the given timeframe.
  """
  if num in range(arr,dept): 
    return True
  else:
    return False






def on_choice():
  """
  It decides whether or not to continue Compound booking.
  """

  choice = 'wrong'
  while choice not in ['Y', 'N', 'y', 'n']:

    choice = input("Want to keep Adding People in Compound: (Y/N) ")

    if choice not in ['Y', 'N', 'y', 'n']:
      print("Sorry, I don't Understand Please Choose Y or N")

  if choice == 'Y' or choice == 'y':
    return True
  else:
    return False


def user_choice_arr():
  """
  Enters the user Input with validation on Login Time.
  """
  choice = 'wrong'
  acceptable_range = range(0,24)
  within_range = False

  #Two Conditions to check 
  #It should be a digit and within range
  while choice.isdigit() == False or within_range == False:
    choice = input("Please Enter LogIn Time (0-24): ")

    #Digit Check
    if not choice.isdigit():
      print("Sorry that is not a digit")

    #Range Check
    if choice.isdigit():
      if int(choice) in acceptable_range:
        within_range = True
      else:
        print("Sorry not in Acceptable Range")
        within_range = False
  return int(choice)

def user_choice_dept():
  """
  Enters the user Input with validation on Logoff Time.
  """
  choice = 'wrong'
  acceptable_range = range(0,24)
  within_range = False

  #Two Conditions to check 
  #It should be a digit and within range
  while choice.isdigit() == False or within_range == False:
    choice = input("Please Enter LogOff Time (0-24): ")

    #Digit Check
    if not choice.isdigit():
      print("Sorry that is not a digit")

    #Range Check
    if choice.isdigit():
      if int(choice) in acceptable_range:
        within_range = True
      else:
        print("Sorry not in Acceptable Range")
        within_range = False
  return int(choice)

def write_json(data,filename="test.json"):
  """
  Write JSON on file
  """
  with open(filename,'w') as f:
    json.dump(data,f,indent=2) #indent with 2 and Dump data to File



file_name = 'test.json'
#Control Flow starts from here
#Added 1 Exception that might occur during opening a file
try:
  with open(file_name) as f:
    data = json.load(f)
    temp = data['Users'] #Create a temporary variable that will load all previous data

    book_on = True

    print("\t\t\t\tWelcome to KECians Ally Compound")
    l_arr = []
    l_dept = []

    pname = input("Please Enter Your Name: ")

  

    print("Welcome Mr.\Ms. {}  to the KECians Ally Compound, For How much duration would you like to stay with us".format(pname))

    parr = user_choice_arr()
 
    l_arr.append(parr)

    pdept = user_choice_dept()
 
    l_dept.append(pdept)

  #JSON Appending List in Dict
    y = {'Name': pname, 'Arrival': parr, 'Departure': pdept}
    temp.append(y)


    tot_time = pdept-parr
    if tot_time < 1:
      print("We have Minimum Booking of 1 Hour")
    else:
      print("Your duration of login Would be {} hours. Enjoy Your Stay!".format(tot_time))
    
    
      write_json(data)

#Room Booking For Single Entry Check
  if not on_choice():
    exit()
  else:
    pass

except FileNotFoundError:
    print("file {} does not exist".format(file_name))

#Added Second Exception that might occur During Opening of File.
try:
  with open('test.json') as f:
    data = json.load(f)
    temp = data['Users']
    while book_on:
      pname = input("Please Enter Your Name: ")

      print("Welcome Mr.\Ms. {}  to the KECians Ally Compound, For How much duration would you like to stay with us".format(pname))
      parr = user_choice_arr()
      if room_check(parr, l_arr[-1], l_dept[-1]):
         print("Compound Cannot be booked as our Inventory is Full, You can register for any other time with us. Sorry for Inconvenience")
         continue
    
      l_arr.append(parr)

      pdept = user_choice_dept()
      if room_check(parr, l_arr[-1], l_dept[-1]):
        print("Compound Cannot be booked as our Inventory is Full, You can register for any other time with us. Sorry for Inconvenience")
        continue
  
      l_dept.append(pdept)

    #JSON Appending List in Dict
      y = {'Name': pname, 'Arrival': parr, 'Departure': pdept}
      temp.append(y)

      tot_time = pdept-parr
      if tot_time < 1:
        print("We have Minimum Booking of 1 Hour")
      else:
        print("Your duration of login Would be {} hours. Enjoy Your Stay!".format(tot_time))
   
    #Check Continue Booking
      book_on = on_choice()
  
    write_json(data)


except FileNotFoundError:
    print("file {} does not exist".format(file_name))
