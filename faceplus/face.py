import requests
import json
import base64
img_address=input('请输入图片地址:')
img=open(img_address,'rb') #二进制方式打开图文件
img_data=base64.b64encode(img.read()) #读取文件内容，转换为base64编码
img.close()
parameter={
    'api_key':'-uR1XEM-JmNCZyjsBXG0m_8RVpmFPXUQ',
    'api_secret':'MzK4rMpLF9A-ntIZjfO7RIbtGQc8e_6f',
    'image_base64':img_data,
    'return_attributes':'age,gender,emotion,beauty'
} #请求参数
r=requests.post('https://api-cn.faceplusplus.com/facepp/v3/detect',data=parameter) #发起请求
face_data=r.text #返回数据
face_json_data=json.loads(face_data) #加载json数据
face_list_data=face_json_data['faces'][0]['attributes'] #创建一个字典存放面部数据
def del_data(): #处理并输出
    emotion=face_list_data['emotion']
    your_emotion=max(emotion.items(), key=lambda x: x[1])[0] #取表情最大数值并返回key
    if your_emotion=='anger': #输出表情状态
        status='愤怒'
    elif your_emotion=='disgust':
        status='厌恶'
    elif your_emotion=='fear':
        status='恐惧'
    elif your_emotion=='happiness':
        status='高兴'
    elif your_emotion=='neutral':
        status='平静'
    elif your_emotion=='sadness':
        status='伤心'
    else:
        status='惊讶'
    print(status)
    gender=face_list_data['gender']['value']
    if gender=='Female': #输出性别
        print('女性')
    else:
        print('男性')
    age=face_list_data['age']['value']
    print('年龄:',age)
    if gender=='Female':
        beauty=face_list_data['beauty']['female_score']
    else:
        beauty=face_list_data['beauty']['male_score']
    print('你的颜值分数是',beauty) #输出颜值分数
del_data() #启动

