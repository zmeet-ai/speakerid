

## 一、声纹识别优势

* **全球领先的声纹识别，返回结果字段中精准识别说话人ID**
* **庞大的声纹数据库，海量音视频文件中毫秒级返回说话人的片段音视频信息**
* 语音增强后的声纹，可抵抗各种背景噪音
* 可对人和各种生物体以及环境声如乐器等声音建立声纹

<br/>

## 二、接口参数规范与鉴权

### 1、接口说明

声纹识别，主要是根据用户传入的语音片段，识别出说话人id；在验证之前，客户需要注册某人的语音片段，便于检索的时候，返回该说话人身份。

<br/>

### 2、接口参数规范

#### (1) 接口要求

需按照以下要求：

| 内容     | 说明                                                         |
| :------- | ------------------------------------------------------------ |
| 请求协议 | https (为提高安全性，强烈推荐https)                          |
| 请求地址 | https://voiceid.abcpen.com *注：服务器IP不固定，为保证您的接口稳定，请勿通过指定IP的方式调用接口，<br/>使用域名方式调用* |
| 接口鉴权 | 签名机制，详见 [signa生成](#signa生成)                       |
| 响应格式 | 统一采用JSON格式                                             |
| 开发语言 | 任意，只要可以向笔声云服务发起https请求的均可                |

#### (2) 鉴权
* 注意下述参数和语音识别等类似，放在http 的get请求中。

参数说明

| 参数  | 类型   | 必须 | 说明                                                         | 示例                         |
| :---- | :----- | :--- | :----------------------------------------------------------- | :--------------------------- |
| appid | string | 是   | 笔声开放平台应用ID， 或使用”X-App-Key“放入header部位         | 595f23df                     |
| ts    | string | 是   | 当前时间戳，从1970年1月1日0点0分0秒开始到现在的秒数， 或使用”X-Timestamp“放入header部位 | 1512041814                   |
| signa | string | 是   | 加密数字签名，或使用”X-App-Signature“放入header部位          | IrrzsJeOFk1NGfJHW6SkHUoN9CU= |

#### (3) signa生成
* python示例

```python
import hashlib
import hmac
import time
import base64

def get_signature(ts, app_id, app_secret):
    tt = (app_id + ts).encode('utf-8')
    md5 = hashlib.md5()
    md5.update(tt)
    baseString = md5.hexdigest()
    baseString = bytes(baseString, encoding='utf-8')

    apiKey = app_secret.encode('utf-8')
    signa = hmac.new(apiKey, baseString, hashlib.sha1).digest()
    signa = base64.b64encode(signa)
    signa = str(signa, 'utf-8')
    return signa
```

#### (4)  返回值

结果格式为json，字段说明如下：

| 参数   | 类型   | 说明                                            |
| :----- | :----- | :---------------------------------------------- |
| code   | string | 结果码(具体见[错误码](#错误码))                 |
| data   | string | 结果数据                                        |
| msg   | string | 描述                                            |

<br/>

## 三、声纹识别API文档
### 1、注册声纹

* 登录鉴权同 [鉴权](#鉴权) 
* POST mutipart/form-data请求

####  /voiceid/register

**请确保spk_name和app_id组合字段的i情景下，不要重复(更新字段的方式晚点提供)**

##### 参数说明

| 参数字段 | 参数类型 | 必须                         | 参数说明                         |
| -------- | -------- | ---------------------------- | -------------------------------- |
| spk_name | string   | 必须                         | 声纹名称，如“sunny”   |
| org_id | string | 必须 | 组织名称，如"abcpen" |
| tag_id | string | 必须 | tag名称，率属于org_id, 如“tech" |
| denoise_audio | boolean | 否                           | 用于是否先做语音降噪；针对人发音的语音数据，建议使用语音降噪；否则不需要 |
| audio    | File | 采样率16k、位长16bit、单声道 | 声音内容，可以是文件或者url链接  |

* 上传某人的语音片段，以注册该说话人的身份。 其中，**spk_name**字段，是在您的组织（org_id)下的某个特定人的名称，您须要确保对其命名的唯一性。 **tag_id**是附属扩展字段，是伴随spk_name而来的扩展段信息。
* 采用 x-www-form-urlencoded 表单方式提交

* 返回参数示例
```json
{"code":"0","msg":"success"}
```
<br/>

### 2、搜素声纹

* 登录鉴权同 [鉴权](#鉴权) 
* POST mutipart/form-data请求

#### /voiceid/recognize

打分最高者为返回识别结果。

##### 参数说明

| 参数字段      | 参数类型 | 必须                         | 参数说明                                 |      |
| ------------- | -------- | ---------------------------- | ---------------------------------------- | ---- |
| org_id        | string   | 必须                         |                                          |      |
| tag_id        | string   | 否                           | 必须保护自己的老板；tag_id，能娶到媳妇。 |      |
| audio         | File     | 采样率16k、位长16bit、单声道 | 声音内容，可以是文件或者url链接          |      |
| denoise_audio | boolean  | 采样率16k、位长16bit、单声道 |                                          |      |

* 采用 x-www-form-urlencoded 表单方式提交
* 返回示例(返回最接近该声纹的前十条数据)

```json
{"code":"0","msg":"success","data":[{"spk_name":"jiaozhu","audio_path":"https://zos.abcpen.com/voiceid/abcpen/20221223/c41bc3cc-49e5-40ad-b5c6-ba9e0051fbe6.flac","score":100.0000080148816},{"spk_name":"jiaozhu2","audio_path":"https://zos.abcpen.com/voiceid/abcpen/20221223/a43fb61a-98ff-4c24-bd5f-731f9b8aa450.flac","score":100.0000080148816}]}
```

<br/>

### 3、删除声纹

* 登录鉴权同 [鉴权](#鉴权)
* GET请求

#### /voiceid/del-spk-name
##### 参数说明

| 参数字段 | 参数类型 | 必须 | 参数                                           |      |
| -------- | -------- | ---- | ---------------------------------------------- | ---- |
| spk_name | string   | 必须 | 声纹名称，如“sunny”                            |      |
| org_id   | string   | 必须 | 必须自己的应用id(当前版本需要，正式环境不需要) |      |
| tag_id   | string   | 必须 | 该组织下的tag                                  |      |

* 返回示例参数
```json
{"code":"0","msg":"success"}
```

### 4、声纹数量

* 登录鉴权同 [鉴权](#鉴权) 
* 返回该组织下声纹数据库里面的所有声纹数量
* GET请求

### /voiceid/count
##### 参数说明

| 参数字段 | 参数类型 | 必须          | 参数说明 |      |
| -------- | -------- | ------------- | -------- | ---- |
| org_id   | string   | 组织名称      |          |      |
| tag_id   | string   | 该组织下的tag |          |      |

* 返回参数示例
```json
{"code":"0","msg":"success","data":{"count":2}}
```
<br/>

### 5、声纹列表

* 登录鉴权同 [鉴权](#鉴权)
* GET 请求

### /voiceid/list
##### 参数说明

| 参数字段 | 参数类型 | 必须 | 参数说明                                   |      |
| -------- | -------- | ---- | ------------------------------------------ | ---- |
| org_id   | string   | 必须 | 自己的应用id(当前版本需要，正式环境不需要) |      |
| tag_id   | string   | 必须 | 该组织下的tag                              |      |
| offset   | integer  | 否   | 返回数据的偏移量，默认为0                  |      |
| limit    | integer  | 否   | 返回数据的最大返回数量，默认为20           |      |

* 返回参数示例
```json
{"code":"0","msg":"success","data":[{"spk_name":"jiaozhu2","audio_path":"https://zos.abcpen.com/voiceid/abcpen/20221223/b10f1d63-4f0c-429f-8a4a-adaf7c3830d5.flac"},{"spk_name":"jiaozhu","audio_path":"https://zos.abcpen.com/voiceid/abcpen/20221223/7b88ac68-64a9-4bb6-9eef-74bb35954379.flac"}]}
```
<br/>

### 6、删除声纹数据库

* 登录鉴权同 [鉴权](#鉴权)
* GET请求
* 删除自己组织下的声纹数据库，试图重建

#### /voiceid/delete-all

##### 参数说明

| 参数字段 | 参数类型 | 必须 | 参数说明               |      |
| -------- | -------- | ---- | ---------------------- | ---- |
| org_id   | string   | 必须 | 某组织名称，如"abcpen" |      |
| tag_id   | string   | 必须 | 该组织下的tag          |      |

* 返回参数示例
```json
{"code":"0","msg":"success"}
```

### 7、返回某个speaker的声纹url路径

#### /voiceid/voice-url

* 登录鉴权同 [鉴权](#鉴权)
* GET请求

* 返回某个speaker的声纹url路径

##### 参数说明

| 参数字段 | 参数类型 | 必须 | 参数说明               |      |
| -------- | -------- | ---- | ---------------------- | ---- |
| org_id   | string   | 必须 | 某组织名称，如"abcpen" |      |
| tag_id   | string   | 必须 | 该组织下的tag          |      |
| spk-name | string   | 必须 | 某个体名称，如"sunny"  |      |

* 返回参数示例
```json
{"code":"0","msg":"success","data":{"audio_path":"https://zos.abcpen.com/voiceid/abcpen/20221223/7b88ac68-64a9-4bb6-9eef-74bb35954379.flac"}}
```
<br/>

## 四、错误码

返回的错误码，统一是字符串数字，比如“0", "10000"等。

| 错误码 | 描述                                                         | 说明                     | 处理方式                                                    |
| :----- | :----------------------------------------------------------- | :----------------------- | :---------------------------------------------------------- |
| 0      | success                                                      | 成功                     |                                                             |
| 10000  | in progress                                                  | 识别中                   | 请继续重试                                                  |
| 10105  | illegal access                                               | 没有权限                 | 检查apiKey，ip，ts等授权参数是否正确                        |
| 10106  | invalid parameter                                            | 无效参数                 | 上传必要的参数， 检查参数格式以及编码                       |
| 10107  | illegal parameter                                            | 非法参数值               | 检查参数值是否超过范围或不符合要求                          |
| 10109  | audio url is not valid http(s) url                           | audio_url不是http[s]链接 | 长语音识别的时候，audio_url必须是http[s]链接                |
| 10110  | no license                                                   | 无授权许可               | 检查参数值是否超过范围或不符合要求                          |
| 10700  | engine error                                                 | 引擎错误                 | 提供接口返回值，向服务提供商反馈                            |
| 10701  | Audio encode error, only support pcm, aac, mpeg2, opus and flac | 音频编码错误             | 支持pcm, aac, mpeg2, opus 和 flac这几种编码，请选择其中一种 |
| 16003  | basic component error                                        | 基础组件异常             | 重试或向服务提供商反馈                                      |
| 10800  | over max connect limit                                       | 超过授权的连接数         | 确认连接数是否超过授权的连接数                              |
