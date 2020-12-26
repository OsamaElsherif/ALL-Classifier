import tensorflow as tf
import cv2
import numpy as np
import os

class Testing():
    def __init__(self, im):
        print("Intiating")
        print(im)
        self.compileing(im)
        
    def preparing(self, tested_img):
        print("preparing")
        IMG_SIZE = 128
        img_array = cv2.imread(tested_img)
        nimg_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
        return nimg_array.reshape(-1, IMG_SIZE, IMG_SIZE, 3)

    def compileing(self, im):
        print("compiling")
        opinions = []

        for model in os.listdir('Models/'):
            model = tf.keras.models.load_model(f'Models/{model}/')
            prediction = model.predict([self.preparing(im)])
            opinions.append(int(prediction[0][0]))

        propability = {i:opinions.count(i) for i in opinions}
        
        CATAGORIES = ['Diseased -- ALL ', 'Non-Diseased -- HEM']

        length = len(opinions)
        self.run(propability=propability, n=0, CATAGORIES=CATAGORIES)
    
    def run(self, length=3, propability={}, n=0, messages=[], CATAGORIES=[]):
        print("running")
        length = length
        propability =  propability
        CATAGORIES_LEN = len(CATAGORIES)

        for n in range(0, CATAGORIES_LEN):
            try:
                fre = propability[n]
                percentage = (fre / length) * 100 
                print(CATAGORIES[n])
                print(f'percentage : {percentage}')
                message = f"{CATAGORIES[n]} : {percentage}"
                print(f"from Normal place {messages}")
                messages.append(message)
                n += 1
            except Exception as e:
                n += 1
                    
        return messages

if __name__ == '__main__':
    #print(Testing('imgs/index.jpeg').run())
    pass


#def prepare(filepath):
#    IMG_SIZE = 128
#    img_arr = cv2.imread(filepath)
#    new_arr = cv2.resize(img_arr, (IMG_SIZE, IMG_SIZE))
#    return new_arr.reshape(-1, IMG_SIZE, IMG_SIZE, 3)
#
#opinions = []
#
#for model in os.listdir('Models/'):
#    model = tf.keras.models.load_model(f'Models/{model}/')
#    prediction = model.predict([prepare(f'testing_data_valid/{img}')])
#    opinions.append(int(prediction[0][0]))
#
#propapility = {i:opinions.count(i) for i in opinions}
#CATS = ['all', 'hem']
#n = 0
#while n <= 1:
#    try:
#        fre = propapility[n]
#        percentage = (fre/3)*100
#        print(f'{CATS[n]} : {percentage}')
#        n += 1
#    except Exception as e:
#        pass



