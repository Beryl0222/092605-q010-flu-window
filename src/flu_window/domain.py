"""儿童流感接种窗口调度的基础登记对象。"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Record:
    record_id: str
    owner_id: str
    state: str
    revision: int
    created_at: str
