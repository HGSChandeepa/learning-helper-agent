### Agent Deployment Steps to GCP Cloud Run

1. **Create a GCP Project**:

   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project or select an existing one.

2. **Enable Cloud Run API**:

   - Navigate to the "APIs & Services" dashboard.
   - Search for "Cloud Run API" and enable it.

3. Login to the Google Cloud Shell:

   - Click on the "Activate Cloud Shell" button in the top right corner of the console.
   - using the Cloud Shell terminal, ensure you are in the correct project by running:
     ```bash
        gcloud auth login
        gcloud config set project <your-project-id>
     ```

4. Export the environment variables:

   - Set the environment variables required for your application. You can do this in the Cloud Shell terminal:
     ```bash
     export GOOGLE_CLOUD_PROJECT=<your-project-id>
     export GOOGLE_CLOUD_LOCATION=us-central1
     export GOOGLE_GENAI_USE_VERTEXAI=TRUE
     export GOOGLE_API_KEY=<your-google-api-key>
     export OPENROUTER_API_KEY=<your-openrouter-api-key>
     ```

5. Deploy the application to Cloud Run:

   - Ensure you are in the directory containing your `Dockerfile` and `main.py`.
   - Use the following command to deploy your application:
     ```bash
        gcloud run deploy capital-agent-service --source . --region $env:GOOGLE_CLOUD_LOCATION --project $env:GOOGLE_CLOUD_PROJECT --allow-unauthenticated --set-env-vars="GOOGLE_CLOUD_PROJECT=$env:GOOGLE_CLOUD_PROJECT,GOOGLE_CLOUD_LOCATION=$env:GOOGLE_CLOUD_LOCATION,GOOGLE_GENAI_USE_VERTEXAI=$env:GOOGLE_GENAI_USE_VERTEXAI,GOOGLE_API_KEY=$env:GOOGLE_API_KEY,OPENROUTER_API_KEY=$env:OPENROUTER_API_KEY"
     ```
