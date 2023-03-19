import json
import requests
from requests_toolbelt import MultipartEncoder


# 参数：图片地址
# 返回：官方链接
def get_link(img_path):
    # 1、初始化需要的数据，包括目标网址、请求头、cookies、图片路径等信息
    url = 'https://afdian.net/api/upload/common-pic'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    cookies = {
                'auth_token': '6f1ed28d2f8821b6394b909fe5533491_20230319122938',
                '_gid':'GA1.2.153730405.1679200180',
                '_ga_6STWKR7T9E': 'GS1.1.1679221713.27.0.1679221713.60.0.0',
                '_ga': 'GA1.1.1649184242.1668054313'
    }

    # 2、使用 MultipartEncoder 创建文件上传的 payload
    file_payload = {
        "name":"file",
        "filename":img_path,
        'file':(img_path,open(img_path,'rb'))
    }
    m = MultipartEncoder(file_payload)

    # 3、补充头
    headers['Content-Type'] = m.content_type # multipart/form-data; boundary=29cf7f1b13584a73a6630a738be8274a

    # 4、发送请求
    response = requests.post(url, headers=headers, data = m, cookies=cookies)
    response.encoding = "unicode_escape" # 将utf-8 转换成 unicode

    # 5、返回响应内容
    # 5.1、将响应内容转换成json
    response_json = json.loads(response.text)
    # 5.2、返回想要的字段link
    link = response_json['link']
    return link

# 发布函数
# 传入：一个字典类型的数据，包含：标题、内容、图片链接
# 返回：响应数据
def publish(publish_data):
    # 1、初始化需要的数据，包括目标网址、请求头、cookies、请求数据等信息
    url = 'https://afdian.net/api/post/publish'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    cookies = {
                'auth_token': '6f1ed28d2f8821b6394b909fe5533491_20230319122938',
                '_gid':'GA1.2.153730405.1679200180',
                '_ga_6STWKR7T9E': 'GS1.1.1679221713.27.0.1679221713.60.0.0',
                '_ga': 'GA1.1.1649184242.1668054313'
    }
    title = publish_data['title']
    content = publish_data['content']
    link = publish_data['link']
    data_dict = {
                "post_id":"",
                "vote_id":"",
                "cate":"normal",
                "title":title,
                "content":content,
                "pics":link,
                "is_public":"1",
                "min_price":"0",
                "audio":"",
                "video":"",
                "audio_thumb":"",
                "video_thumb":"",
                "type":"0",
                "cover":"",
                "group_id":"",
                "is_feed":"0",
                "plan_ids":"",
                "album_ids":"",
                "attachment":"[]",
                "timing":"",
                "optype":"publish",
                "preview_text":""
    }


    # 4、发送请求
    response = requests.post(url, headers=headers, data = data_dict, cookies=cookies)

    # 5、返回响应内容
    response.encoding = "unicode_escape" # 将utf-8 转换成 unicode
    return response.text

if __name__ == "__main__":
    img_path = "img.jpg"
    link = get_link(img_path)
    publish_data = {
        "title" : "标题测试",
        "content" : "内容测试",
        "link" : link
    }
    rep = publish(publish_data)
    print(rep)

