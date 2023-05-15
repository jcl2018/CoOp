# Setup Notes
## 1. Install packages as suggested
- make sure you get GPU version of cuda


    pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117

## 2. Download data
- Example of Caltech101
  - Download
  - Create a "data" folder in root and unzip data
## 3. Change the path in shell files (like zeroshot.sh)

    bash .\scripts\coop\zeroshot.sh caltech101 rn50

# Misc issues
## 1. Ultimate solution to solve SSL error (when you download clip pretrained)
- For mac


    /Applications/Python\ 3.10/Install\ Certificates.command



