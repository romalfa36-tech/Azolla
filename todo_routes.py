from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List
from database import get_db
from models import Todo, User
from schemas import TodoCreate, TodoUpdate, TodoResponse
from auth import get_current_user

router = APIRouter(prefix="/api/todos", tags=["todos"])


@router.post("/", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
async def create_todo(
    todo: TodoCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    new_todo = Todo(
        title=todo.title,
        description=todo.description,
        completed=todo.completed,
        owner_id=current_user.id,
    )
    db.add(new_todo)
    await db.commit()
    await db.refresh(new_todo)
    return new_todo


@router.get("/", response_model=List[TodoResponse])
async def read_todos(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = await db.execute(
        select(Todo)
        .where(Todo.owner_id == current_user.id)
        .offset(skip)
        .limit(limit)
    )
    todos = result.scalars().all()
    return todos


@router.get("/{todo_id}", response_model=TodoResponse)
async def read_todo(
    todo_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = await db.execute(
        select(Todo).where(Todo.id == todo_id, Todo.owner_id == current_user.id)
    )
    todo = result.scalar_one_or_none()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.put("/{todo_id}", response_model=TodoResponse)
async def update_todo(
    todo_id: int,
    todo_update: TodoUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = await db.execute(
        select(Todo).where(Todo.id == todo_id, Todo.owner_id == current_user.id)
    )
    todo = result.scalar_one_or_none()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    update_data = todo_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(todo, field, value)
    
    await db.commit()
    await db.refresh(todo)
    return todo


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(
    todo_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = await db.execute(
        select(Todo).where(Todo.id == todo_id, Todo.owner_id == current_user.id)
    )
    todo = result.scalar_one_or_none()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    await db.delete(todo)
    await db.commit()
    return None
