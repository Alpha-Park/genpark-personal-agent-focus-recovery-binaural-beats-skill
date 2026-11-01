# -*- coding: utf-8 -*-
"""
Personal Agent Focus Recovery Binaural Beats Client
Zero-dependency Auditory Steady-State Response (ASSR) brainwave entrainment calculator,
superior olivary complex phase-difference modeler, and cognitive state soundscape scheduler.
"""

import math
from typing import Dict, List, Any, Optional

class PersonalAgentFocusRecoveryBinauralBeats:
    """
    Calculates carrier and beat frequency pairings for electroencephalographic (EEG) frequency-following
    responses (FFR) via the superior olivary complex, scheduling Gamma, Beta, Alpha, and Theta protocols.
    """

    def calculate_binaural_entrainment_parameters(
        self,
        target_cognitive_state: str = "deep_focus",
        carrier_base_hz: float = 216.0
    ) -> Dict[str, Any]:
        """
        Calculates exact left and right ear sine wave frequencies to induce the desired
        interaural phase difference beat frequency: f_beat = |f_right - f_left|.
        Carrier frequencies between 150Hz and 450Hz achieve the highest auditory cortex entrainment.
        """
        carrier = max(100.0, min(500.0, float(carrier_base_hz)))
        state = str(target_cognitive_state).lower()

        # Brainwave target parameters
        if "gamma" in state or "high_focus" in state or "deep_focus" in state or "code" in state:
            beat_hz = 40.0 # 40 Hz Gamma: Microglial clearance, cognitive binding, peak working memory
            band_name = "Gamma Oscillations (38 - 42 Hz)"
            function_desc = "Peak analytical focus, complex mathematical proof solving, working memory binding."
            max_session_mins = 60.0
        elif "beta" in state or "active_work" in state or "execution" in state:
            beat_hz = 18.0 # 18 Hz Beta: High alertness, administrative execution
            band_name = "Beta Oscillations (15 - 20 Hz)"
            function_desc = "Sustained vigilance, active drafting, structured tactical operations."
            max_session_mins = 90.0
        elif "alpha" in state or "flow" in state or "calm" in state or "stress" in state:
            beat_hz = 10.0 # 10 Hz Alpha: Flow state, sensory gating, reduced anxiety
            band_name = "Alpha Oscillations (8 - 12 Hz)"
            function_desc = "Flow state immersion, reduced cognitive friction, relaxed executive control."
            max_session_mins = 120.0
        elif "theta" in state or "creativ" in state or "idea" in state or "incubate" in state:
            beat_hz = 6.0 # 6 Hz Theta: Hypnagogic insight, diffuse thinking, memory reconsolidation
            band_name = "Theta Oscillations (4 - 7 Hz)"
            function_desc = "Diffuse creative problem incubation, architectural synthesis, cross-domain analogy."
            max_session_mins = 45.0
        elif "sleep" in state or "delta" in state or "recover" in state:
            beat_hz = 2.5 # 2.5 Hz Delta: Slow-wave sleep initiation
            band_name = "Delta Oscillations (1 - 3 Hz)"
            function_desc = "Parasympathetic activation, slow-wave physical recovery, pre-sleep sedation."
            max_session_mins = 45.0
        else:
            beat_hz = 10.0
            band_name = "Alpha Oscillations (10 Hz Baseline)"
            function_desc = "Balanced focus and nervous system stability."
            max_session_mins = 90.0

        f_left = round(carrier, 1)
        f_right = round(carrier + beat_hz, 1)

        return {
            "target_cognitive_state": state,
            "entrainment_eeg_band": band_name,
            "beat_difference_frequency_hz": beat_hz,
            "carrier_frequency_hz": carrier,
            "stereo_channel_frequencies": {
                "left_ear_hz": f_left,
                "right_ear_hz": f_right
            },
            "neurophysiological_mechanism": "Superior olivary complex phase-locking driving cortical Frequency Following Response (FFR).",
            "primary_cognitive_benefit": function_desc,
            "max_safe_session_duration_minutes": max_session_mins,
            "playback_requirement": "Mandatory stereo headphones. Binaural beats cannot form through external speakers."
        }

    def schedule_auditory_entrainment_protocol(
        self,
        work_block_duration_minutes: float = 90.0,
        fatigue_level: str = "moderate"
    ) -> Dict[str, Any]:
        """
        Chains a phased 3-stage auditory entrainment sequence (Alpha warm-up, Gamma peak,
        Theta cool-down) tailored to the user's focus block length and fatigue level.
        """
        total_mins = max(25.0, min(180.0, float(work_block_duration_minutes)))
        fatigue = str(fatigue_level).lower()

        # Dynamic phase timing
        warmup_mins = round(min(15.0, max(5.0, total_mins * 0.12)), 0)
        cooldown_mins = round(min(15.0, max(5.0, total_mins * 0.12)), 0)
        core_mins = round(total_mins - warmup_mins - cooldown_mins, 0)

        # In severe fatigue, replace intense 40Hz Gamma with sustained 10Hz Alpha flow
        if "high" in fatigue or "severe" in fatigue or "exhaust" in fatigue:
            core_state = "10 Hz Alpha Flow (Fatigue-Buffered Sustained Focus)"
            core_beat_hz = 10.0
        else:
            core_state = "40 Hz Gamma Hyper-Focus (Peak Working Memory Binding)"
            core_beat_hz = 40.0

        stages = [
            {
                "phase_index": 1,
                "phase_name": "Stage 1: Attentional Gating Warm-Up",
                "duration_minutes": warmup_mins,
                "beat_frequency_hz": 12.0,
                "eeg_target": "Alpha (12 Hz)",
                "purpose": "Filter environmental sensory distraction and transition prefrontal cortex into single-task flow."
            },
            {
                "phase_index": 2,
                "phase_name": "Stage 2: Core Cognitive Execution",
                "duration_minutes": core_mins,
                "beat_frequency_hz": core_beat_hz,
                "eeg_target": core_state,
                "purpose": "Maximize computational working memory throughput, proof verification, and coding speed."
            },
            {
                "phase_index": 3,
                "phase_name": "Stage 3: Defatigue & Memory Reconsolidation",
                "duration_minutes": cooldown_mins,
                "beat_frequency_hz": 7.0,
                "eeg_target": "Theta / Low Alpha (7 Hz)",
                "purpose": "Prevent post-work mental exhaustion; consolidate newly formed episodic memory."
            }
        ]

        return {
            "total_protocol_duration_minutes": total_mins,
            "fatigue_adaptation_mode": "Active" if "high" in fatigue else "Standard",
            "phased_entrainment_sequence": stages,
            "entrainment_audio_instruction": "Play in stereo at low comfortable volume (45-55 dBA) with optional pink noise backing."
        }
