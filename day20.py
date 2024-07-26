from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

def homepage(request):
    return JSONResponse ("<h1>Hello World</h1>")

def aboutpagee(request):
    return JSONResponse ("<h1>about World</h1><a href='/'>Home</a>")

def contactpage(request):
    return JSONResponse ("<h1>contact world </h1>")

def apiview (request):
    return JSONResponse ({"message":"hello"})

app=Starlette(
    debug=True
    , routes=[
        Route("/",homepage),Route("/about",aboutpagee),Route("/contact",contactpage),Route("/api",apiview),
        
    ],
    )