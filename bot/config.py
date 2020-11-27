class config:
    BOT_TOKEN = "1403765071:AAFU39z8uziZm0fFdJ-VcvbdBvtrWcSo9Jw"
    APP_ID = "2498521"
    API_HASH = "b6ba6f00c0e9d353ae13f972c56f3922"
    DATABASE_URL = "postgres://muwcmjserlywoo:ea2d49efe614a807eafbaca41278954b1add90e5f6085b3a8741d5b13353b7cf@ec2-52-207-25-133.compute-1.amazonaws.com:5432/dam1eb0v2vchk6"
    SUDO_USERS = "1039994326"
    SUPPORT_CHAT_LINK = "https://t.me/joinchat/AAAAAEZPxfT0M6s4NKIDQA"
    DOWNLOAD_DIRECTORY = "./downloads/"


class BotCommands:
  Download = ['download', 'dl']
  Authorize = ['auth', 'authorize']
  SetFolder = ['setfolder', 'setfl']
  Revoke = ['revoke']
  Clone = ['copy', 'clone']
  Delete = ['delete', 'del']
  EmptyTrash = ['emptyTrash']
  Ytdl = ['ytdl']

class Messages:
    START_MSG = "**Hola {}.**\n__Soy un Bot Google Drive Uploader. Puede usarme para cargar cualquier archivo / video a Google Drive desde un enlace directo o Telegram Files.__\n__Puedes saber más en /help.__"

    HELP_MSG = [
        ".",
        "**Subir a Google Drive**\n__I puede cargar archivos desde un enlace directo o archivos de Telegram a su Google Drive. Todo lo que necesito es autenticarme en su cuenta de Google Drive y enviar un enlace de descarga directa o un archivo de Telegram.__\n\n¡Tengo más funciones ...! ¿Quieres saberlo? Simplemente siga este tutorial y lea los mensajes detenidamente.",
        
        f"**Autenticar Google Drive**\n__Envía el /{BotCommands.Authorize[0]} comando y recibirá una URL, visite la URL y siga los pasos y envíe el código recibido aquí. Utilizar /{BotCommands.Revoke[0]} para revocar su cuenta de Google Drive actualmente registrada.__\n\n**Nota: No escucharé ningún comando o mensaje (excepto /{BotCommands.Authorize[0]} comando) hasta que me autorices.\nEntonces, ¡la autorización es obligatoria!**",
        
        f"**Enlaces directos**\n__Envíeme un enlace de descarga directa para un archivo, lo descargaré en mi servidor y lo subiré a su cuenta de Google Drive. Puede cambiar el nombre de los archivos antes de cargarlos en la cuenta de GDrive. Solo envíeme la URL y el nuevo nombre de archivo separados por ' | '.__\n\n**__Ejemplos:__**\n```https://example.com/AFileWithDirectDownloadLink.mkv | Nombre de archivo nuevo.mkv```\n\n**Archivos de Telegram**\n__Para cargar archivos de telegram en su cuenta de Google Drive, simplemente envíeme el archivo y lo descargaré y lo subiré a su cuenta de Google Drive. Nota: La descarga de archivos de Telegram es lenta. puede llevar más tiempo para archivos grandes.__\n\n**Soporte de YouTube-DL**\n__Descarga archivos a través de youtube-dl.\nUse /{BotCommands.Ytdl[0]} (Enlace de YouTube / enlace de sitio compatible con YouTube-DL)__",
        
        f"**Carpeta personalizada para subir**\n__Quiere cargar en una carpeta personalizada o en__ **TeamDrive** __ ?\nUse /{BotCommands.SetFolder[0]} (URL de carpeta) para configurar la carpeta de carga personalizada.\nTodos los archivos se cargan en la carpeta personalizada que proporcionas.__",
        
        f"**Eliminar archivos de Google Drive**\n__Eliminar archivos de Google Drive. Use /{BotCommands.Delete[0]} (URL de archivo / carpeta) para eliminar el archivo.\nTambién puede vaciar el uso de archivos de basura /{BotCommands.EmptyTrash[0]}\nNota: los archivos se eliminan de forma permanente. Este proceso no se puede deshacer.\n\n**Copiar archivos de Google Drive**\n__Sí, clonar o copiar archivos de Google Drive.\n__Use /{BotCommands.Clone[0]} (ID de archivo / ID de carpeta o URL) para copiar archivos de Google Drive en su cuenta de Google Drive.__",
        
        "**Reglas y Precauciones**\n__1. No copie GRANDES archivos / carpetas de Google Drive. Puede bloquear el bot y sus archivos pueden dañarse.\n2. Envíe una solicitud a la vez a por que el bot detiene todos los procesos.\n3. No envíe enlaces lentos @transload primero.\n4. No utilice mal, sobrecargue ni abuse de este servicio gratuito.__",
        
        "**Developed by @Kadma5**"
        ]
     
    RATE_LIMIT_EXCEEDED_MESSAGE = "❗ **Excede el límite de velocidad.**\n__Se superó el límite de frecuencia de usuario. Intente después de 24 horas__"
    
    FILE_NOT_FOUND_MESSAGE = "❗ **No se encontró el archivo / carpeta.**\n__File id - {} Extraviado. Asegúrese de que\'s existe y accesible por la cuenta registrada.__"
    
    INVALID_GDRIVE_URL = "❗ **URL de Google Drive no válida**\nAsegúrese de que la URL de Google Drive tenga un formato válido."
    
    COPIED_SUCCESSFULLY = "✅ **Copiado con éxito.**\n[{}]({}) __({})__"
    
    NOT_AUTH = f"🔑 **No me ha autenticado para subir a ninguna cuenta.**\n__Send /{BotCommands.Authorize[0]} autenticar.__"
    
    DOWNLOADED_SUCCESSFULLY = "📤 **Subiendo archivo ...**\n**Filename:** ```{}```\n**Size:** ```{}```"
    
    UPLOADED_SUCCESSFULLY = "✅ **Subido con éxito.**\n[{}]({}) __({})__"
    
    DOWNLOAD_ERROR = "❗**Falló al descargar**\n{}\n__Link - {}__"
    
    DOWNLOADING = "📥 **Descargando archivo...\nLink:** ```{}```"
    
    ALREADY_AUTH = "🔒 **Ya autorizó su cuenta de Google Drive.**\n__Usa /revoke para revocar la cuenta corriente.__\n__Enviarme un enlace directo o un archivo para cargar en Google Drive__"
    
    FLOW_IS_NONE = f"❗ **Codigo invalido**\n__Run {BotCommands.Authorize[0]} first.__"
    
    AUTH_SUCCESSFULLY = '🔐 **Cuenta de Google Drive autorizada correctamente.**'
    
    INVALID_AUTH_CODE = '❗ **Codigo invalido**\n__El código que ha enviado no es válido o ya se ha utilizado antes. Genere uno nuevo por la URL de autorización__'
    
    AUTH_TEXT = "⛓️ **Para autorizar su cuenta de Google Drive, visite esta [URL]({}) y envía el código generado aquí.**\n__Visite la URL> Permitir permisos> obtendrá un código> cópielo> Envíelo aquí__"
    
    DOWNLOAD_TG_FILE = "📥 **Descargando archivo...**\n**Filename:** ```{}```\n**Size:** ```{}```\n**MimeType:** ```{}```"
    
    PARENT_SET_SUCCESS = '🆔✅ **El enlace de la carpeta personalizada se estableció correctamente.**\n__Su ID de carpeta personalizada - {}\nUse__ ```/{} clear``` __para borrarlo.__'
    
    PARENT_CLEAR_SUCCESS = f'🆔🚮 **El ID de carpeta personalizado se borró correctamente.**\n__Use__ ```/{BotCommands.SetFolder[0]} (Enlace de carpeta)``` __para retrasarlo__.'
    
    CURRENT_PARENT = "🆔 **Su ID de carpeta personalizada actual - {}**\n__Use__ ```/{} (Enlace de carpeta)``` __para cambiarlo.__"
    
    REVOKED = f"🔓 **Se revocó la cuenta registrada actual con éxito.**\n__Use /{BotCommands.Authorize[0]} para autenticarse nuevamente y usar este bot.__"
    
    NOT_FOLDER_LINK = "❗ **Enlace de carpeta no válido.**\n__El enlace que envía no pertenece a una carpeta.__"
    
    CLONING = "🗂️ **Clonando en Google Drive ...**\n__G-Drive Link - {}__"
    
    PROVIDE_GDRIVE_URL = "**❗ Proporcione una URL válida de Google Drive junto con el comando.**\n__Usage - /{} (GDrive Link)__"
    
    INSUFFICIENT_PERMISSONS = "❗ **No tiene permisos suficientes para este archivo.**\n__File id - {}__"
    
    DELETED_SUCCESSFULLY = "🗑️✅ **Archivo eliminado correctamente.**\n__Archivo eliminado de forma permanente !\nFile id - {}__"
    
    WENT_WRONG = "⁉️ **ERROR: ALGO SALIÓ MAL**\n__Por favor, inténtelo de nuevo más tarde.__"
    
    EMPTY_TRASH = "🗑️🚮**¡Basura vaciada con éxito!**"
    
    PROVIDE_YTDL_LINK = "❗**Proporcione un enlace válido compatible con YouTube-DL.**"
