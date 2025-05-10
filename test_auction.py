from unittest.mock import patch, Mock  # importing the library that will fake the url response
from auction import extract_data_from_html, scrape_multiple_pages # importing the functions from auction.py

# simulated HTML that matches the scraper’s expectations
simulated_html = """
<html>
<body>
    <div class="card">
        <div class="course_tag">
            <a href="details.php?refNo=123&itemType=Vehicle">REF123</a>
        </div>
        <div class="course_price">
            <span>₦3,500,000</span>
        </div>
        <h5 class="card-title">2012 Toyota Corolla</h5>
        <p class="card-text">123456789ABCDEFG used</p>
        <div class="card-footer">
            <a class="d-inline-block col text-dark"><span>Automatic</span></a>
            <a class="d-inline-block col text-dark"><span>85,000 km</span></a>
            <a class="d-inline-block col text-dark"><span>Petrol</span></a>
        </div>
    </div>
</body>
</html>
"""

def test_extract_data_from_html():
    result = extract_data_from_html(simulated_html)

    assert isinstance(result, list)
    assert len(result) == 1

    items = result[0]

    assert items['URL'] == "details.php?refNo=123&itemType=Vehicle"
    assert items['Reference Number'] == "REF123"
    assert items['Price'] == "₦3,500,000"
    assert items['Car Title'] == "2012 Toyota Corolla"
    assert items['VIN'] == "123456789ABCDEFG"
    assert items['Condition'] == "used"
    assert items['Transmission'] == "Automatic"
    assert items['Mileage'] == "85,000 km"
    assert items['Fuel Type'] == "Petrol"

@patch('auction.requests.get')
def test_scrape_multiple_pages(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = simulated_html
    mock_get.return_value = mock_response

 # Mock 38 URLs
    test_urls = [f"https://auction.fake/page{i}" for i in range(1, 39)]
    

    result = scrape_multiple_pages(test_urls)

    assert isinstance(result, list)
    assert len(result) == 38  

    for auctioned_items in result:
        assert auctioned_items['Reference Number'] == "REF123"
        assert auctioned_items['Car Title'] == "2012 Toyota Corolla"
       

