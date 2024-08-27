kubectl port-forward service/frontend-application-srv 8080:80
kubectl port-forward service/api-gateway-nodeport-srv 3000:3000
kubectl port-forward service/quotes-nodeport-srv 5000:5000


minikube service frontend-application-srv --url http://192.168.49.2:31895
minikube service api-gateway-nodeport-srv --url http://192.168.49.2:32215/api/randomquote
minikube service quotes-nodeport-srv --url http://192.168.49.2:31759 


curl http://192.168.49.2:32215/api/randomquote
curl http://192.168.49.2:31895
curl http://192.168.49.2:31759

