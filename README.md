# Paper Hearts Recommendation Database

## Overview

The Paper Hearts Recommendation Database is a personalized book recommendation system designed for customers of Paper Hearts Bookstore. The application allows users to input their reading preferences and receive immediate book recommendations based on their preferences. The system also tracks customer input for future recommendations, enhancing the personalized experience over time.

## Features

- **Personalized Book Recommendations**: Customers receive immediate book suggestions based on their input.
- **Data Tracking**: The system records user preferences to improve recommendations for future visits.
- **Data Import**: The application imports book data from Excel files to keep the recommendation database updated.
- **Potential External Links**: Book recommendations may include links to external websites for more information or purchasing options.

## Technologies Used

- **Python**: Core programming language used to implement the application logic.
- **SQLite**: Lightweight database used for storing customer data and book information.
- **Pandas**: Data manipulation library used to import and process data from Excel files.

## How It Works

1. **User Input**: Customers provide their book preferences (e.g., genre, author, past reads).
2. **Data Processing**: The application analyzes user input and compares it against the existing database.
3. **Recommendation Generation**: A personalized book recommendation is generated and displayed, potentially including a link to an external website for more details or purchasing options.
4. **Preference Tracking**: The system stores customer preferences for future recommendations, improving over time.

## Data Input and Output

- **Input**: Book information is imported from Excel files, including metadata like genre, author, and popularity.
- **Output**: The application generates a book recommendation in plain text, possibly accompanied by a link to an external site.

## Dependencies

Before running the application, make sure you have the following installed:

- Python 3.x
- Pandas
- SQLite
- openpyxl (for reading Excel files)

To install dependencies, run:

```bash
pip install pandas openpyxl
