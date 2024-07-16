import pathlib

from django.http import HttpResponse

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    
    my_title = "My page"
    my_context={
        "page_title":my_title
    }
    
    
    #print(this_dir)
    html_ = f"""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
</head>
<body>
    <h1>{page_title} anything? </h1>
</body>
</html>
    """.format(**my_context) #page_title=my_title
   # html_file_path = this_dir/"home.html"
   # html_ = html_file_path.read_text()
        
    return HttpResponse(html_)