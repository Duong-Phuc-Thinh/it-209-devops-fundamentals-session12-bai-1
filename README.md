# Quy trình CI đa phiên bản JDK (Matrix Strategy) cho Java Spring Boot Gradle

Thư mục này chứa cấu hình GitHub Actions CI triển khai Ma trận kiểm thử (Matrix Strategy) cho dự án Java Spring Boot Gradle.

## Chức năng đã thực hiện
1. **Kích hoạt Workflow**: Chạy tự động khi có sự kiện `push` lên nhánh `main`.
2. **Matrix Strategy**: Định nghĩa ma trận kiểm thử chạy song song trên 2 phiên bản JDK: `17` và `21`.
3. **Cấu hình JDK & Caching**: Sử dụng `actions/setup-java@v5` với nhà phân phối `temurin` và bật tính năng cache Gradle (`cache: 'gradle'`) giúp tối ưu thời gian build.
4. **Kiểm thử tự động**: Cấp quyền thực thi cho `./gradlew` và chạy `./gradlew test`.
5. **Script kiểm tra bằng Python**: Chạy `main.py` để kiểm tra tính hợp lệ của file cấu hình `.github/workflows/ci-matrix.yml`.

## Hướng dẫn chạy kiểm tra

Để chạy script Python kiểm tra định dạng workflow:
```bash
python main.py
```
