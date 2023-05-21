from fastapi import FastAPI, Request, Depends, HTTPException, status, Form, Response, Cookie
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import mysql.connector
from fastapi.security import HTTPBasic, HTTPBasicCredentials

#MAIN APP
app = FastAPI()
security = HTTPBasic()

# Configura la carpeta "static" como carpeta de archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")


template = Jinja2Templates(directory="./views")

#MODELO PARA VALIDAD EL FORMULARIO
# Modelo para validar el formulario de registro
class User(BaseModel):
    nombre: str
    apellido: str
    tipo_doc: str
    num_doc: str
    correo: str
    contrasena: str

# Función para conectar con la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="bd_enterprise"
)


#RUTAS BASICAS (RAICES)
#--------------------------------------------------------------------------------------------------
@app.get("/", response_class=HTMLResponse)
def root(req: Request):
    return template.TemplateResponse("index.html", {"request": req})
#--------------------------------------------------------------------------------------------------
@app.get("/index.html", response_class=HTMLResponse)
def root(req: Request):
    return template.TemplateResponse("index.html", {"request": req})
#--------------------------------------------------------------------------------------------------
@app.get("/registro/registro.html", response_class=HTMLResponse)
def inicio(request: Request):
    return template.TemplateResponse("/registro/registro.html", {"request": request})
#--------------------------------------------------------------------------------------------------
@app.get("/inicio_s/inicio.html", response_class=HTMLResponse)
def inicio(request: Request):
    return template.TemplateResponse("/inicio_s/inicio.html", {"request": request})
#--------------------------------------------------------------------------------------------------
@app.get("/postular/postular.html", response_class=HTMLResponse)
def inicio(request: Request):
    return template.TemplateResponse("/postular/postular.html", {"request": request})
#--------------------------------------------------------------------------------------------------



#RUTA DE REGISTRAR POST
# Función para registrar los datos del formulario en la base de datos
@app.post("/registro", response_class=HTMLResponse)
def registrar(request: Request, nombre: str = Form(...), apellido: str = Form(...), tipo_doc: str = Form(...), num_doc: str = Form(...), correo: str = Form(...), contrasena: str = Form(...)):
    # Inserción de los datos en la tabla "usuarios"
    mycursor = db.cursor()
    sql = "INSERT INTO usuarios (nombre, apellido, tipo_doc, num_doc, correo, contrasena) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (nombre, apellido, tipo_doc, num_doc, correo, contrasena)
    mycursor.execute(sql, val)
    db.commit()


    mensaje = "Registrado correctamente!"

    # Retorna el mensaje emergente y el template
    return HTMLResponse(f"""
        <html>
            <body>
                <script>
                    alert("{mensaje}");
                    window.location.href = "/";
                </script>
            </body>
        </html>
    """)
#--------------------------------------------------------------------------------------------------
@app.post("/login", response_class=HTMLResponse)
def login(request: Request, tipo_doc: str = Form(...), num_doc: str = Form(...), contrasena: str = Form(...)):
    # Validación de las credenciales del usuario
    mycursor = db.cursor()
    sql = "SELECT * FROM usuarios WHERE tipo_doc=%s AND num_doc=%s AND contrasena=%s"
    val = (tipo_doc, num_doc, contrasena)
    mycursor.execute(sql, val)
    usuario = mycursor.fetchone()

    # Si las credenciales son correctas, redirige al index
    if usuario is not None:
        return template.TemplateResponse("welcome/welcome.html", {"request": request})
    # Si las credenciales son incorrectas, muestra un mensaje de error y vuelve a mostrar el formulario de login
    else:
        mensaje = "Credenciales incorrectas. Por favor, intente nuevamente."
        return HTMLResponse(f"""
            <html>
                <body>
                    <script>
                        alert("{mensaje}");
                        window.location.href = "/inicio_s/inicio.html";
                    </script>
                </body>
            </html>
        """)
#--------------------------------------------------------------------------------------------------
@app.post("/postular", response_class=HTMLResponse)
def postular(request: Request, nombre: str = Form(...), apellido: str = Form(...), tipo_doc: str = Form(...), num_doc: str = Form(...), correo: str = Form(...)):
    mycursor = db.cursor()
    sql = "INSERT INTO candidatos (nombre, apellido, tipo_doc, num_doc, correo) VALUES (%s, %s, %s, %s, %s)"
    val = (nombre, apellido, tipo_doc, num_doc, correo)
    mycursor.execute(sql, val)
    db.commit()


    mensaje = "Postulado correctamente!"

    # Retorna el mensaje emergente 
    return HTMLResponse(f"""
        <html>
            <body>
                <script>
                    alert("{mensaje}");
                    window.location.href = "/";
                </script>
            </body>
        </html>
    """)


















