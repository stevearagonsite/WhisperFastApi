build:
	gcloud config set project $GCP_PROJECT_ID
	gcloud builds submit --tag us.gcr.io/$GCP_PROJECT_ID/$SERVICE_NAME

deploy:
	gcloud run deploy --image  us.gcr.io/$GCP_PROJECT_ID/$SERVICE_NAME --platform managed --project $GCP_PROJECT_ID --region $GCP_PROJECT_ID

install_dependencies:
	pip install -r requirements.txt

local_test:
	uvicorn "server.api:app" --host "0.0.0.0" --port 8000 --reload
