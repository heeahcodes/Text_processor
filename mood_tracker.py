from datetime import datetime #imports datetime
import csv
import os
def main ():
    mood_map ={"okay" : 1,"calm" : 2,"hopeful": 3,"excited" : 4,"stressed" :5,"irritated" : 6,"anxious" :7,"numb" : 8}
    #dictionary to store mood as key-value pairs
    def mood_logger():
        print('''
        Welcome to Suncatcher 
        Your bite-sized mood logger
        How are you feeling today? 
        ''') #introduction statements

        #records the date, time, half of the day, and day of the week during which the input is made
        now = datetime.now()
        date = now.strftime("%d/%m/%Y") #format DD/MM/YYYY
        time = now.strftime("%I:%M") #format hr/min
        half_day = now.strftime("%p") #format AM/PM
        day = now.strftime("%A") # day of the week

        file_exists = os.path.isfile("mood_log.csv") #os module, checks if the file exists
        #prevents mulitiple copies of the same file
        with open("mood_log.csv", "a", newline='') as file: #opens mentioned csv file for appending new entries
            field_names = ['Date', 'Mood', 'Time', 'AM/PM', 'Day'] #column header names
            writer = csv.DictWriter(file, fieldnames=field_names) #passes rows as dict, corresponds to field names above
            #used over lists as easier to add columns later

            #writes header only if file is new
            if not file_exists:
                writer.writeheader()    #skips for file_exists = True

            writer.writerow({'Date': date,'Mood': user_mood,'Time': time, 'AM/PM': half_day, 'Day': day})
            #appends new entry with corresponding fields into new row
        print("Your mood has been recorded. Take care") #confirmation of completion of one execution of program.

    mood_logger() #function call

if __name__ == '__main__':
        main ()