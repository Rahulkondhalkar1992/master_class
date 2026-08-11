from pathlib import Path

# Change this path if your repository is elsewhere
BASE_DIR = Path.cwd() / "docs"

folders = {
    "00-start-here": [
        "welcome.md",
        "course-roadmap.md",
        "course-prerequisites.md",
        "tools-software-setup.md"
    ],

    "01-azure-fundamentals": [
        "module-overview.md",
        "what-is-cloud-computing.md",
        "azure-regions.md",
        "azure-subscriptions.md",
        "resource-groups.md",
        "azure-architecture.md"
    ],

    "02-azure-storage-adls": [
        "module-overview.md",
        "storage-account.md",
        "blob-storage.md",
        "blob-vs-adls.md",
        "adls-gen2.md",
        "rbac-vs-acl.md",
        "storage-security.md"
    ],

    "03-azure-data-factory": [
        "module-overview.md",
        "what-is-adf.md",
        "adf-architecture.md",
        "linked-service.md",
        "dataset.md",
        "pipeline.md",
        "activity.md",
        "integration-runtime.md",
        "copy-activity.md",
        "lookup-activity.md",
        "foreach-activity.md",
        "parameters-and-variables.md",
        "dynamic-content.md",
        "triggers.md",
        "monitoring.md",
        "incremental-load.md",
        "metadata-driven-framework.md"
    ],

    "04-databricks": [
        "module-overview.md",
        "databricks-architecture.md",
        "workspace.md",
        "clusters.md",
        "jobs.md",
        "unity-catalog.md"
    ],

    "05-pyspark": [
        "module-overview.md",
        "spark-architecture.md",
        "dataframes.md",
        "transformations.md",
        "actions.md",
        "joins.md",
        "window-functions.md"
    ],

    "06-sql": [
        "module-overview.md",
        "sql-fundamentals.md",
        "joins.md",
        "cte.md",
        "window-functions.md",
        "query-optimization.md"
    ],

    "07-python": [
        "module-overview.md",
        "python-fundamentals.md",
        "functions.md",
        "file-handling.md",
        "json.md",
        "api-calls.md"
    ],

    "08-data-modeling": [
        "module-overview.md",
        "oltp-vs-olap.md",
        "fact-and-dimension.md",
        "star-schema.md",
        "snowflake-schema.md",
        "scd-type1-type2.md"
    ],

    "09-git-github": [
        "module-overview.md",
        "git-basics.md",
        "branching.md",
        "merge.md",
        "pull-request.md"
    ],

    "10-agile-scrum": [
        "module-overview.md",
        "agile.md",
        "scrum.md",
        "user-stories.md",
        "sprint-planning.md"
    ],

    "11-delta-lake": [
        "module-overview.md",
        "delta-lake.md",
        "merge.md",
        "time-travel.md",
        "optimize.md",
        "vacuum.md"
    ],

    "12-project": [
        "project-overview.md",
        "architecture.md",
        "bronze-layer.md",
        "silver-layer.md",
        "gold-layer.md"
    ],

    "13-assignments": [
        "adf-assignment.md",
        "databricks-assignment.md",
        "sql-assignment.md"
    ],

    "14-interview-preparation": [
        "azure-interview-questions.md",
        "adls-interview-questions.md",
        "adf-interview-questions.md",
        "databricks-interview-questions.md",
        "pyspark-interview-questions.md",
        "sql-interview-questions.md",
        "python-interview-questions.md",
        "data-modeling-interview-questions.md"
    ],

    "15-cheat-sheets": [
        "adf-cheat-sheet.md",
        "pyspark-cheat-sheet.md",
        "sql-cheat-sheet.md",
        "python-cheat-sheet.md",
        "git-cheat-sheet.md"
    ]
}

BASE_DIR.mkdir(parents=True, exist_ok=True)

for folder, files in folders.items():
    folder_path = BASE_DIR / folder
    folder_path.mkdir(parents=True, exist_ok=True)

    for file in files:
        file_path = folder_path / file

        title = file.replace(".md", "").replace("-", " ").title()

        if not file_path.exists():
            file_path.write_text(
                f"# {title}\n\nContent coming soon...\n",
                encoding="utf-8"
            )

print("✅ Azure Data Engineering course structure created successfully.")