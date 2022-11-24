
# MSDS 434 Final Project Instructions- Spencer Puterbaugh

This is a repository that contains information on how to interact with the application, as well as an example jupyter notebook with python code that will extract the required features from a sound file, or multiple sound files if desired, that are necessary for the model endpoint to return a prediction/classification.

-Example_Notebook Contains a jupyter notebook with example code that can be repurposed for a user to extract features from a sound file(s).
    - Toward the end of the notebook there is code that will take a directory full of subdirectories of sound files and extract all of the features for each of the files
        - This can be very time consuming, so please be careful if you use this to process a large number of files
    - Can be adapted as needed to user requirements.

## Required Features
- The following features are required in order for the model endpoint to be able to return a prediction. The example notebook code will extract all of this information from a sound file.
    - length 
    - chroma_stft_mean 
    - chroma_stft_var 
    - rms_mean 
    - rms_var 
    - spectral_centroid_mean 
    - spectral_centroid_var 
    - spectral_bandwidth_mean 
    - spectral_bandwidth_var 
    - rolloff_mean 
    - rolloff_var 
    - zero_crossing_rate_mean 
    - zero_crossing_rate_var 
    - harmony_mean 
    - harmony_var 
    - perceptr_mean 
    - perceptr_var 
    - tempo 
    - mfcc1_mean 
    - mfcc1_var 
    - mfcc2_mean 
    - mfcc2_var 
    - mfcc3_mean 
    - mfcc3_var 
    - mfcc4_mean 
    - mfcc4_var

## Sample Curl Commands
- The curl commands below can be used as templates to send files or raw json to the /returnJSON endpoint of the application and receive a json formatted response containing the predicted mammal.
- The sound files referenced in the 3 file based commands can be found in the Test_Sounds folder in the root of this git repository.
- The curl commands must be executed from the same directory in which the files are stored on a user's local machine if they are copied directly and sent via the CLI/CMD.
    - Alternatively, you can specificy a file path, or you can use Postman to send the file as well.

    - curl for a sound file
        ```
        curl -F "soundfile=@413377__mbari-mars__gray-whale.wav" https://front-end-microservice-snovrulsya-uc.a.run.app/returnJSON
        ```
    - curl for a csv file with features
        ```
        curl -F "soundfile=@data_test_for_demo_sperm_whale.csv" https://front-end-microservice-snovrulsya-uc.a.run.app/returnJSON  
        ```
    - curl for a json file with features
        ```
        curl -F "soundfile=@json_test_sperm_whale.json" https://front-end-microservice-snovrulsya-uc.a.run.app/returnJSON
        ```
    - curl for raw json
        ```
        curl -X POST -H "Content-type: application/json" -d "{"filename": "404318__mbari-mars__cachalot-sperm-whale.wav", "length": "0.683583856", "chroma_stft_mean": "0.0160944", "chroma_stft_var": "2537.607354", "rms_mean": "2733.158383", "rms_var": "5890.58938", "spectral_centroid_mean": "0.101915484", "spectral_centroid_var": "-263.983551", "spectral_bandwidth_mean": "86.2118454", "spectral_bandwidth_var": "5.556107998", "rolloff_mean": "32.0552063", "rolloff_var": "-4.947262764", "zero_crossing_rate_mean": "13.83352757", "zero_crossing_rate_var": "-8.251721382", "harmony_mean": "7.807394981", "harmony_var": "-7.836720467", "perceptr_mean": "9.65907383", "perceptr_var": "-3.210715294", "tempo": "11.61573505", "mfcc1_mean": "-2.051388502", "mfcc1_var": "12.96432972", "mfcc2_mean": "-2.818068743", "mfcc2_var": "10.1602459", "mfcc3_mean": "-3.692974567", "mfcc3_var": "10.37336254", "mfcc4_mean": "-3.150325537", "mfcc4_var": "8.981236458"}" https://front-end-microservice-snovrulsya-uc.a.run.app/returnJSON
        ```