# [IT]第四次新人任务
 
 "
 本周的任务是了解并实现一个http服务器，以下是任务要求：
 
 >阅读http协议并了解基本的http请求以及其处理方式。
 >实现一个能用静态网页响应请求的http服务器。
 >优化你的服务器使之拥有更好的性能（在各种意义上），请不断尝试，注意你应该找到能够证明性能确实改善的方法。
 >（可选）为你的http服务器添加更多功能，如CGI，https支持等，并不断优化它。
 
 **注意：**
 >异常处理是十分重要的，不论是客户端还是服务器端造成的的错误都要正确的处理。
 >适当的参考是一个好办法，但请不要直接照抄网络上的代码或已有的库的代码。
 "
 
## 完成进度
 
 http和https同时在80和443端口进行
 将html文件中的静态网页返回给客户端 理论上可以支持所有的静态网页文件 支持get和post两种方式
 子线程处理优化,异步以后完成
 
## 文件信息
 
 * data2.py         处理后的 不同格式文件通过http发送的报头信息 和 信息反馈代码 的数据文件 包content_type, responses两个字典
 * origin_data.py   处理前的 数据
 * httpserver.py    服务器程序
 * html             放置html文件的文件夹
 * demoCA cacert.pem privkey.pem     用于ssl加密证书等文件夹和文件
 * old_vesion&reference              旧版本和参考文件
 
## 最后修改
 
 2014-12-25 19:00
 