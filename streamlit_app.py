# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(":cup_with_straw: Customize Your Smoothie :cup_with_straw:")
# st.write(
#     """Replace this example with your own code!
#     **And if you're new to Streamlit,** check
#     out our easy-to-follow guides at
#     [docs.streamlit.io](https://docs.streamlit.io).
#     """
# )
st.write(
    """Choose the fruits you want in your custom Smoothie!
    """
)

name_on_order = st.text_input('Name on Smoothie:')
st.write('The name on your Smoothie will be:', name_on_order)

# option = st.selectbox(
#     "What is your favourite fruit?",
#     ("Banana", "Strawberries", "Peaches"),
# )

# st.write("Your favourite fruit is:", option)
# st.write("Your favourite fruit is:", col)
session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col("FRUIT_NAME"))
# st.dataframe(data=my_dataframe, use_container_width=True)
ingredients_list = st.multiselect("Choose upto 5 ingredients:", my_dataframe)
if ingredients_list:
    # st.write(ingredients_list)
    # st.text(ingredients_list)

    ingredients_string = ''
    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '

    # st.write(ingredients_string)
    my_insert_stmt = """ insert into smoothies.public.orders(ingredients)
            values ('""" + ingredients_string + """','"""+name_on_order+ """')"""

    # st.write(my_insert_stmt)
    # st.stop()
    time_to_insert = st.button('Submit Order')

    if time_to_insert:
        session.sql(my_insert_stmt).collect()

    # if ingredients_string:
    #     session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered!', icon="✅")