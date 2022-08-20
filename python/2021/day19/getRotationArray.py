inputsRaw = [open("rotations.txt","r").read().split("case")][0]

directions = ["X","Y","Z"]

for line in inputsRaw[1:]:
    output = "["
    opperationRaw = line.split("3{")[1].split("}")[0].replace("v.","")
    for opperation in opperationRaw.split(","):
        isNegative = 1 if "-" in opperation else 0
        output += "("+str(isNegative)+","+str(directions.index(opperation[-1]))+"),"
    print(output[:-1] + "],")

