def send_alert(result):

    print("\n==============================")

    print(" FRAUD ALERT ")

    print("==============================")

    print("Decision :", result["decision"])

    print("Risk Score :", result["risk_score"])

    print("Reasons:")

    for reason in result["reasons"]:
        print("-", reason)

    print("==============================\n")