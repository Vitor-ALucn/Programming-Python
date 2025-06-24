# Importing/Exporting DataFrames with Pandas

df.read_csv()  # type: ignore # Reads a CSV file
df.excel()     # type: ignore # Reads an Excel file
df.read_sql()  # type: ignore # Reads from a SQL database
df.to_csv()    # type: ignore # Export DF to CSV file
df.to_excel()  # type: ignore # Export DF to Excel file

# Data Cleaning

df.dropna()  # type: ignore # Remoce missing values
df.fillna()  # type: ignore # Fill in missing values
df.drop()    # type: ignore # Drop specified rows or columns
df.rename()  # type: ignore # Rename columns or index
df.drop_duplicates()  # type: ignore # Remove duplicate rows

# Data transformation

df.pivot()   # type: ignore # Reshape data
df.melt()    # type: ignore # Stack from wide to long
df.concat()  # type: ignore # Bind rows toguether
df.sort_values()  # type: ignore # Sort by column values
df.sort_index()   # type: ignore # Sort by index
df.stack()  # type: ignore # Stack columns to rows

# Statistics

df.mean()      # type: ignore # Calculate mean
df.describe()  # type: ignore # Summary statistics
df.corr()      # type: ignore # Calculate correlation
df.groupby()   # type: ignore # Group by column values
df.value_counts()  # type: ignore # Count unique values in a column