#!/usr/bin/python
# -*- coding:utf-8 -*-

import timeit

class Collatz:

    def __init__(self):

        self.CACHE = {}
        self.usecache = True
        self.TREE = []
        self.recalculate = False
        self.CALCULATIONS = {}

    def _set_time(self):
        return timeit.default_timer()

    def calculate(self, s):

        if s == 1:
            self.TREE.append(s)
            return s
        elif s % 2 == 0:
            c = s / 2
            self.TREE.append(c)
            return c
        else:
            c = s * 3 + 1
            self.TREE.append(c)
            return c

    def _clean(self):
        self.TREE = []

    def _full_clean(self):
        self.__init__()

    def start(self, n):
        self._clean()

        if not isinstance(n, int):
            raise ValueError(u"Variable must be a number.")
        if n <= 1:
            raise ValueError(u"Number can not be 1 or lower.")
        if n in self.CALCULATIONS and not self.recalculate:
            result = self.CALCULATIONS.get(n)
            result["Recalculated"] = False
            return result
        n = int(n)

        started = self._set_time()
        step = 0
        number = n
        while n != 1:

            if self.usecache:
                if n in self.CACHE:
                    n = self.CACHE.get(n)
                    self.TREE.append(n)
                    step += 1
                    continue

            y = n
            n = self.calculate(n)
            self.CACHE.setdefault(y, n)
            step += 1

        ended = self._set_time()

        result = {
            "Number": number,
            "Step": step,
            "Start Time": started,
            "End Time": ended,
            "Calculated Time": ended - started,
            "Tree": self.TREE,
            "Recalculated": True,
        }

        self.CALCULATIONS.setdefault(number, result)
        return result