# [IT]第四次新人任务
 
 **实现一个http服务器**
 
## 完成进度
 
 - 1.http和https同时在80和443端口进行
 - 2.将html文件中的静态网页返回给客户端 理论上可以支持所有的静态网页文件 支持get和post两种方式
 - 3.子线程处理优化,异步以后完成
 
## 文件信息
 
 * data2.py         处理后的 不同格式文件通过http发送的报头信息 和 信息反馈代码 的数据文件 包content_type, responses两个字典
 * origin_data.py   处理前的 数据
 * httpserver.py    服务器程序
 * html             放置html文件的文件夹
 * demoCA cacert.pem privkey.pem     用于ssl加密证书等文件夹和文件
 * old_vesion&reference              旧版本和参考文件
 
## 最后修改
 
 2014-12-25 19:00
 
