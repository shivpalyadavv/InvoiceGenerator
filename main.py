# create a product and price for three items
product1_name, product1_price = 'Sweets', 90.05
product2_name, product2_price = 'Cake', 608.01
product3_name, product3_price = 'Snacks', 99.89

# create a company name and information
company_name = 'Shiv Sweets.'
company_address = 'Pandeypur Chauraha'
company_city = 'Varanasi'

# declare ending message
message = 'Thanks for visiting us today!'

# create a top border
print('*' * 70)

# print company information first using format
print('\t\t{}'.format(company_name.title()))
print('\t\t{}'.format(company_address.title()))
print('\t\t{}'.format(company_city.title()))

# print a line between sections
print('=' * 70)

# print out header for section of items
print('\tProduct Name\tProduct Price')

# create a print statement for each item
print('\t{}\t\t${}'.format(product1_name.title(), product1_price))
print('\t{}\t${}'.format(product2_name.title(), product2_price))
print('\t{}\t\t${}'.format(product3_name.title(), product3_price))

# print a line between sections
print('=' * 70)

# print out header for section of total
print('\t\t\tTotal')

# calculate total price and print out
total = product1_price + product2_price + product3_price
print('\t\t\t${}'.format(total))

# print a line between sections
print('=' * 70)

# output thank you message
print('\n\t{}\n'.format(message))

# create a bottom border
print('*' * 70)