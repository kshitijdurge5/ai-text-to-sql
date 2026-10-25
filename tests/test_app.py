import pytest
from app import validate_readonly_sql

def test_select_allowed(): assert validate_readonly_sql('SELECT * FROM sales')
def test_delete_blocked(): assert not validate_readonly_sql('DELETE FROM sales')
