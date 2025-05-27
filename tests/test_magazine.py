from lib.models.magazine import Magazine

def test_create_magazine():
    mag = Magazine.create("TestMag", "Category")
    assert mag.name == "TestMag"

def test_magazine_methods():
    mag = Magazine.find_by_id(1)
    assert mag.article_titles()
    assert mag.contributors()