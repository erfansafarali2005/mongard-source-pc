from kavenegar import *

def send_otp_code(phone_number , code):
    try:
        api = KavenegarAPI('747A34473956366E7363426253514C4C3169666548326D5366687946432B774D39747063707766537A43493D')
        params = {
            'sender': '' ,
            'receptor': phone_number ,
            'message' : f' میباشد{code} کد تایید شما در سایت عرفان صفرعلی ',
        }
        response = api.sms_send(params)
        print(response)

    except APIException as e :
        print(e)
    except HTTPException as e :
        print(e)