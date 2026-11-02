#!/usr/bin/env python3
"""Awesome AI Localization Pipeline TCO Calculator 2026 (ElevenLabs + RunPod + Vast.ai)."""
import argparse

STACK = {
    "elevenlabs": {"name": "ElevenLabs Studio", "role": "Voice Synthesis & Dubbing", "cost_monthly": 82.50},
    "runpod": {"name": "RunPod Serverless", "role": "Whisper STT & LLM Translation", "cost_monthly": 25.00},
    "vastai": {"name": "Vast.ai GPU Nodes", "role": "Video Rendering & FFMPEG", "cost_monthly": 15.00}
}

def calculate():
    print("=" * 70)
    print("Awesome AI Video Localization Stack 2026: Monthly TCO")
    print("=" * 70)
    print(f"{'Component':<22} {'Role in Pipeline':<30} {'Monthly Cost'}")
    print("-" * 70)
    total = 0.0
    for key, data in STACK.items():
        cost = data["cost_monthly"]
        total += cost
        print(f"{data['name']:<22} {data['role']:<30} ${cost:.2f}/mo")
    print("-" * 70)
    print(f"{'Total Integrated Stack TCO':<53} ${total:.2f}/mo")
    print(f"{'Annual Capital Investment':<53} ${total * 12:.2f}/yr")
    print("=" * 70)
    return total

if __name__ == "__main__":
    calculate()
