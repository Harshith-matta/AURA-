def monitoring_agent(completed_tasks, total_tasks):
    if total_tasks == 0:
        return "No tasks set yet."
    
    progress = (completed_tasks / total_tasks) * 100
    
    if progress < 50:
        return f"⚠️ Low progress: {progress:.1f}%. You need to improve consistency."
    else:
        return f"✅ Good progress: {progress:.1f}%."