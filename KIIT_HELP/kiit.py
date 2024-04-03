import telegram.ext
import json
import datetime
import pytz

def result(user_roll_number):
    desired_timezone = pytz.timezone('Asia/Kolkata')
    current_date = datetime.datetime.now(desired_timezone)
    day_of_week = current_date.strftime("%A")
    day_of_week_output = day_of_week
    day_of_week = day_of_week.upper()
    day_of_week = day_of_week[:3]
    if day_of_week == "SUN":
        day_of_week = "MON"

    with open("Students_Classes_Data/elective.json", 'r') as file1:
        elective_data = json.load(file1)

    with open("Students_Classes_Data/core.json", 'r') as file2:
        core_data = json.load(file2)

    with open("Students_Classes_Data/core-section.json", 'r') as file3:
        section_data = json.load(file3)

    with open("Students_Classes_Data/elective_time.json", 'r') as file4:
        elective_time_data = json.load(file4)

    with open("Students_Classes_Data/name.json", 'r') as file5:
        name_data = json.load(file5)


    roll_numbers_elective = []
    elective_sections = []

    for entry in elective_data:
        if entry["Roll No"] == user_roll_number:
            roll_numbers_elective.append(entry["Roll No"])
            elective_sections.append(entry["Elective Section"])

    for entry in core_data:
        if entry["Roll No"] == user_roll_number:
            core_section = entry["Core Section"]

    for entry in name_data:
        if entry["Roll Number"] == user_roll_number:
            name = entry["Students Name"]

    time_slot = []
    time_slot_e1 = []
    time_slot_e2 = []
    room_no = []
    room_elective_e1 = []
    room_elective_e2 = []
    for entry in section_data:
        if entry["Section"] == core_section and entry["DAY"] == day_of_week:
            room_no.append(entry["ROOM1"])
            time_slot.append(entry["8-9"])
            room_no.append(entry["ROOM2"])
            time_slot.append(entry["9-10"])
            room_no.append(entry["ROOM2"])
            time_slot.append(entry["10-11"])
            room_no.append(entry["ROOM3"])
            time_slot.append(entry["11-12"])
            room_no.append(entry["ROOM4"])
            time_slot.append(entry["12-1"])
            room_no.append(entry["ROOM4"])
            time_slot.append(entry["1-2"])
            room_no.append(entry["ROOM6"])
            time_slot.append(entry["3-4"])
            room_no.append(entry["ROOM7"])
            time_slot.append(entry["4-5"])
            room_no.append(entry["ROOM7"])
            time_slot.append(entry["5-6"])

    for entry in elective_time_data:
        if entry["Section(DE)"] == elective_sections[0] and entry["DAY"] == day_of_week:
            time_slot_e1.append(entry["8-9"])
            time_slot_e1.append(entry["9-10"])
            time_slot_e1.append(entry["10-11"])
            room_elective_e1.append(entry["ROOM1"])
            time_slot_e1.append(entry["11-12"])
            room_elective_e1.append(entry["ROOM2"])

            time_slot_e1.append(entry["12-1"])
            room_elective_e1.append(entry["ROOM3"])

            time_slot_e1.append(entry["1-2"])
            room_elective_e1.append(entry["ROOM4"])

            time_slot_e1.append(entry["3-4"])
            room_elective_e1.append(entry["ROOM5"])
            time_slot_e1.append(entry["4-5"])
            room_elective_e1.append(entry["ROOM6"])
            time_slot_e1.append(entry["5-6"])
        if entry["Section(DE)"] == elective_sections[1] and entry["DAY"] == day_of_week:
            time_slot_e2.append(entry["8-9"])
            time_slot_e2.append(entry["9-10"])
            time_slot_e2.append(entry["10-11"])
            room_elective_e2.append(entry["ROOM1"])
            time_slot_e2.append(entry["11-12"])
            room_elective_e2.append(entry["ROOM2"])
            time_slot_e2.append(entry["12-1"])
            room_elective_e2.append(entry["ROOM3"])
            time_slot_e2.append(entry["1-2"])
            room_elective_e2.append(entry["ROOM4"])
            time_slot_e2.append(entry["3-4"])
            room_elective_e2.append(entry["ROOM5"])
            time_slot_e2.append(entry["4-5"])
            room_elective_e2.append(entry["ROOM6"])
            time_slot_e2.append(entry["5-6"])

    indices_not_e1 = [index for index, value in enumerate(time_slot_e1) if value != "X"]

    for i in indices_not_e1:
        time_slot[i] = time_slot_e1[i]

    indices_not_e2 = [index for index, value in enumerate(time_slot_e2) if value != "X"]

    for i in indices_not_e2:
        time_slot[i] = time_slot_e2[i]

    str1 = "🌟WELCOME TO KIIT HELP🌟\n\n"
    str_details = "📘Your Details : - \n"
    str2 = f"Roll No.: {user_roll_number}\n"
    str3 = f"Name: {name}\n"
    str4 = f"Core-Section: {core_section}\n"
    str5 = f"Elective-1: {elective_sections[0]}\n"
    str6 = f"{room_elective_e1}"
    str7 = f"Elective-2: {elective_sections[1]}\n\n"
    str8 = f"{room_elective_e2}"

    final_str = str1 + str_details + str2 + str3 + str4 + str5 + str7

    def return_slot(inum):
        slot_time = "ty"
        if inum == 0:
            slot_time = "8 AM - 9 AM"
        elif inum == 1:
            slot_time = "9 AM- 10 AM"
        elif inum == 2:
            slot_time = "10 AM- 11 AM"
        elif inum == 3:
            slot_time = "11 AM- 12 PM"
        elif inum == 4:
            slot_time = "12 PM - 1 PM"
        elif inum == 5:
            slot_time = "1 PM- 2 PM"
        elif inum == 6:
            slot_time = "3 PM- 4 PM"
        elif inum == 7:
            slot_time = "4 PM - 5 PM"
        elif inum == 8:
            slot_time = "5 PM- 6 PM"
        return slot_time

    def room(rnum):

        room_n = ""
        if room_no[rnum] == "---":
            if rnum == 3:
                room_n = room_elective_e1[0]
                if room_n == "---":
                    room_n = room_elective_e2[0]
            if rnum == 4:
                room_n = room_elective_e1[1]
                if room_n == "---":
                    room_n = room_elective_e2[1]
            if rnum == 5:
                room_n = room_elective_e1[2]
                if room_n == "---":
                    room_n = room_elective_e2[2]
            if rnum == 6:
                room_n = room_elective_e1[3]
                if room_n == "---":
                    room_n = room_elective_e2[3]
        else:
            room_n = room_no[rnum]
        return room_n

    final_String = final_str + "\n" + f"Your Time table for today ({day_of_week}) is : \n"
    for index, value in enumerate(time_slot):
        if value != "X":
            final_String = final_String + (return_slot(index) + "   " + value + "   " + room(index)) + "\n"

    return final_String
