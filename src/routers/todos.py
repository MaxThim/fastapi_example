from fastapi import FastAPI, HTTPException, status, APIRouter
from pydantic import BaseModel
from models import Todo

router = APIRouter(
    prefix="/todos",
)

todos: list[Todo] = [
    Todo(id=0, task="Buy groceries"),
    Todo(id=1, task="Do laundry"),
    Todo(id=2, task="Clean house"),
]

# Get all todos
@router.get("")
async def get_todos() -> dict[str, list[Todo]]:
    return {"todos": todos}

# Get single todo
@router.get("/{todo_id}")
async def get_todo(todo_id: int) -> dict[int, Todo]:
    for todo in todos:
        if todo.id == todo_id:
            return {todo_id: todo}
    raise HTTPException(status_code=404, detail=f"Todo not found with id: {todo_id}")

# Create a todo
@router.post("", status_code=status.HTTP_201_CREATED)
async def create_todo(todo: Todo) -> dict[str, str]:
    todos.append(todo)
    return {"message": "Todo has been added"}

# Update a todo
@router.put("/{todo_id}")
async def update_todo(todo_id: int, todo: Todo) -> dict[str, str]:
    for todo_item in todos:
        if todo_item.id == todo_id:
            todo_item.id = todo.id
            todo_item.task = todo.task
            return {"message": "Todo has been updated"}
    raise HTTPException(status_code=404, detail=f"Todo not found with id: {todo_id}")

# Delete a todo
@router.delete("/{todo_id}")
async def delete_todo(todo_id: int) -> dict[str, str]:
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message": "Todo has been deleted"}
    raise HTTPException(status_code=404, detail=f"Todo not found with id: {todo_id}")