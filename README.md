# 🏴‍☠️ Unofficial NHentai Database

Welcome to the **unofficial** NHentai database—a project I made out of boredom. **Use it responsibly.**

🔄 **Updated Daily:** Data is refreshed every day but will always be **one day behind** the latest content.

---

## 🐂 Short Description
This database provides structured NHentai metadata, including titles, artist names, categories, and tags. It is updated daily, offering a snapshot of the available content as of the previous day.

---

## 📂 Contents
📁 CSV files are available in the `by_month` folder.

🗄️ To get the SQLite database:
1. Run `merge_database.py` to combine the split parts.
2. The merged database, `database_merged.db`, will be available in the `backend` folder.

---

## 📊 Data Coverage
🚀 Scraping began on **28 February 2025**, meaning older purged content is **not included**.

📥 If you have the missing data:
- Please **open an issue** or submit a **pull request**, and I'll add it.
- If you find incorrect data, report it by opening an issue.

📝 **Wayback Machine Data:**
- For missing content from the purge, I have supplemented the database using **Wayback Machine** data where available.
- However, these entries are **often missing the upload date**.
- As such, they **won't appear in the monthly CSV** exports. You will need the **SQLite database** to access the complete data.

---

## 📝 Available Fields
- **ID**: NHentai identifier  
- **EN_TITLE**: English title  
- **JP_TITLE**: Japanese title  
- **CLEAN_TITLE**: Clean English title  
- **LANGUAGE**: Language of the content  
- **ARTIST**: Artist(s) involved  
- **GROUP_NAME**: Doujinshi circle or group  
- **CATEGORY**: Main category (e.g., Doujinshi, Manga)  
- **PARODY**: Parodied works  
- **CHARACTER**: Characters featured  
- **TAGS**: Associated tags  
- **PAGES**: Number of pages  
- **UPLOAD_DATE**: Date of upload  

---

## ⚠️ Disclaimer
💡 This project is **unofficial** and provided **as-is** with no guarantees. Use at your own discretion.
