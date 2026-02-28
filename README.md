# config-driven-pipeline
Python-based configurable data pipeline that processes datasets, applies preprocessing rules, simulates training execution, and generates logs and final reports using a config-driven workflow.
## Task 5: Config-Driven Pipeline (Config → Process → Output)

### Objective

To design a configurable data processing pipeline controlled entirely through a configuration file that manages preprocessing, training simulation, and report generation.

### Description

In this task, a Config-Driven Pipeline was developed using Python to automate dataset processing workflows. The pipeline reads instructions from a configuration file, performs preprocessing operations, simulates a training process, and generates structured outputs including cleaned datasets, execution logs, and final reports. The workflow ensures flexibility by allowing pipeline behavior to be modified without changing the source code.

### Tasks Performed

* Designed configuration file structure (`config.json`)
* Defined input dataset and working directory
* Implemented configuration loader
* Applied preprocessing rules based on config settings
* Built training simulation module
* Generated execution logs
* Created automated reporting system
* Organized outputs inside working directory
* Generated cleaned dataset preview
* Produced final pipeline report

### Tools Used

* Python
* JSON Configuration Handling
* File Processing
* Logging Module
* VS Code

### Configuration Fields

The configuration file includes:

* **input_csv** – Input dataset path
* **work_dir** – Output working directory
* **preprocessing_rules** – Data cleaning instructions
* **training_settings** – Training simulation parameters

### Output Files

All outputs are saved inside the configured working directory:

* **cleaned_preview.csv** – Processed dataset preview
* **training.log** – Training simulation logs
* **final_report.json** – Pipeline execution summary

### Result

The Config-Driven Pipeline successfully executes data processing workflows based on configuration settings, producing cleaned datasets, training logs, and structured reports while maintaining flexibility and scalability.

