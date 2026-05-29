#!/usr/bin/env python3
"""
HubBase All Platforms (hbap) Launcher
Unified entry point for HubBase PC, HubBasePE, HubBaseJE, and the website.
"""

import os
import sys
import subprocess
import webbrowser


def _run_py(script, cwd):
    """Run a Python script in a new console window (blocks until done)."""
    if sys.platform == "win32":
        py = sys.executable
        if py.endswith("pythonw.exe"):
            py = py[:-11] + "python.exe"
        print("Launching... (close HubBase window to return)")
        subprocess.run([py, script], cwd=cwd,
                       creationflags=subprocess.CREATE_NEW_CONSOLE)
    else:
        subprocess.run([sys.executable, script], cwd=cwd)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PC_DIR = os.path.join(BASE_DIR, "pc")
PE_DIR = os.path.join(BASE_DIR, "pe")
JE_DIR = os.path.join(BASE_DIR, "je")
WEBSITE_DIR = os.path.join(BASE_DIR, "website")
BETAS_DIR = os.path.join(PC_DIR, "betas")
RCS_DIR = os.path.join(PC_DIR, "rcs")


def launch_pc():
    """Launch HubBase (PC edition)."""
    pc_main = os.path.join(PC_DIR, "HubBase.py")
    if not os.path.exists(pc_main):
        print("Error: {} not found.".format(pc_main))
        return
    _run_py(pc_main, PC_DIR)


def launch_pe():
    """Launch HubBasePE (Pocket Edition)."""
    pe_main = os.path.join(PE_DIR, "Main.py")
    if not os.path.exists(pe_main):
        print("Error: {} not found.".format(pe_main))
        return
    _run_py(pe_main, PE_DIR)


def launch_je():
    """Launch HubBaseJE (Java/JS Edition) via Node.js."""
    je_main = os.path.join(JE_DIR, "HB-JS.js")
    if not os.path.exists(je_main):
        print("Error: {} not found.".format(je_main))
        return
    os.chdir(JE_DIR)
    try:
        if sys.platform == "win32":
            subprocess.Popen(["node", je_main], cwd=JE_DIR,
                             creationflags=subprocess.CREATE_NEW_CONSOLE)
        else:
            subprocess.Popen(["node", je_main], cwd=JE_DIR)
        print("[Launched Node.js in a new window -- check your taskbar]")
    except FileNotFoundError:
        print("Error: Node.js is not installed or not in PATH.")
        print("Download Node.js from https://nodejs.org/")


def open_website():
    """Open the HubBase Authority website in the default browser."""
    index = os.path.join(WEBSITE_DIR, "index-pr-hb-d.html")
    if os.path.exists(index):
        webbrowser.open("file://" + os.path.abspath(index))
    else:
        webbrowser.open("https://hubbase-authority.vercel.app")


def launch_version_backlog():
    """Launch HubBase Version Backlog."""
    vb_script = os.path.join(PC_DIR, "Version Backlog.py")
    if not os.path.exists(vb_script):
        print("Error: {} not found.".format(vb_script))
        return
    _run_py(vb_script, PC_DIR)


def launch_betas():
    """Launch HubBase (Betas branch)."""
    beta_script = os.path.join(BETAS_DIR, "HubBaseB.py")
    if not os.path.exists(beta_script):
        print("Error: {} not found.".format(beta_script))
        return
    _run_py(beta_script, BETAS_DIR)


def launch_rcs():
    """Launch HubBase (RCs branch)."""
    rc_script = os.path.join(RCS_DIR, "HubBaseB.py")
    if not os.path.exists(rc_script):
        print("Error: {} not found.".format(rc_script))
        return
    _run_py(rc_script, RCS_DIR)


def show_menu():
    """Display the launcher menu."""
    W = 42
    line = "+" + "-" * W + "+"
    def L(text): return "|" + text.ljust(W) + "|"
    menu = "\n".join([
        line,
        L("       HubBase All Platforms Launcher"),
        L("         v0.1.0.indev1"),
        line,
        L("  1) HubBase (PC Edition)"),
        L("  2) HubBasePE (Pocket Edition)"),
        L("  3) HubBaseJE (Java/JS Edition)"),
        L("  4) Open Website"),
        L("  5) Version Backlog"),
        L("  6) HubBase Betas Branch"),
        L("  7) HubBase RCs Branch"),
        L("  0) Exit"),
        line,
    ])
    print("\n" + menu)


def main():
    while True:
        show_menu()
        choice = input("Select an option: ").strip()
        if choice == "1":
            launch_pc()
        elif choice == "2":
            launch_pe()
        elif choice == "3":
            launch_je()
        elif choice == "4":
            open_website()
        elif choice == "5":
            launch_version_backlog()
        elif choice == "6":
            launch_betas()
        elif choice == "7":
            launch_rcs()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        if choice != "0":
            input("\nPress Enter to return to the menu...")


if __name__ == "__main__":
    main()
