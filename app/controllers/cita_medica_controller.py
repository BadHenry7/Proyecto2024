import mysql.connector
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.citas_medicas_model import Citasm,Buscar,Reportesss, EditarCita,Chaocita,Upditon
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
  
    def editar_cita(self, cita: EditarCita):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                           
                          SELECT cita.fecha,  cita.hora, usuario.nombre AS nombre_usuario,  paciente.nombre AS nombre_paciente, cita.id   
            FROM cita
            INNER JOIN usuario AS usuario ON cita.id_usuario = usuario.id
            INNER JOIN usuario AS paciente ON cita.id_paciente = paciente.id 
            WHERE cita.id=%s """, (cita.id,))
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                hora_v = str(data[1])
                if len(hora_v) == 7:  # Verificar si la hora tene el formato "H:mm:ss"
                     hora_v = "0" + hora_v 
                content={
                    'fecha':data[0],
                    'hora':hora_v,
                    'medico':data[2],
                    'paciente':data[3],
                    'id':data[4]

                
                }
                print(data[1])
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
    

    def get_cita_admin(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                           
                          SELECT cita.fecha,  cita.hora, usuario.nombre AS nombre_usuario,  paciente.nombre AS nombre_paciente, cita.id   
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
                    'paciente':data[3],
                    'id':data[4]

                
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


    def update_cita(self, cita: Upditon):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
            UPDATE cita
            SET fecha = %s,
            hora = %s,
            id_usuario = %s
            WHERE id = %s
            """,(cita.fecha,cita.hora,cita.id_usuario,cita.id,))
            conn.commit()
           
            return {"resultado": "cita actualizada correctamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()   
       
    def delete_cita(self, cita: Chaocita):
        try: 
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('DELETE FROM cita WHERE id = %s',(cita.id,))
            conn.commit()           
            return {"resultado": "cita eliminada correctamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    
#-------------------------------------------------------Para abajo los reportes--------------------------------------------
    
    def reportes_citas(self, cita: Reportesss):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                           
            SELECT cita.fecha, cita.hora, usuario.nombre AS nombre_usuario,  paciente.nombre AS nombre_paciente     
            FROM cita
            INNER JOIN usuario AS usuario ON cita.id_usuario = usuario.id 
            INNER JOIN usuario AS paciente ON cita.id_paciente = paciente.id 
            WHERE cita.fecha BETWEEN %s AND %s
                           """,(cita.fecha, cita.fecha2))
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
#-------------------------------------------------------Para abajo las estadisticas--------------------------------------------

    def estadisticas_citas(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                           
          SELECT COUNT(c.id_paciente) AS "citas", u.nombre AS "doctor"
            FROM cita c
            JOIN usuario u ON c.id_usuario = u.id
            GROUP BY u.nombre;

                           """,)
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'citas':data[0], 
                    'doctor':data[1], 

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

    def estadisticas2_citas(self):#Estadisticas para saber cuantas citas hay por dia
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""                       
         SELECT  fecha  AS fecha, COUNT(*) AS citas_por_dia
         FROM cita
        GROUP BY fecha  
        ORDER BY fecha 
                           """,)
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'Fecha':data[0], 
                    'citas_dia':data[1], 

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

    def estadisticas3_citas(self):#Estadisticas para saber cuantas citas hay por dia
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SET lc_time_names = 'es_ES'")
            cursor.execute("""                       
    SELECT 
    MONTHNAME(fecha) AS mes, 
    COUNT(*) AS citas_por_mes
    FROM cita
    GROUP BY mes
    ORDER BY fecha
                           """,)
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'Fecha':data[0], 
                    'citas_mes':data[1], 

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


    def estadisticas4_citas(self):#Estadisticas para saber cuantas citas hay por dia
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""                       
        SELECT 
         YEAR(fecha) AS year,
         COUNT(*) AS citas_por_mes
        FROM cita
        GROUP BY  year
        ORDER BY  year
                           """,)
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'Fecha':data[0], 
                    'citas_year':data[1], 

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