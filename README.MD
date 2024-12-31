# Tugas Akhir Mahasisa S1 Informatika Telkom University
Dibuat dalam format paper sebagai pengganti sidang. Tautan paper dapat diakses pada link [berikut](https://github.com/AbiyaMakruf/TelU-Tubes-TugasAkhir-KlasifikasiPenyakitTanamanApel/blob/b351c36564f996a1cf0d8e82cfada3626502c55c/Classification%20of%20Apple%20Leaf%20Diseases%20Using%20a%20Modified%20EfficientNet.pdf) dan tautan slide presentasi dapat diakses pada link [berikut](https://github.com/AbiyaMakruf/TelU-Tubes-TugasAkhir-KlasifikasiPenyakitTanamanApel/blob/d272042199a2a8a413af3facef52b1da064b7991/Presentasi%20ICICyTA%202024.pdf).

# Script create key for SSH
ssh-keygen -t rsa -b 4096 -C "aabbiiyyaa@gmail.com"

cat ~/.ssh/id_rsa.pub

ssh -T git@github.com


# Script startup pod

- Pastikan direktori .ssh ada
    ```
    mkdir -p ~/.ssh
    ```

- Copy SSH key dari volume persisten ke ~/.ssh setiap kali startup
    ```
    cp /workspace/ssh/id_rsa ~/.ssh/id_rsa
    cp /workspace/ssh/id_rsa.pub ~/.ssh/id_rsa.pub
    ```

- Set permission yang benar untuk SSH key
    ```
    chmod 600 ~/.ssh/id_rsa
    chmod 644 ~/.ssh/id_rsa.pub
    ```

- Tambahkan GitHub ke daftar known_hosts jika belum ada
    ```
    if ! grep -q "github.com" ~/.ssh/known_hosts; then
    ssh-keyscan github.com >> ~/.ssh/known_hosts
    fi
    ```

# To Do
- ~Berdasarkan train EN B0-B7 pilih variasi yang memberikan test acc tertinggi. ENB3 (Not Trainable) 0.80 & ENB7 (Trainable) 0.84~
- ~Menggunakan model tersebut lakukan downsampling ke dataset cadangan kemudian test ulang (coba segmented dan non segmented)~
- ~Menggunakan model tersebut lakukan train ulang menggunakan dataset cadangan kemudian test ke dataset utama~
- Menggunakan model tersebut lakukan modifikasi menggunakan hardcode
- Menggunakan model tersebut train ulang namun menggunakan K fold cross validation

# QnA
- Apakah modifikasi itu wajib? Atau dengan menggunakan fine-tuning (melatih ulang beberapa layer) saja sudah cukup?
- Apakah modifikasinya seperti menghapus beberapa layer saja diperbolehkan? atau harus add new layer?
- Apakah import efficientNet diperbolehkan? Atau harus menggunakan source code asli efficientNet?
- Kapan harus mengganti judul di SK TA?
- Apakah di BAB IV saya harus memasukan performansi dari B0-B7 baik untuk yang fine tuning dan tanpa fine tuning?
- Apakah BAB III harus saya tulis ulang? Karena berbeda dengan apa yang saya tulis ketika proposal.
- Karena tidak ada penelitian sebelumnya yang menggunakan dataset berbeda untuk train dan test seperti saya, bagaimana acuan dari model yang saya buat sudah cukup baik? Karena saat ini paling tinggi adalah 0.84

# Running Ubuntu
- List distro: wsl --list --verbose
- Terminate: wsl -t Ubuntu
- Start: wsl --distribution Ubuntu

# Referensi Dari Openlibrary
- https://openlibrary.telkomuniversity.ac.id/home/catalog/id/217314/slug/klasifikasi-penyakit-citra-daun-pada-tanaman-anggur-berbasis-machine-learning-dalam-bentuk-buku-karya-ilmiah.html
- https://openlibrary.telkomuniversity.ac.id/home/catalog/id/215210/slug/klasifikasi-penyakit-tanaman-menggunakan-convolutional-neural-network-cnn-dan-pemantauan-pertumbuhan-tanaman-cabai-dalam-bentuk-buku-karya-ilmiah.html

# Laporan TA

1. Apakah melakukan modifikasi (add/delete layer) itu wajib atau fine-tuning saja cukup? Jika iya apakah harus menggunakan source code asli atau boleh menggunakan import?
2. Apakah pada penulisan TA hanya melanjutkan bab IV dan V atau boleh menulis ulang bab I-III jika terdapat revisi?

Yg nomor 1 modif juga, bukan cuma fine tuning, nanti dibandingkan hasil ketiganya (original, fine tuning, modif+finetuning). Source code bangun sendiri, cari dulu aja kodingan orang.
Nomor 2 silakan klo ada yg perlu disesuaikan di bab 1-3

- Original (not modified, imagenet, 100 %freeze)
- Original (not modified, imagenet, 50% freeze)
- Original (not modified, None, 100% train)
- Modified (Modified repeats = 1, None, 100% train)

# Acknoledment
- Jika precision tinggi tetapi recall rendah, sistem mendeteksi kanker hanya saat sangat yakin, tetapi beberapa pasien kanker mungkin tidak terdeteksi.
- Jika recall tinggi tetapi precision rendah, sistem menangkap hampir semua pasien kanker tetapi mungkin memberi banyak alarm palsu.
- F1-score yang tinggi menunjukkan sistem yang seimbang dalam ketepatan dan sensitivitas, cocok untuk deteksi yang membutuhkan keseimbangan.
