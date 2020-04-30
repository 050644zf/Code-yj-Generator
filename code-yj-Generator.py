#需要matplot进行绘图
#python -m pip install -U matplotlib
import matplotlib.pyplot as plt
import re
from codeyj import code2img,codeyjencode

if __name__=='__main__':

    #在这里输入需要进行codeyj编码的字符串(全大写)
    ostr="W"

    img=code2img(codeyjencode(ostr))

    plt.imshow(img,cmap='gray'),plt.axis('off'),plt.title(ostr),plt.show()