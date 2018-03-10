
##################################
# imports
##################################
from __future__ import print_function
import os, sys
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
# import ML stuff
from resnet50 import ResNet50
from keras.preprocessing import image
from imagenet_utils import preprocess_input, decode_predictions
import numpy as np


##################################
# simple keras deep learning
##################################
class ImageClassifier:
    @staticmethod
    def predict(filename):
        assert os.path.isfile(filename) and 'cannot find file'
        model = ResNet50(weights='imagenet')

        img = image.load_img(filename, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        preds = decode_predictions(model.predict(x))
        if len(preds) == 0:
            return None
        return preds[0][0][1]


##################################
# main
##################################
def main():
    #
    # get image
    #
    if len(sys.argv) != 2:
        print('Usage:\npython classify.py <image file>')
        sys.exit(-1)
   
    #
    # classfiy
    #
    print('content:\n')
    print('>  ' + ImageClassifier.predict(sys.argv[1]) + '  <\n')


##################################
# run
##################################
if __name__ == '__main__':
    main()
    
