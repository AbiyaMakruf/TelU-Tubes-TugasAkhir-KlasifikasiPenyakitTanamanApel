#!/bin/bash

# Script untuk menginstal nano pada sistem Linux

# Memperbarui repositori paket
echo "Memperbarui repositori paket..."
apt-get update
apt-get install -y nano
git config --global user.email "aabbiiyyaa@gmail.com"
git config --global user.name "AbiyaMakruf"
pip install gdown
pip install pandas
pip install scikit-learn
pip install scipy 
pip install opencv-python
pip install seaborn
echo "Inisialisasi Berhasil"