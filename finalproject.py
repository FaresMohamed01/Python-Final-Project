#Python Final Project - Fares Mohamed
import tkinter
import tkinter.messagebox

class FinalProject:

    # initializer function to create frames, radio buttons and pack them in addition to calling tkinter loop
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title ("University Information System")
        self.main_window.geometry("400x150")

        self.options_frame = tkinter.Frame(self.main_window)
        self.users_frame = tkinter.Frame(self.main_window)
        self.information_frame = tkinter.Frame(self.main_window)

        self.radio = tkinter.IntVar()
        self.instructor = tkinter.Radiobutton(self.options_frame, text='Get Instructor Info',
                                       variable=self.radio, value = 1, command=self.get_instructor_info)
        self.department = tkinter.Radiobutton(self.options_frame, text='Get Department Info',
                                       variable=self.radio, value = 2, command = self.get_department_info)
        self.clear = tkinter.Radiobutton(self.options_frame, text='Clear',
                                       variable=self.radio, value = 3, command = self.clear_info)
        self.quit = tkinter.Radiobutton(self.options_frame, text='Quit',
                                       variable=self.radio, value = 4, command=self.main_window.destroy)

        self.instructor.pack(side='left')
        self.department.pack(side='left')
        self.clear.pack(side='left')
        self.quit.pack(side='left')

        self.options_frame.pack(anchor='w')
        self.users_frame.pack(anchor='w')
        self.information_frame.pack(anchor='w')

        tkinter.mainloop()
        

    # clear_info function to destory user and information frames
    def clear_info (self):
        self.users_frame.destroy()
        self.information_frame.destroy()


    # get_instructor_info function to create entry box for instructor id and submit button.
    def get_instructor_info (self):
        self.clear_info()

        self.users_frame = tkinter.Frame(self.main_window)
        self.users_frame.pack(anchor="w")
        
        self.instructor_label = tkinter.Label(self.users_frame, text='Enter instructor ID:')
        self.instructor_label.pack(side = "left")
        
        self.instructor_entry = tkinter.Entry(self.users_frame, width=14)
        self.instructor_entry.pack(side = "left")
        
        self.submit = tkinter.Button(self.users_frame, text='Submit', command = self.read_instructor_info)
        self.submit.pack(side = "left")

        self.instructor_entry.bind('<Return>', self.read_instructor_info)


    # get_department_info function to create entry box for department name and submit button.
    def get_department_info (self):
        self.clear_info()

        self.users_frame = tkinter.Frame(self.main_window)
        self.users_frame.pack(anchor="w")

        self.department_label = tkinter.Label(self.users_frame, text='Enter department name:')
        self.department_label.pack(side = "left")
        
        self.department_entry = tkinter.Entry(self.users_frame, width=14)
        self.department_entry.pack(side = "left")
        
        self.submit = tkinter.Button(self.users_frame, text='Submit', command = self.read_department_info)
        self.submit.pack(side = "left")

        self.department_entry.bind('<Return>', self.read_department_info)

        
    # function that reads the information of the entered ID from instructor and department files
    def read_instructor_info (self, event = None):
        check = False

        with open ('instructor.txt', 'r') as instructorFile:
            for instructor in instructorFile:
                instructor_file = instructor.split(",")
                instructor_id = instructor_file[0]
                instructor_name = instructor_file[1]
                instructor_dept = instructor_file[2].strip()
                with open ('department.txt', 'r') as departmentFile:
                    for department in departmentFile:
                        department_file = department.split(",")
                        dept_name = department_file[0]
                        dept_building = department_file[1]
                        if dept_name in instructor:
                            if instructor_id == self.instructor_entry.get():
                                self.information_frame.destroy()
                                self.information_frame = tkinter.Frame(self.main_window)
                                self.information_frame.pack(anchor="w")

                                self.name_label = tkinter.Label(self.information_frame, text=f'Name: {instructor_name}')
                                self.name_label.pack(anchor='w')
                                
                                self.dept_label = tkinter.Label(self.information_frame, text=f'Department: {instructor_dept}')
                                self.dept_label.pack(anchor='w')
                    
                                self.building_label = tkinter.Label(self.information_frame, text=f'Building: {dept_building}')
                                self.building_label.pack(anchor='w')
                                
                                check = True
        if check == False:
            self.information_frame.destroy()
            
            self.information_frame = tkinter.Frame(self.main_window)
            self.information_frame.pack(anchor="w")
            
            self.error_label = tkinter.Label(self.information_frame, text="Information not found.")
            self.error_label.pack(anchor='w')


    # function that reads the information of the entered deparment name from department file
    def read_department_info (self, event = None):
        check = False

        with open ('department.txt', 'r') as departmentFile:
            for department in departmentFile:
                department_file = department.split(",")
                dept_name = department_file[0]
                dept_building = department_file[1]
                dept_budget = department_file[2]
                if dept_name == self.department_entry.get():
                    self.information_frame.destroy()
                    
                    self.information_frame = tkinter.Frame(self.main_window)
                    self.information_frame.pack(anchor="w")

                    self.name_label = tkinter.Label(self.information_frame, text=f'Building: {dept_building}')
                    self.name_label.pack(anchor='w')
                    
                    self.dept_label = tkinter.Label(self.information_frame, text=f'Budget: {dept_budget}')
                    self.dept_label.pack(anchor='w')
                    
                    check = True
        if check == False:
            self.information_frame.destroy()

            self.information_frame = tkinter.Frame(self.main_window)
            self.information_frame.pack(anchor="w")

            self.error_label = tkinter.Label(self.information_frame, text="Information not found.")
            self.error_label.pack(anchor='w')


# Calling the main class 
if __name__ == '__main__':
    final_project = FinalProject()
