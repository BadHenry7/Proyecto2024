import mysql.connector
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.diagnosticos_model import Diagnosticos
from fastapi.encoders import jsonable_encoder

class diagnosticoController:
        
    def create_diagnosticos(self, diagnosticos: Diagnosticos):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO diagnosticos (id_usuario,resultado,fecha_diagnostico,estado) VALUES (%s,%s,%s,%s)", (diagnosticos.id_usuario, diagnosticos.resultado, diagnosticos.fecha_diagnostico,diagnosticos.estado,))
            conn.commit()
            conn.close()
            return {"resultado": "diagnosticos añadida correctamente"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    def get_diagnostico(self, diagnosticos_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM diagnosticos WHERE id = %s", (diagnosticos_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'id_usuario':int(result[1]),
                    'resultado':str(result[2]),
                    'fecha_diagnostico':str(result[3]),
                    'estado':bool(result[4]),
                  
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="diagnostico not find")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
       
    def get_diagnosticos(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM diagnosticos")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'id_usuario':data[1],
                    'resultado':data[2],
                    'fecha_diagnostico':data[3],
                    'estado':data[4],
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="diagnosticos not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()


    def update_diagnosticos(self, diagnosticos_id: int, diagnosticos: Diagnosticos):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
            UPDATE diagnosticos
            SET id_usuario = %s,
            resultado = %s,
            fecha_diagnostico = %s,
            estado = %s 
            WHERE id = %s
            """,(diagnosticos.id_usuario, diagnosticos.resultado, diagnosticos.fecha_diagnostico,diagnosticos.estado,diagnosticos_id,))
            conn.commit()
           
            return {"resultado": "Diagnosticos actualizado correctamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()   
       
    def delete_diagnosticos(self, diagnosticos_id: int):
        try: 
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('DELETE FROM diagnosticos WHERE id = %s',(diagnosticos_id,))
            conn.commit()           
            return {"resultado": "Diagnosticos eliminado correctamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    