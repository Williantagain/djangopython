from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html', {})
    """nous avons créé une fonction (def) appelée post_list qui prend une 
    request (requête) et qui va return (retourner) la valeur donnée par une autre fonction render
     qui va assembler notre template blog/post_list.html."""
