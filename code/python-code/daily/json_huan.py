import json
date=[{"name":"张三","age":18}]


#将python列表或者字典转换成JSON字符串
json_str=json.dumps(date,ensure_ascii=False)#当有中文时要表明不用ASCII转换
print(type(json_str))
print(json_str)

##将JSON字符串转换成python列表或者字典
s='{"name":"张三","age":18}'
ls=json.loads(s)
print(type(ls))
print(ls)