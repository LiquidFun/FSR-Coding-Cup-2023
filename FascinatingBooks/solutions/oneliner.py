print("no" if set("abcdefghijklmnopqrstuvwxyz") - set(''.join(input().lower() for _ in int(input()))) else "yes")
