import instaloader

def download_multiple_reels_from_file(file_path):
    # Instaloader'ı başlat
    L = instaloader.Instaloader()
    
    # Dosyadan linkleri oku
    with open(file_path, "r") as file:
        video_links = file.readlines()
    
    # Linkleri işleme
    for video_link in video_links:
        video_link = video_link.strip()  # Boşlukları temizle
        try:
            # Video bağlantısından shortcode çıkar
            shortcode = video_link.split("/")[-2]
            
            # Video postunu al
            post = instaloader.Post.from_shortcode(L.context, shortcode)
            
            # Videoyu indirme
            L.download_post(post, target='downloads')
            print(f"Video {video_link} başarıyla indirildi!")
        except Exception as e:
            print(f"Video {video_link} indirilirken hata oluştu: {e}")

# 'links.txt' dosyasından linkleri oku
download_multiple_reels_from_file("links.txt")
