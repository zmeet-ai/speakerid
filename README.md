

## 一、声纹识别优势

* **全球领先的声纹识别，返回结果字段中精准识别说话人ID**
* **庞大的声纹数据库，海量音视频文件中毫秒级返回说话人的片段音视频信息**
* 语音增强后的声纹，可抵抗各种背景噪音
* 可对人和各种生物体以及环境声如乐器等声音建立声纹

## 二、声纹识别API文档

### 1、接口说明

声纹识别，主要是根据用户传入的语音片段，识别出说话人id；在验证之前，客户需要注册某人的语音片段，便于检索的时候，返回该说话人身份。

### 2、接口参数规范

#### a 接口要求

集成实时语音转写API时，需按照以下要求。

| 内容     | 说明                                                         |
| :------- | ------------------------------------------------------------ |
| 请求协议 | http[s] (为提高安全性，强烈推荐https)                        |
| 请求地址 | http[s]://voiceid.abcpen.com *注：服务器IP不固定，为保证您的接口稳定，请勿通过指定IP的方式调用接口，使用域名方式调用* |
| 接口鉴权 | 签名机制，详见 [signa生成](#signa生成)                       |
| 响应格式 | 统一采用JSON格式                                             |
| 开发语言 | 任意，只要可以向笔声云服务发起http[s]请求的均可 

#### b 鉴权
* * 注意下述参数采用 **x-www-form-urlencoded** 表单方式提交

参数说明

| 参数  | 类型   | 必须 | 说明                                                | 示例                         |
| :---- | :----- | :--- | :-------------------------------------------------- | :--------------------------- |
| appid | string | 是   | 笔声开放平台应用ID                                  | 595f23df                     |
| ts    | string | 是   | 当前时间戳，从1970年1月1日0点0分0秒开始到现在的秒数 | 1512041814                   |
| signa | string | 是   | 加密数字签名（基于HMACSHA1算法）                    | IrrzsJeOFk1NGfJHW6SkHUoN9CU= |

#### c signa生成
* python示例

```python
import hashlib
import hmac
import time
import base64

def get_signature(timestamp, dev_id, dev_key):
    ts = str(timestamp)
    id_ts = str(dev_id) + ts
    signature = hmac.new(str(dev_key).encode(), id_ts.encode(),
                         digestmod=hashlib.sha256).hexdigest()
    return signature
```

#### d  返回值

结果格式为json，字段说明如下：

| 参数   | 类型   | 说明                                            |
| :----- | :----- | :---------------------------------------------- |
| code   | string | 结果码(具体见[错误码](#错误码))                 |
| data   | string | 结果数据                                        |
| msg   | string | 描述                                            |


### 3、注册声纹

####  /audio/register

##### 参数说明

| 参数字段 | 参数类型 | 必须                         | 参数说明                         |      |
| -------- | -------- | ---------------------------- | -------------------------------- | ---- |
| spk_name | string   | 必须                         | 声纹名称，如“张三”               |      |
| app_id   | string   | 必须                         | 自己的应用id                     |      |
| tag_id   | string   | 否                           | 标签，用于自定义字段 |      |
| audio    | 声音内容 | 采样率16k、位长16bit、单声道 | 声音内容，可以是文件或者url链接  |      |

* 上传某人的语音片段，以注册该说话人的身份。 其中，**spk_name**字段，是在您的组织（app_id)下的某个特定人的名称，您须要确保对其命名的唯一性。 **tag_id**是附属扩展字段，是伴随spk_name而来的扩展可选字段信息。
* 采用 x-www-form-urlencoded 表单方式提交

### 4、搜素声纹

#### /audio/search
##### 参数说明

| 参数字段 | 参数类型 | 必须                         | 参数说明                        |      |
| -------- | -------- | ---------------------------- | ------------------------------- | ---- |
| app_id   | string   | 必须                         | 自己的应用id                    |      |
| audio    | 声音内容 | 采样率16k、位长16bit、单声道 | 声音内容，可以是文件或者url链接 |      |

* 采用 x-www-form-urlencoded 表单方式提交
* 返回示例(返回最接近该声纹的前十条数据)

```json
[["https://translate.abcpen.com/data?audio_path=dataset/777-126732-0003.flac",["777-126732-0003.flac",100.0,null,null,null]],["https://translate.abcpen.com/data?audio_path=dataset/777-126732-0004.flac",["777-126732-0004.flac",100.0,null,null,null]],["https://translate.abcpen.com/data?audio_path=dataset/3752-4944-0011.flac",["3752-4944-0011.flac",39.53543305397034,null,null,null]],["https://translate.abcpen.com/data?audio_path=dataset/2086-149214-0001.flac",["2086-149214-0001.flac",-47.27879762649536,null,null,null]],["https://translate.abcpen.com/data?audio_path=dataset/3752-4943-0003.flac",["3752-4943-0003.flac",-71.01322412490845,null,null,null]],["https://translate.abcpen.com/data?audio_path=dataset/2078-142845-0001.flac",["2078-142845-0001.flac",-73.0065107345581,null,null,null]],["https://translate.abcpen.com/data?audio_path=dataset/2086-149220-0003.flac",["2086-149220-0003.flac",-81.18547201156616,null,null,null]],["https://translate.abcpen.com/data?audio_path=dataset/1993-147964-0002.flac",["1993-147964-0002.flac",-82.17806816101074,null,null,null]],["https://translate.abcpen.com/data?audio_path=dataset/2086-149214-0002.flac",["2086-149214-0002.flac",-82.7784776687622,null,null,null]]]
```

### 5、删除声纹

#### /voiceid/del
##### 参数说明

| 参数字段 | 参数类型 | 必须 | 参数说明           |      |
| -------- | -------- | ---- | ------------------ | ---- |
| spk_name | string   | 必须 | 声纹名称，如“张三” |      |
| app_id   | string   | 必须 | 自己的应用id       |      |


### 6、声纹数量
### /voiceid/count

### 7、声纹列表

### /voiceid/list


## 错误码

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
