from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='../templates/')

@app.get('/')
async def root(request: Request):
    result = None
    return templates.TemplateResponse(
            'quiz.html', 
            context={
                'request': request,
                'result': result
            }
    )

@app.post('/')
async def root(request: Request, color: str = Form(...)):
    result = color
    return templates.TemplateResponse(
            'result.html', 
            context={
                'request': request,
                'result': result
            }
    )

