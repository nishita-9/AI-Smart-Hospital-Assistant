def response_agent(analysis, planning):

    print("\n========== AI SMART HOSPITAL ASSISTANT ==========\n")

    print(f"Possible Illness : {analysis['illness']}")
    print(f"Severity         : {analysis['severity']}")

    print("\nRecommended Care Plan:")

    for item in planning["plan"]:

        if item.strip() != "":
            print(item)

    print("\nRecommended Doctor :")
    print(planning["doctor"])

    print("\n===============================================")