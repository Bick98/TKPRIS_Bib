from app import app
from flask import render_template, request, session
from utils import get_db_connection
from models.index_model import get_books
import pandas as pd


@app.route('/index', methods=['get', 'post'])
def index():
    con = get_db_connection()

    df_books = get_books(con)

    html = render_template(
        'index.html',
        books = df_books,
        len=len
        )

    return html