from fastapi import HTTPException
from fastapi import APIRouter
from decouple import config
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pydantic import BaseModel


router = APIRouter()

port = 587
smtp_server = config('M_HOST')
login = config('M_USERNAME')
password = config('M_PASSWORD')
sender_email = config('M_FROM')

async def send_email(subject: str, email_to: str, code: str):

    body = f"""<!doctype html>
<html lang="en" dir="auto" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
<title></title>
<!--[if !mso]><!-->
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<!--<![endif]-->
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style type="text/css">
#outlook a{{padding:0;}}body{{margin:0;padding:0;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;}}table,td{{border-collapse:collapse;mso-table-lspace:0pt;mso-table-rspace:0pt;}}img{{border:0;height:auto;line-height:100%;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;}}p{{display:block;margin:0;}}
</style>
<!--[if mso]> <noscript><xml><o:OfficeDocumentSettings><o:AllowPNG/><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml></noscript>
<![endif]-->
<!--[if lte mso 11]>
<style type="text/css">
.y{{width:100% !important;}}
</style>
<![endif]-->
<!--[if !mso]><!-->
<link href="https://fonts.googleapis.com/css?family=Inter:400,700" rel="stylesheet" type="text/css">
<!--<![endif]-->
<style type="text/css">
@media only screen and (min-width:599px){{.m6{{width:568px!important;max-width:568px;}}.h1{{width:536px!important;max-width:536px;}}}}
</style>
<style media="screen and (min-width:599px)">.moz-text-html .m6{{width:568px!important;max-width:568px;}}.moz-text-html .h1{{width:536px!important;max-width:536px;}}
</style>
<style type="text/css">
noinput.mn-checkbox{{display:block!important;max-height:none!important;visibility:visible!important;}}
</style>
<style type="text/css">
u+.emailify .g-screen{{background:#000;mix-blend-mode:screen;display:inline-block;padding:0;margin:0;}}u+.emailify .g-diff{{background:#000;mix-blend-mode:difference;display:inline-block;padding:0;margin:0;}}p{{-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;}}a[x-apple-data-detectors]{{color:inherit!important;text-decoration:none!important;}}u+.emailify a{{color:inherit!important;text-decoration:none!important;}}#MessageViewBody a{{color:inherit!important;text-decoration:none!important;}}
@media only screen and (max-width:599px){{.emailify{{height:100%!important;margin:0!important;padding:0!important;width:100%!important;}}td.x{{padding-left:0!important;padding-right:0!important;}}div.r.e>table>tbody>tr>td,div.r.e>div>table>tbody>tr>td{{padding-right:16px!important}}div.r.ys>table>tbody>tr>td,div.r.ys>div>table>tbody>tr>td{{padding-left:16px!important}}td.v.c>div.i>a.l.m{{padding-right:8px!important;}}div.h.eya>table>tbody>tr>td{{padding-top:32px!important}}div.h.e>table>tbody>tr>td{{padding-right:16px!important}}div.h.mg>table>tbody>tr>td{{padding-bottom:32px!important}}div.h.ys>table>tbody>tr>td{{padding-left:16px!important}}td.x.t span,td.x.t>div,td.x.t{{font-size:32px!important}}td.x.tnq span,td.x.tnq>div,td.x.tnq{{line-height:37px!important}}}}
</style>
<meta name="format-detection" content="telephone=no, date=no, address=no, email=no, url=no">
<meta name="x-apple-disable-message-reformatting">
<meta name="color-scheme" content="light dark">
<meta name="supported-color-schemes" content="light dark">
<!--[if gte mso 9]>
<style>a:link{{mso-style-priority:99;color:inherit;text-decoration:none;}}a:visited{{mso-style-priority:99;color:inherit;text-decoration:none;}}li{{margin-left:-1em !important}}table,td,p,div,span,ul,ol,li,a,h1,h2,h3,h4,h5,h6{{mso-hyphenate:none;}}sup,sub{{font-size: 100% !important;}}
</style>
<![endif]-->
</head>
<body lang="en" link="#DD0000" vlink="#DD0000" class="emailify" style="mso-line-height-rule:exactly;mso-hyphenate:none;word-spacing:normal;background-color:#f5f5f5;">
<!--[if mso | IE]>
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:600px;" width="600"><tr><td style="line-height:0;font-size:0;mso-line-height-rule:exactly;">
<![endif]--><div class="r e ys" style="background:#eeeeee;background-color:#eeeeee;margin:0px auto;max-width:600px;">
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#eeeeee;background-color:#eeeeee;width:100%;"><tbody><tr><td style="border:none;direction:ltr;font-size:0;padding:16px 16px 16px 16px;text-align:left;">
<!--[if mso | IE]>
<table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td style="vertical-align:middle;width:568px;">
<![endif]--><div class="m6 y" style="font-size:0;text-align:left;direction:ltr;display:inline-block;vertical-align:middle;width:100%;">
<table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border:none;vertical-align:middle;" width="100%"><tbody><tr><td align="center" class="v c" style="font-size:0;word-break:break-word;"><div class="i" style>
<!--[if mso | IE]>
<table role="presentation" border="0" cellpadding="0" cellspacing="0" align="center"><tr><td style="padding:0;padding-top:0;padding-left:0;padding-right:8px;padding-bottom:0;">
<![endif]-->
<!--[if mso | IE]>
</td><td style="padding:0;padding-top:0;padding-left:0;padding-right:0;padding-bottom:0;">
<![endif]-->
<!--[if mso | IE]>
</td></tr></table>
<![endif]--></div>
</td></tr></tbody></table></div>
<!--[if mso | IE]>
</td></tr></table>
<![endif]-->
</td></tr></tbody></table></div>
<!--[if mso | IE]>
</td></tr></table>
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:600px;" width="600"><tr><td style="line-height:0;font-size:0;mso-line-height-rule:exactly;"><v:image style="border:0;height:321px;mso-position-horizontal:center;position:absolute;top:0;width:600px;z-index:-3;" src="https://i.ibb.co/bbWt4Jn/5f395e2cc5cf2a4c2b769965ff027ea2.jpg" xmlns:v="urn:schemas-microsoft-com:vml"/><v:rect style="border:0;height:321px;mso-position-horizontal:center;position:absolute;top:0;width:600px;z-index:-4;" fillcolor="#000000" stroke="false" strokecolor="none" strokeweight="0" xmlns:v="urn:schemas-microsoft-com:vml"/>
<![endif]--><div class="h eya e mg ys" style="margin:0 auto;max-width:600px;">
<table border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;"><tbody><tr style="vertical-align:top;"><td background="https://i.ibb.co/bbWt4Jn/5f395e2cc5cf2a4c2b769965ff027ea2.jpg" style="background:#000000 url('https://i.ibb.co/bbWt4Jn/5f395e2cc5cf2a4c2b769965ff027ea2.jpg') no-repeat center center / cover; background-size: cover;background-position:center center;background-repeat:no-repeat;padding:16px 16px 16px 16px;vertical-align:middle;height:289px;" height="289">
<!--[if mso | IE]>
<table border="0" cellpadding="0" cellspacing="0" style="width:600px;" width="600"><tr><td style="padding:16px 16px 16px 16px;">
<![endif]--><div style="margin:0px auto;">
<table border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;margin:0;"><tbody><tr><td style>
<table border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;margin:0;"><tbody><tr><td align="center" class="x t tnq" style="font-size:0;word-break:break-word;"><div style="text-align:center;"><p style="Margin:0;text-align:center;mso-line-height-alt:61px;"><span style="font-size:50px;font-family:'Inter','Arial',sans-serif;font-weight:700;color:#ffffff;line-height:122%;mso-line-height-alt:61px;">Ecommerce SV</span></p></div>
</td></tr></tbody></table>
</td></tr></tbody></table></div>
<!--[if mso | IE]>
</td></tr></table>
<![endif]-->
</td></tr></tbody></table></div>
<!--[if mso | IE]>
</td></tr></table>
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:600px;" width="600"><tr><td style="line-height:0;font-size:0;mso-line-height-rule:exactly;">
<![endif]--><div class="r e ys" style="background:#fffffe;background-color:#fffffe;margin:0px auto;max-width:600px;">
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#fffffe;background-color:#fffffe;width:100%;"><tbody><tr><td style="border:none;direction:ltr;font-size:0;padding:32px 32px 32px 32px;text-align:left;">
<!--[if mso | IE]>
<table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td style="vertical-align:middle;width:536px;">
<![endif]--><div class="h1 y" style="font-size:0;text-align:left;direction:ltr;display:inline-block;vertical-align:middle;width:100%;">
<table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border:none;vertical-align:middle;" width="100%"><tbody><tr><td align="center" class="x m" style="font-size:0;padding-bottom:8px;word-break:break-word;"><div style="text-align:center;"><p style="Margin:0;text-align:center;mso-line-height-alt:32px;"><span style="font-size:28px;font-family:'Inter','Arial',sans-serif;font-weight:700;color:#000000;line-height:114%;mso-line-height-alt:32px;">Verifica tu cuenta</span></p></div>
</td></tr><tr><td align="center" class="x" style="font-size:0;padding-bottom:0;word-break:break-word;"><div style="text-align:center;"><p style="Margin:0;text-align:center;mso-line-height-alt:24px;"><span style="font-size:16px;font-family:'Inter','Arial',sans-serif;font-weight:400;color:#777777;line-height:150%;mso-line-height-alt:24px;">Ingresa el siguiente c&#243;digo en la app para verificar tu cuenta y acceder a la mejor plataforma de comercio electr&#243;nico de El Salvador.</span></p></div>
</td></tr></tbody></table></div>
<!--[if mso | IE]>
</td></tr></table>
<![endif]-->
</td></tr></tbody></table></div>
<!--[if mso | IE]>
</td></tr></table>
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:600px;" width="600"><tr><td style="line-height:0;font-size:0;mso-line-height-rule:exactly;">
<![endif]--><div class="r e ys" style="background:#fffffe;background-color:#fffffe;margin:0px auto;max-width:600px;">
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#fffffe;background-color:#fffffe;width:100%;"><tbody><tr><td style="border:none;direction:ltr;font-size:0;padding:32px 32px 32px 32px;text-align:left;">
<!--[if mso | IE]>
<table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td style="vertical-align:middle;width:536px;">
<![endif]--><div class="h1 y" style="font-size:0;text-align:left;direction:ltr;display:inline-block;vertical-align:middle;width:100%;">
<table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border:none;vertical-align:middle;" width="100%"><tbody><tr><td align="center" class="x" style="font-size:0;word-break:break-word;"><div style="text-align:center;"><p style="Margin:0;text-align:center;mso-line-height-alt:32px;"><span style="font-size:28px;font-family:'Inter','Arial',sans-serif;font-weight:700;color:#000000;line-height:114%;mso-line-height-alt:32px;">{code}</span></p></div>
</td></tr></tbody></table></div>
<!--[if mso | IE]>
</td></tr></table>
<![endif]-->
</td></tr></tbody></table></div>
<!--[if mso | IE]>
</td></tr></table>
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:600px;" width="600"><tr><td style="line-height:0;font-size:0;mso-line-height-rule:exactly;">
<![endif]--><div class="r e ys" style="background:#eeeeee;background-color:#eeeeee;margin:0px auto;max-width:600px;">
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#eeeeee;background-color:#eeeeee;width:100%;"><tbody><tr><td style="border:none;direction:ltr;font-size:0;padding:16px 16px 16px 16px;text-align:left;">
<!--[if mso | IE]>
<table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td style="vertical-align:middle;width:568px;">
<![endif]--><div class="m6 y" style="font-size:0;text-align:left;direction:ltr;display:inline-block;vertical-align:middle;width:100%;">
<table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border:none;vertical-align:middle;" width="100%"><tbody><tr><td align="center" class="x m" style="font-size:0;padding-bottom:8px;word-break:break-word;">
</td></tr><tr><td align="center" style="font-size:0;padding:0;padding-bottom:0;word-break:break-word;">
<!--[if mso | IE]>
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation"><tr><td>
<![endif]-->
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="float:none;display:inline-table;"><tbody><tr><td style="padding:0;vertical-align:middle;">
<table border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:136px;"><tbody><tr><td style="font-size:0;height:40px;vertical-align:middle;width:136px;"> 
</td></tr></tbody></table>
</td></tr></tbody></table>
<!--[if mso | IE]>
</td></tr></table>
<![endif]-->
</td></tr></tbody></table></div>
<!--[if mso | IE]>
</td></tr></table>
<![endif]-->
</td></tr></tbody></table></div>
<!--[if mso | IE]>
</td></tr></table>
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:600px;" width="600"><tr><td style="line-height:0;font-size:0;mso-line-height-rule:exactly;">
<![endif]--><div class="r e ys" style="background:#eeeeee;background-color:#eeeeee;margin:0px auto;max-width:600px;">
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#eeeeee;background-color:#eeeeee;width:100%;"><tbody><tr><td style="border:none;direction:ltr;font-size:0;padding:16px 16px 16px 16px;text-align:left;">
<!--[if mso | IE]>
<table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td style="vertical-align:middle;width:568px;">
<![endif]--><div class="m6 y" style="font-size:0;text-align:left;direction:ltr;display:inline-block;vertical-align:middle;width:100%;">
<table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border:none;vertical-align:middle;" width="100%"><tbody><tr><td align="center" class="x m" style="font-size:0;padding-bottom:16px;word-break:break-word;"><div style="text-align:center;"><p style="Margin:0;text-align:center;mso-line-height-alt:13px;"><span style="font-size:11px;font-family:'Inter','Arial',sans-serif;font-weight:400;color:#aaaaaa;line-height:118%;mso-line-height-alt:13px;">Si no has comenzado un proceso de registro en Ecommerce SV ignora este correo electr&#243;nico.</span></p></div>
</td></tr><tr><td align="center" class="v c" style="font-size:0;padding-bottom:0;word-break:break-word;"><div class="i" style>
<!--[if mso | IE]>
<table role="presentation" border="0" cellpadding="0" cellspacing="0" align="center"><tr><td style="padding:0;padding-top:0;padding-left:0;padding-right:0;padding-bottom:0;">
<![endif]-->
<!--[if mso | IE]>
</td></tr></table>
<![endif]--></div>
</td></tr></tbody></table></div>
<!--[if mso | IE]>
</td></tr></table>
<![endif]-->
</td></tr></tbody></table></div>
<!--[if mso | IE]>
</td></tr></table>
<![endif]--></div>
</body>
</html>
"""

    
    part = MIMEText(body, "html")
    message = MIMEMultipart('alternative')
    message['From'] = sender_email
    message['To'] = email_to
    message['Subject'] = subject
    message.attach(part)

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(login, password)
        server.sendmail(sender_email, email_to, message.as_string())
        server.quit()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return {"message": "Email sent successfully"}
    