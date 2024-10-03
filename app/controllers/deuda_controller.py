import mysql.connector
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.deuda_model import Deuda
from fastapi.encoders import jsonable_encoder

class debtController:
        
    def create_debt(self, deuda: Deuda):   #

        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO deuda (id_usuario,monto_total,monto_pagado,saldo_restante,descripcion,fecha_deuda,estado) VALUES (%s,%s,%s,%s,%s,%s,%s)", (deuda.id_usuario, deuda.monto_total, deuda.monto_pagado,deuda.saldo_restante,deuda.descripcion,deuda.fecha_deuda,deuda.estado,))
            conn.commit()
            conn.close()
            return {"resultado": "deuda generada correctamente"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    def get_debt(self, deuda_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM deuda WHERE id = %s", (deuda_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'id_usuario':int(result[1]),
                    'monto_total':float(result[2]),
                    'monto_pagado':float(result[3]),
                    'saldo_restante':float(result[4]),
                    'descripcion':str(result[5]),
                    'fecha_deuda':str(result[6]),
                    'estado':bool(result[7])
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="deuda not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
       
    def get_debts(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM deuda")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'id_usuario':data[1],
                    'monto_total':data[2],
                    'monto_pagado':data[3],
                    'saldo_restante':data[4],
                    'descripcion':data[5],
                    'fecha_deuda':data[6],
                    'estado':data[7],
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="deudas not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()


    def update_debts(self, deuda_id: int, deuda: Deuda):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
            UPDATE deuda
            SET id_usuario = %s,
            monto_total = %s,
            monto_pagado = %s,
            saldo_restante = %s,
            descripcion = %s ,
            fecha_deuda = %s,
            estado = %s
            WHERE id = %s
            """,(deuda.id_usuario, deuda.monto_total, deuda.monto_pagado, deuda.saldo_restante,deuda.descripcion,deuda.fecha_deuda,deuda.estado,deuda_id,))
            conn.commit()
           
            return {"resultado": "Deuda actualizada correctamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()   
       
    def delete_debts(self, deuda_id: int):
        try: 
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('DELETE FROM deuda WHERE id = %s',(deuda_id,))
            conn.commit()           
            return {"resultado": "Deuda eliminada correctamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    