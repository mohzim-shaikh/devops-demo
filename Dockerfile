############################################################
# Dockerfile to build Flask App
# Based on
############################################################

# Set the base image
FROM debian:bullseye-slim

# File Author / Maintainer
LABEL image.author="carlos.tighe@universityofgalway.ie"

RUN apt-get update && apt-get install --no-install-recommends -y apache2 \
    libapache2-mod-wsgi-py3 \
    python3 \
    python3-pip \
    && apt-get clean \
    && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/*

# Copy over and install the requirements
COPY ./app/requirements.txt /var/www/devops-demo/app/requirements.txt
RUN pip install -r /var/www/devops-demo/app/requirements.txt --no-cache-dir

# Copy over the apache configuration file and enable the site
COPY ./devops-demo.conf /etc/apache2/sites-available/devops-demo.conf
# Copy over the wsgi file, run.py and the app
COPY ./ /var/www/devops-demo/

RUN a2dissite 000-default.conf && \
    a2ensite devops-demo.conf && \
    a2enmod headers

# LINK apache config to docker logs.
RUN ln -sf /proc/self/fd/1 /var/log/apache2/access.log && \
    ln -sf /proc/self/fd/1 /var/log/apache2/error.log

EXPOSE 80

WORKDIR /var/www/devops-demo

CMD  ["/usr/sbin/apache2ctl -D FOREGROUND"]
