print("Adding two SKUs does not change the split much, it just changes A and B to 4 and C stays at 2. Changing the classification thresholds increases the middle tier B to 4 but keeps tiers A and C at 3.")


skus = [
    {"sku": "BRK-100", "demand": 2000, "cost": 45},
    {"sku": "GSK-220", "demand": 1500, "cost": 30},
    {"sku": "BLT-010", "demand": 10000, "cost": 2},
    {"sku": "BRG-330", "demand": 800, "cost": 60},
    {"sku": "SEAL-500","demand": 3000, "cost": 5},
    {"sku": "MTR-700", "demand": 50, "cost": 800},
    {"sku": "WSH-050", "demand": 20000, "cost": 0.5},
    {"sku": "CBL-900", "demand": 400, "cost": 25},
    {"sku": "New1-900", "demand": 450, "cost": 25},
    {"sku": "New2-800", "demand": 400, "cost": 35}
]

def usage_value(demand, cost):
    return demand * cost

def assign_tier(cum_pct):
    if cum_pct <= 70:
        return "A"
    elif cum_pct <= 90:
        return "B"
    else:
        return "C"

def classify_inventory(skus):
    for item in skus:
        item["value"] = usage_value(item["demand"], item["cost"])
    skus_sorted = sorted(skus, key=lambda item: item["value"], reverse=True)
    total_value = sum(item["value"] for item in skus_sorted)
    running_total = 0
    for item in skus_sorted:
        running_total += item["value"]
        item["cum_pct"] = (running_total / total_value) * 100
        item["tier"] = assign_tier(item["cum_pct"])
    return skus_sorted   # <-- this is what you use outside the function

skus = [
    {"sku": "BRK-100", "demand": 2000, "cost": 45},
    # ... rest of your SKUs
]

result = classify_inventory(skus)   # <-- call it and capture the return value

for item in result:
    print(item["sku"], "| value:", item["value"],
          "| cum %:", round(item["cum_pct"], 1),
          "| tier:", item["tier"])

tier_counts = {"A": 0, "B": 0, "C": 0}
for item in result:
    tier_counts[item["tier"]] += 1
print(tier_counts)