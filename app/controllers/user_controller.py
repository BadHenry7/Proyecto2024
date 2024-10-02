import mysql.connector
from fastapi import HTTPException, UploadFile
from app.config.db_config import get_db_connection
from app.models.user_model import User
from fastapi.encoders import jsonable_encoder
from typing import List
import pandas as pd

class UserController:
        
    
    
    def create_user(self, user: User):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO usuario (usuario,password,nombre,apellido,documento,telefono,id_rol,estado) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (user.usuario,user.password,user.nombre,user.apellido,user.documento,user.telefono,user.id_rol,user.estado))
            conn.commit()
            conn.close()
            return {"resultado": "Usuario creado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    
    def create_user_masivo(self, file: UploadFile):
        conn = None
        try:
            # Leer el archivo Excel
            df = pd.read_excel(file.file, engine='openpyxl')

            required_columns = ['usuario', 'password', 'nombre', 'apellido', 'documento', 'telefono', 'id_rol', 'estado']
            for col in required_columns:
                if col not in df.columns:
                    return {"error": f"Falta la columna: {col}"}
            
            # Conectar a la base de datos
            conn = get_db_connection()
            cursor = conn.cursor()

            for index, row in df.iterrows():
                cursor.execute(
                    "INSERT INTO usuario (usuario,password,nombre,apellido,documento,telefono,id_rol,estado) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                    (row['usuario'], row['password'], row['nombre'], row['apellido'], row['documento'], row['telefono'], row['id_rol'], row['estado'])
                )
            
            conn.commit()  # Hacer commit después de todas las inserciones
            return {"resultado": "Users creados exitosamente"}
        except mysql.connector.Error as err:
            if conn:
                conn.rollback()  # Asegúrate de que conn esté definido
            return {"error": str(err)}
        except Exception as e:
            if conn:
                conn.rollback()
            return {"error": f"Un error inesperado ocurrió: {str(e)}"}
        finally:
            if conn:
                conn.close()

    

    def get_user(self, user_id: int):
        
        try:
            
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuario WHERE id = %s", (user_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'usuario':result[1],
                    'password':result[2],
                    'nombre':result[3],
                    'apellido':result[4],
                    'documento':result[5],
                    'telefono':result[6],
                    'id_rol':int(result[7]),
                    'estado':bool(result[8]),
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="User not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
       

    def get_users(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuario")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'usuario':data[1],
                    'password':data[2],
                    'nombre':data[3],
                    'apellido':data[4],
                    'documento':data[5],
                    'telefono':data[6],
                    'id_rol':data[7],
                    'estado':data[8]
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="User not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
  
    
    def update_user(self, user_id: int, user: User):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
            UPDATE usuario
            SET usuario = %s,
            password = %s,
            nombre=%s,
            apellido = %s,
            documento=%s,
            telefono=%s,    
            estado= %s                 
            WHERE id = %s
            """,(user.usuario,user.password,user.nombre,user.apellido,user.documento,user.telefono,user.estado,user_id,))
            conn.commit()
           
            return {"resultado": "Usuario actualizado correctamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()    
       
    def delete_user(self, user_id: int):
        try: 
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('DELETE FROM usuario WHERE id = %s',(user_id,))
            conn.commit()           
            return {"resultado": "Usuario eliminado correctamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()




            
##user_controller = UserController()


#AFK