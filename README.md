# AI Image Analyzer & Organizer

A FastAPI-based tool that analyzes images using OpenAI GPT-4o-mini Vision and automatically saves them into organized folders based on their content.

---

## What It Does

1. **Analyzes** — Sends the image to GPT-4o-mini Vision and gets back a description, category, and 3-word summary
2. **Organizes** — Saves the image into a subfolder named after its category with a meaningful filename using 3-word summary

For example, upload a random photo called `IMG_3847.jpg` and it gets saved as:
```
uploads/
└── nature/
    └── IMG_3847_green_forest_trees.jpg
```

---

## Tech Stack

- **FastAPI** — API framework
- **OpenAI GPT-4o-mini Vision** — Image analysis
- **Pydantic** — Data validation & structured responses
- **Python 3.11+**

---

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/ahmad-al-jolani/ai-image-analyzer-organizer.git
cd ai-image-analyzer-organizer
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables

```bash
cp .env.example .env
```

Then open `.env` and fill in your values:

```env
APP_NAME=AI Image Analyzer & Organizer
APP_VERSION=1.0.0
IMAGE_TYPE=["image/jpeg", "image/png"]
IMAGE_SIZE=5242880
OPENAI_API_KEY=your_openai_api_key_here
```

### 4. Run the server

```bash
uvicorn main:app --reload
```

API will be running at `http://localhost:8000`

---

## API Endpoints

### `GET /health/`
Health check — confirms the app is running.

**Response:**
```json
{
    "status": "UP",
    "app_name": "AI Image Analyzer & Organizer",
    "app_version": "1.0.0"
}
```

---

### `POST /upload/`
Upload an image to analyze and organize.

**Request:** `multipart/form-data` with a `file` field.

**Response:**
```json
{
  "description": "A golden retriever playing in a green park",
  "category": "animals",
  "summary": "dog park play",
  "save_status": [
    "image save successfully to: /uploads/animals",
    "Image saved with this name: IMG_3847_dog_park_play.jpg"
  ]
}
```

**Validation rules:**
- Accepted formats: `image/jpeg`, `image/png` (configurable)
- Max file size: 5MB (configurable)

---

## Notes

- The tool processes **one image at a time**
- Uploaded images are saved to the `uploads/` folder at the project root, organized into subfolders by category
- Subfolders are created automatically if they don't exist

---
