#encoding:utf-8

"""
正则表达式练习:基本上所有的都用到了
"""

"""
最简单的正则表达式是普通字符串，可以匹配自身
'[pjc]ython'可以匹配'python'、'jython'、'cython'
'[a-zA-Z0-9]'可以匹配一个任意大小写字母或数字
'[^abc]'可以一个匹配任意除'a'、'b'、'c'之外的字符
'python|perl'或'p(ython|erl)'都可以匹配'python'或'perl'
子模式后面加上问号表示可选。r'(http://)?(www\.)?python\.org'只能匹配'http://www.python.org'、'http://python.org'、'www.python.org'和'python.org'
'^http'只能匹配所有以'http'开头的字符串
(pattern)*：允许模式重复0次或多次
(pattern)+：允许模式重复1次或多次
(pattern){m,n}：允许模式重复m~n次

'(a|b)*c'：匹配多个（包含0个）a或b，后面紧跟一个字母c。
'ab{1,}'：等价于'ab+'，匹配以字母a开头后面带1个至多个字母b的字符串。
'^[a-zA-Z]{1}([a-zA-Z0-9._]){4,19}$'：匹配长度为5-20的字符串，必须以字母开头、可带数字、“_”、“.”的字串。
'^(\w){6,20}$'：匹配长度为6-20的字符串，可以包含字母、数字、下划线。
'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'：检查给定字符串是否为合法IP地址。
'^(13[4-9]\d{8})|(15[01289]\d{8})$'：检查给定字符串是否为移动手机号码。
'^[a-zA-Z]+$'：检查给定字符串是否只包含英文字母大小写。
'^\w+@(\w+\.)+\w+$'：检查给定字符串是否为合法电子邮件地址


'^(\-)?\d+(\.\d{1,2})?$'：检查给定字符串是否为最多带有2位小数的正数或负数。
'[\u4e00-\u9fa5]'：匹配给定字符串中所有汉字。
'^\d{18}|\d{15}$'：检查给定字符串是否为合法身份证格式。
'\d{4}-\d{1,2}-\d{1,2}'：匹配指定格式的日期，例如2016-1-31。
'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[,._]).{8,}$'：检查给定字符串是否为强密码，必须同时包含英语字母大写字母、英文小写字母、数字或特殊符号（如英文逗号、英文句号、下划线），并且长度必须至少8位。
"(?!.*[\'\"\/;=%?]).+"：如果给定字符串中包含’、”、/、;、=、%、?则匹配失败。
'(.)\\1+'：匹配任意字符的一次或多次重复出现。
'((?P<f>\b\w+\b)\s+(?P=f))'：匹配连续出现两次的单词。
'((?P<f>.)(?P=f)(?P<g>.)(?P=g))'：匹配AABB形式的成语或字母组合。


"""

