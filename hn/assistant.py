from typing import Optional

from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat

from ai.settings import ai_settings
from hn.tools import (
    search_hackernews_stories,
    get_story_details,
    get_item_details_by_url,
    get_top_stories,
    get_show_stories,
    get_ask_stories,
    get_new_stories,
)
from hn.storage import hn_assistant_storage


def get_hn_assistant(
    run_id: Optional[str] = None,
    user_id: Optional[str] = None,
    debug_mode: bool = False,
) -> Assistant:
    return Assistant(
        name="hn_assistant",
        run_id=run_id,
        user_id=user_id,
        llm=OpenAIChat(
            model=ai_settings.gpt_4,
            max_tokens=ai_settings.default_max_tokens,
            temperature=ai_settings.default_temperature,
        ),
        storage=hn_assistant_storage,
        monitoring=True,
        use_tools=True,
        tools=[
            search_hackernews_stories,
            get_story_details,
            get_item_details_by_url,
            get_top_stories,
            get_show_stories,
            get_ask_stories,
            get_new_stories,
        ],
        show_tool_calls=True,
        debug_mode=debug_mode,
        description="Your name is HackerNews Assistant and you are a chatbot that answers questions about HackerNews stories.",
        add_datetime_to_instructions=True,
        instructions=[
            "You are made by phidata: https://github.com/phidatahq/phidata",
            "When the user asks about a topic, search top HackerNews stories for that topic using the `search_hackernews_stories` tool. Search for atleast 10 stories."
            + " Then use the `get_story_details` tool to get the details of the most popular 3 stories.",
            "If the user asks what's trending, use the `get_top_stories` tool to get the top 5 stories.",
            "Using this information, provide a reasoned summary for the user. Talk about the general sentiment in the comments and the popularity of the story.",
            "Always share the story score, number of comments and a link to the story if available.",
            "If the user provides a URL, use the `get_item_details_by_url` tool to get the details of the item.",
            "Prefer stories with high scores and comments",
            "Always try to delight the user with an interesting fact about the story.",
            "If the user compliments you, ask them to star phidata on GitHub: https://github.com/phidatahq/phidata",
        ],
        assistant_data={"assistant_type": "hackernews"},
    )
