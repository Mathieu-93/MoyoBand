import sqlite3
import csv

from patient import Patient

conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute("""CREATE TABLE patients (
            first text,
            last text,
            ID integer,
            TMP real,
            BMP real
    )""")

def insert_pat(pat) :
    with conn:
        c.execute("INSERT INTO patients VALUES (:first, :last, :ID, :TMP, :BMP)",
            {'first': pat.first, 'last': pat.last, 'ID': pat.ID, 'TMP':pat.TEMP, 'BMP':pat.BMP})


def get_pat_by_ID(id):
    c.execute("SELECT * FROM patients WHERE ID=:ID", {'ID': id})
    return c.fetchall()


def update_BMP(pat, bmp):
    with conn:
        c.execute("""UPDATE patients SET BMP = :BMP
                    WHERE first = :first AND last = :last""",
                  {'first': pat.first, 'last': pat.last, 'BMP': bmp})
def update_TMP(pat, tmp):
    with conn:
        c.execute("""UPDATE patients SET TMP = :TMP
                    WHERE first = :first AND last = :last""",
                  {'first': pat.first, 'last': pat.last, 'TMP': tmp})


def remove_emp(pat):
    with conn:
        c.execute("DELETE from patients WHERE first = :first AND last = :last",
                  {'first': pat.first, 'last': pat.last})

############## BASIC EXAMPLE ####################
# pat_1 = Patient('Mateusz', 'Kowalski', 3412, 37, 103)
# pat_2 = Patient('Jakub', 'Nowak', 1234, 36, 103)

# insert_pat(pat_2)
# insert_pat(pat_1)
# update_BMP(pat_1,120)


# pats = get_pat_by_ID(3412)
# print(pats)

############# DEMO SIMULATION ##################
with open('inputFile.csv' , 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    PatientID =set() # unique value

    for line in csv_reader:
        pat_current = Patient(line[0],line[1],line[2],line[3],line[4])
        if(line[2]not in PatientID): # chack if it's in our base
            PatientID.add(line[2])
            insert_pat(pat_current)
        update_BMP(pat_current,line[4]) # every time update value
        update_TMP(pat_current,line[3])
        print(pat_current.PatientInformation)
        # print(line) # uncomment if you want to see format of object line


    patById = get_pat_by_ID(1212)
    print(patById)

conn.close()
