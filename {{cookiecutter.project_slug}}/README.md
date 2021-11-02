# Fastapi started project

### Environment

```
Docker
Python 3.8
Poetry
Fastapi
```

### 本機測試及開發

```
$ docker build -t fastapi-started-project:latest .

$ docker run --rm -p 8000:8000 fastapi-started-project:latest
```

### Deploy to Cloud Run

1. 安裝及設定 [Google Cloud SDK (gcloud)](https://cloud.google.com/sdk/docs/install)

2. gcloud 指定 GCP project

   ```shell
   $ gcloud config set project {PROJECT_ID}
   ```

3. Use Cloud Build to build docker image and push to Container Registry
   ```shell
   $ gcloud builds submit --tag asia.gcr.io/{PROJECT_ID}/fastapi-started-project
   ```

- Deploy to Cloud Run
  ```shell
  $ gcloud run deploy --image asia.gcr.io/{PROJECT_ID}/fastapi-started-project \
    --platform managed \
    --port 8000 \
    --memory 1Gi \
    --timeout=2m \
  ```
