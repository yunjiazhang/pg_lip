from core.cardinality_estimation_quality.cardinality_estimation_quality import *

class PostgreConnector:

    def __init__(self,):
        server='localhost' 
        username='postgres'
        password='postgres'
        db_name='imdbload'
        self.db_url = f"host={server} port=5432 user={username} dbname={db_name} password={password} options='-c statement_timeout={6000000}' "
        db = self.db_url.format(db_name)
        self.PG = Postgres(db)

    def get_plan(self, sql_str):
        assert 'explain' not in sql_str.lower()
        return self.PG.explain(sql_str)[0][0][0]


class QueryPlan:
    
    class PlanNode:
        def __init__(self, left=None, right=None, op=None, table=None):
            self.left, self.right, self.op, self.table = left, right, op, table

    def __init__(self, pg_plan_json):
        pass
        

    

class LipRewriter:

    def __init__(self):
        pass

    def _get_PG_plan():
        pass
    
    def rewrite(self, sql_str):
        pass

if __name__ == '__main__':
    conn = PostgreConnector()
    plan = conn.get_plan("""SELECT MIN(mc.note) AS production_note,
       MIN(t.title) AS movie_title,
       MIN(t.production_year) AS movie_year
FROM company_type AS ct,
     info_type AS it,
     movie_companies AS mc,
     movie_info_idx AS mi_idx,
     title AS t
WHERE ct.kind = 'production companies'
  AND it.info = 'top 250 rank'
  AND mc.note NOT LIKE '%(as Metro-Goldwyn-Mayer Pictures)%'
  AND (mc.note LIKE '%(co-production)%'
       OR mc.note LIKE '%(presents)%')
  AND ct.id = mc.company_type_id
  AND t.id = mc.movie_id
  AND t.id = mi_idx.movie_id
  AND mc.movie_id = mi_idx.movie_id
  AND it.id = mi_idx.info_type_id;
""")
    print(plan)
    

