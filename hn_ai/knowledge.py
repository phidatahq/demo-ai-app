from phi.knowledge import AssistantKnowledge
from phi.embedder.openai import OpenAIEmbedder
from phi.vectordb.pgvector import PgVector

from db.session import db_url

hn_knowledge_base = AssistantKnowledge(
    vector_db=PgVector(
        schema="ai",
        db_url=db_url,
        collection="hn_documents",
        embedder=OpenAIEmbedder(model="text-embedding-3-small"),
    ),
    num_documents=10,
)
