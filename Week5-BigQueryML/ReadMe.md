
# MSDS 434 Project Week 5 GCP Set Up BigQuery ML Trained Model - Spencer Puterbaugh

- This document has been assembled in order to show the actions taken to work on the final project for this course
- This documents details the actions taken to create a machine learning model (deep neural network) that will serve as the basis of the predictions served by the application.
- A sql query was developed that was executed within BigQuery in order to train the model based on the dataset created in alignment with week 4's content
    - This function needed to have more than the default memory of 256 MiB allocated in order to successfully complete its work.




## Training the model

1. Run the query below within a BigQuery SQL editor in order to execute the function and train a BigQuery ML based model based on the dataset/table stored in BigQuery.
CREATE OR REPLACE MODEL marine_mammal_sound_data.marine_mammal_classifier
```
OPTIONS(MODEL_TYPE = 'DNN_CLASSIFIER',
         ACTIVATION_FN = 'RELU',
         BATCH_SIZE = 128,
         DROPOUT = 0.2,
         EARLY_STOP = FALSE ,
         HIDDEN_UNITS = [512, 256, 128, 64],
         INPUT_LABEL_COLS = ['label'],
         MAX_ITERATIONS = 100,
         OPTIMIZER = 'ADAM',
         DATA_SPLIT_METHOD = 'AUTO_SPLIT')
AS SELECT length,
chroma_stft_mean,
chroma_stft_var,
rms_mean,
rms_var,
spectral_centroid_mean,
spectral_centroid_var,
spectral_bandwidth_mean,
spectral_bandwidth_var,
rolloff_mean,
rolloff_var,
zero_crossing_rate_mean,
zero_crossing_rate_var,
harmony_mean,
harmony_var,
perceptr_mean,
perceptr_var,
tempo,
mfcc1_mean,
mfcc1_var,
mfcc2_mean,
mfcc2_var,
mfcc3_mean,
mfcc3_var,
mfcc4_mean,
mfcc4_var,
label
FROM marine_mammal_sound_data.sound_data
--exclude labels with very few samples
--BQ only supports 50 labels anyways right now for neural networks
WHERE label not in ('HarbourSeal','Commerson\'sDolphin','HoodedSeal','NewZealandFurSeal','SeaOtter');
```

2. The model took approximately 50 minutes to train. Overall metrics were decent, however they were not as good as the model that was trained locally using Tensorflow. Put in screenshots.

3. The model was exported to the cloud bucket created in week 3, and named MARINE_MAMMAL_CLASSIFIER