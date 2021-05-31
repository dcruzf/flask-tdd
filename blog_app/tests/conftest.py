import os
import tempfile  # This module provides generic, low- and high-level interfaces

# for creating temporary files and directories

import pytest

from blog.models import Article


# “Autouse” fixtures are a convenient way to make all tests
# automatically request them. https://docs.pytest.org/en/6.2.x/fixture.html
@pytest.fixture(autouse=True)
def database():
    """
    Create a temporary database before testing and then delete it.
    """
    _, file_name = tempfile.mkstemp()
    os.environ["DATABASE_NAME"] = file_name
    Article.create_table(database_name=file_name)

    yield
    # Remove (delete) the file path. This function is semantically
    # identical to remove()
    # https://docs.python.org/3/library/os.html#os.unlink
    os.unlink(file_name)
