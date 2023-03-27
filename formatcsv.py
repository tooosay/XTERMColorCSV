import csv

def read_csv(filename,delimiter=','):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, skipinitialspace=True,delimiter=delimiter)
        header = next(reader)  # Skip header row
        for row in reader:
            yield row



def generate_csv(source, out, delimiter=','):
    delm = "|"
    columns = ["number".ljust(7), "name".center(14), "hex".center(9), "rgb".center(16), "hsl".center(16)]
    with open(out, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=delm)
        writer.writerow(columns)
        for row in read_csv(source, delimiter=delimiter):
            number = row[0].ljust(4," ")
            name = row[1].replace(" (SYSTEM)", "").ljust(17," ")
            hexa = row[2].ljust(9)
            rgb = row[3].replace("rgb", "").ljust(16)
            hsl = row[4].replace("hsl", "").replace("%", "")
            columns = [number, name, hexa, rgb, hsl]
            writer.writerow(columns)

            
        
    

source = "xtermcolor.csv"
out = "256color.csv"
delimiter = ";"
# generate_csv(source, out)

generate_csv(source, out, delimiter)