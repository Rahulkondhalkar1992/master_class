"""Assignments and practice preview content."""

ASSIGNMENT_CATEGORIES = [
    {
        "key": "sql",
        "icon": "🗄️",
        "title": "SQL",
        "subtitle": "30+ Practical Problems",
        "levels": [
            {
                "badge": "BEGINNER",
                "items": ["Filtering & aggregations", "Basic joins", "GROUP BY scenarios"],
            },
            {
                "badge": "INTERMEDIATE",
                "items": ["Multi-join queries", "CTEs", "Window functions"],
            },
            {
                "badge": "ADVANCED",
                "items": ["Deduplication patterns", "Incremental logic", "Performance-minded SQL"],
            },
        ],
    },
    {
        "key": "python",
        "icon": "🐍",
        "title": "Python",
        "subtitle": "Practical Coding Exercises",
        "levels": [
            {
                "badge": "BEGINNER",
                "items": ["List processing", "Dictionaries", "Functions"],
            },
            {
                "badge": "INTERMEDIATE",
                "items": ["File handling", "JSON transforms", "Error handling"],
            },
            {
                "badge": "ADVANCED",
                "items": ["Data cleaning scripts", "Reusable utilities", "API data pulls"],
            },
        ],
    },
    {
        "key": "pyspark",
        "icon": "⚡",
        "title": "PySpark",
        "subtitle": "Data Engineering Challenges",
        "levels": [
            {
                "badge": "BEGINNER",
                "items": ["DataFrame basics", "Select / filter / withColumn"],
            },
            {
                "badge": "INTERMEDIATE",
                "items": ["Joins", "Aggregations", "Window functions"],
            },
            {
                "badge": "ADVANCED",
                "items": ["Skew awareness", "Repartition strategy", "Pipeline transforms"],
            },
        ],
    },
]

SQL_PRACTICE = [
    {
        "id": "01",
        "title": "Top customers by sales",
        "prompt": "Find the top 5 customers based on total sales.",
        "starter": "SELECT\n    customer_id,\n    SUM(amount) AS total_sales\nFROM orders\n-- complete the query\n;",
        "hint": "Use GROUP BY and ORDER BY with LIMIT/TOP depending on dialect.",
    },
    {
        "id": "02",
        "title": "Latest status per order",
        "prompt": "For each order_id, return only the latest status row.",
        "starter": "WITH ranked AS (\n    SELECT *,\n           ROW_NUMBER() OVER (PARTITION BY order_id ORDER BY updated_at DESC) AS rn\n    FROM order_status\n)\nSELECT *\nFROM ranked\nWHERE rn = 1;",
        "hint": "Window functions are ideal for latest-record patterns.",
    },
    {
        "id": "03",
        "title": "Active customers without orders",
        "prompt": "List active customers who have not placed any order in the last 90 days.",
        "starter": "SELECT c.customer_id, c.customer_name\nFROM customers c\nLEFT JOIN orders o\n  ON c.customer_id = o.customer_id\n AND o.order_date >= CURRENT_DATE - INTERVAL '90' DAY\nWHERE c.is_active = 1\n  AND o.order_id IS NULL;",
        "hint": "LEFT JOIN + NULL check is a common anti-join pattern.",
    },
    {
        "id": "04",
        "title": "Daily revenue trend",
        "prompt": "Calculate daily revenue and day-over-day change.",
        "starter": "SELECT\n    order_date,\n    SUM(amount) AS revenue,\n    LAG(SUM(amount)) OVER (ORDER BY order_date) AS prev_day_revenue\nFROM orders\nGROUP BY order_date\nORDER BY order_date;",
        "hint": "Combine aggregation with LAG for trend analysis.",
    },
    {
        "id": "05",
        "title": "Duplicate email detection",
        "prompt": "Find email addresses that appear more than once in the customers table.",
        "starter": "SELECT email, COUNT(*) AS cnt\nFROM customers\nGROUP BY email\nHAVING COUNT(*) > 1;",
        "hint": "HAVING filters after aggregation.",
    },
]

PYTHON_PRACTICE = [
    {
        "id": "01",
        "title": "Find duplicates",
        "prompt": "Find duplicate values from a list and return them as a sorted unique list.",
        "starter": "def find_duplicates(data):\n    seen = set()\n    duplicates = set()\n    for item in data:\n        if item in seen:\n            duplicates.add(item)\n        else:\n            seen.add(item)\n    return sorted(duplicates)\n",
        "hint": "Track seen values with a set.",
    },
    {
        "id": "02",
        "title": "Flatten nested dict keys",
        "prompt": "Count frequency of values in a list of dictionaries for a given key.",
        "starter": "from collections import Counter\n\ndef count_by_key(rows, key):\n    values = [row.get(key) for row in rows if key in row]\n    return dict(Counter(values))\n",
        "hint": "collections.Counter is useful for frequency maps.",
    },
    {
        "id": "03",
        "title": "Safe JSON loader",
        "prompt": "Write a function that loads JSON text and returns {} on invalid input.",
        "starter": "import json\n\ndef safe_json_loads(text):\n    try:\n        return json.loads(text)\n    except (TypeError, json.JSONDecodeError):\n        return {}\n",
        "hint": "Always handle malformed payloads defensively.",
    },
    {
        "id": "04",
        "title": "Chunk a list",
        "prompt": "Split a list into chunks of size n.",
        "starter": "def chunk_list(items, n):\n    if n <= 0:\n        raise ValueError('n must be positive')\n    return [items[i:i+n] for i in range(0, len(items), n)]\n",
        "hint": "Slicing in steps of n is a clean approach.",
    },
]
