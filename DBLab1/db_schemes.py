

class DepartmentScheme:
    production = ""
    id = ""

    def __init__(self,
                 department_id="",
                 production="dich"):
        self.id = department_id
        self.production = production


class WorkerScheme:
    id = ""
    name = "vasya"
    is_still_working = "true"
    department_id = "0"

    def __init__(self,
                 worker_id="0",
                 name="vasya",
                 is_still_working="true",
                 department_id="null"):
        self.id = worker_id
        self.name = name
        self.is_still_working = is_still_working
        self.department_id = department_id


class JournalScheme:
    id = "0"
    worker_id = "null"
    entrance = "2004-10-19 10:23:54"
    exit = "2004-10-19 10:23:54"

    def __init__(self, journal_id="0",
                 worker_id="null",
                 entrance_time="2004-10-19 10:23:54",
                 exit_time="2004-10-19 10:23:54"):
        self.id = journal_id
        self.worker_id = worker_id
        self.entrance = entrance_time
        self.exit = exit_time


class WorkerCardScheme:
    id = "0"
    worker_id = "null"
    is_active = "true"

    def __init__(self, card_id="0",
                 worker_id="null",
                 is_active="true"):
        self.id = card_id
        self.worker_id = worker_id
        self.is_active = is_active
