# syntax = docker/dockerfile:1

# NOTE, for cache/speed purpose, we need to enable buildkit
# 	@ref: https://docs.docker.com/develop/develop-images/build_enhancements/
#       @ref: https://github.com/moby/buildkit/blob/master/frontend/dockerfile/docs/syntax.md#run---mounttypecache

ARG CNNL_TEST_CUDA_VERSION="11.7.1"
ARG CNNL_TEST_CUDNN="-cudnn8"
ARG CNNL_TEST_DISTRO="ubuntu20.04"

FROM nvidia/cuda:${CNNL_TEST_CUDA_VERSION}${CNNL_TEST_CUDNN}-devel-${CNNL_TEST_DISTRO} AS yellow

ARG CNNL_TEST_CUDA_VERSION_SHORT="117"
ARG CNNL_TEST_PYTORCH_VERSION="1.13.0"
ARG CNNL_TEST_PYTORCH_META="torch==1.13.1+cu117 torchvision==0.14.1+cu117 torchaudio==0.13.1+cu117"
#ARG CNNL_TEST_PYTORCH_SOURCE="-f https://download.pytorch.org/whl/torch_stable.html"
ARG CNNL_TEST_PYTORCH_SOURCE="-f https://mirror.sjtu.edu.cn/pytorch-wheels/cu117/?mirror_intel_list"
ARG CNNL_TEST_MMCV_VERSION="1.7.0"
ARG CNNL_TEST_MMCV_DEP_VER="cu117/torch1.13"
ARG CNNL_TEST_TF_VERSION="2.11.0"
ARG CNNL_TEST_ONNX_VERSION="1.12.0"
ARG CNNL_TEST_PADDLE_VERSION="2.4.1"

LABEL maintainer "Jia Minghao <jiaminghao@cambricon.com>"

ARG DEBIAN_FRONTEND=noninteractive

# Cache /var/lib/apt/lists/* and /var/cache/apt/archives/partial/ and /var/cache/apt/*.bin, no more apt-get clean
RUN sed -i -r 's|(^.+$)|// \0|g' /etc/apt/apt.conf.d/docker-clean; echo 'Binary::apt::APT::Keep-Downloaded-Packages "true";' > /etc/apt/apt.conf.d/keep-cache

RUN --mount=type=cache,target=/var/cache/apt --mount=type=cache,target=/var/lib/apt apt-get update --fix-missing \
    && apt-get install -y --no-install-recommends bzip2 ca-certificates git wget curl openssh-server patchelf lftp tree less vim sudo rsync cmake \
                                                  ninja-build protobuf-compiler jupyter python3 python3-pip python3-dev \
    && apt-get install -y --no-install-recommends ipython3 python3-protobuf python3-tqdm python3-matplotlib python3-numpy python3-h5py python3-sympy \
                                                  python3-ipython python3-ipdb python3-plotly python3-pandas python3-scipy python3-opencv python3-jinja2 \
    && apt-get install -y --no-install-recommends python3-aiomysql python3-pydantic \
    && apt-get install -y --no-install-recommends python3-setuptools python3-venv python3-wheel \
    && update-alternatives --install /usr/bin/python python /usr/bin/python3 10 \
    && update-alternatives --install /usr/bin/ipython ipython /usr/bin/ipython3 10 \
    && update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 10

# For Ubuntu20.04 specific
RUN --mount=type=cache,target=/var/cache/apt --mount=type=cache,target=/var/lib/apt apt-get update --fix-missing \
    && apt-get install -y --no-install-recommends ripgrep

RUN --mount=type=cache,target=/root/.cache echo "install python modules" \
    && python3 -m pip install cupy-cuda${CNNL_TEST_CUDA_VERSION_SHORT} \
    # @ref https://pytorch.org/get-started/previous-versions/ \
    && python3 -m pip install ${CNNL_TEST_PYTORCH_META} ${CNNL_TEST_PYTORCH_SOURCE} \
    # @ref https://www.tensorflow.org/install/gpu \
    && python3 -m pip install tensorflow==${CNNL_TEST_TF_VERSION} \
    # @ref https://mmcv.readthedocs.io/en/latest/get_started/installation.html \
    && python3 -m pip install mmcv-full==${CNNL_TEST_MMCV_VERSION} -f https://download.openmmlab.com/mmcv/dist/${CNNL_TEST_MMCV_DEP_VER}/index.html \
    # @ref https://github.com/pybind/pybind11 \
    && python3 -m pip install pybind11==2.10.2

RUN --mount=type=cache,target=/root/.cache echo "install python modules" \
    # @ref https://onnxruntime.ai \
    && python3 -m pip install onnxruntime-gpu==${CNNL_TEST_ONNX_VERSION} onnx==${CNNL_TEST_ONNX_VERSION}

# For CUDA specific
# TODO red region need 440.64 specific version
#RUN --mount=type=cache,target=/var/cache/apt --mount=type=cache,target=/var/lib/apt echo "will install cuda driver" \
#    && echo "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64 /" | tee -a /etc/apt/sources.list.d/cuda_ubuntu1804.list \
#    && echo "deb https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64 /" | tee -a /etc/apt/sources.list.d/nvidia-ml_ubuntu1804.list \
#    && apt-get update --fix-missing \
#    && apt-get install -y --no-install-recommends libnvidia-compute-440=440.64.00-0ubuntu1 nvidia-utils-440=440.64.00-0ubuntu1

#RUN --mount=type=cache,target=/mnt cd /mnt \
#    && wget -c https://us.download.nvidia.com/XFree86/Linux-x86_64/440.64/NVIDIA-Linux-x86_64-440.64.run \
#    && cp NVIDIA-Linux-x86_64-440.64.run /tmp

#For disabling CUDA>=11.2 constraint
ENV NVIDIA_DISABLE_REQUIRE=1

# Update, install more python modules
RUN --mount=type=cache,target=/var/cache/apt --mount=type=cache,target=/var/lib/apt --mount=type=cache,target=/root/.cache apt-get update \
  && apt-get install -y --no-install-recommends python3-sqlalchemy python3-tqdm \
  && apt-get install -y --no-install-recommends python3-numba python3-yaml \
  && apt-get install -y --no-install-recommends python3-llvmlite python3-skimage


# FIXME
## 	workaround for TensorFlow and NumPy compatibility issue (for numpy 1.24, numpy.typeDict deleted but tensorflow 2.11 still used it)
##      SharedArray is depended by OpenPCDet below, which needs to be compiled based on NumPy C Api
#		    rm -f /root/.cache/pip/wheels/86/a2/0d/fafb27e442cf41a06afdf6b29fccc4eb5c2037183f8b64f615/SharedArray-3.2.2-cp38-cp38-linux_x86_64.whl \
RUN --mount=type=cache,target=/root/.cache echo "workaround for tf and numpy" \
    && python3 -m pip install --upgrade numpy==1.22.4 \
    && python3 -m pip uninstall -q -y SharedArray \
    && python3 -m pip install --upgrade SharedArray

# https://github.com/open-mmlab/OpenPCDet commit 4713332c5b73b32ac23b425022a06861bfa23b89
#RUN --mount=type=cache,target=/root/.cache python3 -m pip install -r https://raw.githubusercontent.com/open-mmlab/OpenPCDet/4713332c5b73b32ac23b425022a06861bfa23b89/requirements.txt \
RUN --mount=type=cache,target=/root/.cache \
  curl https://raw.githubusercontent.com/open-mmlab/OpenPCDet/4713332c5b73b32ac23b425022a06861bfa23b89/requirements.txt | grep -v '^json' | grep -v '^cv2' | grep -Eo '(^[^#]+)' | xargs python3 -m pip install \
  && python3 -m pip install spconv spconv-cu${CNNL_TEST_CUDA_VERSION_SHORT}

RUN --mount=type=cache,target=/root/.cache python3 -m pip install torch-scatter -f https://data.pyg.org/whl/torch-${CNNL_TEST_PYTORCH_VERSION}+cu${CNNL_TEST_CUDA_VERSION_SHORT}.html

# https://github.com/PaddlePaddle/Paddle
RUN --mount=type=cache,target=/root/.cache python3 -m pip install paddlepaddle-gpu==${CNNL_TEST_PADDLE_VERSION}.post${CNNL_TEST_CUDA_VERSION_SHORT} -f https://www.paddlepaddle.org.cn/whl/linux/mkl/avx/stable.html

FROM yellow AS build_pcdet
ENV TORCH_CUDA_ARCH_LIST="3.5 5.2 6.0 6.1 7.0 7.5 8.0 8.6+PTX"
RUN --mount=type=cache,target=/tmp/OpenPCDet mkdir -p /tmp/OpenPCDet && cd /tmp/OpenPCDet \
  && git clone --single-branch https://github.com/open-mmlab/OpenPCDet.git . || git pull \
  && git checkout 4713332c5b73b32ac23b425022a06861bfa23b89 \
  && python3 setup.py bdist_wheel && mkdir -p /dist && mv dist/*.whl /dist/

FROM yellow AS red

# RUN echo "/usr/local/cuda-11.2/compat" > /etc/ld.so.conf.d/zzz_cuda_compat.conf

RUN --mount=type=cache,target=/root/.cache --mount=type=bind,from=build_pcdet,source=/dist,target=/dist ls /dist \
  && python3 -m pip install /dist/*.whl

ARG DEBIAN_FRONTEND=noninteractive
RUN --mount=type=cache,target=/var/cache/apt --mount=type=cache,target=/var/lib/apt apt-get update --fix-missing \
  && apt-get install -y --no-install-recommends iputils-ping dnsutils net-tools

# https://pip.pypa.io/en/stable/topics/configuration/
# PIP_INDEX_URL
RUN echo "[global]\nindex-url = http://mirrors.cambricon.com/pypi/web/simple\n[install]\ntrusted-host = mirrors.cambricon.com" > /etc/pip.conf

# setup bashrc
ENV OSH=/usr/local/src/oh-my-bash
RUN git clone --depth=1 https://github.com/ohmybash/oh-my-bash.git $OSH \
  && cat $OSH/templates/bashrc.osh-template >> /etc/bash.bashrc     

RUN sed -i "/^export OSH=/ c export OSH=$OSH"  /etc/bash.bashrc     
RUN sed -i "/^OSH_THEME=/ c export OSH_THEME=\"\${OSH_THEME:-random}\""  /etc/bash.bashrc
RUN sed -i -r "s/^# (DISABLE_AUTO_UPDATE=.*)/\1/g" /etc/bash.bashrc

# more bashrc, ref: https://github.com/tensorflow/tensorflow/blob/master/tensorflow/tools/dockerfiles/bashrc https://hub.docker.com/layers/tensorflow/tensorflow/latest-devel-gpu/images/sha256-f60847027e60cc3661505e7a426dbf57ffc921dee6110ea8c31684d71c74e621?context=explore

# setup permission
RUN echo "setup permission" \
  && groupadd -g 10028 SW-group07 \
  && groupadd -g 10003 NG-group01 \
  && groupadd -g 10035 NG-group01R1 \
  && groupadd -g 10042 SW-group10 \
  && groupadd -g 10049 SW-groupcnnl \
  && groupadd -g 30005 SOFT_TRAIN \
  && groupadd -g 51002 softtest   \
  && groupadd -g 51003 streleasedev \
  && groupadd -g 51004 streleasetest \
  && useradd -g 10028 -G 10028,10003,10035,10042,10049,30005,51002,51003,51004 -u 13529 -m svc-jenkins -s /bin/bash \
  && useradd -g 10003 -G 10028,10003,10035,10042,10049,30005,51002,51003,51004 -u 17499 -m docker-user -s /bin/bash \
  && gpasswd -a svc-jenkins sudo \
  && gpasswd -a docker-user sudo \
  && echo "%sudo   ALL=(ALL:ALL) NOPASSWD:ALL" > /etc/sudoers.d/neuware \
  && touch /home/docker-user/.sudo_as_admin_successful \
  && echo "umask 0002" | tee -a /etc/bash.bashrc

# change mirror
RUN echo "change mirror" \
  && sed -i -e 's/archive.ubuntu.com/mirrors.cambricon.com/g' /etc/apt/sources.list \
  && sed -i -e 's/security.ubuntu.com/mirrors.cambricon.com/g' /etc/apt/sources.list


USER docker-user

