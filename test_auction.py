from auction import extract_data_from_html

def test_extract_data_from_html():
    links = assert extract_data_from_html.urls()
    assert isinstance(links, list)         

