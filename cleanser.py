import re
# this function will cleanse string into numnber
def cleanse_value(value, id = None):

    # Convert the value to string in case it's not
    value_str = str(value).strip()

    # Strip leading and trailing spaces
    value_str = value_str.replace(' ', '').replace("'",'')

    # Correcting formatting for negative numbers ("- 100.00" into "-100.0")
    if value_str.startswith('- '):
        value_str = '-' + value_str[2:]

    # Check if the comma is used as a decimal separator
    if re.search(r',\d{1,2}$', value_str):
        # Comma is used as a decimal separator
        value_str = value_str.replace(',', '.')
    else:
        # Comma is thousand separator, so remove it
        value_str = value_str.replace(',', '')

    # Check for empty strings after stripping spaces
    if not value_str:
        return np.nan, None

    # Convert to float or return 'error' in case of invalid format
    try:
        return float(value_str), None
    except ValueError:
        error_msg = f"Could not convert {value} to number for {id}. Replaced by 0.0"
        return 0.0, error_msg

values = ['123.4', '123.45', '123.450', '123,450', '123,450.10', '123,45', '123,4', '123 450', '123 450.22', '123 450,22', '123 ds.33']
for v in values:
    print(cleanse_value(v))
