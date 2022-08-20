def printImage(image):
    for line in  image:
        print(line.replace("0",".").replace("1","#"))

def enlargeImage(image, enlargeBy, default):
    newImage = []
    for i in range(enlargeBy):
        newImage.append(default * (len(image[0])+(2*enlargeBy)))
    for line in image:
        newImage.append(enlargeBy * default + line + enlargeBy * default)
    for i in range(enlargeBy):
        newImage.append(default*(len(image[0])+(2*enlargeBy)))
    return newImage

def getPixel(image, y,x,default):
    if y < 0 or y > len(image)-1 or x < 0 or x > len(image[0]):
        return default
    return image[y][x]

def getPixelBrightness(image, y, x, algorithem, default):
    surounding = ""
    for yOffset in range(-1,2):
        for xOffset in range(-1,2):
            surounding += getPixel(image,y+yOffset,x+xOffset,default)
    return algorithem[int(surounding,2)]

def applyEnhancement(image, algorithem, default):
    newImage = []
    image = enlargeImage(image,2,default)
    for y in range(len(image)-1):
        newLine = ""
        for x in range(len(image[0])-1):
            newLine += getPixelBrightness(image,y,x,algorithem, default)
        newImage.append(newLine)
    return newImage


input = open("input.txt","r").read().split("\n\n")

algorithem = input[0].replace(".","0").replace("#","1")

originalImage = input[1].replace(".","0").replace("#","1").split("\n")

originalImage = applyEnhancement(originalImage,algorithem,"0")
originalImage = applyEnhancement(originalImage,algorithem,algorithem[0])

printImage(originalImage)

print(str(originalImage).count("1"))