from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates

from quiz import find_majority, check_for_duplicates

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
async def root(
        request: Request, 
        r0c0: int = Form(...),
        r0c1: int = Form(...),
        r0c2: int = Form(...),
        r0c3: int = Form(...),
        r1c0: int = Form(...),
        r1c1: int = Form(...),
        r1c2: int = Form(...),
        r1c3: int = Form(...),
        r2c0: int = Form(...),
        r2c1: int = Form(...),
        r2c2: int = Form(...),
        r2c3: int = Form(...),
        r3c0: int = Form(...),
        r3c1: int = Form(...),
        r3c2: int = Form(...),
        r3c3: int = Form(...),
):
    Rankings = [
            [r0c0, r0c1, r0c2, r0c3],
            [r1c0, r1c1, r1c2, r1c3],
            [r2c0, r2c1, r2c2, r2c3],
            [r3c0, r3c1, r3c2, r3c3]
    ]

    if check_for_duplicates(Rankings):
        return templates.TemplateResponse(
                'quiz.html', 
                context={
                    'request': request,
                    'result': None
                }
        )

    colors, totals = find_majority(Rankings)
    result = {'colors': colors, 'totals': totals, 'rankings': Rankings}

    return templates.TemplateResponse(
            'result.html', 
            context={
                'request': request,
                'result': result,
            }
    )

