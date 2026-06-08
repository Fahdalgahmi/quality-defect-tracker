from fastapi import FastAPI
from dotenv import load_dotenv
import psycopg2
import os
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_connection():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

@app.get("/")
def home():
    return {"message": "Quality Defect Tracker API Running"}

@app.get("/test-db")
def test_db():
    try:
        conn = get_connection()
        conn.close()
        return {"status": "Database Connected Successfully"}
    except Exception as e:
        return {"error": str(e)}



class Defect(BaseModel):
    defect_date: str
    shift: str
    part_number: str
    machine: str | None = None
    defect_type: str
    quantity: int
    severity: str | None = None
    root_cause: str | None = None
    corrective_action: str | None = None
    status: str = "Open"
    comments: str | None = None


@app.post("/defects")
def add_defect(defect: Defect):
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO defects (
                defect_date, shift, part_number, machine, defect_type,
                quantity, severity, root_cause, corrective_action, status, comments
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING defect_id;
        """, (
            defect.defect_date,
            defect.shift,
            defect.part_number,
            defect.machine,
            defect.defect_type,
            defect.quantity,
            defect.severity,
            defect.root_cause,
            defect.corrective_action,
            defect.status,
            defect.comments
        ))

        defect_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()

        return {"message": "Defect added successfully", "defect_id": defect_id}

    except Exception as e:
        return {"error": str(e)}
    
@app.get("/defects")
def get_defects():
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT *
            FROM defects
            ORDER BY defect_id DESC
        """)

        rows = cur.fetchall()

        defects = []

        for row in rows:
            defects.append({
                "defect_id": row[0],
                "defect_date": row[1],
                "shift": row[2],
                "part_number": row[3],
                "machine": row[4],
                "defect_type": row[5],
                "quantity": row[6],
                "severity": row[7],
                "root_cause": row[8],
                "corrective_action": row[9],
                "status": row[10],
                "comments": row[11]
            })

        cur.close()
        conn.close()

        return defects

    except Exception as e:
        return {"error": str(e)}
    

@app.put("/defects/{defect_id}/status")
def update_defect_status(defect_id: int, status: str):
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            UPDATE defects
            SET status = %s
            WHERE defect_id = %s
            RETURNING defect_id;
        """, (status, defect_id))

        updated = cur.fetchone()

        conn.commit()
        cur.close()
        conn.close()

        if updated:
            return {"message": "Status updated successfully"}
        else:
            return {"error": "Defect not found"}

    except Exception as e:
        return {"error": str(e)}
    

@app.delete("/defects/{defect_id}")
def delete_defect(defect_id: int):
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            DELETE FROM defects
            WHERE defect_id = %s
            RETURNING defect_id;
        """, (defect_id,))

        deleted = cur.fetchone()

        conn.commit()
        cur.close()
        conn.close()

        if deleted:
            return {"message": "Defect deleted successfully"}
        else:
            return {"error": "Defect not found"}

    except Exception as e:
        return {"error": str(e)}