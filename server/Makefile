OPTIONS=--notebook-dir=../jupyter_home --config=../jupyter_home/jupyter_notebook_config.py

start:
	jupyter lab $(OPTIONS)

start.notebook:
	jupyter notebook $(OPTIONS)


REMOTE_URL=http://external-enterprise-gateway.pdp-jupyter-enterprise-gateway.svc.ad1.io.navercorp.com:8888
start.with-gateway:
	KERNEL_LAUNCH_TIMEOUT=300 jupyter lab --gateway-url=$(REMOTE_URL) $(OPTIONS)
