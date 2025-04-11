# Vietnamese Handwriting Recognition with LSTM 🖋️

Dự án nhận dạng chữ viết tay tiếng Việt từ ảnh sử dụng mô hình LSTM kết hợp với TensorFlow.

## 📁 Cấu trúc thư mục

DAKHMT/
│
├── .gitignore
├── README.md
├── requirements.txt
├── hw_env/
│
├── src/
│   └── main.py
│
├── tests/
│   └── test_main.py
│
├── .vscode/
│   ├── launch.json
│   └── settings.json
│
└── data/
    ├── InkData_line
    ├── InkData_word
    ├── InkData_paragraph
    ├── InkData_line.csv
    ├── InkData_word.csv
    └── InkData_paragraph.csv

## ⚙️ Hướng dẫn chạy

### 1. Tạo môi trường ảo

```bash
python -m venv hw_env

```
### 2. Kích hoạt môi trường

#### Windows
```bash
.\hw_env\Scripts\activate
```
#### MacOS / Linux
```bash
source hw_env/bin/activate
```
### 3. Cài thư viện cần thiết
```bash
pip install -r requirements.txt


