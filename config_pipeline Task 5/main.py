import json
import pandas as pd
import os
import time


# -----------------------------
# LOAD CONFIG
# -----------------------------
def load_config():
    with open("config.json", "r") as f:
        return json.load(f)


# -----------------------------
# PREPROCESSING
# -----------------------------
def preprocess(config):

    print("Preprocessing started...")

    df = pd.read_csv(config["input_csv"])

    # convert numeric columns
    for col in config["preprocessing"]["numeric_columns"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # drop missing rows
    if config["preprocessing"]["drop_missing"]:
        df = df.dropna()

    output_path = os.path.join(
        config["work_dir"],
        "cleaned.csv"
    )

    df.to_csv(output_path, index=False)

    print("Cleaned data saved")

    return df


# -----------------------------
# TRAINING SIMULATION
# -----------------------------
def train(config):

    print("Training started...")

    epochs = config["training"]["epochs"]

    log_path = os.path.join(
        config["work_dir"],
        "training.log"
    )

    with open(log_path, "w") as log:

        for epoch in range(1, epochs + 1):

            loss = 1 / epoch
            message = f"Epoch {epoch} Loss={loss}\n"

            print(message.strip())
            log.write(message)

            time.sleep(0.5)

    print("Training completed")

    return {"final_loss": loss}


# -----------------------------
# REPORT GENERATION
# -----------------------------
def generate_report(config, df, result):

    report = {
        "total_rows": len(df),
        "columns": list(df.columns),
        "training_result": result
    }

    report_path = os.path.join(
        config["work_dir"],
        "final_report.json"
    )

    with open(report_path, "w") as f:
        json.dump(report, f, indent=4)

    print("Report generated")


# -----------------------------
# PIPELINE RUNNER
# -----------------------------
def run_pipeline():

    config = load_config()

    os.makedirs(config["work_dir"], exist_ok=True)

    df = preprocess(config)

    result = train(config)

    generate_report(config, df, result)

    print("\n✅ PIPELINE COMPLETED SUCCESSFULLY")


# -----------------------------
# START
# -----------------------------
if __name__ == "__main__":
    run_pipeline()