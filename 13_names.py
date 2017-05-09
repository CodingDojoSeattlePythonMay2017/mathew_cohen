students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }


# Part I
def lstStudents(lst):
    for student in lst:
        firstName = student['first_name']
        lastName = student['last_name']
        print('{} {}'.format(firstName,lastName))
        

lstStudents(students)

print('')

# Part II
def lstUsers(lst):
    for key, data in lst.items():
        for value in data:
            firstName = value['first_name']
            lastName = value['last_name']
            print('{} {} - {}'.format(firstName,lastName,(len(firstName)+len(lastName))))

lstUsers(users)