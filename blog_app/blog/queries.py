from typing import List

from pydantic import BaseModel

from blog.models import Article


class ListArticlesQuery(BaseModel):
    """
    This query lists all articles
    """

    def execute(self) -> List[Article]:
        articles = Article.list()

        return articles


class GetArticleByIDQuery(BaseModel):
    """
    This query retrieves article by id
    """

    id: str

    def execute(self) -> Article:
        article = Article.get_by_id(self.id)

        return article
