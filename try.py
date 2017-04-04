# coding=utf-8
# -*- coding: utf-8 -*-

import math

# def judge(selfLocation, centerLocation, extent):
#     def distance(latitude1, latitude2, longitude1, longitude2):
#         radLat1 = math.radians(latitude1)
#         radLat2 = math.radians(latitude2)
#         radLon1 = math.radians(longitude1)
#         radLon2 = math.radians(longitude2)
#         a = radLat1 - radLat2
#         b = radLon1 - radLon2
#         r = 6378137
#         l = 2 * r * math.asin((math.sin(a / 2.) ** 2 + math.cos(radLat1) * math.cos(radLat2) * math.sin(b / 2.) ** 2) ** 0.5)
#         return l


def twoCircle(r1, r2, l):
    if r2 > r1:
        r1, r2 = r2, r1
    if r1 > l + r2:  # 整个被吞了
        return math.pi * r2 ** 2
    if r1 > l:  # 圆心被吞了
        dy = (r1 ** 2 - ((r1 ** 2 - r2 ** 2 + l ** 2) / (2 * l)) ** 2) ** 0.5
        a = 2 * math.asin(dy / r1)
        b = 2 * math.asin(dy / r2)
        s = math.pi * r2 ** 2 + r1 ** 2 / 2 * (a - math.sin(a)) - r2 ** 2 / 2 * (b - math.sin(b))
        return s
    elif r1 <= l - r2:  # 相离
        return 0
    elif r1 <= l:  # 普通相交
        dy = (r1 ** 2 - ((r1 ** 2 - r2 ** 2 + l ** 2) / (2 * l)) ** 2) ** 0.5
        a = 2 * math.asin(dy / r1)
        b = 2 * math.asin(dy / r2)
        s = r1 ** 2 / 2 * (a - math.sin(a)) + r2 ** 2 / 2 * (b - math.sin(b))
        return s


def dProbability(x, dx):
    probability1 = (twoCircle(R1, x + dx, R) - twoCircle(R1, x, R)) / (math.pi * R1 ** 2)
    probability2 = twoCircle(T, R2, x) / (math.pi * R2 ** 2)
    return probability1 * probability2


def integral(func, upperLimit, lowerLimit, d):
    dx = (upperLimit - lowerLimit) / d
    x = lowerLimit
    result = 0
    while x < upperLimit:
        result += func(x, dx)
        x += dx
    return result

    # lat1 = float(selfLocation[0])
    # lon1 = float(selfLocation[1])
    # lat2 = float(centerLocation[0])
    # lon2 = float(centerLocation[1])
# R = distance(lat1, lat2, lon1, lon2)
# R1 = float(centerLocation[2])
# R2 = float(selfLocation[2])
# T = float(extent)
R = 20.
R1 = 40.
R2 = 40.
T = 10.
upper = R + R1
lower = R - R1
if lower <= 0:
    lower = 0.0001
print integral(dProbability, upper, lower, 1000.)
