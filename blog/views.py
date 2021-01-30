from django.shortcuts import render
# Create your views here.
def index(request):

    code =request.POST.get('code')
    print(code)
    div=f"""
<pre>
    #Your Code Here Here
    {code}
</pre>
    """
    return render(request,'index.html',{'dd':div})