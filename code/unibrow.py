'''
Solution unibrow.py
'''

import pandas as pd
import streamlit as st
import pandaslib as pl

st.title("UniBrow")
st.caption("The Universal data browser")

file = st.file_uploader("Upload a file:", type=["csv", "xlsx", "json"])
if file:
    file_type = pl.get_file_extension(file.name)
    df = pl.load_file(file, file_type)
    cols = pl.get_column_names(df)
    selected_cols = st.multiselect("Select columns to display", cols, default=cols)
    if st.toggle("Filter data"):
        stcols = st.columns(3)
        text_cols = pl.get_columns_of_type(df, 'object')
        filter_col = stcols[0].selectbox("Select column to filter", text_cols)
        if filter_col:
            vals = pl.get_unique_values(df, filter_col)
            val = stcols[1].selectbox("Select value to filter On", vals)
            df_show = df[df[filter_col] == val][selected_cols]
    else:
        df_show = df[selected_cols]
    
    st.dataframe(df_show)
    st.dataframe(df_show.describe())

'''
import pandas as pd
import streamlit as st
import pandaslib as pl

st.title("UniBrow")
st.caption("The Universal data browser")

file_path = st.text_input("Enter file path")
if file_path:
    ext = pl.get_file_extension(file_path)
    st.write(f"File extension: {ext}")
    df = pl.load_file(file_path, ext)
    cols = pl.get_column_names(df)
    chosen_col = st.multiselect("Choose columns to display", cols, default=cols)
    df= df[chosen_col]
    obj_cols = pl.get_columns_of_type(df, 'object')
    filter_col = st.selectbox("Choose a column to filter", obj_cols)
    unique = pl.get_unique_values(df, filter_col)
    unique.insert(0, 'N/A')
    filter_val = st.selectbox("Choose a value to filter", unique)
    if filter_val and filter_val != 'N/A':
        df = df[df[filter_col] == filter_val]
    st.write(df)
    st.write(df.describe())
'''