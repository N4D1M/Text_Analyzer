from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    if request.method == 'POST':
        val1 = request.POST.get('chk1','off')
        val2 = request.POST.get('chk2','off')
        val3 = request.POST.get('chk3','off')
        val4 = request.POST.get('chk4','off')
        val5 = request.POST.get('chk5','off')
        val6 = request.POST.get('chk6','off')
        val7 = request.POST.get('chk7','off')
        val8 = request.POST.get('chk8','off')
        val9 = request.POST.get('chk9','off')
        val10 = request.POST.get('chk10','off')
        val11 = request.POST.get('chk11','off')
        val12 = request.POST.get('chk12','off')
        
        info = request.POST.get('text')
        
        params = {}
        # info=""
        if val1 == "on":
            params = {"purpose":"Show Information","msg":info,'info':info}
            return render(request,'index.html',params)

        elif val2 == "on":
            words = info.split()
            count_words = len(words)
            params = {"purpose":"Count Words","msg":count_words,'info':info}
            return render(request,'index.html',params)

        elif val3 == "on":
            count = 0
            count_lines = info.split("\n")
            for i in count_lines:
                if i:
                    count += 1
            params = {"purpose":"Count Lines","msg":count,'info':info}
            return render(request,'index.html',params)

        elif val4 == "on":
            data = info.split()
            word_count = {}
            for i in data:
                word = info.count(i)
                word_count.update({i:word})
            # params = {"purpose":"Count word Frequency","msg":word_count.items(),'info':info}
            params = {"purpose":"Count Word Frequency","msg":word_count,'msg1':word_count.items(),'info':info}
            return render(request,'index.html',params)

        elif val5 == "on":
            uppercase = ""
            for char in info:
                uppercase = uppercase + char.upper()
            params = {"purpose":"Convert Into UPPERCASE","msg":uppercase,'info':info}
            return render(request,'index.html',params)
        
        elif val6 == "on":
            lowercase = ""
            for char in info:
                lowercase = lowercase + char.lower()
            params = {"purpose":"convert into lowercase","msg":lowercase,'info':info}
            return render(request,'index.html',params)

        elif val7 == "on":
            info1 = ""
            punc_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '|', '+', '.', '=', '{', '}', '[', ']', '"', ';', ':', '`', '~', '-', '_']
            for p in info:
                if p not in punc_list:
                    info1+=p
            params = {"purpose":"Remove Punctuation","msg":info1,'info':info}
            return render(request,'index.html',params)
        
        elif val8 == "on":
            v1=[]
            v = info.split()
            vow = "aeiouAEIOU"
            for i in v:
                if i[0] in vow:
                    v1.append(i)
            v =' '.join(v1)
            params = {"purpose":"Vowel Starting Words","msg":v,'info':info}
            return render(request,'index.html',params)

        elif val9 == "on":
            params = {"purpose":"Find Single Character","msg":v,'info':info}
            return render(request,'index.html',params)
        else:
            return HttpResponse("<h1>Error....</h1>")
        
            # info = request.POST.get('text')
    else:
        return render(request,'index.html')



        # return render(request,'form.html',{'msg':info})

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
    