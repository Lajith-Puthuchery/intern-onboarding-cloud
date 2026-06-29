# Intern Onboarding Starter App

Basic Python Flask app for cloud fundamentals hands-on.

## Files

```text
File	Purpose
app.py	Python Flask app
requirements.txt	Python dependency list
Dockerfile	Container image build recipe
k8s/namespace.yaml	Creates namespace test
k8s/deployment.yaml	Deploys 2 app replicas
k8s/service.yaml	Exposes the app inside the cluster
```

## Local Docker

```bash
docker build -t intern-starter-app:local .
docker run -p 8080:8080 intern-starter-app:local
```

Open:

```text
http://localhost:8080
```

## GKE Deployment

Cluster:

```bash
gcloud container clusters get-credentials intern-onboarding \
  --zone us-central1-a \
  --project qpe-play
```

Image used by the Kubernetes manifest:

```text
us-central1-docker.pkg.dev/qpe-play/cloud-run-source-deploy/intern-starter-app:latest
```

Build and push:

```bash
gcloud auth configure-docker us-central1-docker.pkg.dev
docker buildx build --platform linux/amd64 \
  -t us-central1-docker.pkg.dev/qpe-play/cloud-run-source-deploy/intern-starter-app:latest \
  --push .
```

Deploy:

```bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl get pods -n test
kubectl get service intern-starter-app -n test
```

Use port-forward to access the app locally:

```bash
kubectl port-forward -n test service/intern-starter-app 8080:80
```

Then open:

```text
http://localhost:8080
```

Clean up:

```bash
kubectl delete -f k8s/service.yaml
kubectl delete -f k8s/deployment.yaml
```

## Minikube Fallback

Use this when interns do not have GCP access.

```bash
minikube start
eval $(minikube docker-env)
docker build -t intern-starter-app:local .
```

For minikube, change the image in `k8s/deployment.yaml` to:

```text
intern-starter-app:local
```

And set:

```text
imagePullPolicy: Never
```

Then deploy:

```bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl get pods -n test
kubectl port-forward -n test service/intern-starter-app 8080:80
```

Open:

```text
http://localhost:8080
```
