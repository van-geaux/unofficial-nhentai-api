# 🏴‍☠️ Unofficial NHentai API

Welcome to the **Unofficial NHentai API**—a project I made out of boredom. **Use it responsibly.**

🔄 **Updated Daily:** Data is refreshed every day but will always be **one day behind** the latest content.

---

## 🐂 Short Description
This API provides structured NHentai metadata, including titles, artist names, categories, and tags. It is updated daily, offering a snapshot of the available content as of the previous day.

---

## 📂 Database & CSV
- 📁 CSV files are available in the `by_month` folder.
- 🗄️ To get the SQLite database:
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

## 📡 API Documentation
Base URL: `https://nhapi.geaux.id`

### 🔍 Search & Filter Endpoints

#### Get Item by ID
**Endpoint:**
```http
GET /id/{item_id}
```
**Example:**
```http
GET /id/123456
```
**Response:**
```json
{
  "ID": 123456,
  "EN_TITLE": "Example Title",
  "JP_TITLE": "サンプルタイトル",
  "CLEAN_TITLE": "Example Title",
  "LANGUAGE": "English",
  "ARTIST": "Artist Name",
  "GROUP_NAME": "Doujin Group",
  "CATEGORY": "Manga",
  "PARODY": "Parody Name",
  "CHARACTER": "Character Name",
  "TAGS": "tag1, tag2, tag3",
  "PAGES": 32,
  "UPLOAD_DATE": "2025-03-01"
}
```

#### Search by Filters
You can apply multiple filters using query parameters:
```http
GET /search?parody=evangelion&character=ritsuko&artist=someartist&tags=mature&limit=10&offset=0
```

**Query Parameters:**
- `parody` (optional) - Filter by parody title
- `character` (optional) - Filter by character name
- `artist` (optional) - Filter by artist name
- `tags` (optional) - Filter by tags (comma-separated)
- `limit` (optional) - Number of results per request (default: 10, max: 100)
- `offset` (optional) - Pagination offset (default: 0)

**Example Response:**
```json
{
  "items": [
    {
      "ID": 123456,
      "EN_TITLE": "Example Title",
      "CATEGORY": "Manga",
      "PARODY": "Evangelion",
      "CHARACTER": "Ritsuko",
      "ARTIST": "SomeArtist",
      "TAGS": "mature, sci-fi",
      "PAGES": 32,
      "UPLOAD_DATE": "2025-03-01"
    }
  ],
  "limit": 10,
  "offset": 0
}
```

---

## ⚠️ Disclaimer
💡 This project is **unofficial** and provided **as-is** with no guarantees. Use at your own discretion.

