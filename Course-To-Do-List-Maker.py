# Download SmartConsole.py from: https://github.com/VladFeldfix/Smart-Console/blob/main/SmartConsole.py
from SmartConsole import *

class main:
    # constructor
    def __init__(self):
        # load smart console
        self.sc = SmartConsole("Course To Do List Maker", "1.1")

        # set-up main memu
        self.sc.add_main_menu_item("RUN", self.run)

        # start
        self.sc.start()
    
    def run(self):
        course_name = self.sc.input("What is the course code?").upper()
        for i in range(1,9):
            print("%s UN0%s - CHECK GRADES FOR PREVIOUS WEEK" % (course_name,i))
            print("%s UN0%s - READING ASSIGNMENT" % (course_name,i))
            print("%s UN0%s - WRITTEN / PROGRAMMING ASSIGNMENT" % (course_name,i))
            print("%s UN0%s - DISCUSSION ASSIGNMENT" % (course_name,i))
            print("%s UN0%s - SELF QUIZ" % (course_name,i))
            print("%s UN0%s - GRADED QUIZ" % (course_name,i))
            print("%s UN0%s - PEER ASSESSMENT 1" % (course_name,i))
            print("%s UN0%s - PEER ASSESSMENT 2" % (course_name,i))
            print("%s UN0%s - PEER ASSESSMENT 3" % (course_name,i))
            print("%s UN0%s - RATE AND COMMENT 1" % (course_name,i))
            print("%s UN0%s - RATE AND COMMENT 2" % (course_name,i))
            print("%s UN0%s - RATE AND COMMENT 3" % (course_name,i))
            print("%s UN0%s - LEARNING JOURNAL" % (course_name,i))
            print("--------------------------------------------------------------------------------------")
        print("%s UN09 - final exam" % (course_name))

        # restart
        self.sc.restart()

main()
