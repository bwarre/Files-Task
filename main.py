import csv
rows_to_keep = []   #every row that does not have 3 absences will be appended to this.
def read_csv(file_name):
    with open(file_name, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        iter_csv = iter(csvreader)
        for row in iter_csv:
            if row[4] == 'Absent' and row[6] == 'Absent' and row[8] == 'Absent': #checks for 3 absences.
                pass
            else:
                rows_to_keep.append(row) #if less than 3 absences then we keep the row.

read_csv("al_results_2020.csv")
print(rows_to_keep)

def write_csv(file_name: str, file_data):   #we now need to write a csv file for data that does not have 3 absences.
    with open(file_name, "w", newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(file_data)

write_csv("not_absent.csv", rows_to_keep) #name the new file "not_absent.csv" containing all non absent data.

