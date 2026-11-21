import csv
import requests

LABEL_STUDIO_URL = "http://localhost:8080"
API_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6ODEwMjQ3MDE1MSwiaWF0IjoxNzk1MjcwMTUxLCJqdGkiOiJlNGNkOGNlY2IzNzg0M2NlOTc5YjcxNmNmOTBlOTUxNiIsInVzZXJfaWQiOiIxIn0.JsUCphC8QD5HFMxu_EhEvGKQkjMQaZKAOEq52fOcbQ8"
PROJECT_ID = 5
CSV_FILE = "deneme.csv"
TEXT_COLUMN = "text"

def get_auth_header(token):
    if token.startswith("eyJ"):
        res = requests.post(
            f"{LABEL_STUDIO_URL}/api/token/refresh",
            json={"refresh": token}
        )
        if res.status_code == 200:
            access_token = res.json().get("access")
            return {"Authorization": f"Bearer {access_token}"}
    return {"Authorization": f"Token {token}"}

def import_csv_to_label_studio():
    tasks = []
    with open(CSV_FILE, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            sms_text = row.get(TEXT_COLUMN, "").strip()
            if sms_text:
                tasks.append({"data": {"text": sms_text}})

    if not tasks:
        print("Hata: CSV dosyasinda yuklenecek SMS bulunamadi.")
        return

    headers = get_auth_header(API_TOKEN)
    headers["Content-Type"] = "application/json"

    url = f"{LABEL_STUDIO_URL}/api/projects/{PROJECT_ID}/import"
    response = requests.post(url, headers=headers, json=tasks)

    if response.status_code in (200, 201):
        print(f"Basarili! {len(tasks)} adet SMS, Proje #{PROJECT_ID} icine aktarildi.")
    else:
        print(f"Hata olustu! Durum kodu: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    import_csv_to_label_studio()