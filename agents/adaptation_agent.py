def adaptation_agent(days_left, progress):
    if days_left <= 7:
        return "Switch to exam mode: focus only on high-priority topics."
    
    if progress < 50:
        return "Reduce workload and focus on completing fewer but important tasks."
    
    return "Maintain current plan and increase difficulty gradually."