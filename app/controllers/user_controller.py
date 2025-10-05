import mysql.connector
from fastapi import HTTPException, UploadFile
from app.config.db_config import get_db_connection
from app.models.user_model import *
from fastapi.encoders import jsonable_encoder

from typing import List
import pandas as pd
import cv2
import mediapipe as mp
import base64
import numpy as np
from fastapi.responses import HTMLResponse, StreamingResponse

from pwdlib import PasswordHash
password_hash = PasswordHash.recommended()


class UserController:
    # def verify_password(plain_password, hashed_password):
    #     return password_hash.verify(plain_password, hashed_password)
    

    # def get_password_hash(password):
    #     return password_hash.hash(password)


    # def authenticate_user(fake_db, username: str, password: str):
    #     user = Login(fake_db, username)
    #     if not user:
    #         return False
    #     if not UserController.verify_password(password, user.hashed_password):
    #         return False
    #     return user
    
    def login(self, user: Login):
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT id, usuario, nombre, password, apellido, id_rol FROM usuario     WHERE usuario=%s",(user.usuario,))
            result = cursor.fetchone()
                    
            if not result:
               raise HTTPException(status_code=404, detail="User not found")
            hashed_password = result["password"]
            print("hashed_password", hashed_password)
            print("user.password", user.password)
            print(repr(hashed_password))
            if not password_hash.verify(user.password,hashed_password,):
                raise HTTPException(status_code=400, detail="Incorrect password")
            
            
            payload = []
            content = {} 
           
            content = {
    'id': result['id'],
    'usuario': result['usuario'],
    'nombre': result['nombre'],
    'apellido': result['apellido'],
    'rol': result['id_rol']
}
            payload.append(content)
            content = {}
            json_data = jsonable_encoder(payload)
            return {"resultado": json_data}        

        except mysql.connector.Error as err:
            conn.rollback()
            print(f"Error en la base de datos: {err}")
            raise HTTPException(status_code=500, detail=f"Error en la base de datos: {str(err)}")
        
        finally:
            conn.close()        

    
    def create_user(self, user: User):   
        try:
            print("111111111111111", user)
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuario WHERE usuario= %s  ||  documento= %s", (user.usuario,user.documento))
            result = cursor.fetchall()

            if result:
               
                content = {}    
                content={"Informacion":"Ya_existe"}
              
                return jsonable_encoder(content)
            else:   
                hashed_password = password_hash.hash(user.password)
                cursor.execute("INSERT INTO usuario (usuario,password,nombre,apellido,documento,telefono,id_rol,estado, genero, edad, completado) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (user.usuario,hashed_password,user.nombre,user.apellido,user.documento,user.telefono,user.id_rol,user.estado, user.genero, user.edad,1))
                conn.commit()
                conn.close()
                id=cursor.lastrowid
                return {"id": id, "Informacion": "Creado"}


        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()    
    
    def create_user_masivo (self, file: UploadFile):
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

    
    def get_user(self, user: Buscar):
        
        try:
            
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""SELECT usuario.*, rol.*
                FROM usuario
                JOIN rol ON usuario.id_rol = rol.id
                        WHERE usuario.id=%s """, (user.id,))
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
                    'roles_name':result[17],
                    'edad': result[9],
                    'genero': result[10],
                    'estatura': result[13],
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





    def get_user_document(self, user: Buscar_document):
        
        try:
            
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""SELECT u.*
                FROM usuario u
                JOIN cita c ON u.id = c.id_paciente
                WHERE u.documento = %s
                AND c.id_usuario = %s
                            """, (user.documento,user.id_doctor,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            if result:
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
            cursor.execute("""SELECT usuario.*, rol.*
                FROM usuario
                JOIN rol ON usuario.id_rol = rol.id
                        WHERE usuario.id_rol!=1 and completado!=0
                           """)
            result = cursor.fetchall()
            usuarios_ordenados = sorted(result, key=lambda  data: (not data[8], data[1].lower()))
            
            payload = []
            content = {} 
            for data in usuarios_ordenados:
                print (data[8])
                content={
                    'id':data[0],
                    'usuario':data[1],
                    'password':data[2],
                    'nombre':data[3],
                    'apellido':data[4],
                    'documento':data[5],
                    'telefono':data[6],
                    'id_rol':data[7],
                    'estado':data[8],
                    'nombre_rol':data[17],
                   

                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return json_data
            else:
                raise HTTPException(status_code=404, detail="User not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()


    def get_medico_especialidad(self, user: Buscar):
        
        try:
            
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""SELECT usuario.*, atrixusuario.valor
                FROM usuario
               LEFT JOIN atrixusuario ON usuario.id = atrixusuario.id_usuario
                        WHERE usuario.id=%s""", (user.id,))
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
                    'edad': result[9],
                    'genero': result[10],
                    'estatura': result[13],
                    'especialidad': result[16]
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


    def get_medicos(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuario WHERE id_rol=3")
            result = cursor.fetchall()
            usuarios_ordenados = sorted(result, key=lambda  data: (not data[8], data[1].lower()))

            payload = []
            content = {} 
            for data in usuarios_ordenados:
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


    def get_paciente(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuario where id_rol=2")
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

    def get_medico(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuario where id_rol=3")
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

       
    def update_user(self, user: Actualizar):
        try:
            print("user", user)
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT genero, edad,id_rol, password FROM usuario WHERE id = %s", (user.id,))
            actual = cursor.fetchone()
            genero = user.genero if user.genero is not None else actual[0]
            edad = user.edad if user.edad is not None else actual[1]
            password = user.password if user.password is not None else actual[2]
            rol=user.id_rol if user.id_rol is not None else actual[3]
            
            cursor.execute("""
            UPDATE usuario
            SET usuario = %s,
            nombre=%s,
            apellido = %s,
            documento=%s,
            telefono=%s ,
            id_rol=%s,
            estado =%s,
            genero=%s,
            edad=%s, 
            password=%s
            WHERE id = %s
            """,(user.usuario,user.nombre,user.apellido,user.documento,user.telefono,rol,user.estado,genero, edad,password,user.id,))
            conn.commit()
           
            return {"resultado": "Usuario actualizado correctamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()    

             
    def update_adm(self, adm: ActualizarAdm):
        try:
            
            conn = get_db_connection()
            cursor = conn.cursor()
            print ("eeeeeeeeeeeeeeee")
            cursor.execute("""
            UPDATE usuario
            SET usuario = %s,
            nombre=%s,
            apellido = %s,
            documento=%s,
            password=%s,                           
            telefono=%s,
            genero=%s,
            edad=%s, 
            estatura=%s
            WHERE id = %s
            """,(adm.usuario,adm.nombre,adm.apellido,adm.documento,adm.password,adm.telefono, adm.genero, adm.edad ,adm.estatura, adm.id,))
            conn.commit()
            print ("ssssssssssssss",cursor)
            if cursor.rowcount == 0:
                return {"error": "No se actualizó ningún usuario. Verifique si el ID es correcto o si los datos no han cambiado."}
            else:
                return {"resultado": "Usuario actualizado correctamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
            return {"error": f"Error al actualizar usuario: {err}"}
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


    

    # def login(self, user: Login):
    #     try:
    #         conn = get_db_connection()
    #         cursor = conn.cursor()
    #         cursor.execute("SELECT * FROM usuario where estado!=0 AND usuario = %s AND password = %s",(user.usuario, user.password,))
    #         result = cursor.fetchall()
    #         payload = []
    #         content = {} 
    #         for data in result:
    #             content={
    #                 'usuario':data[1],
    #                 'password':data[2],
    #                 'nombre':data[3],
    #                 'apellido': data [4],
    #                 'id':data[0],
    #                 'rol':data[7],


    #             }
    #             payload.append(content)
    #             content = {}
    #         json_data = jsonable_encoder(payload)        
    #         if result:
    #            return {"resultado": json_data}
    #         else:
    #             raise HTTPException(status_code=404, detail="User not found")  
    #     except mysql.connector.Error as err:
    #         conn.rollback()
    #     finally:
    #         conn.close()


    def verif_user(self, user: Verif_user):   
        try:
            print("111111111111111", user)
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuario WHERE usuario= %s ", (user.usuario,))

            result = cursor.fetchone()

            if result:
                
                id=result[0]
               
                
            
                cursor.execute("SELECT * FROM sesiongoogle where google_id = %s",(user.google_id,))
                result_google= cursor.fetchone()
                
                if result_google:
                    content = {}    
                    print ("rol_v", result[7])
                    content={"Informacion":"Ya_existe", 'id':int(result[0]),'rol_v':int(result[7]), 'estado':bool(result[15]), }
                    return jsonable_encoder(content)

                else:
                    print ("*--------**-/*/",user)
                    cursor.execute("INSERT INTO sesiongoogle (id_usuario, google_id, access_token, foto, estado) VALUES (%s, %s, %s, %s,%s)",
                               (id, user.google_id, user.access_token,user.foto,user.estado,))
                    conn.commit()
                   
                    content = {}    
                    content={"Informacion":"Ya_existe", 'id':int(result[0]),'rol_v':int(result[7]), 'estado':bool(result[15]), }

                    return jsonable_encoder(content)



                
            else:   
                print ("*--------**-/*/",user)
                cursor.execute("INSERT INTO usuario (usuario,password,nombre,apellido,telefono,id_rol,estado, genero, edad, completado) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (user.usuario,"LOGINadminLOGIN1",user.nombre,user.apellido,"000000",2,0, "genero", 0,0))
                id=cursor.lastrowid
                cursor.execute("INSERT INTO sesiongoogle (id_usuario, google_id, access_token, foto, estado) VALUES (%s, %s, %s, %s,%s)",
                               (id, user.google_id, user.access_token,user.foto,user.estado,))
                conn.commit()
    
                content = {}    
                content={"Informacion":"Registrada", 'id': id}
                return jsonable_encoder(content)

               
                    

        except mysql.connector.Error as err:
            conn.rollback()
            print(f"Error en la base de datos: {err}")  
        finally:
            conn.close() 






  
    def verificar_usuario(self, user: login_google):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM sesiongoogle where google_id = %s",(user.verif_user.google_id,))
            result = cursor.fetchone()
            if result:
               print("-------------")
               return {"resultado": "usuario ya registrado"}
            else:
                print("-----------------2")
                user_id=self.create_user(user.user)
                print("Usuario registrando", user_id)
                cursor.execute("INSERT INTO sesiongoogle (id_usuario, google_id, access_token, foto, estado) VALUES (%s, %s, %s, %s,%s)",
                               (user_id, user.verif_user.google_id, user.verif_user.access_token,user.verif_user.foto,))
                return {"resultado": "usuario registrado"}             
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()


    # try: 
        
    #     # Buscar si el usuario ya existe en la BD
    #     #const [rows] = await db.execute('SELECT * FROM usuarios WHERE google_id = ?', [google_id]);

    #     if (rows.length > 0) {
    #         console.log("Usuario ya registrado:", rows[0]);
    #         return res.json(rows[0]);  // Si existe, devolver sus datos
    #     } else {
    #         console.log("Nuevo usuario, registrándolo en la BD...");
    #         await db.execute('4 INTO usuarios (google_id,     access_token) VALUES (?, ?, ?, ?, ?)', 
    #             [google_id, nombre, email, foto, access_token]);

    #         return res.json({ google_id, nombre, email, foto });
    #     }
 




    def estado_user(self, user: Estado):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
            UPDATE usuario
            SET
            estado =  %s                
            WHERE id = %s
            """,(user.estado,user.id,))
            conn.commit()
           
            return {"resultado": "Usuario desactivado correctamente :c"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close() 

    def Actualizar_estatura(self, promedio: str, id: int ):
        try:
            print ("id a actualizar", id)
            print ("estatura", promedio)

            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
            UPDATE usuario
            SET
            Estatura =  %s                
            WHERE id = %s
            """,(promedio,id))
            conn.commit()
           
            return {"resultado": "Estatura actualizada correctamente "} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close() 

    detener_captura = False

    def Estatura_user(self, id):
        ALTURA_REFERENCIA_M = 1.70    # Altura real de la persona de referencia (en metros)
        PIXEL_REF = 368                # Medida en píxeles de esa persona 
        global detener_captura
        detener_captura = False 

        # Inicializa MediaPipe Pose
        mp_pose = mp.solutions.pose # Esta es el Módulo para detectar posturas
        pose = mp_pose.Pose() #Crea una instancia de detección de pose
        mp_drawing = mp.solutions.drawing_utils #Utilidad para dibujar el esqueleto en la imagen
        historial_alturas = []

        # Abre la cámara (el  0  significa que abre  la cámara por defecto)
        cap = cv2.VideoCapture(0)
        while cap.isOpened()  and not detener_captura:
            ret, frame = cap.read()    # Leer frame de la cámara
            if not ret:
                break

            # Rota la imagen para cámara en vertical
            #frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

            # Convierte de BGR ( el cual es el formato que usa OpenCV) a RGB (formato que usa MediaPipe)
            image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            #Procesa la imagen para detectar landmarks del cuerpo  | Pose es la instancia que se creo arriba
            results = pose.process(image_rgb)

            if results.pose_landmarks:
                # Dibuja puntos y líneas del esqueleto
                mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

                    # Obtiene el alto y ancho del frame
                h, w, _ = frame.shape

                # Obtiene la coordenada Y de la nariz 
                head_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y * h)

                # Obtiene las coordenadas Y de los tobillos
                left_ankle_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ANKLE].y * h)
                right_ankle_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE].y * h)
                
                #Toma el tobillo más bajo
                foot_y = max(left_ankle_y, right_ankle_y)

                # Calcula la altura en píxeles
                altura_px = foot_y - head_y

                #print("Altura en píxeles detectada:", altura_px)


                # Estimación de altura
                altura_estim = (altura_px / PIXEL_REF) * ALTURA_REFERENCIA_M
                print("Estatura  detectada:", altura_estim)


                # Mostrar resultado en pantalla dentro del video
                cv2.putText(frame, f"Altura aprox: {altura_estim:.2f} m", (10, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)


                # Codifica el frame como imagen JPEG
                flag, encodedImage = cv2.imencode(".jpg", frame)
                if not flag:
                    continue

                

                yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')

            historial_alturas.append(altura_estim)



            if len(historial_alturas) >= 10:
                  promedio = sum(historial_alturas) / len(historial_alturas)
                  print("ya", promedio, "y la id del usuario es", id)
                  historial_alturas.clear()
                  #self.Actualizar_estatura(promedio, id)
                 
                 
            # # Mostrar ventana
            # cv2.imshow("Altura con MediaPipe Pose", frame)
            
            # if cv2.waitKey(1) & 0xFF == 27:  # Presiona ESC para salir
            #     break
        print("ahora deberia de cerrarseeeeeeeeeeee")
        self.Actualizar_estatura(promedio, id)
        # Libera la cámara 
        cap.release()
        #Cierra todas las ventanas creadas por OpenCV 
        cv2.destroyAllWindows()

           
    def video_feed(self, id: int):
        print("entra primera vez")
        return StreamingResponse(self.Estatura_user(id),
                             media_type="multipart/x-mixed-replace; boundary=frame")
    



    def telegram_id_user(self, user: Buscar):
        try:
            print("user", user)
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT id_telegram FROM usuario WHERE id_telegram = %s", (user.id,))
            rv = cursor.fetchone()

            if rv:
                return {"resultado": "Ya fue creado"} 
            else:
            
                cursor.execute("""
                UPDATE usuario
                SET id_telegram = %s
                WHERE id = %s
                """,(user.id_telegram,user.id,))
                conn.commit()
            
                return {"resultado": "Usuario actualizado correctamente"}   
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()    

 
    def detener_altura(self):
        global detener_captura
        detener_captura = True
        return {"mensaje": "Captura detenida"}
    


    def ValidarIncapacidad(self, user: ValidarIncapacidad):
        try:
    
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""SELECT usuario FROM usuario WHERE id=%s and documento=%s""",(user.id, user.cedula,))
            rv= cursor.fetchone()
            if rv:
                return {"resultado": "Correcto"}
            else:
                 return {"resultado": "Incorrecto"}
                
        except mysql.connector.Error as err:
            if conn:
                conn.rollback()
            return {"error": f"Un error inesperado ocurrió: {str(err)}"}
        finally:
            conn.close() 
    
    #StreamingResponse, es una clase de FastAPI que permite enviar datos como un flujo continuo, útil para video o audio.
    #Estatura_user devuelve frames JPEG uno a uno (cada imagen del video).
   # media_type="multipart/x-mixed-replace; boundary=frame": Es usado para enviar múltiples imágenes como un solo flujo. Así se simula el video en el navegador.
            
##user_controller = UserController()


#AFK