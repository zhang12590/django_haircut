import pymysql
# coon = pymysql.connect('localhost','root','123456',charset='utf8')
# cur = coon.cursor()
# cur.execute('create database if not exists hair default charset utf8 collate utf8_general_ci;')
# coon.commit()
# cur.close()
# coon.close()
pymysql.install_as_MySQLdb()