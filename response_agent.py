def response_agent(analysis, planning, research):

    print("\n========== AI SMART HOSPITAL ASSISTANT ==========\n")

    print(f"Possible Illness : {analysis['illness']}")
    print(f"Severity         : {analysis['severity']}")
    print(f"Cause            : {planning['cause']}")

    print("\nPrecautions:")

    for item in research["precautions"]:
        print(f"• {item}")

    print("\nRecommended Care Plan:")

    for item in planning["plan"]:
        print(f"• {item}")

    print("\nRecommended Doctor :")
    print(planning["doctor"])

    print("\nSuggested Medicine :")
    print(planning["medicine"])

    print("\n===============================================")