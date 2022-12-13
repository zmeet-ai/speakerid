

## ZmeetAI 语音识别优势

* **全球领先的声纹识别，返回结果字段中精准识别说话人ID**
* **庞大的声纹数据库，海量音视频文件中毫秒级返回说话人的片段音视频信息**
* **全球领先的降噪算法，返回的音视频文件，可包含降噪后的清晰语音**
* **全球领先的高精准中英文等语音识别算法**

**目前仅注册声纹和搜索声纹支持**， 别的api等待发布

## 注册声纹

###  /audio/register

### 参数说明

| 参数字段 | 参数类型 | 必须                         | 参数说明                         |      |
| -------- | -------- | ---------------------------- | -------------------------------- | ---- |
| spk_name | string   | 必须                         | 声纹名称，如“张三”               |      |
| app_id   | string   | 必须                         | 自己的应用id                     |      |
| tag_id   | string   | 否                           | 标签，用于自定义字段 |      |
| audio    | 声音内容 | 采样率16k、位长16bit、单声道 | 声音内容，可以是文件或者url链接  |      |

* 该功能目前支持（20221213）
* 采用 x-www-form-urlencoded 表单方式提交

## 搜素声纹

### /audio/search
### 参数说明

| 参数字段 | 参数类型 | 必须                         | 参数说明                        |      |
| -------- | -------- | ---------------------------- | ------------------------------- | ---- |
| app_id   | string   | 必须                         | 自己的应用id                    |      |
| audio    | 声音内容 | 采样率16k、位长16bit、单声道 | 声音内容，可以是文件或者url链接 |      |

* 该功能目前支持（20221213）
* 采用 x-www-form-urlencoded 表单方式提交
* 返回示例(返回最接近该声纹的前十条数据)
```json
[["https://translate.abcpen.com/data?audio_path=dataset/777-126732-0003.flac",["777-126732-0003.flac",100.0,null,null,null]],["https://translate.abcpen.com/data?audio_path=dataset/777-126732-0004.flac",["777-126732-0004.flac",100.0,null,null,null]],["https://translate.abcpen.com/data?audio_path=dataset/3752-4944-0011.flac",["3752-4944-0011.flac",39.53543305397034,null,null,null]],["https://translate.abcpen.com/data?audio_path=dataset/2086-149214-0001.flac",["2086-149214-0001.flac",-47.27879762649536,null,null,null]],["https://translate.abcpen.com/data?audio_path=dataset/3752-4943-0003.flac",["3752-4943-0003.flac",-71.01322412490845,null,null,null]],["https://translate.abcpen.com/data?audio_path=dataset/2078-142845-0001.flac",["2078-142845-0001.flac",-73.0065107345581,null,null,null]],["https://translate.abcpen.com/data?audio_path=dataset/2086-149220-0003.flac",["2086-149220-0003.flac",-81.18547201156616,null,null,null]],["https://translate.abcpen.com/data?audio_path=dataset/1993-147964-0002.flac",["1993-147964-0002.flac",-82.17806816101074,null,null,null]],["https://translate.abcpen.com/data?audio_path=dataset/2086-149214-0002.flac",["2086-149214-0002.flac",-82.7784776687622,null,null,null]]]
```

## 删除声纹

### /voiceid/del
### 参数说明

| 参数字段 | 参数类型 | 必须 | 参数说明           |      |
| -------- | -------- | ---- | ------------------ | ---- |
| spk_name | string   | 必须 | 声纹名称，如“张三” |      |
| app_id   | string   | 必须 | 自己的应用id       |      |


## 声纹数量
### /voiceid/count

## 声纹列表

### /voiceid/list




## 接口Demo

目前仅提供部分开发语言的demo，其他语言请参照下方接口文档进行开发。

## 接口参数规范

集成实时语音转写API时，需按照以下要求。

| 内容     | 说明                                                         |
| :------- | ------------------------------------------------------------ |
| 请求协议 | http[s] (为提高安全性，强烈推荐https)                        |
| 请求地址 | http[s]://ai.abcpen.com/v1/asr/long?{请求参数} *注：服务器IP不固定，为保证您的接口稳定，请勿通过指定IP的方式调用接口，使用域名方式调用* |
| 接口鉴权 | 签名机制，详见 [signa生成](#signa生成)                       |
| 响应格式 | 统一采用JSON格式                                             |
| 开发语言 | 任意，只要可以向笔声云服务发起HTTP请求的均可                 |
| 语言种类 | 中文普通话、中英混合识别、英文                               |



## 接口调用流程

*注：* 若需配置IP白名单，请发送邮件到support@abcpen.com
* * 注意下述参数采用 **x-www-form-urlencoded** 表单方式提交

参数说明

| 参数  | 类型   | 必须 | 说明                                                | 示例                         |
| :---- | :----- | :--- | :-------------------------------------------------- | :--------------------------- |
| appid | string | 是   | 笔声开放平台应用ID                                  | 595f23df                     |
| ts    | string | 是   | 当前时间戳，从1970年1月1日0点0分0秒开始到现在的秒数 | 1512041814                   |
| signa | string | 是   | 加密数字签名（基于HMACSHA1算法）                    | IrrzsJeOFk1NGfJHW6SkHUoN9CU= |

#### signa生成

1.获取baseString，baseString由app_id和当前时间戳ts拼接而成，假如app_id为595f23df，ts为1512041814，则baseString为

> 595f23df1512041814

2.对baseString进行MD5，假如baseString为上一步生成的595f23df1512041814，MD5之后则为

> 0829d4012497c14a30e7e72aeebe565e

3.以app_secret为key对MD5之后的baseString进行HmacSHA1加密，然后再对加密后的字符串进行base64编码。
假如app_secret为d9f4aa7ea6d94faca62cd88a28fd5234，MD5之后的baseString为上一步生成的0829d4012497c14a30e7e72aeebe565e，
则加密之后再进行base64编码得到的signa为

> IrrzsJeOFk1NGfJHW6SkHUoN9CU=

备注：

- app_secret：接口密钥，在应用中添加实时语音转写服务时自动生成，调用方注意保管；
- signa的生成公式：HmacSHA1(MD5(app_id + ts), app_secret)，具体的生成方法参考本git实例代码；


#### 返回值

结果格式为json，字段说明如下：

| 参数 | 类型   | 说明                            |
| :--- | :----- | :------------------------------ |
| code | string | 结果码(具体见[错误码](#错误码)) |
| data | string | 结果数据                        |
| desc | string | 描述                            |

其中sid字段主要用于DEBUG追查问题，如果出现问题，可以提供sid帮助确认问题。





#### 接收错误信息

交互过程中，在服务端出现异常而中断服务时（如会话超时），会将异常信息以 text message 形式返回给客户端并关闭连接。

## 白名单

在调用该业务接口时

- 若关闭IP白名单，接口认为IP不限，不会校验IP。
- 若打开IP白名单，则服务端会检查调用方IP是否在笔声开放平台配置的IP白名单中，对于没有配置到白名单中的IP发来的请求，服务端会拒绝服务。

IP白名单规则

- IP白名单，在 控制台-我的应用-相应服务的应用管理卡片上 编辑，保存后五分钟左右生效；
- 不同Appid的不同服务都需要分别设置IP白名单；
- IP白名单需设置为外网IP，请勿设置局域网IP。
- 如果服务器返回结果如下所示(illegal client_ip)，则表示由于未配置IP白名单或配置有误，服务端拒绝服务。

```json
{
	"action": "error",
	"code": "10105",
	"data": "",
	"desc": "illegal access|illegal client_ip: xx.xx.xx.xx",
	"sid": "rta..."
}
```

## 错误码

| 错误码 | 描述                                                         | 说明                     | 处理方式                                                    |
| :----- | :----------------------------------------------------------- | :----------------------- | :---------------------------------------------------------- |
| 0      | success                                                      | 成功                     |                                                             |
| -1     | in progress                                                  | 识别中                   | 请继续重试                                                  |
| -2     | audio encode error                                           | 音频编码错误             | 请编码成正确的格式，再提交请求                              |
| 10105  | illegal access                                               | 没有权限                 | 检查apiKey，ip，ts等授权参数是否正确                        |
| 10106  | invalid parameter                                            | 无效参数                 | 上传必要的参数， 检查参数格式以及编码                       |
| 10107  | illegal parameter                                            | 非法参数值               | 检查参数值是否超过范围或不符合要求                          |
| 10109  | audio url is not valid http(s) url                           | audio_url不是http[s]链接 | 长语音识别的时候，audio_url必须是http[s]链接                |
| 10110  | no license                                                   | 无授权许可               | 检查参数值是否超过范围或不符合要求                          |
| 10700  | engine error                                                 | 引擎错误                 | 提供接口返回值，向服务提供商反馈                            |
| 10701  | Audio encode error, only support pcm, aac, mpeg2, opus and flac | 音频编码错误             | 支持pcm, aac, mpeg2, opus 和 flac这几种编码，请选择其中一种 |
| 10702  | Audio sample error, only support 8000、16000、44100 and 48000 Hz | 音频采样率错误           | 支持 8000、16000、44100 和 48000 Hz，请选择其中一种         |
| 10202  | websocket connect error                                      | websocket连接错误        | 检查网络是否正常                                            |
| 10204  | websocket write error                                        | 服务端websocket写错误    | 检查网络是否正常，向服务提供商反馈                          |
| 10205  | websocket read error                                         | 服务端websocket读错误    | 检查网络是否正常，向服务提供商反馈                          |
| 16003  | basic component error                                        | 基础组件异常             | 重试或向服务提供商反馈                                      |
| 10800  | over max connect limit                                       | 超过授权的连接数         | 确认连接数是否超过授权的连接数                              |
