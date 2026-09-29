"""LLM-as-a-Judge Rubric Scoring Engine.
100% Python Standard Library.
"""

class RubricJudgeEngine:
    """Computes weighted composite evaluation scores across multiple standard rubric dimensions."""
    @classmethod
    def score_response(cls, scores_dict):
        weights = {"helpfulness": 0.3, "correctness": 0.4, "conciseness": 0.15, "safety": 0.15}
        composite = 0.0
        for crit, wt in weights.items():
            val = scores_dict.get(crit, 3)
            composite += val * wt
        return {
            "composite_score": round(composite, 2),
            "normalized_score": round(composite / 5.0, 4),
            "criteria_scores": scores_dict
        }
