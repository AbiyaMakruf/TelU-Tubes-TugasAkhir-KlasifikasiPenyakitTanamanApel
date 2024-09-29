#!/bin/bash

# Script untuk menginstal nano pada sistem Linux

# Memperbarui repositori paket
echo "Memperbarui repositori paket..."
apt-get update
apt-get install -y nano
echo "Inisialisasi Berhasil"