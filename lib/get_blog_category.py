import sys

from .gpt_providers.openai_gpt_provider import openai_chatgpt
from .gpt_providers.gemini_pro_text import gemini_text_response

from loguru import logger
logger.remove()
logger.add(sys.stdout,
        colorize=True,
        format="<level>{level}</level>|<green>{file}:{line}:{function}</green>| {message}"
    )


def get_blog_categories(blog_article, gpt_providers):
    """
    Function to generate blog categories for given blog content.
    """
    prompt = f"""As an expert SEO and content writer, I will provide you with blog content.
            Suggest only 2 blog categories which are most relevant to provided blog content,
            by identifying the main topic. Also consider the target audience and the
            blog's category taxonomy. Only reply with comma separated values. 
            The blog content is: '{blog_article}'"
    """
    logger.info("Generating blog categories for the given blog.")
    if 'gemini' in gpt_providers:
        try:
            response = gemini_text_response(prompt)
            return response
        except Exception as err:
            logger.error(f"Failed to get response from gemini: {err}")
    elif 'openai' in gpt_providers:
        try:
            response = openai_chatgpt(prompt)
            return response
        except Exception as err:
            SystemError(f"Error in generating blog get_blog_categories: {err}")
