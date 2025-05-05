# %%
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

# %%
# MySQL database connection detail
mysql_user = 'analyst'
mysql_password = 'go_lions'
mysql_host = 'db.isba.co'
mysql_db = 'basket_craft'

# Postgres database connection detail
pg_user = 'postgres'
pg_password = 'isba_4715'
pg_host = 'isba-dev-02.cmb4w8cmqb26.us-east-1.rds.amazonaws.com'
pg_db = 'basket_craft'

# %%
# Build connection strings
mysql_conn_str = f'mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}'
pg_conn_str = f'postgresql+psycopg2://{pg_user}:{pg_password}@{pg_host}/{pg_db}'

# %%
# Create database engines
mysql_engine = create_engine(mysql_conn_str)
pg_engine = create_engine(pg_conn_str)

# %%
query = """
SELECT * FROM website_sessions
WHERE created_at BETWEEN '2023-12-01' AND '2023-12-31 23:59:59'
"""

# %%
df = pd.read_sql(query, mysql_engine)


# %%
df.to_sql('website_sessions', pg_engine, schema = 'raw', if_exists='replace', index=False)

# %%
print(f'{len(df)} records loaded into postgres website_sessions table')
# %%
df
# %%
