CHART_NAME=enterprise-gateway
HELM_VALUES_OPTIONS=--values=multi-tenancy.values.yaml
deploy:
	ncc helm upgrade $(HELM_VALUES_OPTIONS) --install $(CHART_NAME) ./helm

delete:
	ncc helm delete --purge $(CHART_NAME)

HOST_FORWARD_PORT=8889
web.port-forward:
	kubectl port-forward services/$(CHART_NAME) $(HOST_FORWARD_PORT):8888

start.client:
	KERNEL_LAUNCH_TIMEOUT=300 jupyter notebook --gateway-url=http://localhost:8889

REMOTE_URL=http://external-enterprise-gateway.pdp-jupyter-enterprise-gateway.svc.ad1.io.navercorp.com:8888
start.remote:
	KERNEL_LAUNCH_TIMEOUT=300 jupyter lab --gateway-url=$(REMOTE_URL) --notebook-dir=../jupyter_home

expose:
	kubectl expose service/$(CHART_NAME) --name external-$(CHART_NAME) --type LoadBalancer