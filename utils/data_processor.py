from datetime import datetime
from collections import defaultdict

def clean_and_validate(records):
    valid = []
    invalid = 0

    for r in records:
        try:
            if not r['TransactionID'].startswith('T'):
                invalid += 1
                continue
            if not r['CustomerID'] or not r['Region']:
                invalid += 1
                continue

            r['Quantity'] = int(r['Quantity'].replace(',', ''))
            r['UnitPrice'] = float(r['UnitPrice'].replace(',', ''))

            if r['Quantity'] <= 0 or r['UnitPrice'] <= 0:
                invalid += 1
                continue

            r['Date'] = datetime.strptime(r['Date'], '%Y-%m-%d')
            r['ProductName'] = r['ProductName'].replace(',', '')
            valid.append(r)

        except:
            invalid += 1

    print(f"Invalid records removed: {invalid}")
    print(f"Valid records after cleaning: {len(valid)}")
    return valid


def calculate_total_revenue(transactions):
    return sum(t['Quantity'] * t['UnitPrice'] for t in transactions)
