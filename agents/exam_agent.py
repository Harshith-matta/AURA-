from collections import Counter
import re

def exam_agent(text):
    words = re.findall(r'\w+', text.lower())
    
    # Remove common words
    stop_words = {"the", "is", "and", "of", "to", "in", "a", "for"}
    filtered = [w for w in words if w not in stop_words]
    
    freq = Counter(filtered)
    common = freq.most_common(10)
    
    important_topics = [word for word, count in common]
    
    return {
        "important_topics": important_topics,
        "message": "Focus on these high-frequency topics for exams."
    }