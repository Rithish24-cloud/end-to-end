# End-to-End CI/CD Pipeline for Python Flask Application on AWS

This project demonstrates a complete DevOps workflow using:

- GitHub
- Jenkins
- Docker
- AWS EC2
- Prometheus
- Grafana

## Application Endpoints
- `/` -> Home page
- `/about` -> About project
- `/health` -> Health check

## CI/CD Flow
1. Developer pushes code to GitHub
2. Jenkins pulls latest code
3. Jenkins builds Docker image
4. Docker container is deployed on EC2
5. Prometheus collects metrics
6. Grafana shows dashboards