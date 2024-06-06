# Use a Linux-based image as a parent image
FROM debian:bullseye

# Set the working directory in the container
WORKDIR /app

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    poppler-utils \
    libgl1-mesa-glx \ 
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --upgrade pip

RUN python3 -m pip install --upgrade Pillow

RUN python3 -m pip install deepdoctection[pt]

RUN python3 -m pip install torch==1.12.0 torchvision==0.13.0

RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/facebookresearch/detectron2.git /app/detectron2
WORKDIR /app/detectron2
RUN python3 -m pip install -e .


# Return to the working directory
WORKDIR /app

EXPOSE 8000

# Copy the current directory contents into the container at /app
COPY . .
RUN python3 -m pip install -r ./requirements.txt

# Run pdftotext -v to check the version of pdftotext
RUN pdftotext -v

# Run main.py when the container launches
CMD ["python3", "app.py"]
