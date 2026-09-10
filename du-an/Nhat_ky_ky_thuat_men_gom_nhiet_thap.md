# NHẬT KÝ KỸ THUẬT — KIỂM SOÁT AN TOÀN MEN GỐM NHIỆT THẤP

Tài liệu này là bản dữ liệu dạng bảng (Markdown), tương ứng với file `Nhat_ky_ky_thuat_men_gom_nhiet_thap.xlsx`, dùng để:
- Lưu trữ dữ liệu dạng văn bản thuần, dễ đọc bởi cả người và công cụ AI/máy
- Dán trực tiếp vào công cụ AI để phân tích, so sánh giữa các mẻ, hoặc hỏi gợi ý điều chỉnh công thức
- Xuất/nhập dễ dàng giữa các hệ thống khác nhau (Excel, Notion, cơ sở dữ liệu...)

**Cách cập nhật:** mỗi lần có mẻ thử mới, thêm một dòng vào bảng tương ứng bên dưới, giữ nguyên thứ tự cột. Không xóa dòng cũ — dữ liệu lịch sử là giá trị cốt lõi để tìm quy luật giữa các mẻ.

---

## 1. Ghi chú vận hành

- Mã mẻ dùng thống nhất giữa Bảng 2 và Bảng 3 (ví dụ: `M001`, `M002`...) để liên kết dữ liệu.
- Cột **% Hấp thụ nước** = (Khối lượng sau ngâm − Khối lượng khô) / Khối lượng khô × 100.
- Cột **Cần gửi kiểm định bên thứ 3?** chỉ ghi "Có" khi mẻ đạt cả: (a) ngưỡng hấp thụ nước, (b) không rạn men sau sốc nhiệt, (c) không đổi màu dung dịch giấm.
- Ngưỡng tham chiếu chì (Pb) theo FDA: đĩa phẳng ≤ 3.0 µg/mL · bát ≤ 1.0 µg/mL · cốc nhỏ ≤ 0.5 µg/mL (tham khảo, cần đối chiếu quy định hiện hành).

---

## 2. Bảng Log mẻ thử — Công thức, đường cong nung & sàng lọc an toàn (Bước 1–4)

| Mã mẻ | Ngày thử | Dòng sản phẩm | Xương | Men | Cone/Nhiệt độ đỉnh (°C) | Tốc độ tăng nhiệt 0–200°C (°C/giờ) | Thời gian giữ nhiệt đỉnh (phút) | Tốc độ làm nguội qua 573°C (°C/giờ) | Bầu không khí lò | B1: Quan sát bề mặt/âm gõ | B2: W1 (g) | B2: W2 (g) | B2: % Hấp thụ nước | B2: Ngưỡng mục tiêu (%) | B2: Đạt ngưỡng xốp? | B3: Rạn men sau sốc nhiệt? | B4: Đổi màu giấm 24h? | B5: Cần gửi kiểm định? | Ghi chú |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| M001 | 2026-09-05 | Đồ dùng hàng ngày | X-04 | M-04 | 1150 | 80 | 30 | 80 | Khử nhẹ | Bề mặt còn sạn do còn để sạn, có lỗ kim khả năng do đất cũ vẫn còn lượng 409 cao, âm gõ đục của xương nhiều sạn | 150.0 | 151.8 | 1.20 | 3.0 | Đạt | Không | Không | Chưa đủ điều kiện gửi kiểm định | Cần giữ nhiệt đỉnh trên 30p đến 1h để men có độ mịn hơn cũng như xương thiêu kết tốt hơn. |
| | | | | | | | | | | | | | | | | | | |

---

## 3. Bảng Kiểm định bên thứ 3 (Bước 5)

| Mã mẻ | Ngày gửi kiểm định | Đơn vị kiểm định | Phương pháp | Hình dạng sản phẩm | Kết quả Pb (µg/mL) | Ngưỡng tham chiếu Pb (µg/mL) | Đạt/Không đạt Pb | Kết quả Cd (µg/mL) | Ngưỡng tham chiếu Cd (µg/mL) | Đạt/Không đạt Cd | Kết luận cuối cùng | Ghi chú |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| M001 | 2026-09-15 | Quatest 3 | FDA acetic acid method | Bát | 0.42 | 1.0 | Đạt | 0.05 | 0.5 | Đạt | AN TOÀN – có thể công bố | Kết quả nằm trong ngưỡng tham chiếu FDA cho bát. |
| | | | | | | | | | | | | |

---

## 4. Bảng tham chiếu ngưỡng Pb theo hình dạng sản phẩm (FDA)

| Hình dạng sản phẩm | Ngưỡng Pb (µg/mL) |
|---|---|
| Đĩa phẳng | 3.0 |
| Bát | 1.0 |
| Cốc nhỏ | 0.5 |

---

*Khi dùng file này với công cụ AI để phân tích: có thể dán nguyên Bảng 2 hoặc Bảng 3 kèm câu hỏi cụ thể (ví dụ "so sánh % hấp thụ nước giữa các mẻ có tỷ lệ tro gỗ khác nhau" hoặc "mẻ nào có nguy cơ chưa gửi kiểm định nhưng đã đủ điều kiện") để nhận phân tích chính xác hơn.*
