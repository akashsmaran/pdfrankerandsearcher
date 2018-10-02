import PyPDF2 
from nltk import word_tokenize  
from nltk.corpus import stopwords
import nltk
# creating a pdf file object 
def dict_return(pdf):
    pdfFileObj = open(pdf, 'rb') 
    
    # creating a pdf reader object 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    
    # printing number of pages in pdf file 
    n = pdfReader.numPages
    dic = {}
    doc = []  
    # creating a page object 
    for i in range(n):
        pageObj = pdfReader.getPage(i)
        a = str(pageObj.extractText())
        word = ""
        for char in a:
            if char not in '''!()-[]{};:'"\,<>./?@#$%^&*_~''':
                word = word + char
        #word = a.split(" ")
        word = word.lower()
        word1 = word_tokenize(word)
        #print(word1)
        for x in word1:
            doc.append(x)

    #print(doc)
    stop = set(stopwords.words('english'))
    listop = [i for i in doc if i not in stop]
    ps = nltk.stem.PorterStemmer()
    listopandstem = [ps.stem(i) for i in listop]
    #print(listopandstem)
    for value, wor in enumerate(listopandstem):
        if(wor in dic):
            dic[wor].append(value)
        else:
            dic[wor] = [value]
    #print(dic)
    pdfFileObj.close() 
    return dic
pdf = ['wehack_dataset/15147_split_1.pdf','wehack_dataset/15147_split_2.pdf',
'wehack_dataset/15147_split_3.pdf','wehack_dataset/15147_split_4.pdf','wehack_dataset/15147_split_5.pdf',
'wehack_dataset/15147_split_6.pdf','wehack_dataset/15147_split_7.pdf','wehack_dataset/15147_split_8.pdf',
'wehack_dataset/15147_split_9.pdf','wehack_dataset/15147_split_10.pdf']
def ret_dic():
    list_of_doc = []
    for i in pdf:
        list_of_doc.append(dict_return(i))
    return list_of_doc
#print(dict_return('wehack_dataset/15147_split_10.pdf')["pattern"])