import matplotlib.pyplot as plt
import os
import numpy as np
from pds4_tools import pds4_read
import colour
from colour_demosaicing import demosaicing_CFA_Bayer_Menon2007
from skimage import exposure
from skimage import img_as_float

filePath = 'change5'
image_2BL = []
image_2B = []
for root, dirs, files in os.walk(filePath):
    for path in files:
        if path.endswith('2BL'):
            image_2BL.append('change5/'+path)
        elif path.endswith('2B'):
            image_2B.append('change5/'+path)

def read_pds(path):
    data = pds4_read(path, quiet=True)
    img = np.array(data[0].data)
    img = img_as_float(img)
    return img

cctf_encoding = colour.cctf_encoding
_ = colour.utilities.filter_warnings()

def modifie_img(img, CFA='RGGB'):
    # Menon2007 yields better edges than bilinear
    modified_img = cctf_encoding(demosaicing_CFA_Bayer_Menon2007(img, CFA))
    p2, p98 = np.percentile(modified_img, (2, 98))
    modified_img = exposure.rescale_intensity(modified_img, in_range=(p2, p98))
    return modified_img

def plot_img(image):
    fig, ax_img = plt.subplots(figsize=(10,10))
    # Show image
    ax_img.imshow(image)
    ax_img.set_axis_off()

for path in image_2BL:
    img = read_pds(path)
    final = modifie_img(img)
    plot_img(final)
    #plt.savefig('{}'.format(str(path)),dpi=1000,bbox_inches = 'tight')
    plt.savefig(f'{path}.png',dpi=1000,bbox_inches = 'tight')
    plt.show()


