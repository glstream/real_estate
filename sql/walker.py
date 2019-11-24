import os 

tuple_list = [('W Seattle', 2.0, '+', b'\xf0\x9f\x93\x88'), 
('Central Seattle SE, Leshi, Mt Baker', 22.1, '+', b'\xf0\x9f\x93\x88'), 
('Central Seattle SW, Beacon Hill', -14.4, '', b'\xf0\x9f\x93\x89'), 
('Central Seattle, Capitol Hill', -1.0, '', b'\xf0\x9f\x93\x89'), 
('Queen Anne', 15.1, '+', b'\xf0\x9f\x93\x88'), 
('Ballard, Greenlake', -3.2, '', b'\xf0\x9f\x93\x89'), 
('N Seattle', 1.0, '+', b'\xf0\x9f\x93\x88')]
[('W Seattle', 3.9, '+', b'\xf0\x9f\x93\x88'), 
('Central Seattle SE, Leshi, Mt Baker', 18.3, '+', b'\xf0\x9f\x93\x88'), 
('Central Seattle SW, Beacon Hill', -18.0, '', b'\xf0\x9f\x93\x89'), 
('Central Seattle, Capitol Hill', 13.0, '+', b'\xf0\x9f\x93\x88'), 
('Queen Anne', 8.6, '+', b'\xf0\x9f\x93\x88'),
 ('Ballard, Greenlake', -5.7, '', b'\xf0\x9f\x93\x89'), 
 ('N Seattle', 7.3, '+', b'\xf0\x9f\x93\x88')]
[('W Seattle', -26.1, '', b'\xf0\x9f\x93\x89'), 
('Central Seattle SE, Leshi, Mt Baker', 0.0, '', b'\t\xe2\x86\x94'), 
('Central Seattle SW, Beacon Hill', 0.0, '', b'\t\xe2\x86\x94'), 
('Central Seattle, Capitol Hill', -12.4, '', b'\xf0\x9f\x93\x89'),
 ('Queen Anne', 1.0, '+', b'\xf0\x9f\x93\x88'), 
 ('Ballard, Greenlake', -5.7, '', b'\xf0\x9f\x93\x89'), 
 ('N Seattle', 1.5, '+', b'\xf0\x9f\x93\x88')]

t = tuple_list

for i in tuple_list:
    print(i[0])

