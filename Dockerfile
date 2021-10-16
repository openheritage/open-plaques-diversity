FROM jupyter/scipy-notebook:lab-3.1.17

RUN mamba install --yes \
    nltk \
    numpy \
    wikipedia \
    && mamba clean --all -f -y

RUN pip install qwikidata

RUN fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"
