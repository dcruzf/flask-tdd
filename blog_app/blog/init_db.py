import pathlib
import os

print(os.getcwd())
print(f"{pathlib.Path(__file__).parent.absolute()}")


from blog.models import Article


if __name__ == "__main__":
    from blog.models import Article

    Article.create_table()
