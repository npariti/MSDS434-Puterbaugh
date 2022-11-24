from flask import Flask, render_template, jsonify, request, render_template_string
import pandas as pd
import json
import os
import csv
import numpy as np
import pickle
import librosa
from google.cloud import aiplatform
from google.cloud import aiplatform_v1
from google.api import httpbody_pb2
from base64 import b64encode


app = Flask(__name__)

sound_folder = os.path.join('static','sounds')
app.config["UPLOAD_FOLDER"] = sound_folder


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    soundfile = request.files['soundfile']
    sound_path = './static/sounds/' + soundfile.filename
    #soundfile.save(sound_path)

    file_name, file_extension = os.path.splitext(sound_path)

    if file_extension == '.wav':
        header = "length chroma_stft_mean chroma_stft_var rms_mean rms_var spectral_centroid_mean spectral_centroid_var spectral_bandwidth_mean \
            spectral_bandwidth_var rolloff_mean rolloff_var zero_crossing_rate_mean zero_crossing_rate_var harmony_mean harmony_var perceptr_mean \
            perceptr_var tempo mfcc1_mean mfcc1_var mfcc2_mean mfcc2_var mfcc3_mean mfcc3_var mfcc4_mean mfcc4_var".split()

        df = pd.DataFrame(columns=header)

        sound = soundfile
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
        cols = df.columns
        df[cols[:]] = df[cols[:]].apply(pd.to_numeric, errors='coerce')
        df_json = df.to_json(orient='records')
        parsed=json.loads(df_json)
        json_object = {"signature_name":"predict","instances": parsed}

        REGION = "us-central1"
        PROJECT_ID = "msds434-puterbaugh"

        endpoint = aiplatform.Endpoint(endpoint_name=f"projects/msds434-puterbaugh/locations/us-central1/endpoints/3281650782771871744")
        #print("endpoint resource name = ",endpoint.resource_name)

        http_body = httpbody_pb2.HttpBody(
            data=json.dumps(json_object).encode("utf-8"),
            content_type="application/json",
        )

        req = aiplatform_v1.RawPredictRequest(
            http_body=http_body, endpoint=endpoint.resource_name
        )

        API_ENDPOINT = "{}-aiplatform.googleapis.com".format(REGION)
        client_options = {"api_endpoint": API_ENDPOINT}

        pred_client = aiplatform.gapic.PredictionServiceClient(client_options=client_options)

        response = pred_client.raw_predict(req)

        response_parsed = response.data.decode('utf-8')

        json_output = json.loads(response_parsed)
        
        result = json_output['predictions'][0]['classes'][0]  

        return render_template('index.html',prediction_text='File Name: {} ===> Predicted Marine Mammal: {}'.format(soundfile.filename, result))

    elif file_extension == '.csv':
        df = pd.read_csv(soundfile)
        df.drop(df.columns[0],axis=1,inplace=True)
        cols = df.columns
        df[cols[:]] = df[cols[:]].apply(pd.to_numeric, errors='coerce')
        df_json = df.to_json(orient='records')
        parsed=json.loads(df_json)

        json_object = {"signature_name":"predict","instances": parsed}

        REGION = "us-central1"
        PROJECT_ID = "msds434-puterbaugh"

        endpoint = aiplatform.Endpoint(endpoint_name=f"projects/msds434-puterbaugh/locations/us-central1/endpoints/3281650782771871744")
        #print("endpoint resource name = ",endpoint.resource_name)

        http_body = httpbody_pb2.HttpBody(
            data=json.dumps(json_object).encode("utf-8"),
            content_type="application/json",
        )

        req = aiplatform_v1.RawPredictRequest(
            http_body=http_body, endpoint=endpoint.resource_name
        )

        API_ENDPOINT = "{}-aiplatform.googleapis.com".format(REGION)
        client_options = {"api_endpoint": API_ENDPOINT}

        pred_client = aiplatform.gapic.PredictionServiceClient(client_options=client_options)

        response = pred_client.raw_predict(req)
 
        response_parsed = response.data.decode('utf-8')
 
        json_output = json.loads(response_parsed)

        result = json_output['predictions'][0]['classes'][0]

        return render_template('index.html',prediction_text='File Name: {} ===> Predicted Marine Mammal: {}'.format(soundfile.filename, result))

    elif file_extension == '.json':
        data = json.load(soundfile)
        df = pd.DataFrame([data])
        df.drop(df.columns[0],axis=1,inplace=True)
        cols = df.columns
        df[cols[:]] = df[cols[:]].apply(pd.to_numeric, errors='coerce')
        df_json = df.to_json(orient='records')
        parsed=json.loads(df_json)

        json_object = {"signature_name":"predict","instances": parsed}
  

        REGION = "us-central1"
        PROJECT_ID = "msds434-puterbaugh"

        endpoint = aiplatform.Endpoint(endpoint_name=f"projects/msds434-puterbaugh/locations/us-central1/endpoints/3281650782771871744")
        #print("endpoint resource name = ",endpoint.resource_name)

        http_body = httpbody_pb2.HttpBody(
            data=json.dumps(json_object).encode("utf-8"),
            content_type="application/json",
        )

        req = aiplatform_v1.RawPredictRequest(
            http_body=http_body, endpoint=endpoint.resource_name
        )

        API_ENDPOINT = "{}-aiplatform.googleapis.com".format(REGION)
        client_options = {"api_endpoint": API_ENDPOINT}

        pred_client = aiplatform.gapic.PredictionServiceClient(client_options=client_options)

        response = pred_client.raw_predict(req)
 
        response_parsed = response.data.decode('utf-8')
 
        json_output = json.loads(response_parsed)

        result = json_output['predictions'][0]['classes'][0]
        

        return render_template('index.html',prediction_text='File Name: {} ===> Predicted Marine Mammal: {}'.format(soundfile.filename, result))

    else:
        return render_template('index.html',prediction_text='File format not recognized! Please use a .wav file or a .csv file containing the required features.')
##
##
@app.route('/returnJSON', methods=['POST'])
def predictJSON():
    content_type_start = request.headers.get('Content-Type')
    print(content_type_start)
    content_type = content_type_start.split(';')[0]
    print(content_type)
    if content_type == 'multipart/form-data':
        soundfile = request.files['soundfile']
        sound_path = './static/sounds/' + soundfile.filename
        #soundfile.save(sound_path)

        file_name, file_extension = os.path.splitext(sound_path)

        if file_extension == '.wav':
            header = "length chroma_stft_mean chroma_stft_var rms_mean rms_var spectral_centroid_mean spectral_centroid_var spectral_bandwidth_mean \
                spectral_bandwidth_var rolloff_mean rolloff_var zero_crossing_rate_mean zero_crossing_rate_var harmony_mean harmony_var perceptr_mean \
                perceptr_var tempo mfcc1_mean mfcc1_var mfcc2_mean mfcc2_var mfcc3_mean mfcc3_var mfcc4_mean mfcc4_var".split()

            df = pd.DataFrame(columns=header)

            sound = soundfile
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
            cols = df.columns
            df[cols[:]] = df[cols[:]].apply(pd.to_numeric, errors='coerce')
            df_json = df.to_json(orient='records')
            parsed=json.loads(df_json)
            
            json_object = {"signature_name":"predict","instances": parsed}
            

            REGION = "us-central1"
            PROJECT_ID = "msds434-puterbaugh"

            endpoint = aiplatform.Endpoint(endpoint_name=f"projects/msds434-puterbaugh/locations/us-central1/endpoints/3281650782771871744")
            #print("endpoint resource name = ",endpoint.resource_name)

            http_body = httpbody_pb2.HttpBody(
                data=json.dumps(json_object).encode("utf-8"),
                content_type="application/json",
            )

            req = aiplatform_v1.RawPredictRequest(
                http_body=http_body, endpoint=endpoint.resource_name
            )

            API_ENDPOINT = "{}-aiplatform.googleapis.com".format(REGION)
            client_options = {"api_endpoint": API_ENDPOINT}

            pred_client = aiplatform.gapic.PredictionServiceClient(client_options=client_options)

            response = pred_client.raw_predict(req)
            
            response_parsed = response.data.decode('utf-8')
            
            json_output = json.loads(response_parsed)
            
            result = json_output['predictions'][0]['classes'][0]
            
            return jsonify({"file_name": str(soundfile.filename), "predicted_mammal": str(result)})

        elif file_extension == '.csv':
            df = pd.read_csv(soundfile)
            df.drop(df.columns[0],axis=1,inplace=True)
            print(df)
            cols = df.columns
            df[cols[:]] = df[cols[:]].apply(pd.to_numeric, errors='coerce')
            df_json = df.to_json(orient='records')
            parsed=json.loads(df_json)
            
            json_object = {"signature_name":"predict","instances": parsed}
            

            REGION = "us-central1"
            PROJECT_ID = "msds434-puterbaugh"

            endpoint = aiplatform.Endpoint(endpoint_name=f"projects/msds434-puterbaugh/locations/us-central1/endpoints/3281650782771871744")
            #print("endpoint resource name = ",endpoint.resource_name)

            http_body = httpbody_pb2.HttpBody(
                data=json.dumps(json_object).encode("utf-8"),
                content_type="application/json",
            )

            req = aiplatform_v1.RawPredictRequest(
                http_body=http_body, endpoint=endpoint.resource_name
            )

            API_ENDPOINT = "{}-aiplatform.googleapis.com".format(REGION)
            client_options = {"api_endpoint": API_ENDPOINT}

            pred_client = aiplatform.gapic.PredictionServiceClient(client_options=client_options)

            response = pred_client.raw_predict(req)
            
            response_parsed = response.data.decode('utf-8')
            
            json_output = json.loads(response_parsed)
            
            result = json_output['predictions'][0]['classes'][0]

            return jsonify({"file_name": str(soundfile.filename), "predicted_mammal": str(result)})

        elif file_extension == '.json':
            data = json.load(soundfile)
            df = pd.DataFrame([data])
            df.drop(df.columns[0],axis=1,inplace=True)
            cols = df.columns
            df[cols[:]] = df[cols[:]].apply(pd.to_numeric, errors='coerce')
            df_json = df.to_json(orient='records')
            parsed=json.loads(df_json)
        
            json_object = {"signature_name":"predict","instances": parsed}
            

            REGION = "us-central1"
            PROJECT_ID = "msds434-puterbaugh"

            endpoint = aiplatform.Endpoint(endpoint_name=f"projects/msds434-puterbaugh/locations/us-central1/endpoints/3281650782771871744")
            #print("endpoint resource name = ",endpoint.resource_name)

            http_body = httpbody_pb2.HttpBody(
                data=json.dumps(json_object).encode("utf-8"),
                content_type="application/json",
            )

            req = aiplatform_v1.RawPredictRequest(
                http_body=http_body, endpoint=endpoint.resource_name
            )

            API_ENDPOINT = "{}-aiplatform.googleapis.com".format(REGION)
            client_options = {"api_endpoint": API_ENDPOINT}

            pred_client = aiplatform.gapic.PredictionServiceClient(client_options=client_options)

            response = pred_client.raw_predict(req)
           
            response_parsed = response.data.decode('utf-8')
            
            json_output = json.loads(response_parsed)
            
            result = json_output['predictions'][0]['classes'][0]
            
            return jsonify({"file_name": str(soundfile.filename), "predicted_mammal": str(result)})

        else:
            return 'Content type is not supported at this time!'

    elif content_type == 'application/json' or content_type == 'text/plain':
            print(request.data)
            request_string = request.data.decode('UTF-8')
            request_string = request_string[1:-1]
            print(request_string)
            data = {i.split(': ')[0]: i.split(': ')[1] for i in request_string.split(', ')}
            print(data)
            df = pd.DataFrame.from_dict([data])
            filename = df['filename'].iloc[0]
            df.drop(df.columns[0],axis=1,inplace=True)
            print(df)
            cols = df.columns
            df[cols[:]] = df[cols[:]].apply(pd.to_numeric, errors='coerce')
            print(df)
            df_json = df.to_json(orient='records')
            parsed=json.loads(df_json)
            json_object = {"signature_name":"predict","instances": parsed}

            REGION = "us-central1"
            PROJECT_ID = "msds434-puterbaugh"

            endpoint = aiplatform.Endpoint(endpoint_name=f"projects/msds434-puterbaugh/locations/us-central1/endpoints/3281650782771871744")
            #print("endpoint resource name = ",endpoint.resource_name)

            http_body = httpbody_pb2.HttpBody(
                data=json.dumps(json_object).encode("utf-8"),
                content_type="application/json",
            )

            req = aiplatform_v1.RawPredictRequest(
                http_body=http_body, endpoint=endpoint.resource_name
            )

            API_ENDPOINT = "{}-aiplatform.googleapis.com".format(REGION)
            client_options = {"api_endpoint": API_ENDPOINT}

            pred_client = aiplatform.gapic.PredictionServiceClient(client_options=client_options)

            response = pred_client.raw_predict(req)

            response_parsed = response.data.decode('utf-8')
 
            json_output = json.loads(response_parsed)

            result = json_output['predictions'][0]['classes'][0]
            
            return jsonify({"file_name": str(filename), "predicted_mammal": str(result)})

    else:
        return 'Content type is not supported at this time!'
        

if __name__ == "__main__":
##    app.run(debug=True)
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
