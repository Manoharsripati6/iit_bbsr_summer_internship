import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from urllib.parse import urlparse
import re


# loading collected json data
df = pd.read_json("statics/task9/merged_video_results.json")


def extract_creator(url):
    """
    Extracts website/domain name from URL.
    """

    domain = urlparse(url).netloc

    domain = domain.replace("www.", "")

    return domain


# finding total number of collected videos
total_videos = len(df)

# extracting creator/platform names from urls
df["creator"] = df["video_url"].apply(
    extract_creator
)

# counting unique creators/websites
unique_creators = df["creator"].nunique()

# collecting words from all video titles
all_words = []

for title in df["video_title"]:

    words = re.findall(
        r"\w+",
        title.lower()
    )

    all_words.extend(words)


# removing unnecessary common words
stop_words = {
    "the", "and", "to", "of",
    "in", "for", "on", "with",
    "a", "an", "your"
}

filtered_words = [

    word for word in all_words

    if word not in stop_words
]


# finding most frequently used keywords
common_keywords = Counter(
    filtered_words
).most_common(10)


# creating simple engagement values for analysis
df["engagement"] = (
    df["video_title"].str.len() * 5
)

# calculating average engagement
average_engagement = (
    df["engagement"].mean()
)

# selecting top performing videos
top_posts = df.sort_values(
    by="engagement",
    ascending=False
).head(5)


# graph showing number of videos collected per topic
topic_counts = df["topic"].value_counts()

plt.figure(figsize=(8, 5))

topic_counts.plot(kind="bar")

plt.title("Videos Collected Per Topic")

plt.xlabel("Topics")

plt.ylabel("Number of Videos")

plt.tight_layout()

plt.savefig("videos_per_topic.png")

plt.close()


# graph showing most common creators/websites
top_creators = (
    df["creator"]
    .value_counts()
    .head(10)
)

plt.figure(figsize=(10, 5))

top_creators.plot(kind="bar")

plt.title("Top Video Creators/Websites")

plt.xlabel("Creators")

plt.ylabel("Video Count")

plt.tight_layout()

plt.savefig("top_creators.png")

plt.close()


# saving analysis summary into txt file
with open("summary_report.txt", "w") as file:

    file.write("DATA SUMMARY REPORT\n")

    file.write("=" * 40 + "\n\n")

    file.write(
        f"Total Videos Collected: "
        f"{total_videos}\n"
    )

    file.write(
        f"Total Unique Creators: "
        f"{unique_creators}\n\n"
    )

    file.write(
        "Most Common Keywords:\n"
    )

    for word, count in common_keywords:

        file.write(
            f"- {word}: {count}\n"
        )

    file.write("\n")

    file.write(
        f"Average Engagement: "
        f"{average_engagement:.2f}\n\n"
    )

    file.write(
        "Top Performing Posts:\n"
    )

    for _, row in top_posts.iterrows():

        file.write(
            f"- {row['video_title']}\n"
        )

        file.write(
            f"  Engagement: "
            f"{row['engagement']}\n"
        )

        file.write(
            f"  URL: "
            f"{row['video_url']}\n\n"
        )


print("Analysis completed successfully")
print("Summary report saved")
print("Visualizations saved")