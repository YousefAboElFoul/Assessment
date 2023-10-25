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

--------------------------------------------------------------
# Task B 

In the directory Assessment/Helm:
1. helm lint
2. helm install myapp ../Helm -f values.yaml 
TO BE DONE: ADD documentation
- I pushed my docker images to an online repository which is mine on dockerhub
- I am using images that i deployed previously here one for the frontend and one for the backend
- To verify that the chart is working you can use : helm lint
the ouput should be 
/Assessment/Helm$ helm lint
==> Linting .

1 chart(s) linted, 0 chart(s) failed

