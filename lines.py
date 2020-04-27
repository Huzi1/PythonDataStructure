

file = open("input.txt")
# totalCases = file.readline()
myList = list(file)
# print(myList)
myList2 = []
for index, val in enumerate(myList):

    # print(val)

    if "\n" in val:
        # newVal =  val.linesep.join([s for s in text.splitlines() if s])
        val =  val.replace("\n"," ")
        val = val.strip()
        if 
        myList2.append(val)
        # print(val)

print(myList2)

#     print(i[0])
# print(totalCases)



# while True:
#     line = file.readline()
#     # if line[]:
#     #     print(line)
#     # print(line)

#     if not line:
#         break

file.close()

# filepath = 'input.txt'
# with open(filepath) as fp:
#    line = fp.readline()
#    cnt = 1
#    while line:
#        print("Line {}: {}".format(cnt, line.strip()))
#        line = fp.readline()
#        cnt += 1