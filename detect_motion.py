from SimpleCV import*
import time

MIN_BLOB_SIZE = 1000

c = Camera()

old_image = c.getImage()

while True:
    time.sleep(1)
    new_image = c.getImage()
    diff = new_image - old_image
    blobs = diff.findBlobs(minsize=MIN_BLOB_SIZE)
    if blobs:
        print("Movement detected")
    old_image = new_image
