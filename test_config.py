from app.config.settings import settings  # Ajusta la ruta según tu carpeta

def test_settings():
    print("--- Verificando Configuración ---")
    try:
        print(f"Proyecto: {settings.PROJECT_NAME}")
        print(f"Versión:  {settings.API_VERSION}")
        print(f"Versión v1:  {settings.API_V1_STR}")
        print(f"Clave Secreta: {settings.SECRET_KEY}")
        print(f"Servidor: {settings.POSTGRES_SERVER}")
        print(f"Base de Datos: {settings.POSTGRES_DB}")
        print(f"Usuario DB: {settings.POSTGRES_USER}")
        print(f"Contraseña DB: {settings.POSTGRES_PASSWORD}")
        print(f"Puerto DB: {settings.POSTGRES_PORT}")

        
        # Intentamos generar la URL de la DB
        db_url = settings.SQLALCHEMY_DATABASE_URL
        print(f"Database URL: {db_url}")

        print("\n✅ ¡Configuración cargada con éxito!")
    except Exception as e:
        print(f"\n❌ Error al cargar la configuración: {e}")

if __name__ == "__main__":
    test_settings()