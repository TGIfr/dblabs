from database import Database
from get_char import switch
from check_input import CheckInput
from db_schemes import WorkerScheme
from db_schemes import WorkerCardScheme
from db_schemes import DepartmentScheme
from db_schemes import JournalScheme
import datetime

db = Database()


class UserInput:
    def read_worker_input(self):
        workerEntity = WorkerScheme()
        workerEntity.name = input("enter worker name: ")
        workerEntity.id = input("enter worker id: ")
        workerEntity.is_still_working = input("enter worker is still working (True/False): ")
        while workerEntity.is_still_working != "True" and workerEntity.is_still_working != "False":
            workerEntity.is_still_working = input("Wrong input!\nTry again: ")
        workerEntity.is_still_working = bool(workerEntity.is_still_working)
        workerEntity.department_id = input("enter department id: ")
        while not CheckInput.check_department_existence(workerEntity.department_id):
            input_str = input("There is no such department!\nWanna add?\n(y/n): ")
            for case in switch(input_str):
                if case('y'):
                    department_entity = self.read_department_input()
                    workerEntity.department_id = department_entity.id
                    db.insert_department(department_entity)
                    break
                if case('n'):
                    print("can't insert worker")
                    return
                else:
                    print("____________________")
                    print("no such option, try again!")
        return workerEntity

    def read_worker_card_input(self):
        worker_card_entity = WorkerCardScheme()
        worker_card_entity.id = input("enter id: ")
        worker_card_entity.worker_id = input("enter worker_id: ")
        while not CheckInput.check_worker_existence(worker_card_entity.worker_id):
            input_str = input("There is no such worker!\nWanna add?\n(y/n): ")
            for case in switch(input_str):
                if case('y'):
                    worker_entity = self.read_worker_input()
                    worker_card_entity.worker_id = worker_entity.id
                    db.insert_worker(worker_entity)
                    break
                if case('n'):
                    print("can't insert worker card ")
                    return
                else:
                    print("____________________")
                    print("no such option, try again!")

        worker_card_entity.is_active = input("enter is active: ")
        while worker_card_entity.is_active != "True" and worker_card_entity.is_active != "False":
            worker_card_entity.is_active = input("Wrong input!\nTry again: ")
        worker_card_entity.is_active = bool(worker_card_entity.is_active)
        return worker_card_entity

    def read_department_input(self):
        department_entity = DepartmentScheme()
        department_entity.id = input("enter id: ")
        department_entity.production = input("enter production: ")
        return department_entity

    def read_journal_input(self):
        journal_entity = JournalScheme()
        journal_entity.id = input("enter id: ")
        print("exit timestamp:")
        journal_entity.exit = self.get_date()
        print("entrance timestamp:")
        journal_entity.entrance = self.get_date()
        journal_entity.worker_id = input("worker id: ")
        while not CheckInput.check_worker_existence(journal_entity.worker_id):

            input_str = input("There is no such worker!\nWanna add?\n(y/n): ")
            for case in switch(input_str):
                if case('y'):
                    worker_entity = self.read_worker_input()
                    journal_entity.worker_id = worker_entity.id
                    db.insert_worker(worker_entity)
                    break
                if case('n'):
                    print("can't insert journal")
                    return
                else:
                    print("____________________")
                    print("no such option, try again!")
        return journal_entity

    def read_worker_update_input(self):
        workerEntity = WorkerScheme()
        workerEntity.name = input("enter worker name: ")
        workerEntity.id = input("enter worker id: ")
        if CheckInput.check_worker_existence(workerEntity.id):
            workerEntity.is_still_working = input("enter worker is still working (True/False): ")
            while workerEntity.is_still_working != "True" and workerEntity.is_still_working != "False":
                workerEntity.is_still_working = input("Wrong input!\nTry again: ")
            workerEntity.is_still_working = bool(workerEntity.is_still_working)
            workerEntity.department_id = input("enter department id: ")
            while not CheckInput.check_department_existence(workerEntity.department_id):
                input_str = input("There is no such department!\nWanna add?\n(y/n): ")
                for case in switch(input_str):
                    if case('y'):
                        department_entity = self.read_department_input()
                        workerEntity.department_id = department_entity.id
                        db.insert_department(department_entity)
                        break
                    if case('n'):
                        print("can't insert worker")
                        return
                    else:
                        print("____________________")
                        print("no such option, try again!")
            return workerEntity
        else:
            print("There is no such worker in db!")
            return None

    def read_worker_card_update_input(self):
        worker_card_entity = WorkerCardScheme()
        worker_card_entity.id = input("enter id: ")
        if CheckInput.check_worker_card_existence(worker_card_entity.id):
            worker_card_entity.worker_id = input("enter worker_id: ")
            while not CheckInput.check_worker_existence(worker_card_entity.worker_id):
                input_str = input("There is no such worker!\nWanna add?\n(y/n): ")
                for case in switch(input_str):
                    if case('y'):
                        worker_entity = self.read_worker_input()
                        worker_card_entity.worker_id = worker_entity.id
                        db.insert_worker(worker_entity)
                        break
                    if case('n'):
                        print("can't insert worker card ")
                        return
                    else:
                        print("____________________")
                        print("no such option, try again!")

            worker_card_entity.is_active = input("enter is active: ")
            while worker_card_entity.is_active != "True" and worker_card_entity.is_active != "False":
                worker_card_entity.is_active = input("Wrong input!\nTry again: ")
                worker_card_entity.is_active = bool(worker_card_entity.is_active)

            return worker_card_entity
        else:
            print("There is no such worker card in db!")
            return None

    def read_department_update_input(self):
        department_entity = DepartmentScheme()
        department_entity.id = input("enter id: ")
        if CheckInput.check_department_existence(department_entity.id):
            department_entity.production = input("enter production: ")
            return department_entity
        else:
            print("There is no such department in db!")
            return None

    def read_journal_update_input(self):
        journal_entity = JournalScheme()
        journal_entity.id = input("enter id: ")
        if CheckInput.check_journal_existence(journal_entity.id):
            print("exit timestamp:")
            journal_entity.exit = self.get_date()
            print("entrance timestamp:")
            journal_entity.entrance = self.get_date()
            journal_entity.worker_id = input("worker id: ")
            while not CheckInput.check_worker_existence(journal_entity.worker_id):

                input_str = input("There is no such worker!\nWanna add?\n(y/n): ")
                for case in switch(input_str):
                    if case('y'):
                        worker_entity = self.read_worker_input()
                        journal_entity.worker_id = worker_entity.id
                        db.insert_worker(worker_entity)
                        break
                    if case('n'):
                        print("can't insert journal")
                        return
                    else:
                        print("____________________")
                        print("no such option, try again!")
            return journal_entity
        else:
            print("There is no such journal in db!")
            return None


    def get_boolean(self):
        is_active = input("enter worker if worker is active (True/False): ")
        while is_active != "True" and is_active != "False":
            is_active = input("Wrong input!\nTry again: ")

        return is_active

    def get_id(self):
        return input("input id: ")

    def get_date(self):
        date = input("enter timestamp(format: %Y-%m-%d %H:%M:%S): ")
        while not CheckInput.test_timestamp(date):
            date = input("Wrong input!\nTry again: ")
        return datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')








