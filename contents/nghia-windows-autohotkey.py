import os











# Đường dẫn đến thư mục Startup
startup = os.path.join(os.environ['APPDATA'], r'Microsoft\Windows\Start Menu\Programs\Startup')
print(f"🚀 {startup}")

nghia_ahk_link = os.path.join(startup, "nghia-windows-autohotkey.ahk")
print(f"🚀 {nghia_ahk_link}")

nghia_ahk = os.path.join(os.getcwd(), "nghia-windows-autohotkey.ahk")
print(f"🚀 {nghia_ahk}")




try:
    if os.path.exists(nghia_ahk_link):
        os.remove(nghia_ahk_link)
        print(f"Đã xóa symlink: {nghia_ahk_link}")
    os.symlink(os.path.abspath(nghia_ahk), nghia_ahk_link)
    print(f"Tạo link: {nghia_ahk_link}")
except OSError as e:
    print(f"Lỗi: {e}")
