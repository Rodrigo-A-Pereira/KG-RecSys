FROM neo4j:latest
RUN apt-get update && \
      apt-get -y install sudo
USER root
RUN apt-get install curl -y
USER neo4j
CMD ["neo4j"]
