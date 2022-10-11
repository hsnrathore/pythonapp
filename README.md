######## Building The Application ########

This a python flask based app which i have already dockerize using the Dockerfile present in the repo. Application code is inside src directory

To build a new docker image for this application you can make use of the following command inside the repository:

docker build -t <name of your docker account>/pythonapp:slimv4 .

######## Deployment of Application on k8s ########

This application can be deployed in a kubernetes cluster all the related manifest files are already present in the repository. This application makes use of ingress controller to publish the application via ingress resource (present in ingress-resource.yaml). To run the application make sure nginx-ingress-controller is deployed on the k8s cluster. If its not deployed you can follow the official guide (https://docs.nginx.com/nginx-ingress-controller/installation) to deploy it on cluster alternatively you can make use of the following helm commands to deploy the controller:


$ git clone https://github.com/nginxinc/kubernetes-ingress.git --branch v2.4.0
$ cd kubernetes-ingress/deployments/helm-chart
$ helm repo add nginx-stable https://helm.nginx.com/stable
$ helm repo update
$ helm install my-release nginx-stable/nginx-ingress


Once the nginx ingress controller has been deployed run the following commands to spin up the pythonapp as a deployment and expose it using the clusterip service to nginx resource:

kubectl apply -f deployment-manifest.yaml
kubectl apply -f service-manifest.yaml
kubectl apply -f ingress-resource.yaml

Note: Container exposes the application on port 8080/TCP