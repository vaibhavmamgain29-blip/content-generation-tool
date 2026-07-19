# Deploying to AWS

The app is a two-container stack (nginx frontend + FastAPI backend) defined
in `docker-compose.yml`. There are two supported paths to AWS.

## Option A — AWS App Runner (recommended, simplest)

App Runner gives you a public HTTPS URL with managed TLS and auto-deploy.

### Single-image path (merge the two services)

App Runner runs one image per service. The simplest approach is to keep the
two-service split and deploy the **frontend** image to App Runner, with the
**backend** reachable from it. For a single-service deployment, build a
combined image:

1. Build and push the frontend and backend images to ECR:
   ```bash
   aws ecr create-repository --repository-name content-studio-frontend
   aws ecr create-repository --repository-name content-studio-backend

   docker compose build

   docker tag content-studio-frontend <acct>.dkr.ecr.<region>.amazonaws.com/content-studio-frontend:latest
   docker tag content-studio-backend  <acct>.dkr.ecr.<region>.amazonaws.com/content-studio-backend:latest
   docker push <acct>.dkr.ecr.<region>.amazonaws.com/content-studio-frontend:latest
   docker push <acct>.dkr.ecr.<region>.amazonaws.com/content-studio-backend:latest
   ```

2. Create two App Runner services (or one frontend + one private backend):
   - **Backend service** — image: `content-studio-backend:latest`, port `8000`,
     environment variable `GEMINI_API_KEY` (mark as **Secret**).
   - **Frontend service** — image: `content-studio-frontend:latest`, port `80`.
     Update `nginx.conf` to proxy `/api/` to the backend service's App Runner
     URL instead of `http://backend:8000`, then rebuild and redeploy.

3. App Runner issues a public URL like
   `https://<random>.<region>.awsapprunner.com` with HTTPS.

### Source-repository path

Alternatively, connect App Runner to your GitHub repo and point it at each
service's `Dockerfile` (`backend/Dockerfile`, `frontend/Dockerfile`). Set
`GEMINI_API_KEY` as a secret environment variable in the console.

## Option B — AWS Elastic Beanstalk (Docker platform)

1. Create a `Dockerrun.aws.json v2` at the project root that references both
   images (or build them inside EB with `docker-compose.yml`).
2. `eb init` and `eb create` with the Docker platform.
3. Set `GEMINI_API_KEY` in `eb setenv` (marked secret where supported).

## Option C — ECS + Fargate

For production workloads, use ECS with the two-task definition pattern:

- `backend` task — port 8000, `GEMINI_API_KEY` from Secrets Manager / SSM.
- `frontend` task — port 80, nginx proxies `/api/` to the backend service
  via the internal load balancer or service discovery.

Put an Application Load Balancer in front with an HTTPS listener (ACM cert)
for a public `https://...` URL.

## Required environment variables

| Variable          | Where                              | Example              |
|-------------------|------------------------------------|----------------------|
| `GEMINI_API_KEY`  | backend (secret)                   | `AIza…`              |
| `GEMINI_MODEL`    | backend (optional)                 | `gemini-2.0-flash`   |
| `CORS_ORIGINS`    | backend (comma-separated)          | `https://your-domain`|

## Streaming note

App Runner and ALB both support chunked transfer / SSE, but make sure:

- The proxy in front of the backend has buffering disabled (nginx config
  already sets `proxy_buffering off`).
- The backend response includes `X-Accel-Buffering: no` (already set).
- Any ALB listener uses an HTTP (not HTTPS-to-target) protocol so chunked
  encoding passes through unchanged.
