with open("lezione4/data/file_02.txt", 'r') as f:
    line1 = f.readline()
    line2 = f.readline()


line1_split = [int(x) for x in line1.strip("\n").split(",")]
line2_split = [int(x) for x in line2.strip("\n").split(",")]

print(line1_split)
print(line2_split)


# f.read() --> single string
# f.readline() -> which reads ONE line from the file. And you if you call multiple times, it reads the next one
# f.readlines() -> reads ALL lines and returns a list where the i-th element is the i-th line.


































# i chose this one purposly. it does look like a D.

#         _
#       /X \ 
#     _------_
#    /        \
#   |          |
#   |          |
#   |     __  __)
#   |    /  \/  \
#  /\/\ (o   )o  )
#  /c    \__/ --.
#  \_   _-------'
#   |  /         \
#   | | '\________)
#   |  \_____)
#   |_____ |
#  |_____/\/\
#  /        \
















#        ,,,,,,,,,,,,,,,
#     ,(((((((((())))))))),
#   ,((((((((((()))))))))))),
#  ,(((((((((\\\|///))))))))),
# ,((((((((((///|\\\)))))))))),
# ((((((((//////^\\\\\\))))))))
# ((((((' .-""-   -""-. '))))))
# (((((  `\.-.     .-./`  )))))
# ((((( -=(0) )   (0) )=- )))))
# '((((   /'-'     '-'\   ))))'
#  ((((\   _,   A  ,_    /))))
#  '((((\    \     /    /))))'
#    '((('.   `-o-'   .')))'
#          '-.,___,.-'












#  _._     _,-'""`-._
# (,-.`._,'(       |\`-/|
#    `-.-' \ )-`( , o o)
#          `-    \`_`"'-