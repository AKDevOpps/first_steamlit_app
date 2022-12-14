import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.title('My Parents New Healthy Dinner ')


streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
fruit_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruit_selected]
streamlit.dataframe(fruits_to_show)

def get_fruityvice_data(this_fruity_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ this_fruity_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?' )
  
  if not fruit_choice:
        streamlit.error("please select a fruit to get information")
  else:  
        #fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
        #fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
        #streamlit.dataframe(fruityvice_normalized)
        back_from_function = get_fruityvice_data(fruit_choice)
        streamlit.dataframe(back_from_function)

      
except URLError as e:
       streamlit.error()
    
steamlit.header("the fruit load list contains:")
          def get_fruit_load_list():
           with my_cnx.cursor() as my_cur:
           my_cur.execute("select * from fruit_load_list")
           return my_cur.fetchall()
          
 if steamlit.button('Get Fruit Load List'):
       my_cnx = snowflake.connector.connect(**steamlit.secrets["snowflake"])
       my_data_rows = get_fruit_load_list()
       streamlit.dataframe(my_data_rows)  

