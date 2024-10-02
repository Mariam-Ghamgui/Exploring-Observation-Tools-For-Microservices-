pip install opentelemetry-api opentelemetry-sdk opentelemetry-exporter-jaeger


git clone -b main https://github.com/SigNoz/signoz.git && cd signoz/deploy/


docker compose -f docker/clickhouse-setup/docker-compose.yaml up -d

docker ps

http://localhost:3301/

how to access

1-  docker login

cd signoz/deploy/

   docker-compose -f docker/clickhouse-setup/docker-compose.yaml up -d
   docker-compose -f docker/clickhouse-setup/docker-compose.yaml ps

   http://localhost:3301/



   secon way--------------------------.
   snap install helm

   helm repo add signoz https://charts.signoz.io
   helm repo update

   kubectl create namespace signoz

   helm install my-release signoz/signoz -n signoz


   kubectl get pods -n signoz -w


   kubectl port-forward -n signoz my-release-signoz-frontend-7dbd8f99bc-j46z2  3301:3301


   http://localhost:3301/

   cd ApiGateway

npm install @opentelemetry/sdk-node @opentelemetry/auto-instrumentations-node @opentelemetry/exporter-trace-otlp-http


docker build -t mariamghamgui/api-gateway:latest ./ApiGateway
docker push mariamghamgui/api-gateway:latest

docker build -t mariamghamgui/quotes:latest ./QuoteService
docker push mariamghamgui/quotes:latest

kubectl apply -f kubernetes/


twaaa netdata

   curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash

      helm repo add netdata https://netdata.github.io/helmchart/

      helm repo update   

         kubectl create namespace netdata

            helm install netdata netdata/netdata --namespace netdata

               kubectl get pods -n netdata -w

               kubectl port-forward --namespace netdata netdata-parent-6c94c78645-4htbd 19999:19999

               http://localhost:19999


               For more detailed application monitoring, you can install the Netdata agent in your application containers. Add the following to your Dockerfiles:


               To enable alerts, you can configure Netdata to send notifications to various platforms like Slack, Discord, or email. This can be done by editing the netdata.conf file in the Netdata configuration.

kubectl logs -f -n netdata deployment/netdata-parent

This setup will give you a comprehensive view of your cluster and application performance. You can further customize Netdata's configuration to suit your specific monitoring needs.
Let me know if you need any clarification on these steps or if you encounter any issues during the implementation!



coroot

   helm repo add coroot https://coroot.github.io/helm-charts

      helm repo update

         kubectl create namespace coroot

            helm install coroot coroot/coroot -n coroot


               kubectl get pods -n coroot -w


                  kubectl port-forward -n coroot svc/coroot 8080:8080


                  Now you can access the Coroot dashboard by opening a web browser and navigating to http://localhost:8080.


                  For the API Gateway (Node.js):
Install the required packages:

   npm install @opentelemetry/api @opentelemetry/sdk-node @opentelemetry/auto-instrumentations-node @opentelemetry/exporter-metrics-otlp-http


   For the Quote Service (Python):
Install the required packages:


   pip install opentelemetry-api opentelemetry-sdk opentelemetry-instrumentation-flask opentelemetry-exporter-otlp


   To enable Coroot to collect logs, you can use Fluent Bit. Add this to your Helm installation:
       helm upgrade coroot coroot/coroot -n coroot --set fluentBit.enabled=true

       13. For more detailed network traffic analysis, you can enable eBPF monitoring:
           helm upgrade coroot coroot/coroot -n coroot --set ebpf.enabled=true

           After completing these steps, Coroot should be collecting metrics, traces, and logs from your services. You can view this data in the Coroot UI.
Remember to adjust the endpoint URLs in the OpenTelemetry configuration if your Coroot installation is named differently or in a different namespace.
Let me know if you need any clarification on these steps or if you encounter any issues during the implementation!









kubectl apply -f kubernetes/api-gateway-depl.yaml
kubectl apply -f kubernetes/quotes-depl.yaml
   kubectl apply -f kubernetes/otel-collector.yaml




automating the Netdata agent as well. Netdata can be automated in Kubernetes using a DaemonSet, which ensures that all (or some) nodes run a copy of the Netdata pod. Here's how we can automate the Netdata agent deployment:
1. Create a new file called netdata-daemonset.yaml in your kubernetes directory with the following content:


2.Create the monitoring namespace if it doesn't exist:
kubectl create namespace monitoring

3.Apply the Netdata DaemonSet configuration
kubectl apply -f kubernetes/netdata-daemonset.yaml

This configuration will:
Deploy Netdata as a DaemonSet, ensuring it runs on every node in your cluster.
Create the necessary RBAC permissions for Netdata to access Kubernetes metrics.
Create a NodePort service to access the Netdata dashboard from outside the cluster.
4. Update your existing deployments to remove the Netdata-specific annotations, as Netdata will now be collecting data from all nodes automatically.


kubectl apply -f kubernetes/api-gateway-depl.yaml
kubectl apply -f kubernetes/quotes-depl.yaml
kubectl apply -f kubernetes/frontend-application-depl.yaml

Port-forwarding: kubectl port-forward -n monitoring service/netdata 19999:19999


Certainly! Let's set up an Ingress to access your application and observability tools. This approach is more robust and production-like compared to port-forwarding. We'll use Nginx Ingress Controller for this purpose.

kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.1/deploy/static/provider/cloud/deploy.yaml


kubectl apply -f kubernetes/ingress.yaml
Get the Ingress IP or hostname:
kubectl get ingress

This will give you an IP address or hostname. Let's assume it's 192.168.49.2 for this example.
Update your /etc/hosts file (on Unix-based systems) or C:\Windows\System32\drivers\etc\hosts (on Windows) to include:
192.168.49.2 microservices.local

. Now you can access your services through the Ingress:
API Gateway: http://microservices.local/api/quote
Quotes Service: http://microservices.local/quotes/api/quote
Netdata: http://microservices.local/netdata
SigNoz: http://microservices.local/signoz
Coroot: http://microservices.local/coroot



from

endpoint: "my-release-otel-collector.signoz.svc.cluster.local:4317"
endpoint: "coroot-otel-collector.coroot.svc.cluster.local:4317"
to


endpoint: "http://microservices.local/signoz"
endpoint: "http://microservices.local/coroot"


kubectl apply -f kubernetes/otel-collector.yaml

kubectl rollout restart deployment api-gateway-depl quotes-depl