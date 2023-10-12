def sort_file(*args, insep=',', inend='\n', outsep=None, outend=None):
    # Check if more than one positional argument is provided
    if len(args) != 1:
        raise TypeError("sort_file() takes exactly one positional argument")

    csv_string = args[0]  # Get the CSV string from args

    # Set default values for outsep and outend
    if outsep is None:
        outsep = insep
    if outend is None:
        outend = inend

    # Split the CSV string into lines
    lines = csv_string.split(inend)

    # Remove blank lines and lines with '#' character
    lines = [line for line in lines if line.strip() and not line.strip().startswith('#')]

    # Sort the lines
    lines.sort()
    sorted_csv = outend.join(lines)

    return sorted_csv.replace(insep,outsep)

csv_data = "John,Doe\nJane,Smith\n# Comment line\nAlice,Johnson\n"
csv2 = "2,3,d\n1,4,d\n8,2,z\n2,4,x\n2,4,a"
sorted_csv = sort_file(csv2, outsep='|')
print(sorted_csv)

# A string with only one item per row
assert sort_file('b\ny\na') == 'a\nb\ny'

# Providing some keyword arguments
assert sort_file('b,b\ny,y\na,a', outsep=':', outend='\t') == 'a:a\tb:b\ty:y'

# Blank lines and lines starting with '#' should not appear in the result
assert sort_file('b,q\n\n#p,y\na,o', outsep='-') == 'a-o\nb-q'

# Proper sorting and ignore blank lines at the end
assert sort_file('2,3,d\n2,4,x\n2,4,a\n\n\n', outend=' -- end\n') == '2,3,d -- end\n2,4,a -- end\n2,4,x'
