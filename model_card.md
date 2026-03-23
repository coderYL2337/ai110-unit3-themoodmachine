# Model Card: Mood Machine

This model card documents the Mood Machine project, which includes both a rule-based mood analyzer and a machine learning (ML) model. Both models were evaluated and compared.

## 1. Model Overview

**Model type:**  
Both the rule-based model and the ML model were implemented and compared.

**Intended purpose:**  
Classify short text messages as moods: positive, negative, neutral, or mixed.

**How it works (brief):**  
- The rule-based model uses word lists and rules to score text, handling negation, slang, emojis, and some sarcasm/mixed signals.
- The ML model uses a bag-of-words CountVectorizer and logistic regression, trained on the same labeled dataset.

## 2. Data

**Dataset description:**  
The dataset contains over 35 posts in `SAMPLE_POSTS`, expanded from the starter set. New posts were added to cover:
  - Slang ("lowkey", "no cap", "highkey")
  - Emojis (":)", ":(", "😂", "🥲", "🙃")
  - Sarcasm (e.g., "I absolutely love when my phone dies in the middle of a call 🙃")
  - Mixed emotions ("Feeling both happy and sad at the same time 🥲", "I love cats but hate dogs")
  - Neutral statements ("I eat at 10", "I slept for 10 hours")
  - Positive/negative posts about specific days ("I love Mondays", "I hate Mondays")
  - Posts using "like" ("I like you")

**Labeling process:**  
Labels were chosen based on the overall sentiment, with "mixed" for posts containing both positive and negative signals, and "neutral" for factual or emotionless statements. Some posts (e.g., "Feeling tired but kind of hopeful") were labeled "mixed" due to ambiguity. Edge cases were discussed and labeled conservatively.

**Important characteristics of your dataset:**  
- Contains slang, emojis, and internet language
- Includes sarcasm and mixed feelings
- Has short, ambiguous, and factual posts
- Attempts to balance positive, negative, neutral, and mixed examples

**Possible issues with the dataset:**  
- Still relatively small; some moods or tones may be underrepresented
- Some labels are subjective ("Feeling tired but kind of hopeful")
- May not generalize to longer or more complex texts

## 3. How the Rule Based Model Works (if used)

**Your scoring rules:**  
- Each positive word/phrase adds +1, each negative word/phrase subtracts -1
- Handles negation ("not happy" flips positive to negative)
- Recognizes multi-word phrases ("that's sick", "is fire")
- Handles slang and emojis (e.g., ":)", "😂" as positive; ":(", "🥲" as negative)
- Special logic for "but" and mixed signals ("I love cats but hate dogs" → mixed)
- Sarcasm detection for patterns like "I love when... 🙃" (flips label)

**Strengths of this approach:**  
- Predictable for clear-cut positive/negative posts
- Handles some slang, emojis, and simple negation
- Can label mixed posts if both positive and negative words are present

**Weaknesses of this approach:**  
- Struggles with subtle sarcasm or context (e.g., "This is fine" is labeled neutral, but could be sarcastic)
- May misclassify posts with rare slang or ambiguous tone
- Relies on word lists; new slang or phrasing may be missed

## 4. How the ML Model Works (if used)

**Features used:**  
Bag of words using CountVectorizer (each word is a feature).

**Training data:**  
Trained on the full `SAMPLE_POSTS` and `TRUE_LABELS` dataset.

**Training behavior:**  
The ML model was very sensitive to the examples and labels. Adding more positive, neutral, and mixed posts improved its ability to classify those moods. It initially misclassified posts like "I love Mondays" as negative until more positive Monday examples were added.

**Strengths and weaknesses:**  
Strengths: Can learn patterns from data, adapts as new examples are added. Weaknesses: Overfits to the training set, may misclassify posts with rare words or ambiguous tone, and is highly sensitive to label balance.

## 5. Evaluation

**How you evaluated the model:**  
Both models were evaluated on the labeled posts in `dataset.py` using accuracy and by reviewing individual predictions.

**Examples of correct predictions:**  
- "I love this class so much" → positive (both models)
- "I hate Mondays" → negative (both models after dataset expansion)
- "I love cats but hate dogs" → mixed (rule-based after logic update, ML after more mixed examples)

**Examples of incorrect predictions:**  
- "I like you" → negative (ML model before positive 'like' examples were added)
- "I slept for 10 hours" → positive (ML model before neutral sleep examples were added)
- "I absolutely love when my phone dies in the middle of a call 🙃" → neutral/positive (ML model, but rule-based correctly flips to negative due to sarcasm logic)

## 6. Limitations

**Key limitations:**
- The dataset is small and may not cover all moods or language styles
- Both models depend heavily on the specific words and labels in the dataset
- Sarcasm is only detected in specific patterns (e.g., "🙃" or "I love when...")
- Subtle or cultural references may be misclassified
- Both models may fail on longer, more complex, or out-of-domain texts

## 7. Ethical Considerations

**Ethical considerations:**
- Misclassifying distress or sarcasm could lead to inappropriate responses
- The model may misinterpret slang, dialect, or cultural references not present in the dataset
- Privacy: analyzing personal messages raises concerns about consent and data use

## 8. Ideas for Improvement

**Ideas for improvement:**
- Add more labeled data, especially for ambiguous or rare moods
- Use TF-IDF or word embeddings for the ML model
- Expand emoji and slang handling
- Use a neural network or transformer for more context
- Improve sarcasm and mixed signal detection
- Add a real test set for better evaluation

**Bias and scope note:**
The dataset is optimized for casual, English, internet-style language with some slang and emojis. It may misinterpret posts from other dialects, cultures, or more formal/technical language. The model is best for short, informal messages and may not generalize to other domains.

**Model comparison:**
- The ML model learned from the labeled data and could fix some failures (e.g., after adding positive 'like' examples, it correctly labeled "I like you").
- The rule-based model was more robust to new slang if the word lists were updated, but struggled with subtlety and context.
- The ML model was highly sensitive to label balance and could overfit or misclassify rare patterns until more examples were added.
