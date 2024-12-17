student_dict = {
    'Arslan' : 98,
    'Jibran' : 88,
    'Taha' : 90
}
print(student_dict['Arslan'])

this_dict = { }
#adding three key:value pairs
this_dict['Brand'] = 'Toyota'
this_dict['Model'] = 'Fortuner'
this_dict['Year'] = '2024'
print(this_dict)

this_dict['Year'] = 2021
#after updating
print(this_dict)

#after removing
this_dict.pop('Year')
print(this_dict)