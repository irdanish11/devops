FROM python:3.10.11-slim-buster

RUN apt-get -y update && apt-get install -y --no-install-recommends \
         wget \
         nginx \
         ca-certificates \
    && rm -rf /var/lib/apt/lists/*


# set the working directory
ARG WORK_DIR="/app"
RUN ["mkdir", "$WORK_DIR"]
WORKDIR ${WORK_DIR}
COPY "requirements.txt" .
RUN pip --no-cache-dir install -r requirements.txt

# Remove build dependencies and other unnecessary packages, which reduces the
# size of the image and also reduces the attack surface when running the model.
RUN apt-get autoremove -y && apt-get clean && apt-get update

# Set up environment variables
# Python output i.e. the (stdout and stderr) streams is
# sent straight to the conatiner log
ENV PYTHONUNBUFFERED=TRUE
# avoid writing byte code (.pyc files)
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="${WORK_DIR}:${PATH}"
ENV APP_DIR=${WORK_DIR}

COPY . .

# Set up the program in the image
ENTRYPOINT [ "python" ]
CMD [ "serve.py" ]
