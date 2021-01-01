# -*- coding: utf-8 -*-
import csv
import random

def csv_to_list(csv_path):
    """read csv, change to list"""
    
    with open(csv_path) as f:
        read_csv = csv.reader(f)
        origina_menu = [row for row in read_csv]
    return origina_menu

def first_manu(origina_menu, budget, menus):
    """select first menu"""

    first_menu= random.choice(origina_menu)
    menus.append(first_menu)
    budget -= int(first_menu[1])
    return menus, budget

def more_select(budget, origina_menu, menus):
    """"choise buyable more menu"""

    while budget > 0:
        candidate = []

        for i in range(len(origina_menu)):
            x = int(i)
            candidate_price = int(origina_menu[x][1])
            if candidate_price <= budget:
                candidate.append(origina_menu[x])

        if not candidate:
            break

        food = random.choice(candidate)

        menus.append(food)
        now_food_price = food[1]
        budget -= int(now_food_price)
    
    return menus, budget

def calculation():
    menus = []

    money = 1000
    budget = money

    csv_path = 'menu.csv'

    origina_menu = csv_to_list(csv_path)
    menus, budget = first_manu(origina_menu, budget, menus)    
    menus, budget = more_select(budget, origina_menu, menus)

    return menus,money,budget

# def result_menu(menus):
#     return menus

# def result_amount(money, budget):
#     total_fee = money - budget
#     return total_fee
