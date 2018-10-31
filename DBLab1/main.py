#!/usr/bin/env python
# encoding: utf-8
import string

import datetime

from get_char import switch
from database import Database
from check_input import CheckInput
from user_input_getters import UserInput
from randomize import Randomize
from fill_db import RandomFillDB

db = Database()
user_input = UserInput()


def delete_entity(db_name):
    if db_name == "worker":
        worker_id = user_input.get_id()

        if not CheckInput.check_worker_existence(worker_id):
            print("There is no such worker in db!\n")
        else:
            db.delete_worker(worker_id)

    elif db_name == "journal":
        journal_id = user_input.get_id()

        if not CheckInput.check_journal_existence(journal_id):
            print("There is no such journal in db!\n")
        else:
            db.delete_journal(journal_id)

    elif db_name == "department":
        department_id = user_input.get_id()

        if not CheckInput.check_department_existence(department_id):
            print("There is no such department in db!\n")
        else:
            db.delete_department(department_id)

    elif db_name == "worker_card":
        worker_card_id = user_input.get_id()

        if not CheckInput.check_worker_card_existence(worker_card_id):
            print("There is no such worker card in db!\n")
        else:
            db.delete_worker_card(worker_card_id)


def update_entity(db_name):
    if db_name == "department":
        department_entity = user_input.read_department_update_input()
        if department_entity is not None:
            db.update_department(department_entity)
            return True

    elif db_name == "journal":
        worker_entity = user_input.read_journal_update_input()
        if worker_entity is not None:
            db.update_journal(worker_entity)
            return True

    elif db_name == "worker":
        worker_entity = user_input.read_worker_update_input()
        if worker_entity is not None:
            db.update_worker(worker_entity)
            return True

    elif db_name == "worker_card":
        worker_card_entity = user_input.read_worker_card_update_input()
        if worker_card_entity is not None:
            db.update_worker_card(worker_card_entity)
            return True

    return False


def add_entity(db_name):
    if db_name == "journal":
        db.insert_journal(user_input.read_journal_input())

    elif db_name == "worker":
        db.insert_worker(user_input.read_worker_input())

    elif db_name == "worker_card":
        db.insert_worker_card(user_input.read_worker_card_input())

    elif db_name == "department":
        db.insert_department(user_input.read_department_input())


def fill_rand(db_name):
    input_str = input("INPUT INTEGER NUMBER OF ENTITIES TO MAKE: ")
    random_fill = RandomFillDB()
    if db_name == "worker":
        random_fill.add_n_workers(int(input_str))

    elif db_name == "journal":
        random_fill.add_n_journals(int(input_str))

    elif db_name == "worker_card":
        random_fill.add_n_worker_cards(int(input_str))

    elif db_name == "department":
        random_fill.add_n_departments(int(input_str))


def get_db_name():
    while 1:
        switchVariable = input(
            "CHOOSE DB BY ITS NUMBER\npossible are: \n\t1 - department, \n\t2 - worker, \n\t3 - worker_card, "
            "\n\t4 - journal,"
            "\n\tb - go to main menu\nType here and press enter: ")
        for case in switch(switchVariable):
            if case('1'):
                return "department"
            if case('2'):
                return "worker"
            if case('3'):
                return "worker_card"
            if case('4'):
                return "journal"
            if case('b'):
                break
            else:
                print("____________________")
                print("no such option, try again!")


def search_in_db(criteria):
    if criteria == "by_exit_range":
        date1 = user_input.get_date()
        date2 = user_input.get_date()
        print(db.search_by_exit_range(date1, date2))

    elif criteria == "by_still_working":
        is_working = user_input.get_boolean()
        print("\nSearch result:")
        print(db.search_by_still_working(is_working))

    elif criteria == "by_exit_range_and_still_working":
        date1 = user_input.get_date()
        date2 = user_input.get_date()
        is_working = user_input.get_boolean()
        print(db.search_by_still_working_and_exit_range(is_working, date1, date2))

    elif criteria == "by_word_not_belong":
        name = input("enter worker name: ")
        print(db.search_by_word_not_belong(name))

    elif criteria == "by_whole_sentence":
        production = input("enter department production: ")
        print(db.search_by_phrase(production))


def get_criteria():
    while 1:
        switchVariable = input("CHOOSE SEARCH CRITERIA BY ITS NUMBER\npossible are: \n\t1 - by_exit_range, \n\t2 - "
                               "by_still_working, \n\t3 - by_exit_range_and_still_working, "
                               "\n\t4 - by_word_not_belong (worker name), \n\t5 - by_whole_sentence (department"
                               " production)\n\tb - go to main menu\nType here and press enter: ")
        for case in switch(switchVariable):
            if case('1'):
                return "by_exit_range"
            if case('2'):
                return "by_still_working"
            if case('3'):
                return "by_exit_range_and_still_working"
            if case('4'):
                return "by_word_not_belong"
            if case('5'):
                return "by_whole_sentence"
            if case('b'):
                break
            else:
                print("____________________")
                print("no such option, try again!")


while 1:
    switchVariable = input("CHOOSE COMMAND BY ITS NUMBER\npossible are: \n\t1 - add_entity, \n\t2 - fill_rand, \n\t3 "
                           "- update_entity\n\t4 - delete_entity,\n\t5 - search_in_db, \n\tq - quit\nType here and press enter: ")
    for case in switch(switchVariable):
        if case('1'):
            db_name = get_db_name()
            print("Table before insertion:\n", db.get_table_string(db_name))
            add_entity(db_name)
            print("Table after insertion:\n", db.get_table_string(db_name))
            print("____________________")
            break
        if case('2'):
            db_name = get_db_name()
            print("Table before insertion:\n", db.get_table_string(db_name))
            fill_rand(db_name)
            print("Table after insertion:\n", db.get_table_string(db_name))
            print("____________________")
            break
        if case('3'):
            db_name = get_db_name()
            print("Table before editing:\n", db.get_table_string(db_name))
            if update_entity(db_name):
                print("Table after editing:\n", db.get_table_string(db_name))
            print("____________________")
            break
        if case('4'):
            db_name = get_db_name()
            print("Table before delete:\n", db.get_table_string(db_name))
            delete_entity(db_name)
            print("Table after delete:\n", db.get_table_string(db_name))
            print("____________________")
            break
        if case('5'):
            criteria = get_criteria()
            search_in_db(criteria)
            print("____________________")
            break
        if case('q'):
            break
        else:
            print("____________________")
            print("no such option, try again!")

    if switchVariable == 'q':
        break
