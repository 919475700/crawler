from bs4 import BeautifulSoup
import requests
html="""
<!DOCTYPE html>
<html>
  <head>
    <link rel="canonical" href="https://blog.csdn.net/sinat_26917383/article/details/52205291"/> 
    <script type="text/javascript">
        var username = "sinat_26917383";
        var _blogger = username;
        var blog_address = "https://blog.csdn.net/sinat_26917383";
        var static_host = "https://csdnimg.cn/release/phoenix/";
        var currentUserName = ""; 
        var fileName = '52205291';
        var commentscount = 3;
        var islock = false;
        window.quickReplyflag = true;
        var totalFloor = 3;
        var isBole = false;
        var isDigg = false;
        var isExpert = false;
        var isAdm = false;
        var baiduKey = "";
        var needInsertBaidu = true;
        var isShowAds = true;
        var ChannelId = 0;
    </script>
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=Edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <meta name="apple-mobile-web-app-status-bar-style" content="black">
    <meta name="referrer" content="always">
    <script src="https://csdnimg.cn/public/common/libs/jquery/jquery-1.9.1.min.js" type="text/javascript"></script>
    <link rel="stylesheet" href="https://csdnimg.cn/public/static/css/avatar.css">
                <link rel="stylesheet" href="https://csdnimg.cn/release/phoenix/production/main-f869aa95a4.css">
          <link rel="stylesheet" href="https://csdnimg.cn/public/common/toolbar/content_toolbar_css/content_toolbar.css">

    <script src="https://csdnimg.cn/rabbit/exposure-click/main-1.0.5.js"></script>
    <script type="text/javascript" src="https://csdnimg.cn/pubfooter/js/tracking-1.0.2.js" charset="utf-8"></script>
    <script type="text/javascript" src="https://csdnimg.cn/release/phoenix/production/main-e96db8abdf.js"></script>

    <script src="https://dup.baidustatic.com/js/ds.js"></script>
    <script type="text/javascript">
        // Traffic Stats of the entire Web site By baidu
        var _hmt = _hmt || [];
        (function() {
            var hm = document.createElement("script");
            hm.src = "https://hm.baidu.com/hm.js?6bcd52f51e9b3dce32bec4a3997715ac";
            var s = document.getElementsByTagName("script")[0];
            s.parentNode.insertBefore(hm, s);
        })();
        // Traffic Stats of the entire Web site By baidu end
    </script>
    <meta name="description" content="准备放下R开始学python,真是痛苦，因为找个IDE都好麻烦，调用起来都没Rsudio那么好用。这个IDE下载模块比较方面，非常快


pycharm的下载与pandas安装：http://bbs.pinggu.org/thread-3633477-1-1.html


pycharm官方教学视频：链接：http://pan.baidu.com/s/1sl3WfGL 密码：03ho" />
    <meta name="keywords" content="pycharm,pandas" />
    <meta http-equiv="Cache-Control" content="no-siteapp" /><link rel="alternate" media="handheld" href="#" />
    <meta name="shenma-site-verification" content="5a59773ab8077d4a62bf469ab966a63b_1497598848">
    <title>python︱模块加载(pip安装)以及pycharm安装与报错解决方式 - CSDN博客</title>
    <link href="https://csdnimg.cn/public/favicon.ico" rel="SHORTCUT ICON">
                      <link rel="stylesheet" href="https://csdnimg.cn/release/phoenix/production/htmledit_views-0a60691e80.css">
            <style>
            .MathJax, .MathJax_Message, .MathJax_Preview{
                display: none
            }
      </style>
</head>
<body>
<script id="toolbar-tpl-scriptId" prod="download" skin="black" src="https://csdnimg.cn/public/common/toolbar/js/content_toolbar.js" type="text/javascript" domain="https://blog.csdn.net/"></script>
<div class="container clearfix">
  <main>
    <div style="display:none;">
      <img src="" onerror='setTimeout(function(){if(!/(csdn.net|iteye.com|baiducontent.com|googleusercontent.com|360webcache.com|sogoucdn.com|bingj.com|baidu.com)$/.test(window.location.hostname)){window.location.href="\x68\x74\x74\x70\x73\x3a\x2f\x2f\x77\x77\x77\x2e\x63\x73\x64\x6e\x2e\x6e\x65\x74"}},3000);'>
    </div>
    <article>
        <h1 class="csdn_top">python︱模块加载(pip安装)以及pycharm安装与报错解决方式</h1>
        <div class="article_bar clearfix">
            <div class="artical_tag">
                <span class="original">
                原创                </span>
                <span class="time">2016年08月14日 17:30:15</span>
            </div>

            <ul class="article_tags clearfix csdn-tracking-statistics tracking-click" data-mod="popu_377" >
                <li class="tit">标签：</li>

<!--          [startarticletags]-->
                                                            <li><a href="http://so.csdn.net/so/search/s.do?q=pycharm&t=blog" target="_blank">pycharm</a> <span>/</span></li>
                                            <li><a href="http://so.csdn.net/so/search/s.do?q=pandas&t=blog" target="_blank">pandas</a> <span>/</span></li>
                                            <li><a href="http://so.csdn.net/so/search/s.do?q=python&t=blog" target="_blank">python</a> <span>/</span></li>
                                            <li><a href="http://so.csdn.net/so/search/s.do?q=加载&t=blog" target="_blank">加载</a> <span>/</span></li>
                                            <li><a href="http://so.csdn.net/so/search/s.do?q=module&t=blog" target="_blank">module</a> <span>/</span></li>
                                    <!--          [endarticletags]-->
            </ul>
            <ul class="right_bar">
                <li><button class="btn-noborder"><i class="icon iconfont icon-read"></i><span class="txt">19685</span></button></li>
                <li class="edit">
                    <a class="btn-noborder" href="" >
                        <i class="icon iconfont icon-bianji"></i><span class="txt">编辑</span>
                    </a>
                </li>
                <li class="del">
                    <a class="btn-noborder" onclick="javascript:deleteArticle(fileName);return false;">
                        <i class="icon iconfont icon-shanchu"></i><span class="txt">删除</span>
                    </a>
                </li>
            </ul>
        </div>
"""
soup=BeautifulSoup(html,'lxml')#使用bs解析库快速解析html中的文本
print(soup.prettify())# 格式化代码
print(soup.title.string)#获取标题
print(soup.head)#获取头的所有信息
print(soup.a)#目前只匹配上的第一个
print(soup.a.attrs['href'])#匹配标签的属性-01
print(soup.a['href'])#匹配标签的属性-02
print(soup.body.h1)#嵌套获取标签
print(soup.ul.contents)#获取子节点-01 获取的是列表
print(soup.ul.children)#获取子节点-02  获取的是迭代器类型的对象地址
for i,child in enumerate(soup.ul.children):#获取子节点-03
    print(i,child) #利用迭代器一个个输出信息 共16行
for i,child in enumerate(soup.ul.descendants):#获取子节点和子孙节点-01
    print(i,child) #利用迭代器一个个输出信息 共42行
print(soup.a.parent)#获取父节点 也只是匹配第一个标签
print(list(enumerate(soup.h1.parent))) #获取祖父节点
print(list(enumerate(soup.title.previous_siblings)))#获取之前的兄弟节点标签
print(list(enumerate(soup.title.next_siblings)))#获取之后的兄弟节点标签
# 标准选择器的使用 find_all(name,attrs,recursive,text)/find(name,attrs,recursive,text)
print(soup.find_all('li'))#根据标签名查找 List对象
print(soup.find_all(attrs={'class','del'}))#根据属性名查找-01 List对象
print(soup.find_all(class_='del'))#根据属性名查找-02 List对象
print(soup.find_all(id="toolbar-tpl-scriptId"))#根据属性名查找-03  List对象
print(soup.find_all(text='编辑'))#根据内容找，但是获取不到位置，只获得了数量
# Css选择器的使用 select() 格式与css样式表中一样
print(soup.select('.del')) #选择class=del 获取标签
print(soup.select('#toolbar-tpl-scriptId')) #选择id=toolbar-tpl-scriptId 获取标签
print(soup.select('ul li')) #选择标签 获取标签
#获取标签内 内容与属性
for ul in soup.select('ul'):
    print(ul['class']) #属性
    print(ul.attrs['class'])#属性
for span in soup.select('span'):
    print(span.get_text()) #内容
# 网页实战：利用css选择器对一个html网页选取自己想要的内容
response =requests.get('https://hao.360.cn/?wd_xp1')
soup2=BeautifulSoup(response.text,'lxml')
for span in soup2.select('span'):
    print(span.get_text()) #内容
#成功打印出360导航中的span标签中的内容