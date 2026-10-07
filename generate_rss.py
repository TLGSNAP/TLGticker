import datetime
import html
import os

# Configuration (Change these to match your info)
FEED_TITLE = "My Raw Text Updates"
FEED_LINK = "https://github.com"
FEED_DESC = "An automated RSS feed powered by a GitHub text file."
TXT_FILE = "content.txt"
XML_FILE = "feed.xml"

def create_rss():
    # Read raw text data safely
    content = ""
    if os.path.exists(TXT_FILE):
        with open(TXT_FILE, "r", encoding="utf-8") as f:
            content = f.read().strip()
    
    if not content:
        content = "No updates available."

    # Format current RFC-822 date for RSS readers
    now = datetime.datetime.now(datetime.timezone.utc)
    pub_date = now.strftime("%a, %d %b %Y %H:%M:%S GMT")

    # Clean text to prevent breaking XML syntax
    safe_content = html.escape(content)

    # Build standard RSS 2.0 XML structures
    rss_xml = f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0" xmlns:atom="http://w3.org">
<channel>
    <title>{FEED_TITLE}</title>
    <link>{FEED_LINK}</link>
    <description>{FEED_DESC}</description>
    <pubDate>{pub_date}</pub_date>
    <lastBuildDate>{pub_date}</lastBuildDate>
    <atom:link href="{FEED_LINK}/raw/main/{XML_FILE}" rel="self" type="application/rss+xml" />
    <item>
        <title>Latest Text Update</title>
        <link>{FEED_LINK}</link>
        <description>{safe_content}</description>
        <pubDate>{pub_date}</pub_date>
        <guid isPermaLink="false">txt-update-{hash(content)}</guid>
    </item>
</channel>
</rss>"""

    # Output the static feed file
    with open(XML_FILE, "w", encoding="utf-8") as f:
        f.write(rss_xml)

if __name__ == "__main__":
    create_rss()
