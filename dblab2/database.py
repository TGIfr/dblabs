import random

import pandas as pd


from db_schemes import WorkerScheme
from db_schemes import WorkerCardScheme
from db_schemes import DepartmentScheme
from db_schemes import JournalScheme

from db_schemes import Base

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime


class Database:
    _engine_ = create_engine('postgresql://dbuser:123456@localhost:5432/dblab1')
    _Session_ = sessionmaker(bind=_engine_)


    # _db_connection = psycopg2.connect(host="localhost", database="dblab1", user="dbuser", password="123456")
    # _db_cur = _db_connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def __init__(self):
        _engine_ = create_engine('postgresql://dbuser:123456@localhost:5432/dblab1')
        _Session_ = sessionmaker(bind=_engine_)
        Base.metadata.create_all(_engine_)
        self._session_ = _Session_()

    def close(self):
        self._session_.close()

    def get_journal(self, journal_id):
        return self._session_.query(JournalScheme).get(journal_id)

    def insert_journal(self, journal_scheme: JournalScheme):
        self._session_.add(journal_scheme)
        self._session_.commit()

    def insert_journal_list(self, journal_scheme_list):
        for journal_scheme in journal_scheme_list:
            self.insert_journal(journal_scheme)

    def update_journal(self, journal_scheme: JournalScheme):
        self.insert_journal(journal_scheme)

    def delete_journal(self, journal_id):
        self._session_.query(JournalScheme).filter_by(id=journal_id).delete()
        self._session_.commit()

    def get_department(self, department_id):
        return self._session_.query(DepartmentScheme).get(department_id)

    def insert_department(self, department_scheme: DepartmentScheme):
        self._session_.add(department_scheme)
        self._session_.commit()

    def insert_department_list(self, department_scheme_list):
        for department_scheme in department_scheme_list:
            self.insert_department(department_scheme)

    def update_department(self, department_scheme: DepartmentScheme):
        self.insert_department(department_scheme)

    def delete_department(self, department_id):
        self._session_.query(DepartmentScheme).filter_by(id=department_id).delete()
        self._session_.commit()

    def get_worker(self, worker_id):
        return self._session_.query(WorkerScheme).get(worker_id)

    def insert_worker(self, worker_scheme: WorkerScheme):
        self._session_.add(worker_scheme)
        self._session_.commit()

    def update_worker(self, worker_scheme: WorkerScheme):
        self.insert_worker(worker_scheme)

    def delete_worker(self, worker_id):
        self._session_.query(WorkerScheme).filter_by(id=worker_id).delete()
        self._session_.commit()

    def get_worker_card(self, worker_card_id):
        return self._session_.query(WorkerCardScheme).get(worker_card_id)

    def insert_worker_card(self, worker_card_scheme: WorkerCardScheme):
        self._session_.add(worker_card_scheme)
        self._session_.commit()

    def insert_worker_card_list(self, worker_card_scheme_list):
        for worker_card_scheme in worker_card_scheme_list:
            self.insert_worker_card(worker_card_scheme)

    def update_worker_card(self, worker_card_scheme: WorkerCardScheme):
        self.insert_worker_card(worker_card_scheme)

    def delete_worker_card(self, worker_card_id):
        self._session_.query(WorkerCardScheme).filter_by(id=worker_card_id).delete()
        self._session_.commit()

    def get_table_string(self, table_name):
        return self._session_.query(Base.metadata.tables[table_name]).all()

    def search_by_still_working(self, still_working):
        res = self._session_.query(WorkerScheme)\
            .filter(WorkerScheme.is_still_working == still_working)\
            .all()
        strings = ""
        for row in res:
            strings += str(row.__dict__) + "\n"
        return strings

    def search_by_exit_range(self, left_boundary, right_boundary):
        res = self._session_.query(JournalScheme) \
            .filter(JournalScheme.exit >= left_boundary.date(),
                    JournalScheme.exit < right_boundary.date()) \
            .all()
        strings = ""
        for row in res:
            strings += str(row.__dict__) + "\n"
        return strings

    def search_by_still_working_and_exit_range(self, still_working, left_boundary, right_boundary):
        res = self._session_.query(JournalScheme)\
            .filter(JournalScheme.worker_id == WorkerScheme.id)\
            .filter(WorkerScheme.is_still_working == still_working,
                    JournalScheme.exit >= left_boundary.date(),
                    JournalScheme.entrance < right_boundary.date())\
            .all()
        strings = ""
        for row in res:
            strings += str(row.__dict__) + "\n"
        return strings


    def search_by_word_not_belong(self, word):
        sql = f"""SELECT * FROM worker WHERE to_tsvector(name) @@ to_tsquery('!{word}');"""
        res = self._session_.execute(sql).fetchall()

        strings = ""
        for row in res:
            strings += str(dict(row.items())) + "\n"
        return strings

    def search_by_phrase(self, phrase):
        sql = f"""SELECT * FROM department 
                  WHERE to_tsvector(production) @@ phraseto_tsquery('english', '{phrase}');"""
        res = self._engine_.execute(sql).fetchall()

        strings = ""
        for row in res:
            strings += str(dict(row.items())) + "\n"
        return strings

    def get_random_worker_id(self):
        rand_index = random.randint(0, self._session_.query(WorkerScheme).count())
        return self._session_.query(WorkerScheme)[rand_index]

    def get_random_department_id(self):
        rand_index = random.randint(0, self._session_.query(DepartmentScheme).count())
        return self._session_.query(DepartmentScheme)[rand_index]
