##########################################################
#  Python module template for helper functions of your own (IAML Level 10)
#  Note that:
#  - Those helper functions of your own for Questions 1, 2, and 3 should be defined in this file.
#  - You can decide function names by yourself.
#  - You do not need to include this header in your submission.
##########################################################
import numpy as np

def normalise(Xtrn, Xtst):
    
    Xtrn /= 255.0
    Xtst /= 255.0
    Xmean = np.mean(Xtrn, axis=0)
    Xtrn_nm = Xtrn - Xmean
    Xtst_nm = Xtst - Xmean
    
    return Xtrn_nm, Xtst_nm

def get_image(pos, distances, class_samples):
    
    idx = np.where(distances == np.sort(distances)[pos])[0][0]
    img = class_samples[idx]
    
    return img, idx

def get_first_samples(X, y):
    
    classes = np.unique(y)
    first_samples = []
    
    for class_label in classes:
        for idx in range(len(X)):
            sample_label = y[idx]
            if(sample_label==class_label):
                first_samples.append(X[idx])
                break
                
    first_samples = np.array(first_samples)
    #print(first_samples.shape)
    
    return first_samples

def get_first_1000(X, y):
    
    classes = np.unique(y)
    first_1000 = []
    labels = []
    condition = 1
    
    for class_label in classes:
        for idx in range(len(X)):
            sample_label = y[idx]
            if(sample_label==class_label):
                first_1000.append(X[idx])
                labels.append(sample_label)
                condition = len(first_1000)%1000
                if(condition == 0):
                    break
                              
    first_1000 = np.array(first_1000)
    labels = np.array(labels)
    
    return first_1000, labels