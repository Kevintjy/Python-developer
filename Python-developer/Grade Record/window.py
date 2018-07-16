"""
This is the main file for the program, run this file
"""
from tkinter import *
from tkinter.messagebox import *
from file_functions import get_all_course, course_number, transfer_gpa


class MainPage(object):
    """
    this is the main page
    """
    def __init__(self, root=None):
        self.root = root
        self.root.geometry("450x300")
        self.create_page()

    def create_page(self):
        self.page = Frame(self.root)    # create the frame
        self.page.pack()
        # create the title using the label
        Label(self.page,text="Grade Record", fg='black', font=('Times',35)).grid(rowspan=1,column=1)

        # create edit button
        Button(self.page, text='edit', command=self.to_edit_page).grid(row=2+course_number(), column=0)

        # create set button
        Button(self.page, text='set', command=self.to_set_page).grid(row=2 + course_number(), column=1)

        # create exit button
        Button(self.page, text='exit', command=self.to_exit).grid(row=2 + course_number(), column=2)

        # if there is a course in result.txt
        with open('result.txt', 'r') as file:
            f = file.read()
            try:
                f = f.strip().strip('\n').split('$')[1:]
            except Exception:
                return
            else:
                # get_row help us to find the position of each new course button and label
                get_row = 0
                # now f is a list including the course information as a str element
                for i in f:
                    get_row += 1
                    whole_mark = 0
                    whole_percent= []
                    course_name = i.strip().split('\n')[0][:6]
                    i = i.strip().split('\n')
                    # now i is a list including the assignment information in a course
                    for j in i:
                        j = j.strip().split(':')[1]
                        # j is a list including the mark for assignment like(90,20)
                        k = j.strip().strip('(').strip(')').split(',')
                        whole_mark += int(k[0]) * int(k[1])
                        whole_percent.append(int(k[1]))
                    current_mark = whole_mark / sum(whole_percent)
                    current_grade = transfer_gpa(current_mark)

                    # for each course, we create a button to link to the detail of this course
                    Button(self.page, text=course_name).grid(row=get_row, column=0)

                    # then we create the labels for course mark and grade
                    Label(self.page, text=str(current_mark)).grid(row=get_row, column=1)
                    Label(self.page, text=str(current_grade)).grid(row=get_row, column=2)


    def to_edit_page(self):
        """
        go to the edit page
        """
        self.page.destroy()
        EditPage(root)

    def to_set_page(self):
        """
        go to the set page
        """
        self.page.destroy()
        SetPage(root)

    def to_exit(self):
        """
        exit the program
        """
        sys.exit()



class EditPage(object):
    """
    This is the edit page, student can edit his mark
    if the assignment/project/exercise is remarked
    """
    def __init__(self, root=None):
        self.root = root
        self.root.geometry("450x300")
        self.edit_name = StringVar()
        self.edit_assignment = StringVar()
        self.edit_mark = StringVar()
        self.edit_percent = StringVar()
        self.create_page()

    def create_page(self):
        self.page = Frame(self.root)    # create the frame
        self.page.pack()
        # create the title using the label
        Label(self.page, text="Edit", fg='black', font=('Times',35)).grid(rowspan=1,column=1)

        # create three name labels and entries
        Label(self.page, text='Course', fg='black').grid(row=2,column=1)
        Entry(self.page, textvariable=self.edit_name).grid(row=2, column=2)

        Label(self.page, text='Assignment', fg='black').grid(row=3,column=1)
        Entry(self.page, textvariable=self.edit_assignment).grid(row=3, column=2)

        Label(self.page, text='mark', fg='black').grid(row=4,column=1)
        Entry(self.page, textvariable=self.edit_mark).grid(row=4, column=2)

        Label(self.page, text='percent', fg='black').grid(row=5,column=1)
        Entry(self.page, textvariable=self.edit_percent).grid(row=5, column=2)

        # set up the button to get back the main window
        Button(self.page, text='back', command=self.back).grid(row=6,column=1)

        # set up the button to add the grade in to result.txt
        Button(self.page, text='ok',command=self.ok).grid(row=6, column=2)

    def update_file(self):
        """
        add an assignment or edit an assignment mark
        """
        file = open('result.txt','r')
        f = file.read()
        # when course code is not in the file
        if self.edit_name.get() not in get_all_course():
            showinfo(title='wrong course code',
                     message='You should add this course first!')
            return
            # when course code is in the file
        f = f.split('$')
        for i in range(len(f)):
            # find the course information
            if self.edit_name.get() in f[i]:
                temp = f[i]
                temp = temp.split('\n')
                # find whether the assignment is in the file
                for j in range(len(temp)):
                    if self.edit_assignment.get() in temp[j]:
                        # if assignment name is in the file, we need to edit
                        temp[j].split(':')[1] = '('+ str(self.edit_mark.get())\
                                                + ',' + str(self.edit_percent.get()) + ')'
                        f[i] = '\n'.join(temp)
                        f = '$'.join(f)
                        file.close()
                        file = open('result.txt', 'w')
                        file.write(f)
                        return
                # if assignment is not in the file, we need to write it down
                f[i] = f[i] + str(self.edit_assignment.get()) +\
                       ': (' + str(self.edit_mark.get()) + ',' + \
                       str(self.edit_percent.get()) + ')' + '\n'+ '        '
                f = '$'.join(f)
                file.close()
                file = open('result.txt', 'w')
                file.write(f)
                return

    def back(self):
        """
        go back to the main screen
        """
        self.page.destroy()
        MainPage(root)

    def ok(self):
        self.update_file()
        self.page.destroy()
        MainPage(root)


class SetPage(object):
    """
    student can add a course here
    """
    def __init__(self, root=None):
        self.root = root
        self.root.geometry("450x300")
        self.set_course = StringVar()
        self.create_page()

    def create_page(self):
        self.page = Frame(self.root)    # create the frame
        self.page.pack()
        # create the title using the label
        Label(self.page, text="Set", fg='black', font=('Times',35)).grid(rowspan=1,column=1)

        # create three name labels and entries
        Label(self.page, text='Course name', fg='black').grid(row=2,column=1)
        Entry(self.page, textvariable=self.set_course).grid(row=3, column=1)

        # set up the button to get back the main window
        Button(self.page, text='back', command=self.back).grid(row=4,column=2)

        # set up the button to add the grade in to result.txt
        Button(self.page, text='ok', command=self.ok).grid(row=4, column=3, sticky=W)

    def ok(self):
        """
        add a course here, write the course name into result.txt
        """
        with open('result.txt', 'r+') as file:
            if len(str(self.set_course.get())) != 6:
                showinfo(title='course code error',message='code is wrong')
                self.page.destroy()
                SetPage(root)
                return
            if str(self.set_course.get()) in file.read():
                showinfo(title='course code error', message='You have already add this course')
                self.page.destroy()
                SetPage(root)
                return
            file.write('\n\n' + '$' + str(self.set_course.get()) + ' ')
            self.back()

    def back(self):
        """
        go back to the main screen
        """
        self.page.destroy()
        MainPage(root)


if __name__ == '__main__':
    root = Tk()
    root.title('Grade record')
    MainPage(root)
    root.mainloop()



