FROM postgres:15-bullseye


COPY ./docker/postgres/maintenance /usr/bin/maintenance

RUN chmod +x /usr/bin/maintenance/*

RUN mv /usr/bin/maintenance/* /usr/bin \
  && rmdir /usr/bin/maintenance