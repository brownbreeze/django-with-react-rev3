# https://hub.docker.com/r/centos/python-38-centos7

FROM registry.access.redhat.com/ubi8/python-38
# Add application sources to a directory that the assemble script expects them
# and set permissions so that the container runs without root access
MAINTAINER {name} <{git mail}>
USER root
RUN yum -y update && \
    yum clean all
EXPOSE 8000
EXPOSE 80
CMD ["/bin/bash"]

