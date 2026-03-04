import re
import json
# Read receipt text from raw.txt
# Explanation: open the file and read the whole receipt as one string
with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()
#Extract all prices
#pattern finds numbers like 308,00 or 1 200,00
prices = re.findall(r"\d[\d ]*,\d{2}", text)
# Convert prices to float to find the sum beacause the format of numbers is wrong to sum
price_values = [float(p.replace(" ", "").replace(",", ".")) for p in prices]
# Find product names
# product names appear after numbers like "1." "2." etc.
products = re.findall(r"\d+\.\n(.+)", text)
# Calculate total amount
# sum all extracted prices
total_amount = sum(price_values)
# Extract date and time
# pattern finds date and time like 18.04.2019 11:13:58
datetime_match = re.search(r"\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2}", text)
datetime = datetime_match.group() if datetime_match else None
# Find payment method
# search for payment line (Банковская карта)
payment_match = re.search(r"(Банковская карта)", text)
payment_method = payment_match.group() if payment_match else None
# 6. Create structured output (JSON)
# store extracted data in dictionary
receipt_data = {
    "products": products,
    "prices": price_values,
    "total": total_amount,
    "datetime": datetime,
    "paymentmethod": payment_method
}
# Print result in readable JSON format
print(json.dumps(receipt_data, indent=4, ensure_ascii=False))