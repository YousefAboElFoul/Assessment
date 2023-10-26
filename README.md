# Assessment
--------------------------------------------------------------
The project is for both Task A and Task B
--------------------------------------------------------------
# Task A

In the directory Assessment:
it could be simply run via using the command line
the command to run is : docker compose up 
So I have the docker compose file , in the docker compose file I define the mysql db with ports , username and password.
In the docker compose , the backend and frontend files have Dockerfiles that are ran on execution

Steps to run:
1- docker compose build
2- docker compose up

--------------------------------------------------------------
# Task B 

In the directory Assessment/Helm:
1. helm lint
2. helm install myapp ../Helm -f values.yaml 


- I pushed my docker images to an online repository which is mine on dockerhub 
- I am using images that i deployed previously here one for the frontend and one for the backend
- In addition , i am using minikube setup ,with docker desktop , helm and wsl.
- To verify that the chart is working you can use : helm lint
the ouput should be 
/Assessment/Helm$ helm lint
==> Linting .

1 chart(s) linted, 0 chart(s) failed
-  helm install myapp ../Helm -f values.yaml
NAME: myapp
LAST DEPLOYED: Wed Oct 25 15:27:13 2023
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
- to check if everything is up and running -> kubectl get pods -n default


myapp-backend-deployment-6c5d76785b-p5n5w    1/1     Running   0          29s
myapp-frontend-deployment-864b79bb6c-65hmw   1/1     Running   0          29s
myapp-mysql-deployment-7657fbf6f-gx5zg       1/1     Running   0          29s

I have used helm since it helps with Scalabillity, Maintainability, and Security.