def response_agent(analysis, plan):

    print("\n========== AI SMART HOSPITAL ASSISTANT ==========\n")

    print(f"Possible Illness : {analysis['illness']}")
    print(f"Severity         : {analysis['severity']}")

    print("\nRecommended Care Plan:")

    for item in plan:
        print(item)

    print("\n===============================================")