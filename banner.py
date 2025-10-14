#!/usr/bin/env python3
"""
ASCII Banner for 6-7 Meme Detector
Shows a cool banner when the detector starts
"""

def print_banner():
    """Print ASCII art banner for the detector"""
    banner = r"""
    ╔════════════════════════════════════════════════════════════╗
    ║                                                            ║
    ║     ██████╗      ███████╗    ███╗   ███╗███████╗███╗   ███║
    ║    ██╔════╝      ╚════██║    ████╗ ████║██╔════╝████╗ ████║
    ║    ███████╗█████╗    ██╔╝    ██╔████╔██║█████╗  ██╔████╔██║
    ║    ██╔═══██╗      ██╔╝       ██║╚██╔╝██║██╔══╝  ██║╚██╔╝██║
    ║    ╚██████╔╝      ███████╗   ██║ ╚═╝ ██║███████╗██║ ╚═╝ ██║
    ║     ╚═════╝       ╚══════╝   ╚═╝     ╚═╝╚══════╝╚═╝     ╚═║
    ║                                                            ║
    ║              ██████╗ ███████╗████████╗███████╗ ██████╗████║
    ║              ██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔════╝╚══██║
    ║              ██║  ██║█████╗     ██║   █████╗  ██║       ████║
    ║              ██║  ██║██╔══╝     ██║   ██╔══╝  ██║       ╚══██║
    ║              ██████╔╝███████╗   ██║   ███████╗╚██████╗  ████║
    ║              ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝ ╚═════╝  ╚══╝║
    ║                                                            ║
    ║                🔥 Show 6 or 7 fingers to trigger! 🔥        ║
    ║                                                            ║
    ╚════════════════════════════════════════════════════════════╝
    """
    print(banner)
    print()

def print_simple_banner():
    """Print a simpler banner for terminals that don't support box drawing"""
    banner = """
    ============================================================
    
                    6-7 MEME DETECTOR
                    
              Show 6 or 7 fingers to trigger!
              
                        🔥🔥🔥
                        
    ============================================================
    """
    print(banner)

if __name__ == "__main__":
    try:
        print_banner()
    except UnicodeEncodeError:
        print_simple_banner()
