# -*- coding: utf-8 -*-

import os
import telebot
import funcionesDB

TOKEN = os.environ['TOKEN']
bot = telebot.TeleBot(TOKEN)

commands = { # command description used in the "ayuda" command
    'hola': 'Comando de inicio',
    'adios': 'Comando de despedida',
    'ayuda': 'Da informacion sobre los comandos disponibles',
    'profesores': 'Información sobre profesores y contactos de una asignatura',
    'horarios': 'Información sobre el horario',
    'examenes': 'Infromación sobre el examen final de la asignatura',
}

def listener(messages):
    for m in messages:
        if m.content_type == 'text':
            chat_id = m.chat.id
            print ("[" + str(chat_id) + "]: " + m.text)
bot.set_update_listener(listener)

@bot.message_handler(commands=['hola'])
def comando_hola(message):
    """Función de bienvenida al bot de Telegram. """
    chat_id = message.chat.id
    bot.send_message(chat_id, "Bienvenid@ al canal de Informática_UGR-Bot, use el comando /ayuda para más información")

@bot.message_handler(commands=['adios'])
def comando_hola(message):
    """Función de despedida del bot de Telegram. """
    chat_id = message.chat.id
    bot.send_message(chat_id, "Hasta pronto!")

@bot.message_handler(commands=['profesores'])
def comando_obtenerGD(message):
    """Función que muestra los profesores y sus contactos. """
    chat_id = message.chat.id
    asignatura = message.text[12:16]

    if(asignatura == ""):
        bot.send_message(chat_id, "Debes indicar la asignatura que deseas buscar. Ej: ALEM")
    else:
        res = funcionesDB.obtenerGuiaDocente(asignatura)
        bot.send_message(chat_id, res)

@bot.message_handler(commands=['horarios'])
def comando_obtenerHO(message):
    """Función que muestra el horario. """
    chat_id = message.chat.id
    curso = message.text[10:11]
    semestre = message.text[12:13]
    grupo = message.text[14:15]
    dia = message.text[16:]

    if(curso == "" or semestre == "" or grupo == "" or dia == ""):
        bot.send_message(chat_id, "Debes indicar el curso, semestre, grupo y dia. Ej: 1 1 A lunes")
    else:
        res = funcionesDB.obtenerHorarios(curso, semestre, grupo, dia)
        bot.send_message(chat_id, res)

@bot.message_handler(commands=['examenes'])
def comando_obtenerEX(message):
    """Función que muestra el examen final de la asignatura. """
    chat_id = message.chat.id
    asignatura = message.text[10:14]
    semestre = message.text[15:16]
    convocatoria = message.text[17:]

    print(asignatura)
    print(semestre)
    print(convocatoria)

    if(asignatura == "" or semestre == "" or convocatoria == ""):
        bot.send_message(chat_id, "Debes indicar la asignatura, semestre y convocatoria. Ej: ALEM 1 ordinaria")
    else:
        res = funcionesDB.obtenerFechaEx(asignatura, semestre, convocatoria)
        bot.send_message(chat_id, res)

@bot.message_handler(commands=['ayuda'])
def command_help(message):
    chat_id = message.chat.id
    help_text = "Estos son los comandos disponibles: \n"
    for key in commands:
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(chat_id, help_text)

bot.polling(none_stop=True)
