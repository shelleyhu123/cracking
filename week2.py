import sys

line_number = 0
space = " "
line_number_two = 20
for line in sys.stdin:
    line = line.strip()
    offset = line.find("Ice")
    line_number += 1
    if line_number == 1:
        print line
    elif line_number > 1 and line_number <= 7:
        print line[:offset], space*line_number*2, line[offset+line_number:]
    elif line_number > 7 and line_number <= 20:
        print line[:offset], space*line_number*2, line[offset+7:]
    elif line_number >20 and line_number <= 35:
        line_number_two = 20
        line_number_two -= 1
        print line[:offset], space*line_number_two*2, line[offset+8:]
    elif line_number > 35:
        line_number_two = 8    
        line_number_two -= 1
        print line[:offset], space*line_number_two*2, line[offset+line_number_two:]
    
    
   