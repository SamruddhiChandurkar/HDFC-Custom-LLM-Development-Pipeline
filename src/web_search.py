import os
import requests
from dotenv import load_dotenv

load_dotenv()


class TavilySearch:

    def __init__(self):

        self.api_key = os.getenv(
            "TAVILY_API_KEY"
        )

        self.url = (
            "https://api.tavily.com/search"
        )

        # Official HDFC Bank domain only
        self.allowed_domain = "hdfcbank.com"

    def is_available(self):

        return bool(self.api_key)

    def search(
        self,
        query,
        max_results=5
    ):

        if not self.api_key:

            return {
                "available": False,
                "query": query,
                "results": [],
                "error": (
                    "TAVILY_API_KEY is not configured."
                )
            }

        # Force HDFC official website search
        hdfc_query = f"site:hdfcbank.com {query}"

        payload = {

            "api_key": self.api_key,

            "query": hdfc_query,

            "search_depth": "advanced",

            "max_results": max_results,

            "include_answer": True,

            "include_raw_content": False,

            "include_domains": [
                "hdfcbank.com"
            ]
        }

        try:

            response = requests.post(
                self.url,
                json=payload,
                timeout=30
            )

            if response.status_code != 200:

                return {
                    "available": False,
                    "query": query,
                    "results": [],
                    "error": (
                        f"Tavily API error "
                        f"{response.status_code}: "
                        f"{response.text}"
                    )
                }

            data = response.json()

            results = []

            for item in data.get(
                "results",
                []
            ):

                url = item.get(
                    "url",
                    ""
                )

                # -----------------------------------------
                # SECURITY: ONLY HDFC OFFICIAL DOMAIN
                # -----------------------------------------

                if "hdfcbank.com" not in url.lower():

                    continue

                results.append({

                    "title": item.get(
                        "title"
                    ),

                    "url": url,

                    "content": item.get(
                        "content"
                    ),

                    "score": item.get(
                        "score"
                    )
                })

            # -----------------------------------------
            # DO NOT TRUST TAVILY ANSWER IF
            # NO HDFC RESULT WAS FOUND
            # -----------------------------------------

            if not results:

                return {

                    "available": True,

                    "query": query,

                    "answer": None,

                    "results": [],

                    "error": (
                        "No verified HDFC Bank "
                        "official website result found."
                    )
                }

            return {

                "available": True,

                "query": query,

                "answer": data.get(
                    "answer"
                ),

                "results": results
            }

        except Exception as error:

            return {

                "available": False,

                "query": query,

                "results": [],

                "error": str(error)
            }