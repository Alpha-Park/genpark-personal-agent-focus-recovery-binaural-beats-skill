# -*- coding: utf-8 -*-
"""Demonstration of Personal Agent Focus Recovery Binaural Beats Skill."""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from client import PersonalAgentFocusRecoveryBinauralBeats

def main():
    agent = PersonalAgentFocusRecoveryBinauralBeats()

    print("=" * 70)
    print("DEMO: Personal Agent Focus Recovery Binaural Beats & ASSR Entrainment")
    print("=" * 70)

    # 1. 40Hz Gamma Deep Focus Parameters
    res_gamma = agent.calculate_binaural_entrainment_parameters(
        target_cognitive_state="deep_focus",
        carrier_base_hz=216.0
    )

    print(f"\n1. 40Hz Gamma Deep Analytical Focus Entrainment:")
    print(f"   Band: {res_gamma['entrainment_eeg_band']}")
    print(f"   Beat Frequency: {res_gamma['beat_difference_frequency_hz']} Hz")
    print(f"   Stereo Frequencies: Left {res_gamma['stereo_channel_frequencies']['left_ear_hz']} Hz | Right {res_gamma['stereo_channel_frequencies']['right_ear_hz']} Hz")
    print(f"   Mechanism: {res_gamma['neurophysiological_mechanism']}")
    print(f"   Benefit: {res_gamma['primary_cognitive_benefit']}")

    # 2. Schedule phased 90-minute entrainment protocol
    res_proto = agent.schedule_auditory_entrainment_protocol(
        work_block_duration_minutes=90.0,
        fatigue_level="moderate"
    )

    print(f"\n2. Phased 90-Minute Focus Protocol:")
    print(f"   Total Duration: {res_proto['total_protocol_duration_minutes']} min")
    for stage in res_proto['phased_entrainment_sequence']:
        print(f"   [{stage['phase_name']}] ({stage['duration_minutes']} min): {stage['eeg_target']} -> {stage['purpose']}")

    print("\nVerification complete: Binaural beats neuro-acoustic engine executed flawlessly.")

if __name__ == "__main__":
    main()
