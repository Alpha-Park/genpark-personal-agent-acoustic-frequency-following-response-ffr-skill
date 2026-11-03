"""
Acoustic Frequency Following Response (FFR) & Subcortical Phase-Locking Engine.
Provides deterministic, zero-dependency modeling of auditory brainstem FFR amplitude (uV),
Phase-Locking Value (PLV), Signal-to-Noise Ratio (SNR dB), and subcortical temporal envelope encoding fidelity.
"""

from typing import Dict, Any, List, Optional


class AcousticFrequencyFollowingResponseClient:
    """
    Deterministic client for calculating Auditory Frequency Following Response (FFR).
    Assesses inferior colliculus phase-locked neural firing, fundamental frequency (F0) tracking,
    cochlear synaptopathy / hidden hearing loss, and speech perception in complex acoustic scenes.
    """

    def __init__(self):
        pass

    def evaluate_ffr(
        self,
        stimulus_fundamental_freq_hz: float,
        ffr_amplitude_uv: float,
        phase_locking_value: float,
        signal_to_noise_ratio_db: float,
        stimulus_cross_correlation: float = 0.72
    ) -> Dict[str, Any]:
        """
        Calculates FFR temporal fidelity and subcortical auditory precision score.
        Normative values (for 100 - 300 Hz fundamental frequency F0):
        - FFR Amplitude: 0.20 - 0.65 uV
        - Phase-Locking Value (PLV): 0.65 - 0.90
        - Signal-to-Noise Ratio (SNR): > 6.0 dB
        - Cross-correlation r: 0.60 - 0.88
        """
        if stimulus_fundamental_freq_hz <= 0 or ffr_amplitude_uv < 0:
            return {"error": "Frequency must be strictly positive and amplitude non-negative"}
        if phase_locking_value < 0 or phase_locking_value > 1.0:
            return {"error": "Phase-Locking Value must be between 0.0 and 1.0"}
        if stimulus_cross_correlation < -1.0 or stimulus_cross_correlation > 1.0:
            return {"error": "Correlation coefficient must be between -1.0 and 1.0"}

        # Subcortical Auditory Temporal Precision Score (0 - 100)
        score = 80.0
        if 0.72 <= phase_locking_value <= 0.95:
            score += 12.0
        elif 0.62 <= phase_locking_value < 0.72:
            score += 5.0
        elif phase_locking_value < 0.45:
            score -= 28.0  # Loss of phase coherence
        elif phase_locking_value < 0.58:
            score -= 15.0

        if signal_to_noise_ratio_db >= 8.0:
            score += 8.0
        elif signal_to_noise_ratio_db >= 5.5:
            score += 3.0
        elif signal_to_noise_ratio_db < 2.0:
            score -= 22.0
        elif signal_to_noise_ratio_db < 4.0:
            score -= 10.0

        if stimulus_cross_correlation >= 0.70:
            score += 5.0
        elif stimulus_cross_correlation < 0.45:
            score -= 15.0

        if 0.22 <= ffr_amplitude_uv <= 0.70:
            score += 5.0
        elif ffr_amplitude_uv < 0.12:
            score -= 15.0

        ffr_score = round(min(100.0, max(5.0, score)), 1)

        if ffr_score >= 85.0 and phase_locking_value >= 0.68 and signal_to_noise_ratio_db >= 6.0:
            tier = "OPTIMAL_SUBCORTICAL_PHASE_LOCKING_PRECISION"
            interp = f"Exceptional auditory brainstem phase-locking (PLV {phase_locking_value}, SNR {signal_to_noise_ratio_db} dB, Amp {ffr_amplitude_uv} uV, r {stimulus_cross_correlation}); pristine temporal envelope representation."
            guidance = "Superior subcortical pitch tracking and speech-in-noise resolution. Robust resistance to acoustic background masking."
        elif phase_locking_value < 0.50 or signal_to_noise_ratio_db < 3.5:
            tier = "DEGRADED_SUBCORTICAL_TEMPORAL_FIDELITY"
            interp = f"Attenuated phase-locking coherence (PLV {phase_locking_value} < 0.60, SNR {signal_to_noise_ratio_db} dB); indicates cochlear synaptopathy or subcortical auditory transmission fatigue."
            guidance = "Subcortical temporal jitter detected. Susceptible to speech understanding fatigue in reverberant open spaces; use high-fidelity acoustic insulation."
        else:
            tier = "MODERATE_AUDITORY_BRAINSTEM_ENCODING"
            interp = f"Moderate FFR fidelity (PLV {phase_locking_value}, SNR {signal_to_noise_ratio_db} dB, Amp {ffr_amplitude_uv} uV); adequate neural representation."
            guidance = "Satisfactory brainstem encoding. Limit continuous headphone usage to protect synaptopathic hair cell junctions."

        return {
            "stimulus_fundamental_freq_hz": stimulus_fundamental_freq_hz,
            "ffr_amplitude_uv": ffr_amplitude_uv,
            "phase_locking_value": phase_locking_value,
            "signal_to_noise_ratio_db": signal_to_noise_ratio_db,
            "stimulus_cross_correlation": stimulus_cross_correlation,
            "subcortical_precision_score": ffr_score,
            "classification": tier,
            "physiological_interpretation": interp,
            "actionable_guidance": guidance
        }
