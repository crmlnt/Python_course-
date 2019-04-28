import statistics as st
import pickle



def general():
    print('Welcome to Grade Central v.1.2')
    print('\n[1] - Enter Grades')
    print('[2] - Delete student')
    print ('[3] - Average student grade')
    print('[4] - Exit')
    inserimento = input('\nWhat would like to do? select an option [1 - 4]: ')

    newStudentGrade = {'Carmine': [100,98,87,93], 'Rosa': [100,97,65,78]}


        
    if inserimento == '1':
        def addStudent():
            
                newStudent = input('\nWrite the name of the student to update: ')
                newGrade = input('Write the student grade: ')
                if newStudent in newStudentGrade:
                    print('Adding grade... ')
                    newStudentGrade[newStudent].append(float(newGrade))
                else:
                    print('student does not exist')
                print('\nWell done, you have registered ', newStudent, 'correctly with a grade of', newGrade)
                print(newStudentGrade)
                
        addStudent()
        
        
        
    elif inserimento == '2':
        def delStudent():
            exStudent = input('Which student do you want to delete?: ')
            del newStudentGrade[exStudent]
            print('Well done', exStudent, 'has been deleted from the DB')
        delStudent()
        
        
    elif inserimento == '3':
        def avGrade():
            average = input('Which student would you like to calculate?: ')
            if average in newStudentGrade:
                print("I'm calculating the average grade... ")
                averageGrade = st.mean(newStudentGrade[average])
                print(averageGrade)
        avGrade()
        
        
    
general()
