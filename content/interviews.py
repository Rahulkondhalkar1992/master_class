"""Interview preparation content."""

EXPERIENCE_TRACKS = [
    {
        "years": "4+ YEARS",
        "focus": "Foundation + Production",
        "points": [
            "Strong SQL / Python / ADF fundamentals",
            "Explain incremental loads and common failures",
            "Demonstrate hands-on pipeline experience",
        ],
    },
    {
        "years": "8+ YEARS",
        "focus": "Architecture + Optimization",
        "points": [
            "Design end-to-end Azure data platforms",
            "Discuss performance, cost, and reliability trade-offs",
            "Lead troubleshooting across ADF and Databricks",
        ],
    },
    {
        "years": "12+ YEARS",
        "focus": "Enterprise + Leadership",
        "points": [
            "Drive architecture standards and governance",
            "Mentor teams and review designs",
            "Communicate with stakeholders on delivery risk",
        ],
    },
]

SCENARIOS = [
    "Pipeline failure in production",
    "Duplicate data in silver layer",
    "Incremental load missing records",
    "Slow Databricks job",
    "Data quality problem before analytics",
    "Unexpected schema change from source",
    "Cost optimization for clusters / ADF runs",
    "Architecture decision between lake and warehouse",
]

SAMPLE_QUESTIONS = [
    {
        "id": "01",
        "module": "ADF",
        "question": "How would you design an incremental data ingestion pipeline?",
        "answer": (
            "Identify a reliable watermark (timestamp or incremental key), store the last "
            "successful watermark, filter source extracts accordingly, land data in bronze, "
            "validate counts/nulls, then merge into curated layers. Include retries, logging, "
            "and a recovery strategy for late-arriving data."
        ),
    },
    {
        "id": "02",
        "module": "Databricks",
        "question": "What would you check first when a Databricks job suddenly becomes slow?",
        "answer": (
            "Review recent code/data volume changes, cluster sizing, shuffle-heavy operations, "
            "skewed joins, unnecessary caching, and job metrics. Compare with a previously "
            "healthy run and isolate whether the bottleneck is compute, data, or query plan."
        ),
    },
    {
        "id": "03",
        "module": "SQL",
        "question": "How do you remove duplicates while keeping the latest record?",
        "answer": (
            "Use a window function such as ROW_NUMBER() partitioned by the business key and "
            "ordered by the update timestamp descending, then keep row_number = 1. Validate "
            "grain and null handling before applying in production."
        ),
    },
    {
        "id": "04",
        "module": "PySpark",
        "question": "When would you prefer broadcast join over a shuffle join?",
        "answer": (
            "When one side of the join is small enough to fit in executor memory, broadcasting "
            "avoids a large shuffle. Confirm size thresholds, monitor memory pressure, and "
            "avoid broadcasting large or growing dimension tables."
        ),
    },
    {
        "id": "05",
        "module": "Architecture",
        "question": "How do you explain a medallion architecture in an interview?",
        "answer": (
            "Bronze stores raw/landed data close to source fidelity, silver cleans and "
            "conforms data for reuse, and gold serves business-ready aggregates or models. "
            "The pattern improves traceability, reprocessing, and separation of concerns."
        ),
    },
]

MOCK_FOCUS = [
    {"title": "Fundamentals", "body": "Core Azure, SQL, Python, and pipeline vocabulary."},
    {"title": "Technical Rounds", "body": "Service-level depth across ADF, Databricks, and storage."},
    {"title": "Scenario Rounds", "body": "Production failures, quality issues, and recovery plans."},
    {"title": "Architecture Rounds", "body": "Design trade-offs, scalability, and governance."},
    {"title": "Troubleshooting", "body": "Structured debugging under time pressure."},
    {"title": "Communication", "body": "Clear explanations of decisions and impact."},
]
