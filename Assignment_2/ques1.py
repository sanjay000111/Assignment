# Write a function that computes the volume of a sphere given its radius.
def volume():
    r = int(input("Enter radius : "))
    vol = (12.56 * r * r * r) / 3
    return vol

result = volume()
print("Volume of sphere is : ",round(result,2))