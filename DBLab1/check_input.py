import datetime

from database import Database


class CheckInput:

    def test_timestamp(time_str):
        try:
            datetime.datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')  # '2004-10-19 10:23:54'
            return True
        except ValueError:
            return False

    def check_worker_existence(worker_id):
        db = Database()
        return db.get_worker(worker_id) is not None

    def check_department_existence(department_id):
        db = Database()
        return db.get_department(department_id) is not None

    def check_worker_card_existence(worker_card_id):
        db = Database()
        return db.get_worker_card(worker_card_id) is not None

    def check_journal_existence(journal_id):
        db = Database()
        return db.get_journal(journal_id) is not None
