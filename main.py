from utils.file_handler import read_sales_file
from utils.data_processor import clean_and_validate, calculate_total_revenue
from utils.api_handler import fetch_all_products, create_product_mapping

def main():
    print("SALES ANALYTICS SYSTEM")

    records = read_sales_file("data/sales_data.txt")
    valid_records = clean_and_validate(records)

    revenue = calculate_total_revenue(valid_records)
    print("Total Revenue:", revenue)

    products = fetch_all_products()
    product_map = create_product_mapping(products)

    print("Process Complete!")

if __name__ == "__main__":
    main()
