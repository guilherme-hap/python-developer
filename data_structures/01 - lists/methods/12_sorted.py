languages = ["python", "js", "c", "java", "csharp"]

print(sorted(languages, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(languages, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]