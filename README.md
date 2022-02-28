# Tucil2_13520060

### Deskripsi Singkat
Program ini merupakan program console-based dalam bahasa python. Program akan menghasilkan convex hull dari himpunan titik pada datasets iris, breast cancer, dan wine dari scikit.

## Prasyarat (pada Windows 10)
Untuk bisa menggunakan program ini, diperlukan prasyarat yang sudah ada pada sistem sebagai berikut

- Python 3.8.10
- Library IPython
- Library Matplotlib
- Library Jupyter Notebook/Jupyterlab
- Library pandas
- Library sklearn
- Library numpy

Semua library di atas dapat di-install menggunakan perintah berikut di commandprompt atau shell

```shell
pip install - r requirements.txt
```

Contoh : (instalasi pandas)

```shell
pip install pandas
```

Untuk instalasi python, boleh dilihat pada laman https://www.tutorialspoint.com/how-to-install-python-in-windows

## How to run (pada Windows 10)

1. Download repo ini dalam bentuk zip melalui website github lalu ekstrak file zip tersebut

2. Buka folder src yang di dalamnya terdapat main.py dan convexHull.py

3. Jalankan cmd.exe pada folder tersebut

4. Pada command prompt jalankan perintah "python main.py"

5. Program akan terbuka di command prompt

6. Program akan meminta input pilihan datasets yang akan digunakan berupa angka 1-3 sesuai nomor datasets pada layar (1 = Iris, 2 = Breast Cancer, 3 = Wine)

7. Program akan meminta input pilihan atribut sumbu x dan y berupa angka sesuai nomor atribut tiap datasets pada layar

8. Program akan menampilkan hasil convex hull pada layar

9. Program akan berhenti ketika anda menekan tombol "X" pada hasil convex hull yang dikeluarkan