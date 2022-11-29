# from matplotlib.pyplot import imshow
# import matplotlib.cm as cm
# import matplotlib.pylab as plt
import PIL
import argparse
import numpy as np
from tensorflow.keras.utils import img_to_array
from keras.models import load_model


def rev_conv_label(label):
    if label == 0 :
        return 'AvenirNext'
    elif label == 1:
        return 'Keyboard'
    elif label == 2 :
        return 'SFCompactRounded-Bold'
    elif label == 3 :
        return 'Times'


if __name__ == '__main__':
    img_path="test_data/Times.jpg"
    pil_im =PIL.Image.open(img_path).convert('L')
    pil_im=pil_im.resize((105,105))
    org_img = img_to_array(pil_im)
    data=[]
    data.append(org_img)
    data = np.asarray(data, dtype="float") / 255.0

    model = load_model('top_model.h5')
    # y = model.predict_classes(data)
    predict_y=model.predict(data) 
    print(predict_y)

    classes_y=np.argmax(predict_y, axis=1)
    print(classes_y)

    label = rev_conv_label(int(classes_y))

    print(f"{img_path}: {label}")
