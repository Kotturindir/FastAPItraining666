from database import newSession, TaskOrm
from schemas import STaskAdd, STaskRead
from sqlalchemy import select


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd):
        async with newSession() as session:
            task_dict = data.model_dump()

            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id
    
    @classmethod
    async def get_all(cls) -> list[STaskRead]:
        async with newSession() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [STaskRead.model_validate(task_model) for task_model in task_models]
            return task_schemas