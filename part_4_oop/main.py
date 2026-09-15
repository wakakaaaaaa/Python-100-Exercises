"""
To-Do List项目的主应用文件。
这个文件将在多个练习中被逐步修改。
"""
# from fastapi import FastAPI
# from pydantic import BaseModel
# from fastapi import HTTPException
#
# # FastAPI应用实例
#
# '''51'''
# app = FastAPI()
#
# @app.get('/zr')
# def root():
#     return {"message": "Hello, World!"}
#
# '''52'''
# class Todo(BaseModel):
#     id : int | None = None
#     title :str
#     completed : bool
#
# db = [
#     Todo(id = 3 ,title = '做早操' , completed = False),
#
# ]
#
# '''53'''
# @app.get('/todos')
# def todofuc():
#     return db
#
# '''54'''
# @app.post('/todos',status_code = 201)
# def creattodo(todo:Todo):
#     new_id = len(db) + 1
#     new_todo = Todo(id = new_id,title = todo.title,completed = todo.completed)
#     db.append(new_todo)
#     return new_todo
#
# '''55'''
# @app.get('/todos/{todo_id}',response_model = Todo)
# def get_single_todo(todo_id:int):
#     for todo in db:
#         if todo.id == todo_id:
#             return todo
#     raise HTTPException(status_code = 404,detail = 'Todo not found')
#
# '''56'''
#
# class ToDoUpdate(BaseModel):
#     id : int | None = None
#     title : str | None = None
#     completed : bool | None = None
#
# @app.put('/todos/{todo_id}',response_model=Todo)
# def update_todo(todo_id:int,update_info:ToDoUpdate):
#     #1.查找对应Id的todo对象
#     target_todo = None
#     for todo in db:
#         if todo.id == todo_id:
#             target_todo = todo
#             break
#
#     #2.找不到对应id，返回404
#     if target_todo is None:
#         raise HTTPException(status_code = 404 ,detail = '您要更新的代办事项不存在')
#
#     #3.更新用户传的代办事项字段
#     update_dict = update_info.model_dump(exclude_none = True)
#     for key , value in update_dict.items():
#         setattr(target_todo,key,value)
#
#     return target_todo
#
#
# '''57'''
# @app.delete( '/todos/{todo_id}')
# def delete_todo(todo_id:int):
#     for todo in db:
#         if todo.id == todo_id:
#             db.remove(todo)
#             return {"message": "Todo deleted"}
#     raise HTTPException(status_code = 404)

# 练习代码将由用户在此处添加

from fastapi import FastAPI
from pydantic import BaseModel,Field
from fastapi import HTTPException
from typing import Optional,List
app = FastAPI()

#基础Todo类
class Todo(BaseModel):
    id:int|None = None
    title:str = Field(...,min_length = 1)
    completed:bool

#更新时使用的TodoUpdate类
class TodoUpdate(BaseModel):
    id:int |None = None
    title:str |None = None
    completed:bool |None = None

#封装所有db操作的TodoRepository类
class TodoRepository:
    def __init__(self):
        #将原来的全局db移动到类内部，不懂为什么这样可以移动到类内部
        self.db = [
        ]

    #1.查询全部todo信息
    #不懂
    def get_all_todos(self,completed:bool | None = None):
        if completed is True:
            return [item for item in self.db if item.completed is True]
        elif completed is False:
            return [item for item in self.db if item.completed is False]
        else:
            result = self.db
        return result




    #2.新增新的todo信息
    def create(self,todo:Todo):
        new_id = len(self.db) + 1
        new_todo = Todo(id = new_id,title = todo.title,completed = todo.completed)
        self.db.append(new_todo)
        return new_todo

    #3.查询Todo,根据id
    def get_by_id(self,todo_id:int):
        for todo in self.db:
            if todo.id == todo_id:
                return todo
        return None

    #4.更新todo信息，可以局部更新
    def update(self,todo_id:int,update_info:TodoUpdate):
        target_todo = self.get_by_id(todo_id)
        if target_todo is None:
            return None
        update_dict = update_info.model_dump(exclude_none = True)
        for key,value in update_dict.items():
            setattr(target_todo,key,value)
        return target_todo

    #5.删除todo,根据id，成功返回T入俄，找不到返回False
    def delete(self,todo_id:int):
        todo = self.get_by_id(todo_id)
        if todo is None:
            return False
        self.db.remove(todo)
        return True

#实例化仓库对象
repo = TodoRepository()
db = repo.db

#-----------------路由层，只处理HTTP，不再直接操作DB列表
#不懂
@app.get('/todos',response_model = List[Todo])
def todofuc(completed:Optional[bool] = None):
    return repo.get_all_todos(completed = completed)

@app.post('/todos',status_code = 201)
def creattodo(todo:Todo):
    return repo.create(todo)

@app.get('/todos/{todo_id}',response_model = Todo)
def get_single_todo(todo_id:int):
    todo = repo.get_by_id(todo_id(todo_id))#2.这个是干什么的？
    todo = repo.get_by_id(todo_id)
    if todo is None:
        raise HTTPException(status_code = 404,detail= 'Todo not found')
        return todo

@app.put('/todos/{todo_id',response_model = Todo)
def update_todo(todo_id:int,update_info :TodoUpdate):
    todo = repo.update(todo_id,update_info)
    if todo is None:
        raise HTTPException(status_code =404,detail = '您要更新的代办事项不存在')
    return todo
@app.delete('/todos/{todo_id')
def delete_todo(todo_id:int):
    ok = repo.delete(todo_id)
    if not ok:
        raise HTTPException(status_code = 404)
    return {"message":"Todo deleted"}