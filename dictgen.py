import csv

def read_csv(filename,delimiter=','):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, skipinitialspace=True,delimiter=delimiter)
        header = next(reader)  # Skip header row
        for row in reader:
            row = [items.strip() for items in row]
            yield row

def gen_dict(csvfile, outfile, dictname, key, val, iskeystring=False, isvalstring=False, delimiter=","):
    with open(outfile, 'a', newline="\n") as out:
        out.write(dictname + " = { \n")
        for row in read_csv(csvfile, delimiter=delimiter):
            if iskeystring and isvalstring:
                out.write(f'    "{row[key]}" : "{row[val]}"')
            elif iskeystring:
                out.write(f'    "{row[key]}" : {row[val]}')
            elif isvalstring:
                out.write(f'    {row[key]} : "{row[val]}"')
            else:
                out.write(f'    {row[key]} : {row[val]}')
            out.write(", \n")
        out.write("}\n")
        
 
csvfile = "256color.csv"
outfile = "dict.py"
delimiter = "|"
# this dictionary is
# key : value
# "dictionary name" : (index of key, index of value, iskeystring, isvalstring)
dictname = {
    "NUMBER_NAME" : (0,1,False,True), 
    "NUMBER_HEX" : (0,2, False, True),
    "NUMBER_RGB" : (0,3, False, False), 
    "NUMBER_HLS" : (0,4, False, False), 
    "NAME_NUMBER" : (1,0, True, False), 
    "NAME_HEX" : (1, 2, True, True),
    "NAME_RGB" : (1,3, True, False), 
    "HEX_NAME" : (2, 1, True, True),
    "HEX_NUMBER" : (2,0, True, False),
}

for name in dictname.keys():
    key,val,iskeystring,isvalstring = dictname[name]
    gen_dict(csvfile, outfile, name, key,val,iskeystring,isvalstring,delimiter=delimiter)