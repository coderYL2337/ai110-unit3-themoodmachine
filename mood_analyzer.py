# mood_analyzer.py
"""
Rule based mood analyzer for short text snippets.

This class starts with very simple logic:
  - Preprocess the text
  - Look for positive and negative words
  - Compute a numeric score
  - Convert that score into a mood label
"""

from typing import List, Dict, Tuple, Optional

from dataset import POSITIVE_WORDS, NEGATIVE_WORDS


class MoodAnalyzer:
    """
    A very simple, rule based mood classifier.
    """

    def __init__(
        self,
        positive_words: Optional[List[str]] = None,
        negative_words: Optional[List[str]] = None,
    ) -> None:
        # Use the default lists from dataset.py if none are provided.
        positive_words = positive_words if positive_words is not None else POSITIVE_WORDS
        negative_words = negative_words if negative_words is not None else NEGATIVE_WORDS

        # Store as sets for faster lookup.
        self.positive_words = set(w.lower() for w in positive_words)
        self.negative_words = set(w.lower() for w in negative_words)

    # ---------------------------------------------------------------------
    # Preprocessing
    # ---------------------------------------------------------------------

    def preprocess(self, text: str, print_tokens: bool = False) -> List[str]:
        """
        Convert raw text into a list of tokens the model can work with.

        Improvements:
          - Strips leading and trailing whitespace
          - Converts everything to lowercase
          - Removes punctuation
          - Splits on spaces
          - Prints tokens for confirmation
        """
        import string
        cleaned = text.strip().lower()
        # Remove punctuation (except emojis)
        cleaned = cleaned.translate(str.maketrans('', '', string.punctuation))
        tokens = cleaned.split()
        if print_tokens:
          print(f"[preprocess] tokens: {tokens}")
        return tokens

    # ---------------------------------------------------------------------
    # Scoring logic
    # ---------------------------------------------------------------------

    def score_text(self, text: str, tokens: List[str] = None) -> int:
        """
        Compute a numeric "mood score" for the given text.

        Positive words increase the score.
        Negative words decrease the score.

        Enhancement: Handle simple negation (e.g., "not happy" or "not bad").
        """
        if tokens is None:
          tokens = self.preprocess(text)
        score = 0
        negation_words = {"not", "never", "no", "n't"}
        negate_next = False

        # Phrase-based scoring (positive and negative)
        import string
        cleaned = text.strip().lower()
        cleaned = cleaned.translate(str.maketrans('', '', string.punctuation))
        # Check for multi-word positive phrases
        for phrase in self.positive_words:
            if " " in phrase and phrase in cleaned:
                score += 1
        # Check for multi-word negative phrases
        for phrase in self.negative_words:
            if " " in phrase and phrase in cleaned:
                score -= 1

        # Single-token scoring
        for token in tokens:
            if token in negation_words:
                negate_next = True
                continue
            if token in self.positive_words and " " not in token:
                if negate_next:
                    score -= 1
                else:
                    score += 1
                negate_next = False
            elif token in self.negative_words and " " not in token:
                if negate_next:
                    score += 1
                else:
                    score -= 1
                negate_next = False
            else:
                negate_next = False
        return score

    # ---------------------------------------------------------------------
    # Label prediction
    # ---------------------------------------------------------------------

    def predict_label(self, text: str) -> str:
        """
        Turn the numeric score for a piece of text into a mood label.

        The default mapping is:
          - score > 0  -> "positive"
          - score < 0  -> "negative"
          - score == 0 -> "neutral"

        You can adjust this mapping if it makes sense for your model.
        """
        tokens = self.preprocess(text, print_tokens=True)
        pos_count = sum(1 for t in tokens if t in self.positive_words)
        neg_count = sum(1 for t in tokens if t in self.negative_words)
        score = self.score_text(text, tokens=tokens)

        lowered = text.strip().lower()

        # Flexible sarcasm_starts: allow adverbs between 'i' and 'love'
        import re
        sarcasm_starts = bool(re.match(r"i( [a-z]+)* love( it)? when", lowered)) or \
          lowered.startswith("i just love when") or \
          lowered.startswith("gotta love when") or \
          lowered.startswith("i love ")

        # Strong sarcasm: contains 🙃 and starts with a positive phrase
        if sarcasm_starts and "🙃" in lowered:
          return "negative"

        # If 🙃 is present anywhere, flip the predicted label (do this before other logic)
        if "🙃" in lowered:
          # Predict as usual, then flip
          if (pos_count > 0 or neg_count > 0) and " but " in lowered:
            base_label = "mixed"
          elif pos_count > 0 and neg_count > 0:
            base_label = "mixed"
          elif score > 0:
            base_label = "positive"
          elif score < 0:
            base_label = "negative"
          else:
            base_label = "neutral"
          if base_label == "positive":
            return "negative"
          elif base_label == "negative":
            return "positive"
          elif base_label == "neutral":
            return "negative"
          else:
            return base_label

        sarcasm = False

        # If 🙃 is present anywhere, flip the predicted label
        if "🙃" in lowered:
          # Predict as usual, then flip
          if (pos_count > 0 or neg_count > 0) and " but " in lowered:
            base_label = "mixed"
          elif pos_count > 0 and neg_count > 0:
            base_label = "mixed"
          elif score > 0:
            base_label = "positive"
          elif score < 0:
            base_label = "negative"
          else:
            base_label = "neutral"
          if base_label == "positive":
            return "negative"
          elif base_label == "negative":
            return "positive"
          elif base_label == "neutral":
            return "negative"
          else:
            return base_label
        has_and_or_but = (" and " in lowered or " but " in lowered)
        if sarcasm_starts:
          # If 'and' or 'but' present, check after them for negative word
          if has_and_or_but:
            for sep in [" and ", " but "]:
              if sep in lowered:
                after = lowered.split(sep, 1)[1]
                for neg in self.negative_words:
                  if neg in after:
                    sarcasm = True
                    break
              if sarcasm:
                break
          else:
            # Otherwise, check if a negative word appears anywhere after the start phrase
            if lowered.startswith("i love it when"):
              after = lowered[len("i love it when"):].strip()
            elif lowered.startswith("i just love when"):
              after = lowered[len("i just love when"):].strip()
            elif lowered.startswith("gotta love when"):
              after = lowered[len("gotta love when"):].strip()
            elif lowered.startswith("i love "):
              after = lowered[len("i love "):].strip()
            else:
              after = lowered
            for neg in self.negative_words:
              if neg in after:
                sarcasm = True
                break
        if sarcasm:
          return "negative"

        # 'but' as a strong signal for mixed: if 'but' is present and at least one positive or negative word is present
        if (pos_count > 0 or neg_count > 0) and " but " in lowered:
          return "mixed"
        # If both positive and negative words are present, label as mixed
        if pos_count > 0 and neg_count > 0:
          return "mixed"
        if score > 0:
          return "positive"
        elif score < 0:
          return "negative"
        else:
          return "neutral"

    # ---------------------------------------------------------------------
    # Explanations (optional but recommended)
    # ---------------------------------------------------------------------

    def explain(self, text: str) -> str:
        """
        Return a short string explaining WHY the model chose its label.

        TODO:
          - Look at the tokens and identify which ones counted as positive
            and which ones counted as negative.
          - Show the final score.
          - Return a short human readable explanation.

        Example explanation (your exact wording can be different):
          'Score = 2 (positive words: ["love", "great"]; negative words: [])'

        The current implementation is a placeholder so the code runs even
        before you implement it.
        """
        tokens = self.preprocess(text)

        positive_hits: List[str] = []
        negative_hits: List[str] = []
        score = 0

        for token in tokens:
            if token in self.positive_words:
                positive_hits.append(token)
                score += 1
            if token in self.negative_words:
                negative_hits.append(token)
                score -= 1

        return (
            f"Score = {score} "
            f"(positive: {positive_hits or '[]'}, "
            f"negative: {negative_hits or '[]'})"
        )
