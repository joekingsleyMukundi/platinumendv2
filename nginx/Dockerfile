FROM nginx:1.21.5-alpine
# remove default nginx config
RUN rm /etc/nginx/conf.d/default.conf
# copy nginx config
COPY default.conf /etc/nginx/conf.d/nginx.conf