# Download SmartConsole.py from: https://github.com/VladFeldfix/Smart-Console/blob/main/SmartConsole.py
from SmartConsole import *

class main:
    # constructor
    def __init__(self):
        # load smart console
        self.sc = SmartConsole("Course To Do List Maker", "1.0")

        # set-up main memu
        self.sc.add_main_menu_item("RUN", self.run)

        # start
        self.sc.start()
    
    def run(self):
        course_name = self.sc.input("What is the course code?").upper()
        for i in range(1,9):
            print("%s UN0%s - check grades for previous week" % (course_name,i))
            print("%s UN0%s - reading assignment" % (course_name,i))
            print("%s UN0%s - written / programming assignment" % (course_name,i))
            print("%s UN0%s - discussion assignment" % (course_name,i))
            print("%s UN0%s - self quiz" % (course_name,i))
            print("%s UN0%s - graded quiz" % (course_name,i))
            print("%s UN0%s - peer assessment 1" % (course_name,i))
            print("%s UN0%s - peer assessment 2" % (course_name,i))
            print("%s UN0%s - peer assessment 3" % (course_name,i))
            print("%s UN0%s - rate and comment 1" % (course_name,i))
            print("%s UN0%s - rate and comment 2" % (course_name,i))
            print("%s UN0%s - rate and comment 3" % (course_name,i))
            print("%s UN0%s - learning journal" % (course_name,i))
            print("--------------------------------------------------------------------------------------")
        print("%s UN09 - final exam" % (course_name))

        # restart
        self.sc.restart()

main()