from db_clean import *
import pandas as pd
import re
from underthesea import word_tokenize

init_db1("../../data/database/youtube_comments_clean.db")


# Kết nối DB1 + DB2
conn_raw = sqlite3.connect("../../data/database/youtube_comments.db")
conn_clean = sqlite3.connect("../../data/database/youtube_comments_clean.db")
abbrev_dict = {
    "ae": "anh em",
    "ak": "anh không",
    "ace": "anh chị em",
    "ad": "admin",
    "add": "thêm",
    "adr": "à được rồi",
    "app": "ứng dụng",
    "atr": "anime",
    "auth": "xác thực",

    "b": "bạn",
    "bg": "background",
    "bjo": "bao giờ",
    "bn": "bao nhiêu",
    "bt": "bình thường",
    "bthg": "bình thường",
    "bth": "bình thường",
    "bik": "biết",
    "bít": "biết",
    "bl": "bình luận",
    "blv": "bình luận viên",
    "bro": "bạn bè",

    "c": "cũng",
    "cc": "có cần",
    "ch": "chưa",
    "cj": "chị",
    "ck": "chồng",
    "cl": "chất lượng",
    "cmnr": "chuẩn ",
    "cmnl": "chuẩn ",
    "cm": "comment",
    "cmsn": "chúc mừng sinh nhật",
    "cmt": "bình luận",
    "cr": "crush",

    "dc": "được",
    "đc": "được",
    "dk": "được không",
    "đk": "được không",
    "dm": "đi mà",
    "đm": "đi mà",
    "dth": "dễ thương",

    "fb": "facebook",
    "ib": "inbox",
    "inb": "inbox",

    "k": "không",
    "kh": "không",
    "khum": "không",
    "hok": "không",
    "kp": "không phải",
    "ko": "không",
    "kbt": "không biết",
    "kq": "kết quả",
    "mn": "mọi người",
}
stopwords = set([
    "và", "của", "là", "có", "cho", "một", "nhưng", "đã", "này", "đó",
    "rằng", "nếu", "thì", "để", "với", "trong", "làm", "ra", "được",
    "ở", "các", "khi", "vậy", "đang", "tôi", "anh", "chị", "em"
])

def mo_rong_tu(words):
    return [abbrev_dict.get(w, w) for w in words]
def clean_text(text):
    # chuyển về cữ thường
    text = text.lower()

    # xóa url , mentions , hashtags
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"#\w+", "", text)

    # xóa ký tự đặc biệt , số
    text = re.sub(r"[^a-zA-ZÀ-ỹ\s]", " ", text)
    text = re.sub(r"\d+", " ", text)

    # xóa khoảng trắng thừa
    text = re.sub(r"\s+", " ", text).strip()

    # loại bỏ kí tự kéo dài chữ
    text = re.sub(r'(.)\1+', r'\1\1', text)

    # xóa teencode
    text = re.sub(r"(:v|:3|:vv+|=+\)+|:+\(+|:D+|:P+|:O+|:\/+)", " ", text)

    # tách từ chuẩn tiếng việt
    words = word_tokenize(text)

    # mở rộng từ viết tắt
    words = mo_rong_tu(words)

    # Xóa stopwords
    words = [w for w in words if w not in stopwords]

    # ghép lại câu
    return " ".join(words)


BATCH_SIZE = 50000
offset = 0

while True:
    # Load batch
    query = f"""
        SELECT *
        FROM comments
        LIMIT {BATCH_SIZE} OFFSET {offset}
    """
    data = pd.read_sql_query(query, conn_raw)

    # Nếu hết dữ liệu thì dừng
    if data.empty:
        print("DONE!")
        break

    print(f"Processing batch: offset={offset} size={len(data)}")

    # Xử lý dữ liệu
    data["clean_text"] = data["text"].apply(clean_text)
    data = data.drop(columns=["text"])

    # Ghi sang DB2
    data.to_sql("comments_clean", conn_clean, if_exists="append", index=False)

    offset += BATCH_SIZE

# Close
conn_raw.close()
conn_clean.close()
