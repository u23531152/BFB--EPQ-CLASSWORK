print("1. The optimal production quantity decreases. A faster machine finishes each run quicker so there is no need for inventory buffer between each run.")
print("2. The two formulas are nearly identical. Since production is much higher tan the demand rate, the d/p reduces to 0. This makes the extra multiplication factor in the EPQ reduce to 1 and this leaves the EPQ formula as the EOQ formula. ")
import math

annual_demand = 12000        # units per year
setup_cost = 50              # cost per production run, in Rand
holding_cost = 2              # cost per unit per year, in Rand
daily_demand_rate = 40       # units sold/used per day
daily_production_rate = 100000  # units your process can make per day

def calculate_epq(demand, setup, hold_cost, d_rate, p_rate):
    return math.sqrt((2 * demand * setup) / (hold_cost * (1 - d_rate / p_rate)))

epq = calculate_epq(annual_demand, setup_cost, holding_cost,
                     daily_demand_rate, daily_production_rate)

runs_per_year = annual_demand / epq
run_length_days = epq / daily_production_rate

max_inventory = epq * (1 - daily_demand_rate / daily_production_rate)

print("Optimal production quantity:", round(epq, 2))
print("Production runs per year:", round(runs_per_year, 2))
print("Length of each run (days):", round(run_length_days, 1))
print("Maximum inventory level:", round(max_inventory, 2))