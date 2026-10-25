import sqlite3
import streamlit as st
from portfolio_visuals import render_visuals
DB = "sample.db"
def validate_readonly_sql(query: str) -> bool:
    q = query.strip().lower()
    return q.startswith("select ") and not any(token in q for token in [";", "--", "/*", " attach ", " pragma ", " drop ", " delete ", " update ", " insert ", " alter "])

def execute_query(query: str):
    if not validate_readonly_sql(query):
        raise ValueError("Only a single read-only SELECT query is allowed in this demo.")
    conn = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    try:
        return conn.execute(query).fetchmany(100)
    finally:
        conn.close()

st.set_page_config(page_title="Text to SQL", page_icon="ðŸ—ƒï¸")
render_visuals('06_text_to_sql')
st.title("Read-only SQL Explorer")
st.caption("Starter: write SQL manually. Natural-language-to-SQL generation is a future extension.")
if st.button("Initialize sample database"):
    import init_db
    st.success("Sample database initialized.")
query = st.text_area("Read-only SELECT query", "SELECT region, SUM(amount) AS total FROM sales GROUP BY region")
if st.button("Run query"):
    try:
        rows = execute_query(query)
        st.write(rows)
    except Exception as e:
        st.error(str(e))

