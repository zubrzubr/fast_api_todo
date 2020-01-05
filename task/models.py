from sqlalchemy import Column, Integer, String, Boolean, Text

from database import Base


class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
    is_done = Column(Boolean, default=False)
