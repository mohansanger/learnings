import csv

file=open(r'C:\Users\Mohan.2.Singh\Downloads\Test PY\Book4.csv','a',newline='')
#writer=csv.writer(file)
#writer.writerow(["Hanu","Creater-Destroyer","M"])
#writer.writerow(["Hanu","Creater-Destroyer","M"])


fieldnames=['player_name', 'fide_rating']
writer=csv.DictWriter(file,fieldnames=fieldnames)

writer.writeheader()
writer.writerow({'player_name': 'Magnus Carlsen', 'fide_rating': 2870})
writer.writerow({'player_name': 'Fabiano Caruana', 'fide_rating': 2822})
writer.writerow({'player_name': 'Ding Liren', 'fide_rating': 2801})