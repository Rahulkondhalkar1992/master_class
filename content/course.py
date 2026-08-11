"""Course information and 90-day learning plan content."""

COURSE = {
    "name": "Azure Data Engineering Master Class",
    "academy": "Azure Learnings Academy",
    "tagline": (
        "Become an Industry-Ready Azure Data Engineer Through Live Learning, "
        "Real-Time Project Execution and Industry-Level Interview Preparation."
    ),
    "objective": (
        "Build strong Azure Data Engineering skills so you can design, implement, debug, "
        "and explain end-to-end pipelines used in real projects — starting with ADF and "
        "progressing through Databricks, SQL, modeling, Python, and production patterns."
    ),
    "highlights": [
        {
            "icon": "👨‍🏫",
            "title": "LIVE CLASSES",
            "body": "100% instructor-led interactive learning. No recorded-only model.",
        },
        {
            "icon": "🏗️",
            "title": "REAL PROJECT",
            "body": "Build an end-to-end industry-style Azure data engineering project.",
        },
        {
            "icon": "🧠",
            "title": "DEEP CONCEPTS",
            "body": "Understand architecture and design decisions — not just syntax.",
        },
        {
            "icon": "🎯",
            "title": "INTERVIEW READY",
            "body": "Technical, scenario-based, and experience-level preparation.",
        },
        {
            "icon": "🗄️",
            "title": "PRACTICAL LABS",
            "body": "SQL + Python + PySpark practice aligned to data engineering work.",
        },
        {
            "icon": "🛡️",
            "title": "2-YEAR SUPPORT",
            "body": "Long-term technical learning support for revision and guidance.",
        },
    ],
    "market_context": [
        {
            "title": "Cloud Adoption",
            "body": "Enterprises continue migrating analytics and data platforms to cloud environments like Azure.",
        },
        {
            "title": "Data Growth",
            "body": "Organizations need reliable pipelines to collect, clean, and deliver growing volumes of data.",
        },
        {
            "title": "AI Depends on Data",
            "body": "Useful AI and analytics outcomes rely on trustworthy, well-modeled, accessible data.",
        },
        {
            "title": "Enterprise Platforms",
            "body": "Azure services such as ADF, Databricks, ADLS, and Synapse are widely used in production estates.",
        },
        {
            "title": "Career Growth",
            "body": "Data engineering roles combine SQL, Python, cloud services, and architecture thinking.",
        },
        {
            "title": "Global Opportunities",
            "body": "Cloud data engineering skills transfer across industries and delivery models.",
        },
    ],
}

COURSE_INFO_SECTIONS = [
    {
        "key": "welcome",
        "icon": "👋",
        "title": "Welcome",
        "body": (
            "Welcome to Azure Learnings Academy — Azure Data Engineering Master Class. "
            "This portal guides you through course information, the 90-day plan, complete syllabus, "
            "roadmap, tools, and enquiry options."
        ),
    },
    {
        "key": "about",
        "icon": "📘",
        "title": "About the Course",
        "body": (
            "A practical, instructor-led program focused on Azure Data Factory, Databricks, "
            "SQL, data modeling, Python, Delta Lake, medallion architecture, security, CI/CD, "
            "and end-to-end project execution — with interview preparation woven throughout."
        ),
    },
    {
        "key": "prerequisites",
        "icon": "✅",
        "title": "Course Prerequisites",
        "items": [
            "Basic computer and IT fundamentals",
            "Willingness to practice regularly",
            "Laptop with stable internet for labs and Azure tooling",
            "Basic SQL awareness is helpful but not mandatory on day one",
            "Prior programming experience is helpful, not assumed as expert-level",
        ],
        "note": "This program does not claim that zero technical knowledge is required.",
    },
    {
        "key": "tools_setup",
        "icon": "🛠️",
        "title": "Tools & Software Setup",
        "items": [
            "Azure Portal access",
            "Azure Storage Explorer",
            "SSMS / pgAdmin (as needed)",
            "VS Code",
            "Python",
            "Git + GitHub",
            "Databricks workspace access (as provided in course)",
        ],
    },
    {
        "key": "azure_account",
        "icon": "☁️",
        "title": "Azure Account Setup",
        "items": [
            "Create or access an Azure subscription for learning labs",
            "Understand tenants, subscriptions, and resource groups",
            "Configure basic access for Storage, ADF, and Databricks resources",
            "Follow instructor guidance for cost-safe lab practices",
        ],
    },
    {
        "key": "methodology",
        "icon": "🔁",
        "title": "Learning Methodology",
        "flow": ["Learn", "Practice", "Implement", "Debug", "Explain", "Interview"],
        "body": (
            "Every module is designed to move from concept clarity to practical implementation "
            "and interview-ready explanation."
        ),
    },
    {
        "key": "how_to_use",
        "icon": "🧭",
        "title": "How to Use This Portal",
        "items": [
            "Start with Course Information and the 90-Day Learning Plan",
            "Follow the Roadmap for the recommended learning sequence",
            "Open Syllabus modules from the sidebar to explore topics",
            "Use Tools & Applications for setup references",
            "Use Enquiry / Join Now or WhatsApp to connect with the team",
        ],
    },
]

LEARNING_PLAN_90 = [
    {
        "days": "Days 01–10",
        "title": "Azure & Storage",
        "icon": "☁️",
        "focus": [
            "Cloud & Azure fundamentals",
            "Subscriptions, resource groups, portal",
            "Storage Account, Blob, ADLS Gen2",
            "Security basics (RBAC / ACL)",
        ],
        "modules": ["azure_fundamentals", "azure_storage"],
    },
    {
        "days": "Days 11–35",
        "title": "Azure Data Factory",
        "icon": "🔄",
        "focus": [
            "ADF architecture and core components",
            "Pipelines, Copy Activity, control flow",
            "Dynamic content, triggers, incremental load",
            "Metadata-driven framework foundations",
        ],
        "modules": ["adf"],
    },
    {
        "days": "Days 36–45",
        "title": "SQL & Data Modeling",
        "icon": "🗄️",
        "focus": [
            "SQL fundamentals to window functions",
            "Optimization basics",
            "Facts, dimensions, star/snowflake",
            "SCD patterns",
        ],
        "modules": ["sql", "data_modeling"],
    },
    {
        "days": "Days 46–50",
        "title": "Python",
        "icon": "🐍",
        "focus": [
            "Python fundamentals for data engineering",
            "Collections, functions, files, JSON, APIs",
            "Practical scripting patterns",
        ],
        "modules": ["python"],
    },
    {
        "days": "Days 51–70",
        "title": "Databricks & PySpark",
        "icon": "🔥",
        "focus": [
            "Databricks workspace, clusters, jobs",
            "Unity Catalog basics",
            "PySpark DataFrames, joins, windows",
            "Performance awareness",
        ],
        "modules": ["databricks", "pyspark"],
    },
    {
        "days": "Days 71–75",
        "title": "Delta Lake",
        "icon": "🟢",
        "focus": [
            "Delta tables and ACID concepts",
            "MERGE / UPSERT patterns",
            "Time travel, OPTIMIZE, Z-ORDER, VACUUM",
        ],
        "modules": ["delta_lake"],
    },
    {
        "days": "Days 76–80",
        "title": "Advanced Data Engineering",
        "icon": "🚀",
        "focus": [
            "Medallion architecture",
            "Security & governance",
            "DevOps / CI/CD concepts",
            "Advanced Databricks & SQL depth",
        ],
        "modules": ["medallion", "security", "devops"],
    },
    {
        "days": "Days 81–90",
        "title": "End-to-End Project",
        "icon": "🎯",
        "focus": [
            "Business requirement to architecture",
            "ADF ingestion + lakehouse layers",
            "Quality, monitoring, CI/CD",
            "Interview-ready project walkthrough",
        ],
        "modules": ["e2e_project", "interview_mod"],
    },
]
