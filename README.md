# Assessment
--------------------------------------------------------------
The project is for both Task A and Task B
--------------------------------------------------------------
For Task A , 
In the directory Assessment:
it could be simply run via using the command line
the command to run is : docker compose up 
TO BE DONE: ADD documentation
--------------------------------------------------------------
For Task B , 
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

