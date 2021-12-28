FROM python:3.10.1-slim-bullseye

# Bring in the python application code
COPY Application/ Work/

# Create arguements with defaults (in case non are supplied)
ARG fizz_buzz_min=1
ARG fizz_buzz_max=30

# Set the environment variables
ENV FIZZ_BUZZ_MIN=$fizz_buzz_min
ENV FIZZ_BUZZ_MAX=$fizz_buzz_max

# Launch the application
ENTRYPOINT ["python", "Work/main.py"]