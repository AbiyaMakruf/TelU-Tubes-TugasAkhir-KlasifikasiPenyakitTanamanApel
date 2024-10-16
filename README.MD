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
- Berdasarkan train EN B0-B7 pilih variasi yang memberikan test acc tertinggi. ENB3 (Not Trainable) 0.80 & ENB7 (Trainable) 0.84
- Menggunakan model tersebut lakukan downsampling ke dataset cadangan kemudian test ulang (coba segmented dan non segmented)
- Menggunakan model tersebut lakukan train ulang menggunakan dataset cadangan kemudian test ke dataset utama
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