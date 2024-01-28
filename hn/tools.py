import json
from typing import List, Optional

from phi.document import Document

from hn.api import HackerNews
from hn.knowledge import hn_knowledge_base
from utils.log import logger

hn = HackerNews()


def search_hackernews_stories(topic: str, num_results: int = 15) -> Optional[str]:
    """Use this function to search Hacker News stories for a given topic.

    Args:
        topic (str): Topic to search for.
        num_results (int): Number of stories to return. Defaults to 15.

    Returns:
        str: JSON string of stories related to the topic.
    """

    relevant_docs: List[Document] = hn_knowledge_base.search(query=topic, num_documents=num_results)
    if len(relevant_docs) == 0:
        return "No results found."
    return json.dumps([doc.to_dict() for doc in relevant_docs])


def get_story_details(id: str) -> Optional[str]:
    """Use this function to get the details of a Hacker News story using its ID.

    Args:
        id (str): ID of the story to get details for.

    Returns:
        str: JSON string of the story details.
    """

    try:
        story = hn.get_item(id)

        story_details = {
            "id": story.item_id,
            "title": story.title,
            "url": story.url,
            "type": story.item_type,
            "author": story.by,
            "score": story.score,
            "total_comments": story.descendants,
            "time": story.time.isoformat(),
        }
        if story.text:
            story_details["text"] = story.text
        if story.kids and len(story.kids) > 0:
            top_comments = []
            for kid_id in story.kids[:10]:
                kid = hn.get_item(kid_id)
                kid_details = {
                    "id": kid.item_id,
                    "author": kid.by,
                }
                if kid.text:
                    kid_details["text"] = kid.text[:200]
                top_comments.append(kid_details)
            story_details["top_comments"] = top_comments

        return json.dumps(story_details)
    except Exception as e:
        return f"Error getting story details: {e}"


def get_item_details_by_url(url: str) -> Optional[str]:
    """Use this function to get the details of a Hacker News item using its URL.

    Args:
        url (str): URL of the item to get details for.

    Returns:
        str: JSON string of the item details.
    """
    from urllib.parse import urlparse, parse_qs

    item_id = None
    try:
        # Parse the URL
        parsed_url = urlparse(url)

        # Parse the query string
        query_params = parse_qs(parsed_url.query)

        # Extract the 'id' parameter
        id_values = query_params.get("id")

        # Return the first 'id' value if available, otherwise None
        item_id = id_values[0] if id_values else None
    except Exception as e:
        return f"Error parsing URL: {e}"

    if not item_id:
        return "No item ID found in URL."

    try:
        item = hn.get_item(item_id)

        item_details = {
            "id": item.item_id,
            "title": item.title,
            "url": item.url,
            "author": item.by,
            "type": item.item_type,
            "score": item.score,
            "total_comments": item.descendants,
            "time": item.time.isoformat(),
        }
        if item.text:
            item_details["text"] = item.text
        if item.kids and len(item.kids) > 0:
            top_comments = []
            for kid_id in item.kids[:10]:
                kid = hn.get_item(kid_id)
                kid_details = {
                    "id": kid.item_id,
                    "author": kid.by,
                }
                if kid.text:
                    kid_details["text"] = kid.text[:200]
                top_comments.append(kid_details)
            item_details["top_comments"] = top_comments

        return json.dumps(item_details)
    except Exception as e:
        return f"Error getting item details: {e}"


def extract_story_details(story) -> Optional[dict]:
    try:
        story_details = {
            "id": story.item_id,
            "title": story.title,
            "url": story.url,
            "author": story.by,
            "type": story.item_type,
            "score": story.score,
            "total_comments": story.descendants,
            "time": story.time.isoformat(),
        }
        if story.text:
            story_details["text"] = story.text
        if story.kids and len(story.kids) > 0:
            top_comments = []
            for kid_id in story.kids[:3]:
                kid = hn.get_item(kid_id)
                kid_details = {
                    "id": kid.item_id,
                    "author": kid.by,
                }
                if kid.text:
                    kid_details["text"] = kid.text[:200]
                top_comments.append(kid_details)
            story_details["top_comments"] = top_comments

        return story_details
    except Exception as e:
        logger.error(f"Error getting story details: {e}")
        return None


def get_top_stories(num_results: int = 5) -> Optional[str]:
    """Use this function to get the top Hacker News stories.

    Args:
        num_results (int): Number of stories to return. Defaults to 5.

    Returns:
        str: JSON string of top stories.
    """

    try:
        top_stories = hn.top_stories(limit=num_results)
        top_story_details = []
        for story in top_stories:
            story_details = extract_story_details(story)
            if story_details:
                top_story_details.append(story_details)
        return json.dumps(top_story_details)
    except Exception as e:
        return f"Error getting top stories: {e}"


def get_show_stories(num_results: int = 10) -> Optional[str]:
    """Use this function to get the SHOW Hacker News stories.

    Args:
        num_results (int): Number of stories to return. Defaults to 10.

    Returns:
        str: JSON string of SHOW HN stories.
    """

    try:
        show_stories = hn.show_stories(limit=num_results)
        show_story_details = []
        for story in show_stories:
            story_details = extract_story_details(story)
            if story_details:
                show_story_details.append(story_details)
        return json.dumps(show_story_details)
    except Exception as e:
        return f"Error getting show stories: {e}"


def get_ask_stories(num_results: int = 10) -> Optional[str]:
    """Use this function to get the ASK Hacker News stories.

    Args:
        num_results (int): Number of stories to return. Defaults to 10.

    Returns:
        str: JSON string of ASK HN stories.
    """

    try:
        ask_stories = hn.ask_stories(limit=num_results)
        ask_story_details = []
        for story in ask_stories:
            story_details = extract_story_details(story)
            if story_details:
                ask_story_details.append(story_details)
        return json.dumps(ask_story_details)
    except Exception as e:
        return f"Error getting ask stories: {e}"


def get_new_stories(num_results: int = 10) -> Optional[str]:
    """Use this function to get the New stories on Hacker News.

    Args:
        num_results (int): Number of stories to return. Defaults to 10.

    Returns:
        str: JSON string of Noew HN stories.
    """

    try:
        new_stories = hn.new_stories(limit=num_results)
        new_story_details = []
        for story in new_stories:
            story_details = extract_story_details(story)
            if story_details:
                new_story_details.append(story_details)
        return json.dumps(new_story_details)
    except Exception as e:
        return f"Error getting new stories: {e}"
