def decision_agent(year, goal, days_left):
    if days_left <= 7:
        return "Focus completely on exams. Prioritize high-weight topics."
    
    if "data" in goal.lower():
        return "Focus on Python, data analysis basics, and small projects."
    
    if "web" in goal.lower():
        return "Focus on HTML, CSS, JavaScript, and build mini projects."
    
    return "Balance academics and skill development."