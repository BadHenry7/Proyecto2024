import mysql.connector
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.citas_medicas_model import Citasm,Buscar
from fastapi.encoders import jsonable_encoder
from datetime import timedelta
class citaController:
        
    def create_cita(self, cita: Citasm):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO cita (fecha,hora,estado,id_usuario,id_paciente) VALUES (%s,%s,%s,%s,%s)", (cita.fecha,cita.hora,cita.estado,cita.id_usuario,cita.id_paciente))
            conn.commit()
            conn.close()
            return {"resultado": "Cita añadida correctamente"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    def get_cita(self, cita_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM cita WHERE id = %s", (cita_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'fecha':str(result[1]),
                    'hora':str(result[2]),
                    'estado':bool(result[3]),
                    'id_usuario':int(result[4]),
                    'id_paciente':int(result[5])
                  
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="cita not find")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
  #SELECT  nombre  FROM cita INNER JOIN usuario ON cita.id_usuario = usuario.id     
    """def get_citas(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM cita")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'fecha':data[1],
                    'hora':data[2],
                    'estado':data[3],
                    'id_usuario':data[4],
                    'id_paciente':data[5],
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="citas not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()"""
    

    def get_citas(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                           
                          SELECT cita.fecha,  cita.hora,  usuario.nombre AS nombre_usuario,  paciente.nombre AS nombre_paciente     
            FROM cita
            INNER JOIN usuario AS usuario ON cita.id_usuario = usuario.id
            INNER JOIN usuario AS paciente ON cita.id_paciente = paciente.id
                           
                           
                           """)
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'fecha':data[0],
                    'hora':str(data[1]),
                    'medico':data[2],
                    'paciente':data[3]
                
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
               
            else:
                raise HTTPException(status_code=404, detail="citas not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def post_citas_users(self, cita: Buscar):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(""" 
                           
                           SELECT cita.fecha,  cita.hora,  usuario.nombre AS nombre_usuario,  paciente.nombre AS nombre_paciente     
                            FROM cita
                             INNER JOIN usuario AS usuario ON cita.id_usuario = usuario.id
                             INNER JOIN usuario AS paciente ON cita.id_paciente = paciente.id WHERE 
                            cita.id_paciente =%s
                           
                           """,(cita.id_paciente,))
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'fecha':data[0],
                    'hora':str(data[1]),
                    'medico':data[2],
                    'paciente':data[3]
                
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
               
            else:
                raise HTTPException(status_code=404, detail="citas not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()        


    def update_cita(self, cita: Citasm):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
            UPDATE cita
            SET fecha = %s,
            hora = %s,
            estado = %s,
            id_usuario = %s,
            id_paciente=%s
            WHERE id = %s
            """,(cita.fecha,cita.hora,cita.estado,cita.id_usuario,cita.id_paciente,))
            conn.commit()
           
            return {"resultado": "cita actualizada correctamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()   
       
    def delete_cita(self, cita_id: int):
        try: 
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('DELETE FROM cita WHERE id = %s',(cita_id,))
            conn.commit()           
            return {"resultado": "cita eliminada correctamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    