import math


# Data
B_TOTAL = 54978
B_NEG = 41484
B_POS = B_TOTAL - B_NEG
W_TOTAL = 38078
W_NEG = 27744
W_POS = W_TOTAL - W_NEG

# Proportions of negative comments
p_b = B_NEG / B_TOTAL
p_w = W_NEG / W_TOTAL

"""
AVERAGE COMMENT SCORES

# Standard Error (pooled standard deviation for z-test)
se = math.sqrt((p_b * (1 - p_b) / B_TOTAL) + (p_w * (1 - p_w) / W_TOTAL))

# Mean difference
mean_diff = p_b - p_w

# Null hypothesis difference
null_diff = 0  # Null hypothesis assumes no difference

# Z-test statistic
z = (mean_diff - null_diff) / se
"""

# Step 2: Calculate pooled proportion (p_combined)
p_combined = (B_NEG + W_NEG) / (B_TOTAL + W_TOTAL)

# Step 3: Calculate standard error
se = math.sqrt(p_combined * (1 - p_combined) * (1 / B_TOTAL + 1 / W_TOTAL))

# Step 4: Calculate z-score
z = (p_b - p_w) / se

# Print the result
print(f"Proportion for Group B: {p_b:.3f}")
print(f"Proportion for Group W: {p_w:.3f}")
print(f"Pooled Proportion: {p_combined:.3f}")
print(f"Standard Error: {se:.6f}")
print(f"Z-Score: {z:.3f}")
