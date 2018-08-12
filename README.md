#### 唐诗宋词 API

基于Django2.0和Djangorestframework的api，数据来源于[**chinese-poetry**][https://github.com/chinese-poetry/chinese-poetry]

##### 使用方法

```
# 虚拟环境
python3 -m venv venv
source venv/bin/activate

# 安装依赖包
pip install requirements.txt

# 生成数据库
$ mysql -u root -p
mysql>source poetry_story.sql

# 迁移数据
cd poetry
python manage.py makemigrations
python manage.py migrate

# 本地调试
python manage.py runserver
```
> 目前还很简陋，to be continued...


