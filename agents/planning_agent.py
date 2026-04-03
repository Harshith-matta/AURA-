def planning_agent(decision):
    if "exams" in decision.lower():
        return [
            "Study 3-4 important topics daily",
            "Revise previous papers",
            "Practice key questions"
        ]
    
    return [
        "2 hrs skill learning",
        "2 hrs academics",
        "1 mini task/project daily"
    ]