from fastapi import FastAPI, File, UploadFile
import easyocr

easyocr_reader_ru = easyocr.Reader(['ru'])
easyocr_reader_en = easyocr.Reader(['en'])


app = FastAPI()


@app.get("/info/")
async def info():
    return "ok"

        
@app.post("/upload")
def upload(file: UploadFile = File(...)):
    try:
        text_ru = easyocr_reader_ru.readtext(file.file.read())
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()
    
    return {"message": ' '.join([x[1] for x in text_ru])}


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=os.getenv("PORT", 8000))