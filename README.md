# djangoweb
djiango服务测试项目



# 如何开始构建脚手架
pip install django==1.11.16

#想要在这个目录配置这些综合管理目录，后面就需要指定东西  .点，点代表当前目录中构建django的脚手架文件，一旦目录不对，会影响整个根目录和入口的
python manage.py startproject xxx项目名  .

#管理目录里的4个文件很重要，init告诉是个包，setting全局配置，urls做路由映射，wsgi（是wsgi要用的），开发中最关注的时候settings和urls**

#mysql数据库驱动
pip install mysqlclient

#创建跟用户相关的app
python manage.py startapp user

#做迁移，会将你所有应用中的model类，解析model类，生成相应的文件，要生成一批迁移，因为所有的应用可能都写了model**

python manage.py makemigrations

#这个会把应用里生成的迁移文件，会把这些迁移文件真正的生成数据库里的表，如果类发生了变化，还会再次生成一个变化 迁移文件，这时候再做迁移，就做表的alter table**
python manage.py  migrate

#创建superuser  admin 1122360asd
python manage.py  createsuperuser



#运行服务，默认启动8000端口
python manage.py  runserver

#models是跟数据库打交道的，tests测试的，views是后面要写的，请求来了如何response的，做视图的就是给人看**