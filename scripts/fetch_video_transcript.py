from __future__ import annotations
import sys
from youtube_transcript_api import YouTubeTranscriptApi

VIDEO_ID = sys.argv[1] if len(sys.argv) > 1 else 'gFWZM0saGGI'

def main() -> None:
    try:
        tr = YouTubeTranscriptApi.get_transcript(VIDEO_ID)
    except Exception as e:
        print(f"ERROR: {type(e).__name__}: {e}")
        sys.exit(1)

    # Print as plain text
    for chunk in tr:
        txt = chunk.get('text', '').strip()
        if txt:
            print(txt)

if __name__ == '__main__':
    main()
