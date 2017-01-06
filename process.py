
import numpy as np
import cv2

#videofilepath = '/Videos/SpiritedAway.mkv'
videofilepath = '/Videos/Mulan.mp4'
#videofilepath = '/Videos/GoodWillHunting.mp4'

cap = cv2.VideoCapture(videofilepath)

length = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
div = 1000
nums = range(0, length-div, div)

num = int(length/div)
i = 0
total="first"
while(cap.isOpened()):
    for number in nums:
        cap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES,number)
        #print number
        ret, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.CV_LOAD_IMAGE_COLOR) #, cv2.COLOR_ BGR2GRAY)
        dim = (int(frame.shape[1]/num)*4, int(frame.shape[0])*4)
        resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
        if total is not "first":
            total = np.concatenate((total, resized), axis=1)
        else:
            total = resized 
    cap.release()
filename = videofilepath.split("/")[-1].split(".")[0]
cv2.imwrite(filename+".png", total)

    #cv2.imshow('frame',frame)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
        #try:
        #    cv2.imwrite("small.png", gray)



# perform the actual resizing of the image and show it

'''
image = cv2.imread('original.png')

dim = (int(image.shape[1]/100), int(image.shape[0]))
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
vis = np.concatenate((resized, resized), axis=1)
cv2.imshow('resized',vis)
'''
#k = cv2.waitKey(0) & 0xFF
#if k == 27:         # wait for ESC key to exit
#    cv2.destroyAllWindows()
#elif k == ord('s'): # wait for 's' key to save and exit
#    cv2.imwrite('messigray.png',img)
        #except:
        #    img = cv2.imread('messi5.jpg',0)
        #    print('unable to save file')
        #print("Saved PNG file with alpha data.")
        #break

#
#cv2.destroyAllWindows()
