import mysql.connector
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.pago_detalle_model import Pago_detalle
from fastapi.encoders import jsonable_encoder

class pay_detail_Controller:
        
    def create_pay_detalle(self, pago_detalle: Pago_detalle):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO pago_detalle (id_pago,tipo_pago,monto,fecha_pago,estado) VALUES (%s,%s,%s,%s,%s)", (pago_detalle.id_pago,pago_detalle.tipo_pago,pago_detalle.monto, pago_detalle.fecha_pago,pago_detalle.estado,))
            conn.commit()
            conn.close()
            return {"resultado": "Pago añadido correctamente"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    def get_pay_detalle(self, pago_detalle_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM pago_detalle WHERE id = %s", (pago_detalle_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'id_pago':int(result[1]),
                    'tipo_pago':str(result[2]),
                    'monto':float(result[3]),
                    'fecha_pago':str(result[4]),
                    'estado':bool(result[5]),
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="Pago not find")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

       
    def get_pays_detalles(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM pago_detalle")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'id_pago':data[1],
                    'tipo_pago':data[2],
                    'monto':data[3],
                    'fecha_pago':data[4],
                    'estado':data[5],
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Pagos not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()


    def update_pay_detalle(self, pago_detalle_id: int, pago_detalle: Pago_detalle):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
            UPDATE pago_detalle
            SET id_pago = %s,
            tipo_pago = %s,
            monto = %s,
            fecha_pago = %s,
            estado = %s 
            WHERE id = %s
            """,(pago_detalle.id_pago, pago_detalle.tipo_pago, pago_detalle.monto, pago_detalle.fecha_pago, pago_detalle.estado,pago_detalle_id,))
            conn.commit()
           
            return {"resultado": "Pago actualizado correctamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()   

       
    def delete_pay_detalle(self, pago_detalle_id: int):
        try: 
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('DELETE FROM pago_detalle WHERE id = %s',(pago_detalle_id,))
            conn.commit()           
            return {"resultado": "pago eliminado correctamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    