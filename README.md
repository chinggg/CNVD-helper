# CNVD-helper

一个辅助提交 CNVD/CNNVD/CVE 漏洞的工具

## 背景

工业和信息化部、国家互联网信息办公室、公安部三部门联合印发[《网络产品安全漏洞管理规定》](http://www.gov.cn/zhengce/zhengceku/2021-07/14/content_5624965.htm)，自2021年9月1日起施行。

![](http://www.huiyelaw.com/images/upload/20210719/154327131681.png)

而提交 CNVD 需要的步骤较为繁琐，不仅要填写网页表单，还要填写 Word 模板并上传压缩包。

上传压缩包文件结构如下：
```
[通用型漏洞名称]
├── email.txt
├── [通用型漏洞名称].docx
└── [通用型漏洞名称](说明：以漏洞名称命名的POC、验证录像ZIP格式整合压缩文件).zip
```

有时需要向多个平台提交漏洞，所需材料相互交叉，不易管理。

使用本工具后，对某一漏洞只需填写一份配置文件，即可：

- 根据 CNNVD 提供的 docx 模板自动生成漏洞提交表
- 生成自动提交 CNVD 网页表单的 JavaScript 代码
- 生成自动提交 CVE 网页表单的 JavaScript 代码

## 使用方法

1. 在 `conf/` 下复制配置文件并填写内容
2. 执行 `python main.py --conf 配置名称`
3. 自动生成对应目录及文件，自行添加附件内容并打包即可

CNVD/CNNVD 区分通用型和事件型漏洞，目前只适配通用型漏洞的模板和表单。

## 参考

[《网络产品安全漏洞管理规定》](http://www.gov.cn/zhengce/zhengceku/2021-07/14/content_5624965.htm)

[国家信息安全漏洞库 (cnnvd.org.cn)](http://www.cnnvd.org.cn/web/wz/tzdym.tag?sign=addvulnerability)

[CNNVD漏洞命名规范](http://www.cnnvd.org.cn/web/wz/bzxqById.tag?id=4&mkid=4)

[CNNVD漏洞分类指南](http://www.cnnvd.org.cn/web/wz/bzxqById.tag?id=3&mkid=3)

[CNNVD漏洞分级规范](http://www.cnnvd.org.cn/web/wz/bzxqById.tag?id=2&mkid=2)
