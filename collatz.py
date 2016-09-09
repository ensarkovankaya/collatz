#!/usr/bin/python
# -*- coding:utf-8 -*-

import timeit

class Collatz:

    def __init__(self):

        self.CACHE = {}  # Cache results of calculate function if savecalculations is True
        self.usecache = True  # if False it will recalculate number every time and not use CACHE
        self.savecalculations = True
        self.saveresults = True
        self.TREE = []  # Each result store here
        self.recalculate = False  # If True, it will recalculate given start function paramater
        self.CALCULATIONS = {}  # Calculation final results cache in here if saveresults is True

    def _set_time(self):
        return timeit.default_timer()

    def calculate(self, s):

        if self.usecache:
            if s in self.CACHE:
                return self.CACHE.get(s)

        if s == 1:
            return s
        elif s % 2 == 0:
            return s / 2
        else:
            return s * 3 + 1

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

        # if calculation done before return last result
        if n in self.CALCULATIONS and not self.recalculate:
            result = self.CALCULATIONS.get(n)
            result["Recalculated"] = False
            return result

        n = int(n)
        started = self._set_time()
        step = 0
        number = n

        while n != 1:
            y = n
            n = self.calculate(n)
            self.TREE.append(n)
            if self.savecalculations:
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

        if self.saveresults:
            self.CALCULATIONS.setdefault(number, result)
        return result