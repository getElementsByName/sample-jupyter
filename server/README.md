# JupyterLab
- https://jupyterlab.readthedocs.io/en/stable/index.html
- JupyterLab is the next-generation web-based user interface for Project Jupyter. 


### pip
```
pip install jupyterlab
```


### docker
```
docker run --rm -p 10000:8888 -e JUPYTER_ENABLE_LAB=yes -v "$PWD":/home/jovyan/work jupyter/datascience-notebook:9b06df75e445
```