from django.shortcuts import render

# Create your views here.

def index(request):
    """A view to return the index page"""
    return render(request, 'home/index.html')

#Django logic below for looping navbar, will work on later
"""
def your_view(request):
    dropdown_titles = ['Title 1', 'Title 2', 'Title 3', 'Title 4', 
                       'Title 5', 'Title 6', 'Title 7', 'Title 8']
    return render(request, 'your_template.html', {'dropdown_titles': dropdown_titles})
    """