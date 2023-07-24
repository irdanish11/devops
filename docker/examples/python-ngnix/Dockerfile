FROM python:3.10.11-slim-buster

RUN apt-get -y update && apt-get install -y --no-install-recommends \
         wget \
         nginx \
         ca-certificates \
    && rm -rf /var/lib/apt/lists/*


# set the working directory
RUN ["mkdir", "/app"]
WORKDIR "/app"
COPY "requirements.txt" .
RUN pip --no-cache-dir install -r requirements.txt

# Remove build dependencies and other unnecessary packages, which reduces the
# size of the image and also reduces the attack surface when running the model.
RUN apt-get autoremove -y && apt-get clean && apt-get update
# Set some environment variables. PYTHONUNBUFFERED keeps Python from buffering
# our standard output stream, which means that logs can be delivered to the
# user quickly. PYTHONDONTWRITEBYTECODE keeps Python from writing the .pyc
# files which are unnecessary in this case. We also update PATH so that the
# serve program can be found when the container is invoked.
ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/app:${PATH}"

COPY . .

# Here we set the port that the container will expose
# EXPOSE 8080

# Set up the program in the image
ENTRYPOINT [ "python" ]
CMD [ "serve.py" ]
