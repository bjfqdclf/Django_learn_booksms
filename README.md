# 实现功能

基于多表的书籍管理系统

- 查看数据库书籍![查看数据库书籍](https://user-images.githubusercontent.com/45928505/137116854-c3b6b7e9-ea6b-44c8-8d90-1448a9a6c35d.png)
- 添加书籍![添加书籍](https://user-images.githubusercontent.com/45928505/137116791-394e3ab0-cefc-40c9-921e-e2d729b16095.png)
- 修改书籍信息![修改书籍信息](https://user-images.githubusercontent.com/45928505/137116920-8eabc048-b41b-4d92-bacc-9a3d81ca3a64.png)

# 数据库信息
- 采用mysql数据库
- 数据库配置: Bookms/settings.py 中的 DATABASES 字典
- 数据库迁移：```import pymysql```
```pymysql.install_as_MySQLdb()```
