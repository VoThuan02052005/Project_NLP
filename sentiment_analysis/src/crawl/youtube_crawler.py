from googleapiclient.discovery import build
import pandas as pd
from tqdm import tqdm
import time


def get_all_youtube_comments(video_id, api_key, max_per_page=100, sleep_time=0.5):
    """
    Crawl toàn bộ bình luận của 1 video YouTube (bao gồm tất cả các trang).

    Args:
        video_id (str): ID của video YouTube (vd: "dQw4w9WgXcQ")
        api_key (str): YouTube API key
        max_per_page (int): Số comment tối đa mỗi trang (tối đa 100)
        sleep_time (float): Thời gian nghỉ giữa các request để tránh bị giới hạn

    Returns:
        pd.DataFrame: DataFrame chứa toàn bộ bình luận
    """
    youtube = build('youtube', 'v3', developerKey=api_key)
    video_request = youtube.videos().list(
        part='snippet',
        id=video_id
    )
    video_response = video_request.execute()
    video_title = video_response['items'][0]['snippet']['title'] if video_response['items'] else "Unknown Title"
    comments = []
    next_page_token = None
    total_count = 0

    pbar = tqdm(desc="Fetching all comments", unit="page")

    while True:
        request = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            maxResults=max_per_page,
            pageToken=next_page_token,
            textFormat='plainText'
        )
        response = request.execute()

        items = response.get('items', [])
        if not items:
            break

        for item in items:
            snippet = item['snippet']['topLevelComment']['snippet']
            comments.append({
                'video_id': video_id,
                'video_title': video_title,
                'author': snippet['authorDisplayName'],
                'text': snippet['textDisplay'],
                'likeCount': snippet.get('likeCount', 0),
                'publishedAt': snippet['publishedAt']
            })
            total_count += 1

        pbar.update(1)
        next_page_token = response.get('nextPageToken')

        if not next_page_token:
            break

        time.sleep(sleep_time)  # tránh bị rate-limit

    pbar.close()
    print(f"✅ Đã lấy tổng cộng {total_count} bình luận.")

    return pd.DataFrame(comments)
