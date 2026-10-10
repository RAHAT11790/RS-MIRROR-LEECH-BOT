"""Single entry point for RS Mirror Leech Bot (native Python, no Docker)."""
from runpy import run_module

if __name__ == "__main__":
    run_module("bot", run_name="__main__", alter_sys=True)
