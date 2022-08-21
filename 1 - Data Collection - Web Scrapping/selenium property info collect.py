# importing libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import random
import time

# parameters
wait_time = random.uniform(1.0, 2.0)
url_1 = 'https://www.dfimoveis.com.br/aluguel/df/todos/apartamento?pagina=1'
url = 'https://www.dfimoveis.com.br/aluguel/df/todos/apartamento?pagina='
class_to_search = 'property-list__item'
output_file = 'selenium property info output.csv'

# xpath
last_page_path = '/html/body/div[1]/section[3]/div[3]/ul/li[18]/span'
property_path = '/html/body/div[1]/section[3]/div[2]/ul/li['
property_title_path = ']/div/div[2]/div[2]/h3[1]/a'
property_subtitle_path = ']/div/div[2]/div[2]/h3[1]/span/span[1]'
property_price_unit_path = ']/div/div[2]/div[2]/h4[1]/span[1]'
property_price_path = ']/div/div[2]/div[2]/h4[1]/span[2]'
property_price_2_unit_path = ']/div/div[2]/div[2]/h4[1]/span[3]'
property_price_2_path = ']/div/div[2]/div[2]/h4[1]/span[4]'
property_type_size_path = ']/div/div[2]/div[2]/ul[2]/li[1]'
property_bedrooms_path = ']/div/div[2]/div[2]/ul[2]/li[2]'
property_suite_path = ']/div/div[2]/div[2]/ul[2]/li[3]'
property_parking_path = ']/div/div[2]/div[2]/ul[2]/li[4]'
property_description_path = ']/div/div[2]/div[2]/p'

# funcion to collect property info
def get_property( i ):
    try:
        title = driver.find_element(By.XPATH, property_path + i + property_title_path)
        all_title.append(title.text)
    except:
        all_title.append('')
    try:
        subtile = driver.find_element(By.XPATH, property_path + i + property_subtitle_path)
        all_subtitle.append(subtile.text)
    except:
        all_subtitle.append('')
    try:
        price_unit = driver.find_element(By.XPATH, property_path + i + property_price_unit_path)
        all_price_unit.append(price_unit.text)
    except:
        all_price_unit.append('')
    try:
        price = driver.find_element(By.XPATH, property_path + i + property_price_path)
        all_price.append(price.text)
    except:
        all_price.append('')
    try:
        price_2_unit = driver.find_element(By.XPATH, property_path + i + property_price_2_unit_path)
        all_price_unit_2.append(price_2_unit.text)
    except:
        all_price_unit_2.append('')
    try:
        price_2 = driver.find_element(By.XPATH, property_path + i + property_price_2_path)
        all_price_2.append(price_2.text)
    except:
        all_price_2.append('')
    try:
        type_size = driver.find_element(By.XPATH, property_path + i + property_type_size_path)
        all_type_size.append(type_size.text)
    except:
        all_type_size.append('')
    try:
        bedrooms = driver.find_element(By.XPATH, property_path + i + property_bedrooms_path)
        all_bedrooms.append(bedrooms.text)
    except:
        all_bedrooms.append('')
    try:
        suite = driver.find_element(By.XPATH, property_path + i + property_suite_path)
        all_suite.append(suite.text)
    except:
        all_suite.append('')
    try:
        parking = driver.find_element(By.XPATH, property_path + i + property_parking_path)
        all_parking.append(parking.text)
    except:
        all_parking.append('')
    try:
        description = driver.find_element(By.XPATH, property_path + i + property_description_path)
        all_description.append(description.text)
    except:
        all_description.append('')
    
# code
if __name__ == '__main__':
    
    # starting the webdriver and going to the specified url
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get( url_1 )
    
    # creating lists to add each property value to them
    all_title = []
    all_subtitle = []
    all_price_unit = []
    all_price = []
    all_price_unit_2 = []
    all_price_2 = []
    all_type_size = []
    all_bedrooms = []
    all_suite = []
    all_parking = []
    all_description = []
    
    #getting the list of properties that will be collected
    property_list = driver.find_elements(By.CLASS_NAME, class_to_search )
    number_elements = len(property_list)
    print('number of element in page 1 is {}'.format(number_elements) )
    
    # using the function to collect
    for i in range( 1 , number_elements + 1):
        get_property( str(i) )
    
    # collecting next pages
    number_pages = int( driver.find_element(By.XPATH, last_page_path).text )
    print('number of pages is {}'.format(number_pages) )
    
    for j  in range( 2 , number_pages + 1):
        # wait time between pages
        time.sleep( wait_time )
        # going to each page
        driver.get( url + str(j) )
        # repeating first page process
        property_list = driver.find_elements(By.CLASS_NAME, class_to_search )
        number_elements = len(property_list)
        print('number of element in page {} is {}'.format(j, number_elements) )
        for i in range( 1 , number_elements + 1):
            get_property( str(i) )
    
    # closing driver
    driver.quit()
    
    # saving results to output file
    output = {
        'title':all_title,
        'subtitle':all_subtitle,
        'price_unit':all_price_unit,
        'price':all_price,
        'price_unit_2':all_price_unit_2,
        'price_2':all_price_2,
        'type_size':all_type_size,
        'bedrooms':all_bedrooms,
        'suite':all_suite,
        'parking':all_parking,
        'description':all_description
        }
    df = pd.DataFrame( output )
    df.to_csv( output_file )