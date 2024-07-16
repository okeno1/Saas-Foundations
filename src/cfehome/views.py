import pathlib

from django.http import HttpResponse

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    
    print(this_dir)
    html_ = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
</head>
<body>
    <h1>Is this anything? (Inline HTML) </h1>
</body>
</html>
    """
   # html_file_path = this_dir/"home.html"
   # html_ = html_file_path.read_text()
        
    return HttpResponse(html_)