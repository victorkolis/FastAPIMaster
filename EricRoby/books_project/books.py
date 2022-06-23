from fastapi import FastAPI, Response, status
import uvicorn

app = FastAPI()


books = {
    'book_1': {'title': 'Title One', 'author': 'Author One', 'id': 1},
    'book_2': {'title': 'Title Two', 'author': 'Author Two', 'id': 2},
    'book_3': {'title': 'Title Three', 'author': 'Author Three', 'id': 3},
    'book_4': {'title': 'Title Four', 'author': 'Author Four', 'id': 4},
    'book_5': {'title': 'Title Five', 'author': 'Author Five', 'id': 5},
}


@app.get('/books')
async def get_all_books():
    return books


@app.get('/books/title/{book_title}')
async def get_book_by_title(book_title):
    return {'Book Title': book_title}


@app.get('/books/id/{book_id}')
async def get_book_by_id(book_id: int, response: Response):
    for key, value in books.items():
        if book_id == value.get('id'):
            response.status_code = status.HTTP_200_OK
            return {'msg': value}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {f'msg': f'Book ID {book_id} not found'}


if __name__ == '__main__':
    uvicorn.run(app='books:app', host='0.0.0.0', port=8000)
