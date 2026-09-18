from fastapi import FastAPI,HTTPException
from data import applications
import uvicorn
from pydantic import BaseModel,EmailStr,HttpUrl
from data import applications
from typing import Literal


class Application(BaseModel):
    fullName: str
    email: EmailStr
    phone: str
    whatsappNumber: str
    university: str
    course: str
    level: str
    track: str
    motivation: str
    portfolioLink: HttpUrl
    resumeLink: HttpUrl
    joinInnovationClub: bool
    status: Literal["pending", "accepted", "rejected"]

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/applications")
def get_applications():
    return applications


@app.get("/applications/{application_id}")
def get_application(application_id: int):
    for application in applications:
        if application["id"] == application_id:
            return application

    raise HTTPException(status_code=404, detail="Application not found")

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=False)

@app.post("/applications", status_code=201)
def create_application(application: Application):
    if applications:
        new_id = max(application["id"] for application in applications) + 1
    else:
     new_id = 1

    new_application = application.model_dump()
    new_application["id"] = new_id

    applications.append(new_application)

    return new_application

@app.put("/applications/{application_id}")
def update_application(application_id: int, application: Application):
    for index, existing_application in enumerate(applications):
        if existing_application["id"] == application_id:
            updated_application = application.model_dump()
            updated_application["id"] = application_id

            applications[index] = updated_application

            return updated_application

    raise HTTPException(status_code=404, detail="Application not found")


@app.delete("/applications/{application_id}")
def delete_application(application_id: int):
    for index, application in enumerate(applications):
        if application["id"] == application_id:
            deleted_application = applications.pop(index)
            return {
                "message": "Application deleted successfully",
                "application": deleted_application
            }

    raise HTTPException(status_code=404, detail="Application not found")









if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=False)
    input("Press Enter to stop the server...") # Forces Windows to keep the process alive
