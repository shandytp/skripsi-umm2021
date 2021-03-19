# Source Code Skripsi 

[Source Dataset](https://www.kaggle.com/navoneel/brain-mri-images-for-brain-tumor-detection)

### Goal
Melakukan klasifikasi tumor otak dengan metode SVM

### Skenario Percobaan
- Skenario Pertama akan menggunakan metode segmentasi Otsu thresholding dalam membantu performa klasifikasi tumor otak menggunakan metode SVM
- Skenario Kedua akan menggunakan metode segmentasi Niblack thresholding dalam membantu performa klasifikasi tumor otak menggunakan metode SVM
- Skenario Ketiga akan menggunakan metode segmentasi Sauvola thresholding dalam membantu performa klasifikasi tumor otak menggunakan metode SVM

### Output
Akan membandingkan hasil dari ketiga skenario dalam bentuk tabel pengujian

### TODO List

- [x] Replikasi model dan codingan dari paper utama
- [x] Membuat function untuk Otsu, Niblack dan Sauvola thresholding
- [x] Apply image function ke test.jpg
- [x] Mengambil nama file dalam bentuk list
- [ ] Apply image function ke list file
- [ ] Train new image dengan model dari paper utama
