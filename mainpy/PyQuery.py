from pyquery import PyQuery as pq
from lxml import etree
html="""
<div xmlns="http://www.w3.org/1999/xhtml" class="c_fn"><i class="icon "></i>
				<a href="/file/9735014.html" target="_blank" title="97  插入java 小程序avi">97  插入java 小程序avi</a>
				</div>
"""
# doc = pq(etree.fromstring(html))# 格式化
doc =pq(html) #同BS库一样获取解析对象 文本初始化
# doc =pq(url='http://fanyi.baidu.com/') #使用Url初始化
# doc =pq(filename='1.html') #读取文件并初始化
# print(doc('a')) #Css选择器 基本选择所有a标签
# print(doc('._blank')) #Css选择器 基本选择所有_blank类
# print(doc('#123')) #Css选择器 基本选择所有123id
# a=doc('a')
# print(a.find('p')) #查找子元素（常用）
# print(a.parent())  #查找父元素
# print(a.parents())  #查找祖父元素

# （重点）可以利用网页审查元素获取Css selector值
# print(doc)
# print(doc('div').find('a')) #获取标签元素
d=pq("<div xmlns='http://www.w3.org/1999/xhtml' class='c_fn'><i class='icon '></i><a href='/file/9735014.html' target='_blank' title='97  插入java 小程序avi'>97  插入java 小程序avi</a></div>")
print(d('div').find('a'))#返回[<p#1>, <p.2>]
print(d('div').find('a').eq(0))#返回[<p#1>]
# print(img.attr.href) #获取属性元素
# print(img.text()) #获取内容
# print(img.html()) #获取其中的html代码

#（重点）可以使用DOM操作对html修改
# logolist=doc('.logolist')
# logolist.add_class('lalalala') #增加class
# print(logolist)
# logolist.remove_class('lalalala') #减少class
# print(logolist)
# ids=doc('#123')
# print(ids.attr('target','myhappy')) #修改属性值
# print(ids.css('','')) #可以修改CSS属性
# ids.remove() #删除标签

# 伪类选择器
# 见W3c中的各种伪类选择器
# a:link {color:#FF0000;} /* 未访问的链接 */
# a:visited {color:#00FF00;} /* 已访问的链接 */
# a:hover {color:#FF00FF;} /* 鼠标划过链接 */
# a:active
# :checked	input:checked	选择所有选中的表单元素
# :disabled	input:disabled	选择所有禁用的表单元素
# :empty	p:empty	选择所有没有子元素的p元素
# :enabled	input:enabled	选择所有启用的表单元素
# :first-of-type	p:first-of-type	选择每个父元素是p元素的第一个p子元素
# :in-range	input:in-range	选择元素指定范围内的值
# :invalid	input:invalid	选择所有无效的元素
# :last-child	p:last-child	选择所有p元素的最后一个子元素
# :last-of-type	p:last-of-type	选择每个p元素是其母元素的最后一个p元素
# :not(selector)	:not(p)	选择所有p以外的元素
# :nth-child(n)	p:nth-child(2)	选择所有p元素的第二个子元素
# :nth-last-child(n)	p:nth-last-child(2)	选择所有p元素倒数的第二个子元素
# :nth-last-of-type(n)	p:nth-last-of-type(2)	选择所有p元素倒数的第二个为p的子元素
# :nth-of-type(n)	p:nth-of-type(2)	选择所有p元素第二个为p的子元素
# :only-of-type	p:only-of-type	选择所有仅有一个子元素为p的元素
# :only-child	p:only-child	选择所有仅有一个子元素的p元素
# :optional	input:optional	选择没有"required"的元素属性
# :out-of-range	input:out-of-range	选择指定范围以外的值的元素属性
# :read-only	input:read-only	选择只读属性的元素属性
# :read-write	input:read-write	选择没有只读属性的元素属性
# :required	input:required	选择有"required"属性指定的元素属性
# :root	root	选择文档的根元素
# :target	#news:target	选择当前活动#news元素(点击URL包含锚的名字)
# :valid	input:valid	选择所有有效值的属性
# :link	a:link	选择所有未访问链接
# :visited	a:visited	选择所有访问过的链接
# :active	a:active	选择正在活动链接
# :hover	a:hover	把鼠标放在链接上的状态
# :focus	input:focus	选择元素输入后具有焦点
# :first-letter	p:first-letter	选择每个<p> 元素的第一个字母
# :first-line	p:first-line	选择每个<p> 元素的第一行
# :first-child	p:first-child	选择器匹配属于任意元素的第一个子元素的 <p> 元素
# :before	p:before	在每个<p>元素之前插入内容
# :after  p:after 在每个<p>元素之后插入内容