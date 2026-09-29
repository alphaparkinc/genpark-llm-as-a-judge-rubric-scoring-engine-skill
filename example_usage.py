from client import RubricJudgeEngine

scores = {"helpfulness": 5, "correctness": 4, "conciseness": 5, "safety": 5}
grade = RubricJudgeEngine.score_response(scores)
print("Composite Grade:", grade)
