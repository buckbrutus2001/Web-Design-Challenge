from prettytable import PrettyTable
csv_file=open('/Resources/cities.cvs')
csv_file = csv_file.readlines()
# print csv_file
headers = csv_file[0]
headers = headers.split(',')
data = csv_file[1]
data = data.split(',')

x = PrettyTable([headers[0],data[1]])

for a in rage(1,len(headers)):
    x.add_row([headers[a],data[a]])
html_code = x.get_html_string()
html_file = open('table.html','w')
html_file = html_file.write(html_code)
