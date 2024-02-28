def get_welcome_email(first_name):    
    return f'''
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html dir="ltr" lang="en">
    <head>
        <meta content="text/html; charset=UTF-8" http-equiv="Content-Type" />
    </head>
    <body
        style="
        background-color: #ffffff;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,
            Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif;
        "
    >
        <table
        align="center"
        width="100%"
        border="0"
        cellpadding="0"
        cellspacing="0"
        role="presentation"
        style="max-width: 37.5em; margin: 0 auto; padding: 20px 0 48px"
        >
        <tbody>
            <tr style="width: 100%">
            <td>
                <div style="background-color: #245501; width: 100%; height:12rem padding-top:1rem;">
                <img
                    alt="Koala"
                    src="https://res.cloudinary.com/dyykmwaqs/image/upload/v1709129920/xkpqyupkiaksfpntexwa.png"
                    style="
                    display: block;
                    outline: none;
                    border: none;
                    text-decoration: none;
                    margin: 0 auto;
                    "
                />
                </div>

                <p style="font-size: 16px; line-height: 26px; margin: 16px 0">
                Hi
                <!-- -->{first_name}<!-- -->,
                </p>
                <p style="font-size: 16px; line-height: 26px; margin: 16px 0">
                Welcome to Greentracker, We're excited to have you on board, !
                </p>
                <table
                align="center"
                width="100%"
                border="0"
                cellpadding="0"
                cellspacing="0"
                role="presentation"
                style="text-align: center"
                >
                <tbody>
                    <tr>
                    <td>
                        <a
                        href="https://getkoala.com"
                        style="
                            background-color: #245501;
                            border-radius: 3px;
                            color: #fff;
                            font-size: 16px;
                            text-decoration: none;
                            text-align: center;
                            display: inline-block;
                            padding: 12px 12px 12px 12px;
                            line-height: 100%;
                            max-width: 100%;
                        "
                        target="_blank"
                        ><span
                            ><!--[if mso
                            ]><i
                                style="
                                letter-spacing: 12px;
                                mso-font-width: -100%;
                                mso-text-raise: 18;
                                "
                                hidden
                                >&nbsp;</i
                            ><!
                            [endif]--></span
                        ><span
                            style="
                            max-width: 100%;
                            display: inline-block;
                            line-height: 120%;
                            mso-padding-alt: 0px;
                            mso-text-raise: 9px;
                            "
                            >Get started</span
                        ><span
                            ><!--[if mso
                            ]><i
                                style="letter-spacing: 12px; mso-font-width: -100%"
                                hidden
                                >&nbsp;</i
                            ><!
                            [endif]--></span
                        ></a
                        >
                    </td>
                    </tr>
                </tbody>
                </table>
                <p style="font-size: 16px; line-height: 26px; margin: 16px 0">
                Best,<br />The Greentracker team
                </p>
                <hr
                style="
                    width: 100%;
                    border: none;
                    border-top: 1px solid #eaeaea;
                    border-color: #cccccc;
                    margin: 20px 0;
                "
                />
            </td>
            </tr>
        </tbody>
        </table>
    </body>
    </html>

        '''
        
def get_forget_pass_email(first_name, link):
    return f'''
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html dir="ltr" lang="en">

  <head>
    <meta content="text/html; charset=UTF-8" http-equiv="Content-Type" />
  </head>
  <div style="display:none;overflow:hidden;line-height:1px;opacity:0;max-height:0;max-width:0">Greentracker reset your password<div> ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿</div>
  </div>

  <body style="background-color:#f6f9fc;padding:10px 0">
    <table align="center" width="100%" border="0" cellPadding="0" cellSpacing="0" role="presentation" style="max-width:37.5em;background-color:#ffffff;border:1px solid #f0f0f0;padding:45px">
      <tbody>
        <tr style="width:100%">
          <td><div style="background-color: #245501; width: 100%; height:12rem padding-top:1rem;">
            <img
              alt="Greentracker"
              src="https://res.cloudinary.com/dyykmwaqs/image/upload/v1709129920/xkpqyupkiaksfpntexwa.png"
              style="
                display: block;
                outline: none;
                border: none;
                text-decoration: none;
                margin: 0 auto;
              "
            />
          </div>
            <table align="center" width="100%" border="0" cellPadding="0" cellSpacing="0" role="presentation">
              <tbody>
                <tr>
                  <td>
                    <p style="font-size:16px;line-height:26px;margin:16px 0;font-family:&#x27;Open Sans&#x27;, &#x27;HelveticaNeue-Light&#x27;, &#x27;Helvetica Neue Light&#x27;, &#x27;Helvetica Neue&#x27;, Helvetica, Arial, &#x27;Lucida Grande&#x27;, sans-serif;font-weight:300;color:#404040">Hi <!-- -->{first_name}<!-- -->,</p>
                    <p style="font-size:16px;line-height:26px;margin:16px 0;font-family:&#x27;Open Sans&#x27;, &#x27;HelveticaNeue-Light&#x27;, &#x27;Helvetica Neue Light&#x27;, &#x27;Helvetica Neue&#x27;, Helvetica, Arial, &#x27;Lucida Grande&#x27;, sans-serif;font-weight:300;color:#404040">Someone recently requested a password change for your Greentracker account. If this was you, you can set a new password here:</p><a href="{link}" style="background-color:#245501;border-radius:4px;color:#fff;font-family:&#x27;Open Sans&#x27;, &#x27;Helvetica Neue&#x27;, Arial;font-size:15px;text-decoration:none;text-align:center;display:inline-block;width:210px;padding:14px 7px 14px 7px;line-height:100%;max-width:100%" target="_blank"><span><!--[if mso]><i style="letter-spacing: 7px;mso-font-width:-100%;mso-text-raise:21" hidden>&nbsp;</i><![endif]--></span><span style="max-width:100%;display:inline-block;line-height:120%;mso-padding-alt:0px;mso-text-raise:10.5px">Reset password</span><span><!--[if mso]><i style="letter-spacing: 7px;mso-font-width:-100%" hidden>&nbsp;</i><![endif]--></span></a>
                    <p style="font-size:16px;line-height:26px;margin:16px 0;font-family:&#x27;Open Sans&#x27;, &#x27;HelveticaNeue-Light&#x27;, &#x27;Helvetica Neue Light&#x27;, &#x27;Helvetica Neue&#x27;, Helvetica, Arial, &#x27;Lucida Grande&#x27;, sans-serif;font-weight:300;color:#404040">If you don&#x27;t want to change your password or didn&#x27;t request this, just ignore and delete this message.</p>
                    <p style="font-size:16px;line-height:26px;margin:16px 0;font-family:&#x27;Open Sans&#x27;, &#x27;HelveticaNeue-Light&#x27;, &#x27;Helvetica Neue Light&#x27;, &#x27;Helvetica Neue&#x27;, Helvetica, Arial, &#x27;Lucida Grande&#x27;, sans-serif;font-weight:300;color:#404040">Happy Greentracking!</p>
                  </td>
                </tr>
              </tbody>
            </table>
          </td>
        </tr>
      </tbody>
    </table>
  </body>

</html>
'''        
