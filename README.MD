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
- Berdasarkan train EN B0-B7 pilih variasi yang memberikan acc dan vall acc tertinggi.
- Menggunakan model tersebut lakukan downsampling ke dataset cadangan kemudian test ulang
- Menggunakan model tersebut lakukan train ulang menggunakan dataset cadangan kemudian test ke dataset utama
- Menggunakan model tersebut lakukan modifikasi menggunakan hardcode
- Menggunakan model tersebut train ulang namun menggunakan K fold cross validation

# QnA
- Apakah modifikasi itu wajib? Atau dengan menggunakan fine-tuning (melatih ulang beberapa layer) saja sudah cukup?
- Apakah modifikasinya seperti menghapus beberapa layer saja diperbolehkan?
- Apakah import diperbolehkan?
- Q: Kapan harus mengganti judul di SK TA?
A:

Q: Apakah di BAB IV saya harus memasukan performansi dari B0-B7 baik untuk yang fine tuning dan tanpa fine tuning?
A:

Q: Apakah harus melakukan modifikasi? Atau melakukan fine tuning saja cukup?
A:

Q: Apakah BAB III harus saya tulis ulang? Karena berbeda dengan ketika proposal.
A:

Q: Karena tidak ada penelitian sebelumnya yang menggunakan dataset berbeda untuk train dan test seperti saya, bagaimana acuan dari model yang saya buat sudah cukup baik? Karena saat ini paling tinggi adalah 0.85
A:


# Running Ubuntu
- List distro: wsl --list --verbose
- Terminate: wsl -t Ubuntu
- Start: wsl --distribution Ubuntu