import json

from phi.document import Document
from phi.utils.log import set_log_level_to_debug

from hn_ai.knowledge import hn_knowledge_base
from utils.log import logger


def load_hackernews_knowledge_base():
    from hackernews import HackerNews

    hn = HackerNews()
    set_log_level_to_debug()

    logger.info("Loading HackerNews knowledge base...")
    top_stories = hn.top_stories(limit=2000)
    logger.info(f"Fetched {len(top_stories)} top stories from HackerNews.")
    show_stories = hn.show_stories(limit=100)
    logger.info(f"Fetched {len(show_stories)} show stories from HackerNews.")
    ask_stories = hn.ask_stories(limit=50)
    logger.info(f"Fetched {len(ask_stories)} ask stories from HackerNews.")
    all_stories = top_stories + show_stories + ask_stories
    logger.info("Creating Documents...")

    documents = []
    for story in all_stories:
        try:
            meta_data = {
                "id": story.item_id,
                "type": story.item_type,
                "author": story.by,
                "score": story.score,
                "total_comments": story.descendants,
                "time": story.time.isoformat(),
            }
            if story.parent:
                meta_data["parent"] = story.parent

            content = {
                "title": story.title,
                "url": story.url,
                "author": story.by,
            }
            if story.text:
                content["text"] = story.text

            documents.append(
                Document(
                    name=str(story.item_id),
                    meta_data=meta_data,
                    content=json.dumps(content),
                )
            )
        except Exception as e:
            logger.error(f"Error creating document for story {story.item_id}: {e}")
    logger.info("Adding Documents to knowledge base...")
    hn_knowledge_base.vector_db.delete()
    hn_knowledge_base.load_documents(documents)


load_hackernews_knowledge_base()
