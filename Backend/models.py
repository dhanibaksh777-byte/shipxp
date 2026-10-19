from Backend.database import base
from sqlalchemy import Column,String,DateTime,Boolean,Integer,ForeignKey,Date
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime,timezone
import uuid


class User(base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid = True),primary_key=True,default = uuid.uuid4)
    github_username = Column(String(39),unique=True,nullable=False)
    hashed_password = Column(String,nullable=False)
    xp = Column(Integer,default=0,nullable=False)

class Quest(base):
    __tablename__ = "quests"
    id = Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    title = Column(String(150),nullable=False)
    description = Column(String)
    xp_reward = Column(Integer,nullable=False)

class UserQuest(base):
    __tablename__ = "userquest"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    quest_id = Column(UUID(as_uuid=True), ForeignKey("quests.id"), nullable=False)
    date = Column(Date, default=lambda: datetime.now(timezone.utc).date(), nullable=False)
    status = Column(String, default="pending", nullable=False)
    completed_at = Column(DateTime(timezone=True), nullable=True)
