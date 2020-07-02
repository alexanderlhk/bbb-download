SEND_EMAIL = False

if SEND_EMAIL:
    COMPANY = ''
    DNS = ''

    ########### PYTHON SMTP CONFIG ##############
    ALERT_RECEIVERS = [""] # dif <---
    ALERT_SENDER = "" # dif <---
    SMTP_HOST = "smtp.gmail.com"
    SMTP_PORT = 587
    SMTP_USER = "" # dif <---
    SMTP_PASS = "" # dif <---
    #############################################
