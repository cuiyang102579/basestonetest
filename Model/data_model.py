# -*- coding:utf-8 -*-
# @author: cuiyang
# @Date: 2022/1/9 13:56
# @Software:basestonetest
# @Site    : 请求数据处理模板
# @File    : data_model.py

from typing import Optional, Dict, List, Any
from pydantic.main import ModelMetaclass
import pandas as pd


class DataTemplate:
    def __init__(self, template: ModelMetaclass):
        self.template: ModelMetaclass = template

    def __repr__(self):
        return f"DataTemplate({self.template().__dict__})"

    def __str__(self):
        return str(self.template())

    @property
    def default(self):
        """Return a single dict containing the default values"""
        return self.template().dict()

    def record(self, record: Optional[Dict] = None):
        """Generate a single dict from the template"""
        if record is None:
            record = {}
        return self.template(**record).dict()

    def records(self, records: List[Dict]) -> List[Dict]:
        """Generate a list of dicts conforming to the template"""
        return [self.template(**record).dict() for record in records]

    def dataframe(self, records: List[Dict]) -> Any:
        """Generate a pandas dataframe from a list of dicts"""
        return pd.DataFrame(self.records(records))
