with open("auth_log.txt", "r") as file:
    logs = file.readlines()

failed_attempts = {}

for line in logs:
    if "Login failed" in line:
        user_part = line.split("user=")[1]
        user = user_part.split(",")[0]

        if user in failed_attempts:
            failed_attempts[user] += 1
        else:
            failed_attempts[user] = 1

for user, count in failed_attempts.items():
    if count >= 3:
        print(f"ALERT: {user} has {count} failed login attempts")