FROM python:3 AS builder

WORKDIR /app

# COPY requirements.txt /app
COPY ./app /app
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE  8080

ENTRYPOINT ["python3"]
CMD ["app.py"]

# FROM builder as dev-envs

# RUN <<EOF
# apk update
# apk add git
# EOF

# RUN <<EOF
# addgroup -S docker
# adduser -S --shell /bin/bash --ingroup docker vscode
# EOF
# # install Docker tools (cli, buildx, compose)
# COPY --from=gloursdocker/docker / /