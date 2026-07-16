#!/usr/bin/env python3
"""
build_index.py
Quét toàn bộ file .md trong gom-data/ (trừ các file _template.md),
đọc phần frontmatter (khối --- ở đầu file) và gộp thành:
  - index.json  (dùng cho script/AI sau này)
  - index.csv   (dùng để mở nhanh bằng Excel/Google Sheets)

Không cần cài thư viện ngoài (không cần pip install pyyaml).
Chạy: python3 _scripts/build_index.py
"""

import os
import re
import json
import csv

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FOLDERS = ["nguyen-lieu", "xuong-gom", "men", "nung-lo"]


def parse_frontmatter(text):
    """Tách khối frontmatter --- ... --- và parse dạng key: value đơn giản."""
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return {}, text
    fm_raw = match.group(1)
    body = text[match.end():]

    data = {}
    for line in fm_raw.splitlines():
        line = line.rstrip()
        if not line.strip() or line.strip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()

        # Danh sách dạng [a, b, c]
        if value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            items = [v.strip().strip('"').strip("'") for v in inner.split(",") if v.strip()]
            data[key] = items
        else:
            data[key] = value.strip('"').strip("'")
    return data, body


def collect_records():
    records = []
    for folder in FOLDERS:
        folder_path = os.path.join(ROOT, folder)
        if not os.path.isdir(folder_path):
            continue
        for fname in sorted(os.listdir(folder_path)):
            if not fname.endswith(".md") or fname.startswith("_"):
                continue
            fpath = os.path.join(folder_path, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                text = f.read()
            meta, _ = parse_frontmatter(text)
            if not meta:
                print(f"⚠️  Bỏ qua (không có frontmatter hợp lệ): {fpath}")
                continue
            meta["_file"] = os.path.relpath(fpath, ROOT)
            records.append(meta)
    return records


def write_json(records, out_path):
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)


def write_csv(records, out_path):
    # Gộp tất cả các key xuất hiện để làm cột, giữ thứ tự ưu tiên các cột chính trước
    priority = ["id", "loai", "ten", "nhom", "trang_thai", "ngay", "ngay_tao", "ngay_lay_mau", "lien_quan", "tags", "_file"]
    all_keys = set()
    for r in records:
        all_keys.update(r.keys())
    ordered_keys = [k for k in priority if k in all_keys] + sorted(all_keys - set(priority))

    with open(out_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=ordered_keys)
        writer.writeheader()
        for r in records:
            row = {}
            for k in ordered_keys:
                v = r.get(k, "")
                if isinstance(v, list):
                    v = "; ".join(v)
                row[k] = v
            writer.writerow(row)


def main():
    records = collect_records()
    if not records:
        print("Không tìm thấy bản ghi nào. Hãy tạo file từ _template.md trong mỗi thư mục trước.")
        return

    json_path = os.path.join(ROOT, "index.json")
    csv_path = os.path.join(ROOT, "index.csv")
    write_json(records, json_path)
    write_csv(records, csv_path)

    print(f"✅ Đã tổng hợp {len(records)} bản ghi.")
    print(f"   → {json_path}")
    print(f"   → {csv_path}")

    # Cảnh báo ID trùng lặp — lỗi phổ biến nhất khi dữ liệu tăng theo năm tháng
    seen = {}
    for r in records:
        rid = r.get("id")
        if not rid:
            continue
        if rid in seen:
            print(f"🚨 CẢNH BÁO: ID trùng lặp '{rid}' — trong {seen[rid]} và {r['_file']}")
        seen[rid] = r["_file"]


if __name__ == "__main__":
    main()
