# CI/CD Pipeline, Deploy Django Applications on AWS EKS using GitHub Actions and Terraform

We plan to utilize GitHub Actions and Terraform to deploy our Django project on AWS EKS.
![readme (9)](https://github.com/codewithmuh/django-aws-eks-github-actions/assets/51082957/c3db3c54-f5e9-4884-a8ba-c2a80fd1c81e)


## Overview:
We will deploy Django Application on aws Elastic Kubernetes(EKS). We will use Github actions for the ci/cd pipeline. We will use EC2 as the self-hosted runner for our GitHub Actions. We will integrate Sonarcube for code analysis and Trivt Image scan to scan our docker images. Also, we will integrate Slack to get Build/deployment notifications.

## Support
<a href="https://www.buymeacoffee.com/codewithmuh" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-yellow.png" alt="Buy Me A Coffee" height="41" width="174"></a>

### Prerequisite
You should have basic Knowledge of AWS services, Docker, Kubernetes, and GitHub Actions.

### Table of Content/Steps:
**1.** Create an AWS EC2 Instance and an IAM Role 

**2.** Add a Self Hosted Runner To AWS EC2

**3.** Python Code Quality Check using Pylint
   
**4.** Docker Installation and Running SonarQube Container

**5.** Integrate SonarQube with GitHub Actions

**6.** Installation of tools (Java JDK, Terraform, Trivy, Kubectl, Node.js, NPM, AWS CLI)

**7.** Provision AWS EKS With Terraform

**8.** Dockerhub and Trivy Image Scan Setup

**9.** Deploy Application(image) to AWS EKS

**10.** Integrate Slack Notifications

**11.** Running Final/Complete Github actions Workflow

**12.** Delete the infrastructure (To Avoid Extra Billing, if you are just using it for learning Purposes)

### Article Link:

### Youtube Video Link: 
# coming Soon
