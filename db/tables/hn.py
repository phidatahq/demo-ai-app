# from datetime import datetime
# from typing import Optional, Dict, Any, List

# from sqlalchemy.dialects.postgresql import JSONB, TEXT, ARRAY
# from sqlalchemy.orm import Mapped, mapped_column
# from sqlalchemy.sql.expression import text
# from sqlalchemy.types import BigInteger, DateTime, String

# from db.tables.base import Base


# class AssistantRunsTable(Base):
#     """
#     Table for storing assistant runs.
#     """

#     __tablename__ = "assistant_runs"

#     id_assistant_run: Mapped[int] = mapped_column(
#         BigInteger, primary_key=True, autoincrement=True, nullable=False, index=True
#     )
#     id_user: Mapped[Optional[int]] = mapped_column(BigInteger)
#     id_workspace: Mapped[Optional[int]] = mapped_column(BigInteger)
#     run_id: Mapped[str] = mapped_column(String, nullable=False)
#     assistant_data: Mapped[Optional[Dict[str, Any]]] = mapped_column(JSONB)
#     created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("now()"))
#     updated_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), onupdate=text("now()"))


# class AssistantEventsTable(Base):
#     """
#     Table for storing assistant events
#     """

#     __tablename__ = "assistant_events"

#     id_assistant_event: Mapped[int] = mapped_column(
#         BigInteger, primary_key=True, autoincrement=True, nullable=False, index=True
#     )
#     id_assistant_run: Mapped[int] = mapped_column(BigInteger, nullable=False, index=True)
#     id_user: Mapped[Optional[int]] = mapped_column(BigInteger)
#     id_workspace: Mapped[Optional[int]] = mapped_column(BigInteger)
#     event_type: Mapped[str] = mapped_column(String, nullable=False, index=True)
#     event_data: Mapped[Optional[Dict[str, Any]]] = mapped_column(JSONB)
#     created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("now()"))


# class AssistantEventReviewTable(Base):
#     """
#     Table for storing assistant event reviews
#     """

#     __tablename__ = "assistant_event_reviews"

#     id_assistant_event_review: Mapped[int] = mapped_column(
#         BigInteger, primary_key=True, autoincrement=True, nullable=False, index=True
#     )
#     id_assistant_event: Mapped[int] = mapped_column(BigInteger, nullable=False, index=True)
#     id_assistant_run: Mapped[int] = mapped_column(BigInteger, nullable=False, index=True)
#     id_user: Mapped[Optional[int]] = mapped_column(BigInteger)
#     score: Mapped[float] = mapped_column(BigInteger, default=0.0)
#     notes: Mapped[Optional[str]] = mapped_column(TEXT)
#     tags: Mapped[Optional[List[str]]] = mapped_column(ARRAY(String))
#     created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("now()"))
#     updated_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), onupdate=text("now()"))
