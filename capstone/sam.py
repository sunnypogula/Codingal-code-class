sample = [1,0,1,1,1,1,1,0,1,0,0,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1]

totalPup = len(sample)
blue_eye = sum(sample)
hazel_eye = totalPup - blue_eye

blue_prop = blue_eye / totalPup
hazelPro = hazel_eye / totalPup

print("Total Puppies:",totalPup)
print("Blue eyes puppies:",blue_eye)
print("Hazel eyes puppies:",hazel_eye)
print("Blue eyes proporation:",blue_prop)
print("Hazel eyes proporation:",hazelPro)
