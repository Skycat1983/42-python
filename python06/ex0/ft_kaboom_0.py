# Exercise requirements from python06.pdf:
# - ft_kaboom_0.py will access the grimoire module directly and then
#   record a light spell, flawlessly.
# - There are multiple ways to avoid circular dependencies; you pick one.
#   Be prepared to explain the different approaches during the evaluation.

from alchemy.grimoire import light_spell_record


if __name__ == "__main__":
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    print("Testing record light spell", end=": ")
    print(light_spell_record("Fantasy", "Earth, wind and fire"))
