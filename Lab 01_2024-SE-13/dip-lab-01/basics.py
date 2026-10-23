# Task 1: Variables and Data Types

width = 640
height = 480
image_name = "sample.png"
is_color = True

print("Width:", width, type(width))
print("Height:", height, type(height))
print("Image name:", image_name, type(image_name))
print("Is color:", is_color, type(is_color))
print("Total pixels:", width * height)

# Task 2: Conditions

for intensity in [-1, 0, 127, 128, 255, 256]:
    if intensity < 0 or intensity > 255:
        label = "Invalid"
    elif intensity >= 128:
        label = "Bright pixel"
    else:
        label = "Dark pixel"

    print(intensity, ":", label)



# Task 3: For and While Loops

for pixel in [20, 130, 255]:
    if pixel >= 128:
        print(pixel, "Bright pixel")
    else:
        print(pixel, "Dark pixel")

counter = 0
while counter < 3:
    print(counter)
    counter += 1


    
# Task 4: Functions

def is_bright(pixel, threshold=128):
    return pixel >= threshold

print(is_bright(127))
print(is_bright(128))
print(is_bright(200, 210))




# Task 5: Lists and Tuples

pixels = [0, 128, 255]

print("First pixel:", pixels[0])

pixels[1] = 150
pixels.append(64)

print("Pixels:", pixels)
print("Length:", len(pixels))

size = (640, 480)
width, height = size

print("Width:", width, "Height:", height)

# Lists can be changed; tuples cannot be changed after creation.



# Task 6: Dictionaries and Sets

image = {"width": 640, "height": 480}
image["mode"] = "RGB"

print("Image width:", image["width"])
print("Image mode:", image["mode"])

labels = set(["cat", "dog", "cat", "bird"])
print("Unique labels:", len(labels))
