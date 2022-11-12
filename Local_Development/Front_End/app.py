from flask import Flask, render_template, jsonify, request, render_template_string
import pandas as pd
import json
from tensorflow import keras
import os
import csv
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import numpy as np
import pickle
import librosa

app = Flask(__name__)

sound_folder = os.path.join('static','sounds')
app.config["UPLOAD_FOLDER"] = sound_folder


cwd = os.getcwd()
###print(cwd)
##
modeldir = cwd+'\\model'
##
##
savedmodel = modeldir+'\\marine_mammal_cnn'
##
##

model = keras.models.load_model('marine_model.h5')

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    soundfile = request.files['soundfile']
    sound_path = './static/sounds/' + soundfile.filename
    soundfile.save(sound_path)

    header = "filename length chroma_stft_mean chroma_stft_var rms_mean rms_var spectral_centroid_mean spectral_centroid_var spectral_bandwidth_mean \
        spectral_bandwidth_var rolloff_mean rolloff_var zero_crossing_rate_mean zero_crossing_rate_var harmony_mean harmony_var perceptr_mean \
        perceptr_var tempo mfcc1_mean mfcc1_var mfcc2_mean mfcc2_var mfcc3_mean mfcc3_var mfcc4_mean mfcc4_var".split()

    df = pd.DataFrame(columns=header)

    scaler = StandardScaler()
    sound = sound_path
    y, sr = librosa.load(sound, mono = True, duration = 60)
    chroma_stft = librosa.feature.chroma_stft(y = y, sr = sr)
    rmse = librosa.feature.rms(y = y)
    spec_cent = librosa.feature.spectral_centroid(y = y, sr = sr)
    spec_bw = librosa.feature.spectral_bandwidth(y = y, sr = sr)
    rolloff = librosa.feature.spectral_rolloff(y = y, sr = sr)
    zcr = librosa.feature.zero_crossing_rate(y)
    mfcc = librosa.feature.mfcc(y = y, sr = sr)

    to_append = f'{soundfile.filename} {np.mean(chroma_stft)} {np.mean(rmse)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(rolloff)} {np.mean(zcr)}'

    for e in mfcc:
        to_append += f' {np.mean(e)}'

    to_append = to_append.split()

    a_series = pd.Series(to_append,index=df.columns)

    df = pd.concat([df, a_series.to_frame().T], ignore_index=True)

    x = scaler.fit_transform(np.array(df.iloc[:, 1:27]))
    

    predictions = model.predict(x)
    encoder = LabelEncoder()
    encoder.classes_ = np.load('mammal_class.npy', allow_pickle=True)
    classes = np.argmax(predictions, axis = 1)
    result = encoder.inverse_transform(classes)

    return render_template('index.html',prediction_text='File Name: {} ===> Predicted Marine Mammal: {}'.format(soundfile.filename, result))


@app.route('/returnJSON', methods=['POST'])
def predictJSON():
    soundfile = request.files['soundfile']
    sound_path = './static/sounds/' + soundfile.filename
    soundfile.save(sound_path)

    header = "filename length chroma_stft_mean chroma_stft_var rms_mean rms_var spectral_centroid_mean spectral_centroid_var spectral_bandwidth_mean \
        spectral_bandwidth_var rolloff_mean rolloff_var zero_crossing_rate_mean zero_crossing_rate_var harmony_mean harmony_var perceptr_mean \
        perceptr_var tempo mfcc1_mean mfcc1_var mfcc2_mean mfcc2_var mfcc3_mean mfcc3_var mfcc4_mean mfcc4_var".split()

    df = pd.DataFrame(columns=header)

    scaler = StandardScaler()
    sound = sound_path
    y, sr = librosa.load(sound, mono = True, duration = 60)
    chroma_stft = librosa.feature.chroma_stft(y = y, sr = sr)
    rmse = librosa.feature.rms(y = y)
    spec_cent = librosa.feature.spectral_centroid(y = y, sr = sr)
    spec_bw = librosa.feature.spectral_bandwidth(y = y, sr = sr)
    rolloff = librosa.feature.spectral_rolloff(y = y, sr = sr)
    zcr = librosa.feature.zero_crossing_rate(y)
    mfcc = librosa.feature.mfcc(y = y, sr = sr)

    to_append = f'{soundfile.filename} {np.mean(chroma_stft)} {np.mean(rmse)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(rolloff)} {np.mean(zcr)}'

    for e in mfcc:
        to_append += f' {np.mean(e)}'

    to_append = to_append.split()

    a_series = pd.Series(to_append,index=df.columns)

    df = pd.concat([df, a_series.to_frame().T], ignore_index=True)
    
##    df_json = df.to_json(orient="records")
##    parsed = json.loads(df_json)

    x = scaler.fit_transform(np.array(df.iloc[:, 1:27]))

    predictions = model.predict(x)
    encoder = LabelEncoder()
    encoder.classes_ = np.load('mammal_class.npy', allow_pickle=True)
    classes = np.argmax(predictions, axis = 1)
    result = encoder.inverse_transform(classes)

    return jsonify({"file_name": str(soundfile.filename), "predicted_mammal": str(result)})

@app.route('/returnFeaturesJSON', methods=['POST'])
def returnFeaturesJSON():
    soundfile = request.files['soundfile']
    sound_path = './static/sounds/' + soundfile.filename
    soundfile.save(sound_path)

    header = "length chroma_stft_mean chroma_stft_var rms_mean rms_var spectral_centroid_mean spectral_centroid_var spectral_bandwidth_mean \
        spectral_bandwidth_var rolloff_mean rolloff_var zero_crossing_rate_mean zero_crossing_rate_var harmony_mean harmony_var perceptr_mean \
        perceptr_var tempo mfcc1_mean mfcc1_var mfcc2_mean mfcc2_var mfcc3_mean mfcc3_var mfcc4_mean mfcc4_var".split()

    df = pd.DataFrame(columns=header)

    scaler = StandardScaler()
    sound = sound_path
    y, sr = librosa.load(sound, mono = True, duration = 60)
    chroma_stft = librosa.feature.chroma_stft(y = y, sr = sr)
    rmse = librosa.feature.rms(y = y)
    spec_cent = librosa.feature.spectral_centroid(y = y, sr = sr)
    spec_bw = librosa.feature.spectral_bandwidth(y = y, sr = sr)
    rolloff = librosa.feature.spectral_rolloff(y = y, sr = sr)
    zcr = librosa.feature.zero_crossing_rate(y)
    mfcc = librosa.feature.mfcc(y = y, sr = sr)

    to_append = f'{np.mean(chroma_stft)} {np.mean(rmse)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(rolloff)} {np.mean(zcr)}'

    for e in mfcc:
        to_append += f' {np.mean(e)}'

    to_append = to_append.split()

    a_series = pd.Series(to_append,index=df.columns)

    df = pd.concat([df, a_series.to_frame().T], ignore_index=True)
    
    df_json = df.to_json(orient="records")
    parsed = json.loads(df_json)

##    x = scaler.fit_transform(np.array(df.iloc[:, 1:27]))
##
##    predictions = model.predict(x)
##    encoder = LabelEncoder()
##    encoder.classes_ = np.load('mammal_class.npy', allow_pickle=True)
##    classes = np.argmax(predictions, axis = 1)
##    result = encoder.inverse_transform(classes)

    return jsonify({"file_name": str(soundfile.filename),  "features": str(json.dumps(parsed))})


##
##@app.route("/", methods=["POST"])
##def index():
##    data = request.json
##    df = pd.DataFrame(data, index=[0])
##    prediction = model.predict(df)
##    predicted_mammal = prediction.flatten()[0]
##    return jsonify({"price": str(predicted_price)})

##@app.route("/")
##def index():
##    return render_template_string("Hello from flask")
##
if __name__ == "__main__":
##    app.run(debug=True)
    app.run()
