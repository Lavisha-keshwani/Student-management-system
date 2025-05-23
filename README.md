# 🎓 Student Management System (CLI-based)

A command-line based Student Management System written in Python. This tool allows managing student data including personal information, grades, and enrolled courses. It features CSV-based persistent storage.

---

### 🔁 Workflow Overview

flowchart TD
    A[Start Program] --> B{Load students_data.csv?}
    B -- Yes --> C[Load Existing Data]
    B -- No --> D[Start with Empty Database]
    C --> E[Display Menu]
    D --> E[Display Menu]

    E --> F[Add Student]
    E --> G[View All Students]
    E --> H[Update Student Info]
    E --> I[Delete Student]
    E --> J[Calculate Average Grade]
    E --> K[Filter Passed Students]
    E --> L[Search by Name]
    E --> M[Sort by Grades]
    E --> N[Save & Exit]

    N --> O[Write to CSV]
    O --> P[Exit]
