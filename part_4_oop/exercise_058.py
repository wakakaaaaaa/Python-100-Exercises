"""
题目 058: 将数据库逻辑重构到单独的类中

要求:
这是一个代码重构练习。修改 `part_4_oop/main.py`。
1. 创建一个 `TodoRepository` 类。
2. 将所有直接操作 `db` 列表的逻辑（增、删、改、查）移入这个类的方法中。
3. 在API路由函数中，实例化 `TodoRepository` 并调用其方法来完成工作。

提示:
目标是让路由函数更简洁，只负责处理HTTP请求和响应，而数据操作则委托给Repository。
"""
# from fastapi import FastAPI
# from pydantic import BaseModel
# from fastapi import HTTPException
#
# app = FastAPI()
#
# #基础Todo类
# class Todo(BaseModel):
#     id:int|None = None
#     title:str
#     completed:bool
#
# #更新时使用的TodoUpdate类
# class TodoUpdate(BaseModel):
#     id:int |None = None
#     title:str |None = None
#     completed:bool |None = None
#
# #发封装所有db操作的TodoRepository类
# class TodoRepository:
#     def __init__(self):
#         #将原来的全局db移动到类内部，不懂为什么这样可以移动到类内部
#         self.db = [
#             Todo(id = 3 ,title = '做早操' ,completed = False)
#         ]
#
#     #1.查询全部todo信息
#     def get_all(self):
#         return self.db
#
#     #2.新增新的todo信息
#     def create(self,todo:Todo):
#         new_id = len(self.db) + 1
#         new_todo = Todo(id = new_id,title = todo.title,completed = todo.completed)
#         self.db.append(new_todo)
#         return new_todo
#
#     #3.查询Todo,根据id
#     def get_by_id(self,todo_id:int):
#         for todo in self.db:
#             if todo.id == todo_id:
#                 return todo
#         return None
#
#     #4.更新todo信息，可以局部更新
#     def update(self,todo_id:int,update_info:TodoUpdate):
#         target_todo = self.get_by_id(todo_id)
#         if target_todo is None:
#             return None
#         update_dict = update_info.model_dump(exclude_none = True)
#         for key,value in update_dict.items():
#             setattr(target_todo,key,value)
#         return target_todo
#
#     #5.删除todo,根据id，成功返回T入俄，找不到返回False
#     def delete(self,todo_id:int):
#         todo = self.get_by_id(todo_id)
#         if todo is None:
#             return False
#         self.db.remove(todo)
#         return True
#
# #实例化仓库对象
# repo = TodoRepository()
#
# #-----------------路由层，只处理HTTP，不再直接操作DB列表
# @app.get('/todos')
# def todofuc():
#     return repo.get_all()
#
# @app.post('/todos',status_code = 201)
# def creattodo(todo:Todo):
#     return repo.create(todo)
#
# @app.get('/todos/{todo_id}',response_model = Todo)
# def get_single_todo(todo_id:int):
#     todo = repo.get_by_id(todo_id(todo_id))#2.这个是干什么的？
#     todo = repo.get_by_id(todo_id)
#     if todo is None:
#         raise HTTPException(status_code = 404,detail= 'Todo not found')
#         return todo
#
# @app.put('/todos/{todo_id',response_model = Todo)
# def update_todo(todo_id:int,update_info :TodoUpdate):
#     todo = repo.update(todo_id,update_info)
#     if todo is None:
#         raise HTTPException(status_code =404,detail = '您要更新的代办事项不存在')
#     return todo
# @app.delete('/todos/{todo_id')
# def delete_todo(todo_id:int):
#     ok = repo.delete(todo_id)
#     if not ok:
#         raise HTTPException(status_code = 404)
#     return {"message":"Todo deleted"}
