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

#read_csv("al_results_2020.csv")
#print(rows_to_keep)

def write_csv(file_name: str, file_data):   #we now need to write a csv file for data that does not have 3 absences.
    with open(file_name, "w", newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(file_data)

#write_csv("not_absent.csv", rows_to_keep) #name the new file "not_absent.csv" containing all non absent data.

#Next is to drop columns Zscore, gender, and syllabus.

import pandas as pd
def remove_column(file_name: str, column_name: str,new_file_name):
    data = pd.read_csv(file_name, low_memory=False) # I had to set low memory = False to get this to work.
    data.drop(column_name, inplace=True, axis=1)
    data.to_csv(new_file_name)
#remove_column("not_absent.csv", 'Zscore','columns_removed_Zscore.csv')
#remove_column("columns_removed_Zscore.csv", 'gender','columns_removed_Zscore_gender.csv')
#remove_column("columns_removed_Zscore_gender.csv", 'syllabus','columns_removed_Zscore_gender_syllabus.csv')




