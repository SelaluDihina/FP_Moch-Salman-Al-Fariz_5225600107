
from pathlib import Path
import argparse

from ultralytics import YOLO


def main():
    parser = argparse.ArgumentParser(
        description="Deteksi botol plastik, pensil, dan laptop menggunakan model YOLOv8."
    )
    parser.add_argument(
        "--source",
        required=True,
        help="Path gambar atau video yang ingin diuji."
    )
    parser.add_argument(
        "--conf",
        type=float,
        default=0.25,
        help="Batas confidence prediksi (default: 0.25)."
    )
    args = parser.parse_args()

    model_path = Path(__file__).resolve().parent / "best.pt"

    if not model_path.exists():
        raise FileNotFoundError(f"Model tidak ditemukan: {model_path}")

    source = Path(args.source)
    if not source.exists():
        raise FileNotFoundError(f"File input tidak ditemukan: {source}")

    model = YOLO(str(model_path))

    model.predict(
        source=str(source),
        conf=args.conf,
        imgsz=640,
        save=True,
        project="hasil_prediksi",
        name="demo",
        exist_ok=True
    )

    print("Selesai! Hasil deteksi tersimpan di folder hasil_prediksi/demo/")


if __name__ == "__main__":
    main()
