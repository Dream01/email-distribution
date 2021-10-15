import csv

with open('users.csv', 'a') as csvfile:
    csvfile = csv.writer(csvfile)
    user = input('User: ')
    email = input('Email: ')
    csvfile.writerow([user, email])
