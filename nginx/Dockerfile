FROM nginx

# Copy custom configuration file from the current directory
COPY nginx.conf /etc/nginx/nginx.conf

# Copying in the SSL configuration for our test domain FQDN www.rti-research.net.  To build this for another domain, just copy the certificate and key file for your FQDN and rebuild.

RUN mkdir -p /etc/nginx/ssl/
COPY nginx.key /etc/nginx/ssl/nginx.key
COPY nginx.crt /etc/nginx/ssl/nginx.crt
