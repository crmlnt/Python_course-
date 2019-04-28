import statistics as st
import pickle

def general():
    print('Welcome to Grade Central v.1.2')
    print('\n[1] - Enter Grades')
    print('[2] - Delete student')
    print ('[3] - Average student grade')
    print('[4] - Exit')
    inserimento = input('\nWhat would like to do? select an option [1 - 4]: ')

    newStudentGrade = {}


        
    if inserimento == '1':
        def addStudent():
            #save the dict in a pickle file
            pickle.dump(newStudentGrade, open('newStudentGrade.dat', 'wb'))
            addNewStudent = True
            while addNewStudent:
                newStudent = input('\nWrite the name of the student to add: ')
                newGrade = input('Write the student grade: ')
                newStudentGrade[newStudent] = newGrade
                print('\nWell done, you have registered ', newStudent, 'correctly with a grade of', newGrade)
                print(newStudentGrade)
                new = input('Would you like to register a new student? Y/N: ')
                if new == 'N':
                    addNewStudent = False;
        addStudent()
        
    elif inserimento == '2':
        def delStudent():
            #load the dict from pickle
            studentDict = pickle.load(open('newStudentGrade.dat', 'rb'))
            exStudent = input('Which student do you want to delete?: ')
            del newStudentGrade[exStudent]
            print('Well done', exStudent, 'has been deleted from the DB')
        delStudent()
    
general()

'''
print('Welcome to Grade Central v.1.2')
print('\n[1] - Enter Grades')
print('[2] - Delete student')
print ('[3] - Average student grade')
print('[4] - Exit')
inserimento = input('\nWhat would like to do? select an option [1 - 4]: ')

newStudentGrade = {}

    
if inserimento == '1':
    def addStudent():
        addNewStudent = True
        while addNewStudent:
            newStudent = input('\nWrite the name of the student to add: ')
            newGrade = input('Write the student grade: ')
            newStudentGrade[newStudent] = newGrade
            print('\nWell done, you have registered ', newStudent, 'correctly with a grade of', newGrade)
            print(newStudentGrade)
            new = input('Would you like to register a new student? Y/N: ')
            if new == 'N':
                addNewStudent = False;
    addStudent()
    
elif inserimento == '2':
    def delStudent():
        exStudent = input('Which student do you want to delete?: ')
        del newStudentGrade[exStudent]
        print('Well done', exStudent, 'has been deleted from the DB')
    delStudent()
'''    
    
