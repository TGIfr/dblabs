from database import Database
from randomize import Randomize as r
from db_schemes import WorkerScheme
from db_schemes import WorkerCardScheme
from db_schemes import DepartmentScheme
from db_schemes import JournalScheme


class RandomFillDB:
    db = Database()

    def add_n_workers(self, n):
        for x in range(0, n):
            self.add_worker()

    def add_worker(self):
        self.db.insert_worker(
            WorkerScheme(
                str(r.generate_random_int(0, 9999)),
                r.generate_random_string(5, 15),
                str(r.generate_random_bool()),
                str(r.generate_random_int(0, 9999))
            )
        )

    def add_n_worker_cards(self, n):
        for x in range(0, n):
            self.add_worker_card()

    def add_worker_card(self):
        self.db.insert_worker_card(
            WorkerCardScheme(
                str(r.generate_random_int(0, 9999)),
                    str(r.generate_random_int(0, 9999)),
                    str(r.generate_random_bool()),
                    )
            )

    def add_n_departments(self, n):
        for x in range(0, n):
            self.add_department()

    def add_department(self):
        self.db.insert_department(
            DepartmentScheme(
                str(r.generate_random_int(0, 9999)),
                    r.generate_random_string(10, 25),
                    )
            )

    def add_n_journals(self, n):
        for x in range(0, n):
            self.add_journal()

    def add_journal(self):
        self.db.insert_journal(
            JournalScheme(
                str(r.generate_random_int(0, 9999)),
                str(r.generate_random_int(0, 9999)),
                str(r.generate_random_date()),
                str(r.generate_random_date())
            )
        )
