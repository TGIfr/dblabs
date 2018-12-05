from sqlalchemy import Column, String, Integer, Boolean, Date

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DepartmentScheme(Base):
    __tablename__ = "department"

    id = Column(Integer, primary_key=True)
    production = Column(String)

    def __init__(self,
                 department_id="",
                 production="dich"):
        self.id = department_id
        self.production = production


class WorkerScheme(Base):
    __tablename__ = "worker"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    is_still_working = Column(Boolean)
    department_id = Column(Integer)

    def __init__(self,
                 worker_id="0",
                 name="vasya",
                 is_still_working="true",
                 department_id="null"):
        self.id = worker_id
        self.name = name
        self.is_still_working = is_still_working
        self.department_id = department_id


class JournalScheme(Base):
    __tablename__ = "journal"

    id = Column(Integer, primary_key=True)
    worker_id = Column(Integer)
    entrance = Column(Date)
    exit = Column(Date)

    def __init__(self, journal_id="0",
                 worker_id="null",
                 entrance_time="2004-10-19 10:23:54",
                 exit_time="2004-10-19 10:23:54"):
        self.id = journal_id
        self.worker_id = worker_id
        self.entrance = entrance_time
        self.exit = exit_time


class WorkerCardScheme(Base):
    __tablename__ = "workercard"

    id = Column(Integer, primary_key=True)
    worker_id = Column(Integer)
    is_active = Column(Boolean)

    def __init__(self, card_id="0",
                 worker_id="null",
                 is_active="true"):
        self.id = card_id
        self.worker_id = worker_id
        self.is_active = is_active
