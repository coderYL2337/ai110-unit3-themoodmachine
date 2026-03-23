"""
Shared data for the Mood Machine lab.

This file defines:
  - POSITIVE_WORDS: starter list of positive words
  - NEGATIVE_WORDS: starter list of negative words
  - SAMPLE_POSTS: short example posts for evaluation and training
  - TRUE_LABELS: human labels for each post in SAMPLE_POSTS
"""

# ---------------------------------------------------------------------
# Starter word lists
# ---------------------------------------------------------------------

POSITIVE_WORDS = [
    "happy",
    "great",
    "good",
    "love",
    "excited",
    "awesome",
    "fun",
    "chill",
    "relaxed",
    "amazing",
    "lol",
    ":)",
    "😂",
    "proud",
    # 'sick' as a standalone word is not always positive, but 'that's sick' as a phrase is slang for amazing
    "that's sick",
    "is fire",
    "was fire",
    "lowkey fire",
    "highkey fire",
    "hopeful",
    "best",
    "no cap",
    "helped",
]

NEGATIVE_WORDS = [
    "sad",
    "bad",
    "terrible",
    "awful",
    "angry",
    "upset",
    "tired",
    "stressed",
    "hate",
    "boring",
    "forgot",
    "spilled",
    ":(",
    "🥲",
    "💀",
    "exhausted",
    "stuck",
    "sucks",
    "rough",
    "nap",
    "rn",
]

# ---------------------------------------------------------------------
# Starter labeled dataset
# ---------------------------------------------------------------------

# Short example posts written as if they were social media updates or messages.
SAMPLE_POSTS = [
    # Added mixed sentiment example
    "I love cats but hate dogs",
    # Added positive examples using 'like'
    "I like you",
    "I like pizza",
    "I like sunny days",
    # Added neutral sleep-related examples
    "I slept for 10 hours",
    "I went to bed early",
    "I woke up at 7",
    # Added neutral examples to improve ML model
    "I forgot my keys",
    "I eat at 10",
    "I love this class so much",
    "Today was a terrible day",
    "Feeling tired but kind of hopeful",
    "This is fine",
    "So excited for the weekend",
    "I am not happy about this",
    # Added realistic posts with slang, emojis, mixed emotions, and subtle tone
    "Lowkey stressed but it's whatever 🤷‍♂️",
    "Best day ever!! 😎✨",
    "Not gonna lie, today was rough but pizza helped 🍕",
    "Highkey need a nap rn",
    "No cap, that movie was fire 🔥",
    "Guess I'm just... here. ¯\\_(ツ)_/¯",
    "I absolutely love when my phone dies in the middle of a call 🙃",
    "Feeling both happy and sad at the same time 🥲",
    # Added negative examples for ML model
    "I hate bugs",
    "I dislike bugs",
    "I hate it when it is so cold",
    "I dislike rainy days",
    "I hate it when it is so humid :(",
    "I can't stand traffic",
    "I really hate being late",
    "I dislike waiting in long lines",
    "I hate Mondays",
    # Added positive examples about Mondays and other days
    "I love Mondays",
    "Mondays are great",
    "I look forward to Mondays",
    "Mondays make me happy",
    "I love Fridays",
    "Fridays are awesome",
    "I look forward to Fridays",
    "Fridays make me happy",
]

# Human labels for each post above.
# Allowed labels in the starter:
#   - "positive"
#   - "negative"
#   - "neutral"
#   - "mixed"
TRUE_LABELS = [
    # Matching mixed label for new post
    "mixed",  # "I love cats but hate dogs"
    # Matching positive labels for new 'like' posts
    "positive",  # "I like you"
    "positive",  # "I like pizza"
    "positive",  # "I like sunny days"
    # Matching neutral labels for new sleep-related posts
    "neutral",  # "I slept for 10 hours"
    "neutral",  # "I went to bed early"
    "neutral",  # "I woke up at 7"
    # Matching neutral labels for new posts
    "neutral",  # "I forgot my keys"
    "neutral",  # "I eat at 10"
    "positive",  # "I love this class so much"
    "negative",  # "Today was a terrible day"
    "mixed",     # "Feeling tired but kind of hopeful"
    "neutral",   # "This is fine"
    "positive",  # "So excited for the weekend"
    "negative",  # "I am not happy about this"
    # Matching labels for new posts
    "mixed",     # "Lowkey stressed but it's whatever 🤷‍♂️"
    "positive",  # "Best day ever!! 😎✨"
    "mixed",     # "Not gonna lie, today was rough but pizza helped 🍕"
    "negative",  # "Highkey need a nap rn"
    "positive",  # "No cap, that movie was fire 🔥"
    "neutral",   # "Guess I'm just... here. ¯\\_(ツ)_/¯"
    "negative",  # "I absolutely love when my phone dies in the middle of a call 🙃" (sarcasm)
    "mixed",     # "Feeling both happy and sad at the same time 🥲"
    "negative",  # "I hate bugs"
    "negative",  # "I dislike bugs"
    "negative",  # "I hate it when it is so cold"
    "negative",  # "I dislike rainy days"
    "negative",  # "I hate it when it is so humid :("
    "negative",  # "I can't stand traffic"
    "negative",  # "I really hate being late"
    "negative",  # "I dislike waiting in long lines"
    "negative",  # "I hate Mondays"
    # Matching positive labels for new posts
    "positive",  # "I love Mondays"
    "positive",  # "Mondays are great"
    "positive",  # "I look forward to Mondays"
    "positive",  # "Mondays make me happy"
    "positive",  # "I love Fridays"
    "positive",  # "Fridays are awesome"
    "positive",  # "I look forward to Fridays"
    "positive",  # "Fridays make me happy"
]

# TODO: Add 5-10 more posts and labels.
#
# Requirements:
#   - For every new post you add to SAMPLE_POSTS, you must add one
#     matching label to TRUE_LABELS.
#   - SAMPLE_POSTS and TRUE_LABELS must always have the same length.
#   - Include a variety of language styles, such as:
#       * Slang ("lowkey", "highkey", "no cap")
#       * Emojis (":)", ":(", "🥲", "😂", "💀")
#       * Sarcasm ("I absolutely love getting stuck in traffic")
#       * Ambiguous or mixed feelings
#
# Tips:
#   - Try to create some examples that are hard to label even for you.
#   - Make a note of any examples that you and a friend might disagree on.
#     Those "edge cases" are interesting to inspect for both the rule based
#     and ML models.
#
# Example of how you might extend the lists:
#
# SAMPLE_POSTS.append("Lowkey stressed but kind of proud of myself")
# TRUE_LABELS.append("mixed")
#
# Remember to keep them aligned:
#   len(SAMPLE_POSTS) == len(TRUE_LABELS)
