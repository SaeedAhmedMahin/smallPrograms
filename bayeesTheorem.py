import numpy as np

# From Bayees Theorem

default_chance = 0.02 # P(D)
not_default_chance = 1 - default_chance # P(!D)

true_positive_rate = 0.90  # P(F|D)
false_positive_rate = 0.05 # P(F|!D)

# P(F) = P(F|D)P(D) + P(F|!D)P(!D)
flag_chance = (true_positive_rate * default_chance) + (false_positive_rate * not_default_chance)
# P(D|F) = P(F|D)P(D)/P(F)
analytical_posterior = (true_positive_rate * default_chance) / flag_chance

print(f"Analytical Posterior: {analytical_posterior:.4f}")
print("-" * 35)

np.random.seed(42)
n_companies = 1_000_000

# Simulate the true state of the companies (0 = Safe, 1 = Default)
# We generate random numbers; if < 0.02, it defaults.
random_states = np.random.rand(n_companies)
true_defaults = random_states < default_chance
true_safes = ~true_defaults

# Step B: Simulate the model flagging companies
random_flags = np.random.rand(n_companies)

# A company is flagged if it's a Default AND falls in the 90% true_positive_rate...
# OR if it's Safe AND falls in the 5% false_positive_rate.
flagged_true_positives = true_defaults & (random_flags < true_positive_rate)
flagged_false_positives = true_safes & (random_flags < false_positive_rate)

# Combine them to find all flagged companies
all_flagged = flagged_true_positives | flagged_false_positives

# Step C: Calculate the simulated posterior
# P(Default | Flag) = (Number of True Positives) / (Total Number Flagged)
total_flags = np.sum(all_flagged)
actual_defaults_caught = np.sum(flagged_true_positives)

simulated_posterior = actual_defaults_caught / total_flags

print(f"Total Companies:      {n_companies:,}")
print(f"Total Flagged:        {total_flags:,}")
print(f"True Defaults Caught: {actual_defaults_caught:,}")
print(f"Simulated Posterior:  {simulated_posterior:.4f}")