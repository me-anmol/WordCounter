from django.shortcuts import render,HttpResponse
from collections import Counter
from urllib.request import urlopen
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.tokenize import word_tokenize
import re 

# Create your views here.
def index (request):
    return render(request,'index.html')

def result(request):
    url = request.POST.get('url')
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text().lower()
    res = re.sub(r'[^\w\s]', '', text) 
    #text = "Nick likes to play football, however he is not too fond of tennis."
    text_tokens = word_tokenize(res)

    tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]


    # Pass the split_it list to instance of Counter class.
    counter = Counter(tokens_without_sw)
    #print(Counter)

    # most_common() produces k frequently encountered
    # input values and their respective counts.
    most_occur = counter.most_common(10)
    print(most_occur)
    return render(request,'result.html',{'most_occur':most_occur})