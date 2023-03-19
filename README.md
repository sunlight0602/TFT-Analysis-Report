# TFT-Analysis-Report

Overlay for Team Fight Tactics. Get information with OCR while gaming. Analyze your play and generate a report.

# Restrictions

- Only for macOS.
- Develop for tw2 server.

# Quick Start
```shell
python3.9 -m venv venv
source ./venv/bin/activate
python -m pip install paddlepaddle -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install "paddleocr>=2.0.1" --upgrade PyMuPDF==1.21.1
pip uninstall numpy
pip install numpy==1.23
python main.py
```
Close by right click and click "exit" on the icon.