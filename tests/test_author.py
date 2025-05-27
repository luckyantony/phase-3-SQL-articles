from lib.models.author import Author

def test_create_author():
    author = Author.create("Test Author")
    assert author.name == "Test Author"

def test_find_author():
    found = Author.find_by_id(1)
    assert found is not None