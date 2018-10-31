import random

import psycopg2
import pandas as pd
import psycopg2.extras

from db_schemes import WorkerScheme
from db_schemes import WorkerCardScheme
from db_schemes import DepartmentScheme
from db_schemes import JournalScheme


class Database():
    _db_connection = psycopg2.connect(host="localhost",database="dblab1", user="dbuser", password="123456")
    _db_cur = _db_connection.cursor(cursor_factory = psycopg2.extras.DictCursor)

    def __init__(self):
        _db_connection = psycopg2.connect(host="localhost",database="dblab1", user="dbuser", password="123456")
        _db_cur = self._db_connection.cursor(cursor_factory = psycopg2.extras.DictCursor)

    def query(self, query, params):
        return self._db_cur.execute(query, params)

    def close(self):
        self._db_connection.close()

    def get_journal(self, journal_id):
        Database._db_cur.execute(f"""SELECT * FROM journal WHERE id = '{journal_id}'""")
        return Database._db_cur.fetchone()

    def insert_journal(self, journal_scheme: JournalScheme):
        sql = "INSERT INTO journal(id, entrance, exit, workerid) " \
              "VALUES(%s, %s, %s, %s);"
        Database._db_cur.execute(sql, (journal_scheme.id, journal_scheme.entrance,
                                       journal_scheme. exit, journal_scheme.worker_id))
        Database._db_connection.commit()

    def insert_journal_list(self, journal_scheme_list):
        for journal_scheme in journal_scheme_list:
            self.insert_journal(journal_scheme)

    def update_journal(self, journal_scheme: JournalScheme):
        sql = """ UPDATE journal
                    SET exit = %s,
                    entrance = %s,
                    workerid = %s
                    WHERE id = %s"""
        Database._db_cur.execute(sql, (journal_scheme.exit, journal_scheme.entrance,
                                       journal_scheme.worker_id, journal_scheme.id))
        Database._db_connection.commit()

    def delete_journal(self, journal_id):
        Database._db_cur.execute(f"""DELETE FROM journal WHERE id = '{journal_id}'""")
        Database._db_connection.commit()

    def get_department(self, department_id):
        Database._db_cur.execute(f"""SELECT * FROM department WHERE id = '{department_id}'""")
        return Database._db_cur.fetchone()

    def insert_department(self, department_scheme: DepartmentScheme):
        sql = "INSERT INTO department(id, production) " \
              "VALUES(%s, %s);"
        Database._db_cur.execute(sql, (department_scheme.id, department_scheme.production))
        Database._db_connection.commit()

    def insert_department_list(self, department_scheme_list):
        for department_scheme in department_scheme_list:
            self.insert_department(department_scheme)

    def update_department(self, department_scheme: DepartmentScheme):
        sql = """ UPDATE department
                    SET production = %s
                    WHERE id = %s"""
        Database._db_cur.execute(sql, (department_scheme.production, department_scheme.id))
        Database._db_connection.commit()

    def delete_department(self, department_id):
        Database._db_cur.execute(f"""DELETE FROM department WHERE id = '{department_id}'""")
        Database._db_connection.commit()

    def get_worker(self, worker_id):
        Database._db_cur.execute(f"""SELECT * FROM worker WHERE id = '{worker_id}'""")
        return Database._db_cur.fetchone()

    def insert_worker(self, worker_scheme: WorkerScheme):
        sql = "INSERT INTO worker(id, name, isstillworking, departmentid) " \
              "VALUES(%s, %s, %s, %s);"
        Database._db_cur.execute(sql, (worker_scheme.id, worker_scheme.name,
                                       worker_scheme.is_still_working, worker_scheme.department_id))
        Database._db_connection.commit()

    def update_worker(self, worker_scheme: WorkerScheme):
        sql = """ UPDATE worker
                    SET name = %s, 
                    isstillworking = %s,
                    departmentid = %s
                    WHERE id = %s"""
        Database._db_cur.execute(sql, (worker_scheme.name, worker_scheme.is_still_working,
                                       worker_scheme.department_id, worker_scheme.id))
        Database._db_connection.commit()

    def delete_worker(self, worker_id):
        Database._db_cur.execute(f"""DELETE FROM worker WHERE id = '{worker_id}'""")
        Database._db_connection.commit()

    def get_worker_card(self, worker_card_id):
        Database._db_cur.execute(f"""SELECT * FROM workercard WHERE id = '{worker_card_id}'""")
        return Database._db_cur.fetchone()

    def insert_worker_card(self, worker_card_scheme: WorkerCardScheme):
        sql = "INSERT INTO workercard(id, isactive, workerid) " \
              "VALUES(%s,  %s, %s);"
        Database._db_cur.execute(sql, (worker_card_scheme.id, worker_card_scheme.is_active,
                                       worker_card_scheme.worker_id))
        Database._db_connection.commit()

    def insert_worker_card_list(self, worker_card_scheme_list):
        for worker_card_scheme in worker_card_scheme_list:
            self.insert_worker_card(worker_card_scheme)

    def update_worker_card(self, worker_card_scheme: WorkerCardScheme):
        sql = """ UPDATE workercard
                    SET isactive = %s,
                    workerid
                    WHERE id = %s"""
        Database._db_cur.execute(sql, (worker_card_scheme.is_active,
                                       worker_card_scheme.worker_id, worker_card_scheme.id))
        Database._db_connection.commit()

    def delete_worker_card(self, worker_card_id):
        Database._db_cur.execute(f"""DELETE FROM workercard WHERE id = '{worker_card_id}'""")
        Database._db_connection.commit()

    def get_table_string(self, table_name):
        sql = "SELECT * FROM {0}".format(table_name)
        return pd.read_sql(sql, self._db_connection)

    def search_by_still_working(self, still_working):
        sql = f"""SELECT * FROM worker WHERE isstillworking = 
                                '{still_working}'"""
        return pd.read_sql(sql, self._db_connection)

    def search_by_exit_range(self, left_boundary, right_boundary):
        sql = f"""SELECT * FROM journal JOIN worker ON worker.id = journal.workerid WHERE exit >= 
                                '{left_boundary}' AND exit < '{right_boundary}'"""
        return pd.read_sql(sql, self._db_connection)

    def search_by_still_working_and_exit_range(self, still_working, left_boundary, right_boundary):
        sql = f"""SELECT * FROM journal JOIN worker ON worker.id = journal.workerid WHERE exit >= 
                                '{left_boundary}' AND exit < '{right_boundary}' AND isstillworking = 
                                '{still_working}' """
        return pd.read_sql(sql, self._db_connection)

    def search_by_word_not_belong(self, word):
        sql = f"""SELECT * FROM worker WHERE to_tsvector(name) @@ to_tsquery('!{word}');"""
        return pd.read_sql(sql, self._db_connection)

    def search_by_phrase(self, phrase):
        sql = f"""SELECT * FROM department 
                  WHERE to_tsvector(production) @@ plainto_tsquery('{phrase}');"""
        return pd.read_sql(sql, self._db_connection)

    def get_random_worker_id(self):
        Database._db_cur.execute("SELECT id FROM worker")
        worker_id_arr = Database._db_cur.fetchall()
        rand_index = random.randint(0, (len(worker_id_arr) - 1))
        return worker_id_arr[rand_index]

    def get_random_department_id(self):
        Database._db_cur.execute("SELECT id FROM department")
        department_id_arr = Database._db_cur.fetchall()
        rand_index = random.randint(0, (len(department_id_arr) - 1))
        return department_id_arr[rand_index]


