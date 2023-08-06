from lib import *
#from implementation import * 
from collections import defaultdict
chartoascii={0:48,
1 :49,
2 :50,
3 :51,
4 :52,
5 :53,
6 :54,
7 :55,
8 :56,
9 :57,
10 :65,
11 :66,
12 :67,
13 :68,
14 :69,
15 :70,
16 :71,
17 :72,
18 :73,
19 :74,
20 :75,
21 :76,
22 :77,
23 :78,
24 :79,
25 :80,
26 :81,
27 :82,
28 :83,
29 :84,
30 :85,
31 :86,
32 :87,
33 :88,
34 :89,
35 :90,
36 :97,
37 :98,
38 :100,
39 :101,
40 :102,
41 :103,
42 :104,
43 :110,
44 :113,
45 :114,
46 :116}

def data_distribution():
    plt.style.use("fivethirtyeight")

    digits_counter=Counter()
    digits_counter.update(label)
    d=[]
    for x in digits_counter.items():
        d.append(list(x))
    digits_counter=d
    digits_counter.sort(key=lambda x:x[0])
    digits=[]
    counts=[]

    for i,j in digits_counter:
        digits.append(i)
        counts.append(j)

    plt.bar(digits,counts)
    plt.title("Distribution of Digits")
    plt.ylabel("total counts")
    plt.tight_layout()
    plt.show()

#function create_img is use to sample image in our training data
def create_img():
    d=defaultdict()
    l=data.iloc[:,1:]
    op=data.iloc[:,0]
    print(op)
    for i in range(2000):
        if op[i] not in d:
            d[op[i]]=1
            gray_scale_array=list(l.iloc[i])
            mode='L'
            size=28,28
            image_out = PIL.Image.new(mode,size)
            image_out.putdata(gray_scale_array)
            image_out.save('sample/test_out{}.png'.format(chr(chartoascii[op[i]])))
#create_img()

#img_show function display any image passed as array 
def img_show(a):
    mode='L'
    size=28,28
    i=PIL.Image.new(mode,size)
    i.putdata(a)
    i.show()
    i.save('demo_digit/pca_{}.png'.format("imp_image"))

#variance
def variance_pca_plot():
    _sum=0
    var=list(variance)
    for i in range(len(var)):
        _sum+=var[i]
        var[i]=_sum
    x_label=[ i for i in range(1,len(var)+1)]
    y_label=var
    print(len(x_label))
    print(len(y_label))
    plt.bar(x_label,y_label)
    plt.title("The cumulative variance of Principal components")
    plt.ylabel("Percentage variance")
    plt.show() 

#variance_pca_plot()

def img_to_array(path):
    im=PIL.Image.open(path)
    print(im.size)
    im.thumbnail((28,28))
    print(im.size)
    x=np.array(im)
    ans=[]
    for i in range(len(x)):
        for j in range(len(x[0])):
            ans.append((0.3 *x[i][j][0] ) + (0.59 * x[i][j][1]) + (0.11 * x[i][j][2]))   
    #print(ans)
    #print(len(ans))
    #img_show(ans)
    return np.array([np.array(ans)])
    
#x=img_to_array("C:/Users/ashish agarwal/Desktop/pavan imp videos/MPR Project/drawn.png")
#print(x)