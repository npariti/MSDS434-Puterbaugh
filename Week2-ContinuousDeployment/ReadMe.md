
# MSDS 434 Project Week 2 GCP Set Up CI/CD - Spencer Puterbaugh

- This document has been assembled in order to show the actions taken to work on the final project for this course.
- This documents details the actions taken to create a CI/CD pipeline from a git repo to automatically publish/update the prediction application.
- These actions took place towards the end of the course, as development had not been completed yet and was done locally for testing purposes.
- To push to GCP, a dockerfile and cloudbuild.yaml file are needed to ensure the pipeline functions as desired.
    - The dockerfile and yaml file can be found in the git repo for this project, along with the python code for the app itself.
- A trigger also needs to be created in GCP that will allow for any changes to be detected and trigger a GCP Cloud Build job that will create the image and store it in your GCP Image repo.
    - These jobs can also be run manually but a triger will allow for CI/CD as required by the project specifications.




## Triggering the function

1. Enable Cloud Build API and Cloud Run Admin API
2. Create a trigger to push build from git to GCP
    - You will need to connect to your Git repo(s) of interest and authorize GCP to read from it.
3. As you make updates to the branch you selected as being the source of the code for the Cloud Build Image, the trigger will automatically detect these chagnes and kick off a new build anytime the new code is pushed/merged into the git repo.
4. It may take several iterations to get the app image to successfully create, as GCP has its own nuances and requirements that can be difficult to accomplish on the first try.
    - I had several builds fail due to insufficient permissions on the service account for cloud build/cloud run.
    - I had several builds fail due to the container crashing because it failed to be able to receive traffic through the proper port.
5. Once the build is completed successfully, you should have an image for the application that can be deployed as you see fit in your environment's configuration.

