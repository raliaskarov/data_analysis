# this function will cleans str into number

def cleanse_value(value, id = None):

    errors = []

    # Convert the value to string in case it's not
    value_str = str(value).strip()

    # Strip leading and trailing spaces
    value_str = value_str.replace(' ', '')

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
        return np.nan

    # Convert to float or return 'error' in case of invalid format
    try:
        return float(value_str)
    except ValueError:
        return f"error when trying to convert {value} after preprocessing into {value_str} for id {id} "
# test
values = ['123.4', '123.45', '123.450', '123,450', '123,450.10', '123,45', '123,4', '123 450', '123 450.22', '123 450,22']
for v in values:
    cleansed = cleanse_value(v, id = v)
    print(f"value {v} cleansed into {cleansed}")
