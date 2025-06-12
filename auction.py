import requests
from bs4 import BeautifulSoup


def extract_data_from_html(html):
    soup = BeautifulSoup(html, "html.parser")
    data = []

    # Find all the blocks that contain the information in each node from all the 38 pages
    car_blocks = soup.find_all("div", class_="card")

    for block in car_blocks:
        # For the items and reference numbers extraction
        link_tag = block.find("div", class_="course_tag").find("a", href=True)
        url = link_tag["href"]
        reference_number = link_tag.text.strip()

        # For the bidding prices extraction
        price_tag = block.find("div", class_="course_price").find("span")
        price = price_tag.text.strip()

        # For the item title extraction
        title_tag = block.find("h5", class_="card-title")
        car_title = title_tag.text.strip()

        #  For the item condition and VIN
        details_tag = block.find("p", class_="card-text")
        details = details_tag.get_text(separator=" ").strip().split()

        # -1 for condition and 0 for VIN
        vin = details[0] if len(details) > 0 else "N/A"
        condition = details[-1] if len(details) > 1 else "N/A"

        # # Extraction of the transmission, mileage, and fuel type [0] for transmission, [1] for mileage, [2] for fuel type
        footer_tags = block.find_all("a", class_="d-inline-block col text-dark")
        transmission = (
            footer_tags[0].find("span").text.strip() if len(footer_tags) > 0 else "N/A"
        )
        mileage = (
            footer_tags[1].find("span").text.strip() if len(footer_tags) > 1 else "N/A"
        )
        fuel_type = (
            footer_tags[2].find("span").text.strip() if len(footer_tags) > 2 else "N/A"
        )

        # after getting the data show the results below
        data.append(
            {
                "URL": url,
                "Reference Number": reference_number,
                "Price": price,
                "Car Title": car_title,
                "Condition": condition,
                "VIN": vin,
                "Transmission": transmission,
                "Mileage": mileage,
                "Fuel Type": fuel_type,
            }
        )

    return data


def scrape_multiple_pages(links):
    all_data = []

    # run a for loop in the links
    for url in links:
        try:
            response = requests.get(url, timeout=15)
            response.raise_for_status()  # Check for request errors

            page_data = extract_data_from_html(response.text)
            all_data.extend(page_data)

            print(f"Data extracted from {url}")

        except requests.exceptions.Timeout:
            print("Request timed out!")

        except requests.RequestException as e:
            print(f"Failed to retrieve data from {url}: {e}")

    return all_data


# List of links to scrape
website_pages = [
    "https://auction.nigeriatradehub.gov.ng/previous_auction.php",
    "https://auction.nigeriatradehub.gov.ng/previous_auction.php?page=2",
    "https://auction.nigeriatradehub.gov.ng/previous_auction.php?page=3",
    "https://auction.nigeriatradehub.gov.ng/previous_auction.php?page=4",
    "https://auction.nigeriatradehub.gov.ng/previous_auction.php?page=5",
    "https://auction.nigeriatradehub.gov.ng/previous_auction.php?page=6",
    "https://auction.nigeriatradehub.gov.ng/previous_auction.php?page=7",
    "https://auction.nigeriatradehub.gov.ng/previous_auction.php?page=8",
    "https://auction.nigeriatradehub.gov.ng/previous_auction.php?page=9",
    "https://auction.nigeriatradehub.gov.ng/previous_auction.php?page=10",
    "https://auction.nigeriatradehub.gov.ng/previous_auction.php?page=11",
    "https://auction.nigeriatradehub.gov.ng/previous_auction.php?page=12",
    "https://auction.nigeriatradehub.gov.ng/previous_auction.php?page=13",
    "https://auction.nigeriatradehub.gov.ng/previous_auction.php?page=14",
    "https://auction.nigeriatradehub.gov.ng/previous_auction.php?page=15",
    "https://auction.nigeriatradehub.gov.ng/previous_auction.php?page=16",
    "https://auction.nigeriatradehub.gov.ng/previous_auction.php?page=17",
    "https://auction.nigeriatradehub.gov.ng/previous_auction.php?page=18",
    "https://auction.nigeriatradehub.gov.ng/previous_auction.php?page=19",
    "https://auction.nigeriatradehub.gov.ng/previous_auction.php?page=20",
    "https://auction.nigeriatradehub.gov.ng/previous_auction.php?page=21",
    "https://auction.nigeriatradehub.gov.ng/previous_auction.php?page=22",
    "https://auction.nigeriatradehub.gov.ng/previous_auction.php?page=23",
    "https://auction.nigeriatradehub.gov.ng/previous_auction.php?page=24",
    "https://auction.nigeriatradehub.gov.ng/previous_auction.php?page=25",
    "https://auction.nigeriatradehub.gov.ng/previous_auction.php?page=26",
    "https://auction.nigeriatradehub.gov.ng/previous_auction.php?page=27",
    "https://auction.nigeriatradehub.gov.ng/previous_auction.php?page=28",
    "https://auction.nigeriatradehub.gov.ng/previous_auction.php?page=29",
    "https://auction.nigeriatradehub.gov.ng/previous_auction.php?page=30",
    "https://auction.nigeriatradehub.gov.ng/previous_auction.php?page=31",
    "https://auction.nigeriatradehub.gov.ng/previous_auction.php?page=32",
    "https://auction.nigeriatradehub.gov.ng/previous_auction.php?page=33",
    "https://auction.nigeriatradehub.gov.ng/previous_auction.php?page=34",
    "https://auction.nigeriatradehub.gov.ng/previous_auction.php?page=35",
    "https://auction.nigeriatradehub.gov.ng/previous_auction.php?page=36",
    "https://auction.nigeriatradehub.gov.ng/previous_auction.php?page=37",
    "https://auction.nigeriatradehub.gov.ng/previous_auction.php?page=38",
    # Add more URLs as needed
]

# Start the scraping process
scraped_data = scrape_multiple_pages(website_pages)
print(f"Data had been scraped {scraped_data}")
