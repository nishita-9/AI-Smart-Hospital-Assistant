def planning_agent(analysis, research):

    return {

        "plan": analysis["care_plan"],

        "doctor": analysis["doctor"],

        "medicine": analysis["medicine"],

        "cause": analysis["cause"],

        "precautions": research["precautions"]
    }