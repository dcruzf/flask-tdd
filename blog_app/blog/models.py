import os
import uuid
import sqlite3
from pydantic import BaseModel, EmailStr, Field


class NotFound(Exception):
    pass


class Article(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    author: EmailStr
    title: str
    content: str

    @classmethod
    def get_by_id(cls, article_id: str):
        con = sqlite3.connect(os.getenv("DATABASE_NAME", "database.db"))
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute(f"SELECT * FROM articles WHERE id={article_id}")

        record = cur.fetchone()

        if record is None:
            raise NotFound

        article = cls(**record)  # Row is unpacked as dict
        con.close()

        return article
