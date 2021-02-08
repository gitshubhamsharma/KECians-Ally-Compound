import json
import psycopg2

con = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres"
)

# cursor
cur = con.cursor()

# execute query
# cur.execute("select pname, arrival, departure from room")

# rows = cur.fetchall()
#
# for r in rows:
#     print(f"pname={(r[0])}, arrival={(r[1])}, departure={r[2]}")


def room_check(num, arr, dept):
    """
  It checks whether the room can be booked if it does not lie in the given timeframe.
  """
    if num in range(arr, dept):
        return True
    else:
        return False


def on_choice():
    """
  It decides whether or not to continue room booking.
  """

    choice = 'wrong'
    while choice not in ['Y', 'N', 'y', 'n']:

        choice = input("Want to keep Adding Compound: (Y/N) ")

        if choice not in ['Y', 'N', 'y', 'n']:
            print("Sorry, I don't Understand Please Choose Y or N")

    if choice == 'Y' or choice == 'y':
        return True
    else:
        return False


def user_choice():
    """
  Enters the user Input of Arrival and Departure
  """
    choice = 'wrong'
    choice1 = 'wrong'

    while 1:
        choice = input("Please Enter the LogIn Time (0-24): ")
        choice1 = input("Please Enter the LogOff Time (0-24): ")
        val = validate_input(choice, choice1)
        if val:
            break
        else:
            print("Please Enter Valid LogIn and LogOff")
            continue
    return int(choice), int(choice1)


def validate_input(choice, choice1):
    """
  Validate Input of Arrival and Departure
  """
    acceptable_range = range(0, 24)
    if choice.isdigit() and choice1.isdigit():
        if int(choice) in acceptable_range and int(choice1) in acceptable_range:
            return True
        else:
            return False


def write_json(data, filename="test.json"):
    """
  Write JSON on file
  """
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)  # indent with 2 and Dump data to File


file_name = 'test.json'
# Control Flow starts from here
# Added 1 Exception that might occur during opening a file
try:
    with open(file_name) as f:
        data = json.load(f)
        temp = data['Users']  # Create a temporary variable that will load all previous data

        book_on = True

        print("\t\t\t\tWelcome to KECian Ally Compound ")
        l_arr = []
        l_dept = []

        pname = input("Please Enter Your Name: ")

        print("Welcome Mr.\Ms. {}  to the KECians Ally Compound, For How much duration would you like to stay with us".format(pname))

        user_choice_input = user_choice()
        par, dar = user_choice_input

        parr = par
        l_arr.append(parr)

        pdept = dar
        l_dept.append(pdept)

        # insert values in DB
        cur.execute("INSERT INTO room (pname, arrival, departure) VALUES (%s, %s, %s)", (pname, par, pdept))

        # JSON Appending List in Dict
        y = {'Name': pname, 'Arrival': parr, 'Departure': pdept}
        temp.append(y)

        tot_time = pdept - parr
        if tot_time < 1:
            print("We have Minimum Compound of 1 Hour")
        else:
            print("Your duration at our Compound Would be {} hours. Enjoy Your Chat!".format(tot_time))

            write_json(data)

    # Room Booking For Single Entry Check
    if not on_choice():
        exit()
    else:
        pass


# except FileNotFoundError:
#    open(test.json)
except FileNotFoundError:
    print("file {} does not exist".format(file_name))

# Added Second Exception that might occur During Opening of File.
try:
    with open('test.json') as f:
        data = json.load(f)
        temp = data['Users']
        while book_on:
            pname = input("Please Enter Your Name: ")

            print("Welcome Mr.\Ms. {}  to the KECians Ally Compound, For How much duration would you like to stay with us".format(pname))
            user_choice_input = user_choice()
            par, dar = user_choice_input

            parr = par
            if room_check(parr, l_arr[-1], l_dept[-1]):
                print("Compound Cannot be booked as our Inventory is Full, You can register for any other time with us. Sorry for Inconvenience")
                continue

            l_arr.append(parr)

            pdept = dar
            if room_check(parr, l_arr[-1], l_dept[-1]):
                print("Compound Cannot be booked as our Inventory is Full, You can register for any other time with us. Sorry for Inconvenience")
                continue

            l_dept.append(pdept)

            # insert values in DB
            cur.execute("INSERT INTO room (pname, arrival, departure) VALUES (%s, %s, %s)", (pname, par, pdept))

            # JSON Appending List in Dict
            y = {'Name': pname, 'Arrival': parr, 'Departure': pdept}
            temp.append(y)

            tot_time = pdept - parr
            if tot_time < 1:
                print("We have Minimum Compound of 1 Hour")
            else:
                print("Your duration at our Compound Would be {} hours. Enjoy Your Chat!".format(tot_time))

            # Check Continue Booking
            book_on = on_choice()

            # check DB
            # rows = cur.fetchall()
            #
            # for r in rows:
            #     print(f"pname={(r[0])}, arrival={(r[1])}, departure={r[2]}")
            #
            # cur.execute("select pname, arrival, departure from room")

        write_json(data)

# except FileNotFoundError:
#    open(test.json)
except FileNotFoundError:
    print("file {} does not exist".format(file_name))

con.commit()

# close the cursor
cur.close()

# Close the DB
con.close()
