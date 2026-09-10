# Hệ thống dữ liệu Gốm — Thiết kế cho lưu trữ dài hạn (5–10+ năm)

## Vì sao đổi cấu trúc từ "4 file lớn" sang "mỗi bản ghi 1 file"?

Sau vài năm, `02-bai-phoi-xuong-gom.md` có thể có 200 bài phối, `04-nhat-ky-nung-lo.md` có thể có 500 mẻ nung — một file dài hàng chục ngàn dòng thì:
- Con người khó kéo tìm, dễ sửa nhầm mục khác
- Nếu sau này bạn dùng AI để tìm kiếm/hỏi đáp (RAG — retrieval-augmented generation), AI cần **tách văn bản thành từng đơn vị nhỏ, độc lập** để tìm đúng đoạn liên quan. Một file lớn buộc AI phải tự cắt nhỏ (không chính xác); nhiều file nhỏ, mỗi file là 1 bản ghi hoàn chỉnh, là dữ liệu "sẵn sàng cho AI" mà không cần xử lý thêm.

## Vì sao có phần "frontmatter" (khối `---` ở đầu file)?

```yaml
---
id: X-07
loai: xuong-gom
ngay_tao: 2026-07-15
trang_thai: dang_thu_nghiem
lien_quan: [NL-DAT-01, NL-DAT-02, NL-KH-01]
tags: [do-hut-nuoc-thap, am-tra]
---
```

Đây là phần **máy đọc được**, tách riêng khỏi phần văn xuôi bên dưới. Lợi ích:
- Ngay hôm nay: dùng để lọc/sắp xếp bằng script đơn giản (không cần AI) — vd "liệt kê tất cả bài phối đang thử nghiệm dùng NL-DAT-01"
- 5-10 năm sau: nếu xây AI tìm kiếm, frontmatter trở thành **bộ lọc chính xác** (chỉ tìm trong nhóm "men", chỉ tìm bài "đã xác nhận", chỉ tìm bài liên quan đến 1 nguyên liệu cụ thể) trước khi AI mới "đọc hiểu" nội dung văn xuôi để trả lời — kết hợp 2 lớp này chính là cách các hệ thống AI tìm kiếm hiện đại vận hành (lọc theo metadata + tìm theo ngữ nghĩa).

## Cấu trúc thư mục

```
gom-data/
├── README.md
├── nguyen-lieu/
│   ├── NL-DAT-01.md      ← đất, tro, khoáng — theo từng vùng/nguồn gốc cụ thể
│   ├── NL-TRO-01.md
│   └── ...
├── xuong-gom/
│   ├── X-01.md           ← bài phối đất làm gốm (phối nhiều NL- theo tỷ lệ)
│   └── ...
├── men/
│   ├── M-01.md           ← bài phối men (phối nhiều NL- theo tỷ lệ)
│   └── ...
├── lo-nung/
│   ├── LOK-01.md         ← từng CÁI LÒ cụ thể (củi/gas/điện/kết hợp) — tách khỏi mẻ nung
│   └── ...
├── nung-lo/
│   ├── LO-014.md         ← từng MẺ NUNG cụ thể, tham chiếu lo_id + các bài xương/men
│   └── ...
├── anh/
│   └── LO-014-A1.jpg
└── _scripts/
    └── build_index.py     ← gộp toàn bộ frontmatter thành 1 bảng tra cứu (index.json/csv)
```

**Phân biệt `lo-nung/` (cái lò) và `nung-lo/` (mẻ nung):** một cái lò (vd `LOK-01` — lò củi bầu 3 buồng) được dùng lại qua hàng trăm mẻ nung (`LO-014`, `LO-015`...). Tách riêng để khi bạn thử nghiệm trên lò gas, lò điện, lò kết hợp sau này, dữ liệu "đặc tính của từng lò" (luồng khí, vị trí nóng/lạnh...) không bị lặp lại hoặc trộn lẫn vào từng mẻ nung — và để so sánh được: "cùng công thức men M-01, trên lò củi vs lò gas cho kết quả khác nhau thế nào".

## Quy tắc bắt buộc (giữ nghiêm để không "vỡ" hệ thống sau nhiều năm)

1. **ID không bao giờ đổi, không bao giờ tái sử dụng** — kể cả khi 1 bài phối bị loại bỏ, giữ nguyên ID, chỉ đổi `trang_thai: da_loai_bo`. Việc "xóa và cấp lại ID cũ cho cái khác" là nguyên nhân phổ biến nhất khiến dữ liệu tra cứu sai sau nhiều năm.
2. **Tên file = ID**, không dùng tên mô tả (không đặt `xuong-am-tra-2026.md`, mà đặt `X-07.md`) — tên mô tả để trong frontmatter (`ten:`), tên file để máy tra cứu ổn định.
3. **Mọi liên kết chéo ghi trong `lien_quan:` của frontmatter**, không chỉ nhắc trong văn xuôi — để script/AI sau này lấy được quan hệ mà không cần "đọc hiểu" câu văn.
4. **Ngày tháng theo chuẩn ISO** `YYYY-MM-DD` — tránh nhầm lẫn định dạng ngày/tháng khi dữ liệu đến từ nhiều năm, nhiều người ghi.

## Chạy thử script tổng hợp

```bash
cd gom-data
python3 _scripts/build_index.py
```
Kết quả tạo ra `index.json` và `index.csv` — bảng tổng hợp toàn bộ ID, loại, ngày, trạng thái, liên quan của mọi file. Đây là nền móng dữ liệu để sau này nạp vào bất kỳ hệ thống AI/database nào mà không cần viết lại từ đầu.
