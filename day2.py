from fastapi import FastAPI,HTTPException


app=FastAPI()

customer_data=[{
  
  "booking_id": "abc123efg456",
  "customer_name": "Hemanth",
  "service": "ac repair",
  "booking_date": "2026-11-05",
  "booking_time": "10:00"
}]

@app.get("/booking/{booking_id}")
async def get_details(booking_id:str):
    try:
     for booking in customer_data:
        if booking["booking_id"]==booking_id:
           return {"message":"Booking found succesfully","data":booking}
     raise HTTPException(status_code=404,detail="invalid booking id")

    except HTTPException as e:
       raise e

    except Exception as e:
       print(e)
       raise HTTPException(status_code=500,detail="internal error")
       



