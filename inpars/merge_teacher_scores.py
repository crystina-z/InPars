import sys
import os
import pickle


def merge_teacher_scores(teacher_scores_dir: str, merged_scores_path: str) -> None:
    merged_scores = {}
    for file in os.listdir(teacher_scores_dir):
        if file.endswith(".pkl"):
            with open(os.path.join(teacher_scores_dir, file), "rb") as f:
                scores = pickle.load(f)
                merged_scores.update(scores)

    with open(merged_scores_path, "wb") as f:
        pickle.dump(merged_scores, f)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python merge_teacher_scores.py <model_name>")
        sys.exit(1)

    model_name = sys.argv[1]
    model_base_name = os.path.basename(model_name)

    teacher_scores_dir = os.path.join("teacher-scores", model_name, "sharded")
    merged_scores_path = os.path.join("teacher-scores", model_name, "merged", f"{model_base_name}.pkl")
    merge_teacher_scores(teacher_scores_dir, merged_scores_path)
