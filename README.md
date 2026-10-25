# Final Project Oprec PENSHIP — Moch Salman Al-Fariz (5225600107)

## Identitas
- **Nama:** Moch Salman Al-Fariz
- **NRP:** 5225600107
- **Program studi:** Game Technology, Politeknik Elektronika Negeri Surabaya (PENS)

## Project Roboflow
- **Project ID Roboflow:** `skyblues-workspace-7pe8m/object-detection-f29qk`, version 2
- **Link Roboflow Universe:** https://universe.roboflow.com/skyblues-workspace-7pe8m/object-detection-f29qk
- **Link dataset Version 2:** https://universe.roboflow.com/skyblues-workspace-7pe8m/object-detection-f29qk/dataset/2
- **Kelas:** `bottle`, `laptop`, `pencil`

## Dataset
- **Jumlah foto asli:** 10 foto botol plastik, 10 foto laptop, dan 10 foto pensil. Total 30 foto asli.
- **Metode pengambilan foto:** Foto diambil sendiri. Variasi jarak, sudut, pencahayaan, dan latar belakang disesuaikan dengan kondisi pengambilan foto yang sebenarnya.
- **Anotasi:** Menggunakan AI labeling Roboflow untuk membantu anotasi awal. Hasil anotasi diperiksa dan dirapikan secara manual.
- **Preprocessing:** Auto-Orient dan resize menjadi 640 × 640 piksel tanpa augmentasi.

## Training
- **Lingkungan training:** Laptop lokal melalui VS Code dan WSL Ubuntu, menggunakan GPU NVIDIA GeForce RTX 2050 dengan VRAM 4 GB.
- **Model:** YOLOv8n pretrained (`yolov8n.pt`).
- **Dataset:** Roboflow Version 2.
- **Parameter training:** 50 epoch, `imgsz=640`, `batch=16`, `seed=0`, optimizer `auto`.
- **Grafik:** Folder `grafik/` berisi `results.png`, `results.csv`, `confusion_matrix.png`, dan `BoxPR_curve.png`.

## Pengembangan Kode
1. Training dijalankan secara lokal melalui VS Code dan WSL Ubuntu menggunakan GPU NVIDIA RTX 2050.
2. File `predict.py` dikembangkan untuk menjalankan deteksi pada gambar atau video menggunakan `best.pt`, dengan parameter confidence yang dapat diatur.
3. Model terbaik hasil training Version 2 disimpan sebagai `best.pt` pada root repository.

## Hasil Eksperimen

Evaluasi model terbaik (`best.pt`) pada validation set Version 2:

| Kelas | Images | Instances | Precision | Recall | mAP50 | mAP50-95 |
|:---|---:|---:|---:|---:|---:|---:|
| Semua kelas | 3 | 3 | 0.917 | 0.989 | 0.995 | 0.908 |
| bottle | 2 | 2 | 1.000 | 0.978 | 0.995 | 0.920 |
| laptop | 1 | 1 | 0.833 | 1.000 | 0.995 | 0.895 |

**Catatan evaluasi:** Validation set hanya berisi 3 gambar dan 3 instance. Karena jumlah sampel evaluasi sangat kecil, metrik tersebut belum cukup untuk menunjukkan kemampuan generalisasi model pada kondisi baru. Kelas `pencil` tidak muncul dalam ringkasan evaluasi validation set ini.

## Analisis dan Kendala
- **Analisis hasil:** Model berhasil dilatih selama 50 epoch dan diuji pada video. Prediksi video menunjukkan model dapat mendeteksi `bottle`, `laptop`, dan `pencil`. Hasil pada video tidak berarti semua objek selalu terdeteksi pada setiap frame.
- **Keterbatasan dataset:** Saat training, 3 gambar training diabaikan karena format label mencampurkan anotasi segmentasi dan deteksi. Validation set juga memberikan peringatan terkait format label campuran. Hal ini perlu diperhatikan ketika menafsirkan hasil eksperimen.
- **Kendala dan penyelesaian:** Model dilatih ulang menggunakan Roboflow Version 2 agar nama kelas sesuai ketentuan proyek. File model terbaik dan grafik evaluasi kemudian disalin ke repository submission.
