from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route

def homepage(request):
    return HTMLResponse ("<h1>Hello World</h1>")

def aboutpagee(request):
    return HTMLResponse ("<h1>about World</h1>")

def contactpage(request):
    return HTMLResponse ("<h1>contact World</h1>")

app=Starlette(
    debug=True
    , routes=[
        Route("/",homepage),Route("/about",aboutpagee),Route("/contact",contactpage),
        
    ],
    )