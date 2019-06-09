from django.shortcuts import render

# Create your views here.
def wordcount(request):
    return render(request, 'wordcount.html')

def result(request):
    text = request.GET['fulltext']
    text_count =len(text)
    words = text.split()
    text2 = "".join(words)
    text2_count = len(text2)
    word_dictionary={}
    
    for word in words:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    return render(request, 'result.html', {'full' : text, 'total' : len(words), 'dictionary' : word_dictionary.items()
    , 'text_with_space' : text_count, 'text_without_space' : text2_count})