import sys
import json
import urllib.parse
import urllib.request

def calculate_bazi_solar(year, month, day, hour, minute, gender):
    # API 基础 URL
    base_url = "https://dao.qbb.me/api/trpc/bazi.calculate"
    
    # 构造 input 参数 (强制为公历数据)
    input_data = {
        "0": {
            "json": {
                "year": int(year),
                "month": int(month),
                "day": int(day),
                "hour": int(hour),
                "minute": int(minute),
                "gender": gender
            }
        }
    }
    
    params = urllib.parse.urlencode({"batch": 1, "input": json.dumps(input_data)})
    url = f"{base_url}?{params}"
    
    headers = {
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'content-type': 'application/json',
        'referer': 'https://dao.qbb.me/',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
    }
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            return data
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    if len(sys.argv) < 7:
        print(json.dumps({"error": "Missing arguments"}))
        sys.exit(1)
    
    # 示例调用: python calculate_bazi.py 1993 3 18 12 0 male
    res = calculate_bazi_solar(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
    print(json.dumps(res, ensure_ascii=False))
