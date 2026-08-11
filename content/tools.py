"""Tools and applications content."""

TOOL_CATEGORIES = [
    {
        "name": "SQL",
        "tools": [
            {
                "name": "SQL Server / SSMS",
                "purpose": "Develop and test T-SQL queries.",
                "why": "Many enterprise sources and warehouses still use SQL Server.",
                "usage": "Practice joins, CTEs, and transformation SQL.",
                "docs": "https://learn.microsoft.com/sql/ssms/",
            },
            {
                "name": "PostgreSQL / pgAdmin",
                "purpose": "Work with open-source relational databases.",
                "why": "Useful for portable SQL practice and analytics labs.",
                "usage": "Practice SQL scenarios and local database workflows.",
                "docs": "https://www.postgresql.org/docs/",
            },
            {
                "name": "Oracle / SQL Developer",
                "purpose": "Explore Oracle SQL environments when needed.",
                "why": "Some source systems in enterprises are Oracle-based.",
                "usage": "Understand source extraction considerations.",
                "docs": "https://docs.oracle.com/en/database/",
            },
        ],
    },
    {
        "name": "Azure",
        "tools": [
            {
                "name": "Azure Portal",
                "purpose": "Manage Azure resources from a web console.",
                "why": "Primary interface for provisioning and monitoring services.",
                "usage": "Create and inspect storage, ADF, Databricks, and related resources.",
                "docs": "https://portal.azure.com/",
            },
            {
                "name": "Azure Storage Explorer",
                "purpose": "Browse and manage blob / ADLS data.",
                "why": "Makes lake folder structures and file checks easier.",
                "usage": "Validate landing zones and file drops.",
                "docs": "https://azure.microsoft.com/products/storage/storage-explorer/",
            },
            {
                "name": "Azure Data Factory",
                "purpose": "Orchestrate ingestion and data movement pipelines.",
                "why": "Core orchestration service in many Azure data platforms.",
                "usage": "Build linked services, datasets, pipelines, and triggers.",
                "docs": "https://learn.microsoft.com/azure/data-factory/",
            },
            {
                "name": "Azure Databricks",
                "purpose": "Process and transform large datasets with Spark.",
                "why": "Widely used for scalable transformations and lakehouse workloads.",
                "usage": "Notebooks, jobs, PySpark transformations, Delta concepts.",
                "docs": "https://learn.microsoft.com/azure/databricks/",
            },
            {
                "name": "Azure Synapse",
                "purpose": "Support analytics and warehouse-style consumption patterns.",
                "why": "Often appears in enterprise Azure analytics architectures.",
                "usage": "Understand integration with lake and reporting layers.",
                "docs": "https://learn.microsoft.com/azure/synapse-analytics/",
            },
        ],
    },
    {
        "name": "Development",
        "tools": [
            {
                "name": "Python",
                "purpose": "Scripting language for data processing and automation.",
                "why": "Essential for data engineering productivity.",
                "usage": "Practice labs, utilities, and PySpark entry point.",
                "docs": "https://docs.python.org/3/",
            },
            {
                "name": "VS Code",
                "purpose": "Lightweight IDE for code, notebooks, and Git.",
                "why": "Fast local development experience.",
                "usage": "Edit Python, SQL, markdown, and project files.",
                "docs": "https://code.visualstudio.com/docs",
            },
            {
                "name": "Git",
                "purpose": "Version control for code and pipeline assets.",
                "why": "Industry-standard collaboration foundation.",
                "usage": "Branching, commits, and change tracking.",
                "docs": "https://git-scm.com/doc",
            },
            {
                "name": "GitHub",
                "purpose": "Host repositories and collaborate via pull requests.",
                "why": "Common platform for team delivery and reviews.",
                "usage": "Store project code and practice PR workflows.",
                "docs": "https://docs.github.com/",
            },
            {
                "name": "GitHub Desktop",
                "purpose": "GUI client for common Git operations.",
                "why": "Helpful if you prefer a visual Git workflow.",
                "usage": "Clone, commit, and sync repositories.",
                "docs": "https://docs.github.com/desktop",
            },
        ],
    },
]
