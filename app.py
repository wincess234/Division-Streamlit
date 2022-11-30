import numpy as np
import pandas as pd
import streamlit as st


def main():
  st.title("Division of Two Numbers")
  html_temp = """
  <div style="background-color:black;padding:10px">
  <h2 style="color:black;text-align:center;">Division of 2 Numbers</h2>
  </div>
  """
  st.markdown(html_temp,unsafe_allow_html=True)
  num1 = st.number_input("Number 1")
  num2 = st.number_input("Number 2")
  
  if(num1==0 or num2==0):
    result = 0
  else:
    result=num1/num2
  
  st.success('The output is {}'.format(result))
  
if __name__=='__main__':
  main()
