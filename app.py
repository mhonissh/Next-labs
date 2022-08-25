# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 13:53:29 2022

@author: ADMIN
"""

import streamlit as st
#import numpy as np
#import pandas as pd
import tensorflow as tf
#from tensorflow import keras

#path = 'C://Users//ADMIN//Downloads//NL//'
#model = tf.saved_model.load(path)
filename = 'pred_model.pb'
graph_def = tf.compat.v1.GraphDef()
with tf.io.gfile.GFile(filename,'rb') as f:
    #graph_def.ParseFromString(f.read())
    tf.import_graph_def(graph_def, name='')


def predict_booking_checkedin(Age,DSC,ALT,LR,BC,
                                 BNS,SR_HF,SR_LF,
                                 SRCrib,SRKSB,SRTB,
                                 SRNAMB,SRQR,
                                 DC_Direct,
                                 DC_Electronic,
                                 DC_Travel):
    
    """Let's Predict Hotel Booking Checking 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: Age
        in: query
        type: number
        required: true
      - name: DSC
        in: query
        type: number
        required: true
      - name: ALT
        in: query
        type: number
        required: true
      - name: LR
        in: query
        type: number
        required: true
      - name: BookingsCanceled,
        in: query
        type: number
        required: true
      - name: BookingsNoShowed
        in: query
        type: number
        required: true
      - name:SRHighFloor
        in: query
        type: number
        required: true
      - name:SRLowFloor
        in: query
        type: number
        required: true
      - name: SRCrib
        in: query
        type: number
        required: true
      - name:SRKingSizeBed
        in: query
        type: number
        required: true
      - name:SRTwinBed
        in: query
        type: number
        required: true
      - name:SRNoAlcoholInMiniBar
        in: query
        type: number
        required: true
      - name:SRQuietRoomDistributionChannel_Direct
        in: query
        type: number
        required: true
      - name:DistributionChannel_Electronic_Distribution
        in: query
        type: number
        required: true
      - name:DistributionChannel_Travel_Agent_Operator
        in: query
        type: number
        required: true
       
    responses:
        200:
            description: The output values
        
    """
    prediction = f.predict([[Age,DSC,ALT,LR,BC,
                                 BNS,SR_HF,SR_LF,
                                 SRCrib,SRKSB,SRTB,
                                 SRNAMB,SRQR,
                                 DC_Direct,
                                 DC_Electronic,
                                 DC_Travel]])
    print(prediction)
    return prediction



def main():
    st.title('Hotel Booking Check-in')
    html_temp = """ 
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Hotel Booking Check-In Predictor App </h2>
    </div> 
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    Age = st.text_input('Age','Type Here')
    DSC = st.text_input('Days Since Creation','Type Here')
    ALT = st.text_input('Avg Leading Time','Type Here')
    LR = st.text_input('Lodging Revenue','Type Here')
    BC = st.text_input('BookingsCanceled','Type 0 or 1 Here')
    BNS = st.text_input('BookingNoShowed','Type 0 or 1 Here')
    SR_HF = st.text_input('Highfloor','Type 0 or 1 Here')
    SR_LF = st.text_input('Lowfloor','Type 0 or 1 Here')
    SRCrib = st.text_input('Crib','Type 0 or 1 Here')
    SRKSB = st.text_input('Kinsizebed','Type 0 or 1 Here')
    SRTB= st.text_input('Twinbed','Type 0 or 1 Here')
    SRNAMB = st.text_input('NoAlcohol','Type 0 or 1 Here')
    SRQR = st.text_input('QuietRoom','Type 0 or 1 Here')
    DC_Direct = st.text_input('DC_Direct','Type 0 or 1 Here')
    DC_Electronic = st.text_input('DC_Electronic','Type 0 or 1 Here')
    DC_Travel = st.text_input('DC_Travel','Type 0 or 1 Here')
    result=""
    if st.button('Predict'):
        result=predict_booking_checkedin(Age,DSC,ALT,LR,BC,
                                 BNS,SR_HF,SR_LF,
                                 SRCrib,SRKSB,SRTB,
                                 SRNAMB,SRQR,
                                 DC_Direct,
                                 DC_Electronic,
                                 DC_Travel)
    st.success('The output is {}'.format(result))
    
if __name__ == '__main__':
    main()