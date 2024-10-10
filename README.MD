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
