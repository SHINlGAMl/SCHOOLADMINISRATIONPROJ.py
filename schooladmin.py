import csv

def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(['NAME', 'AGE', 'CONTACT NUMBER', 'EMAIL ID'])
        
        writer.writerow(info_list)

if __name__ == '__main__':
    condition = True
    student_num = 1

    while condition:
        student_info = input("Enter the student information (name, age, contact number, email id) :".format(student_num))

        #split
        student_info_list = student_info.split(' ')
        print('ENTERED INFORMATION IS:' + str(student_info_list))

        print('\nThe entered information is -\nNAME: {}\nAGE: {}\nCONTACT_NUMBER: {}\nE-MAIL ID: {}'.format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))
        
        choice_check = input("\nIs the entered information correct?(yes/no) : ").lower().strip()
        if choice_check == "yes":
            write_into_csv(student_info_list)

            condition_check = input("\nEnter (yes/no) if you want to enter information for another student : ").lower().strip()

            if condition_check == "yes":
                condition = True
                student_num = student_num + 1

            elif condition_check == "no":
                condition = False

        elif choice_check == "no":
            print("\nPLEASE RE-ENTER THE INFORMATION!!")