# Source for the requirement comments below: python06.pdf v2.0,
# printed pp. 14-15. These describe the assignment, not verified compliance.

# Exercise requirements from python06.pdf:
# - ft_kaboom_1.py will secretly access the dark_spellbook.py directly
#   and then try to record a dark spell.
# - This must fail and raise an exception. You can choose to catch it or
#   not; it's only for pedagogical purposes, indicating that your
#   alchemist laboratory has just exploded.

if __name__ == "__main__":
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")

    from alchemy.grimoire.dark_spellbook import dark_spell_record

    print(dark_spell_record("Fantasy", "Earth, wind and fire"))
