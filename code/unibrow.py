'''
Solution unibrow.py
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
