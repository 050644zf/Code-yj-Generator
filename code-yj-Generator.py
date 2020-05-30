#需要matplot进行绘图/Require matplotlib to print the barcode
#运行以下命令以安装matplotlib/Run the following command to install matplotlib
#python -m pip install -U matplotlib

import matplotlib.pyplot as plt
import re
from codeyj import code2img,codeyjencode

if __name__=='__main__':

    #在这里输入需要进行codeyj编码的字符串(全大写)
    #input your string here (UPPER CASE)
    ostr="STORIES OF AFTERNOON"

    img=code2img(codeyjencode(ostr))

    plt.imshow(img,cmap='gray'),plt.axis('off'),plt.title(ostr),plt.show()