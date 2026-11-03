"""
Example Usage: Acoustic Frequency Following Response (FFR) & Subcortical Phase-Locking.
Demonstrates zero-dependency calculation of FFR amplitude, Phase-Locking Value (PLV), and auditory temporal precision scoring.
"""

from client import AcousticFrequencyFollowingResponseClient


def main():
    client = AcousticFrequencyFollowingResponseClient()
    print("=== Acoustic Frequency Following Response (FFR) Demo ===")

    # Test Case 1: Healthy high-fidelity auditory brainstem phase-locking (150 Hz voice pitch)
    res1 = client.evaluate_ffr(
        stimulus_fundamental_freq_hz=150.0,
        ffr_amplitude_uv=0.42,
        phase_locking_value=0.79,
        signal_to_noise_ratio_db=9.4,
        stimulus_cross_correlation=0.78
    )
    print("\nTest Case 1: Optimal Subcortical Phase-Locking (150 Hz F0)")
    print(f"  Stimulus F0: {res1['stimulus_fundamental_freq_hz']} Hz | FFR Amplitude: {res1['ffr_amplitude_uv']} uV")
    print(f"  Phase-Locking Value (PLV): {res1['phase_locking_value']} | SNR: {res1['signal_to_noise_ratio_db']} dB")
    print(f"  Cross-Correlation r: {res1['stimulus_cross_correlation']}")
    print(f"  Subcortical Precision Score: {res1['subcortical_precision_score']} / 100")
    print(f"  Classification: {res1['classification']}")
    print(f"  Physiological Interpretation: {res1['physiological_interpretation']}")
    print(f"  Actionable Guidance: {res1['actionable_guidance']}")

    # Test Case 2: Degraded phase-locking (cochlear synaptopathy / noise exposure pattern)
    res2 = client.evaluate_ffr(
        stimulus_fundamental_freq_hz=150.0,
        ffr_amplitude_uv=0.18,
        phase_locking_value=0.46,
        signal_to_noise_ratio_db=3.2,
        stimulus_cross_correlation=0.48
    )
    print("\nTest Case 2: Degraded Temporal Fidelity Pattern (Hidden Hearing Loss)")
    print(f"  Phase-Locking Value: {res2['phase_locking_value']} | SNR: {res2['signal_to_noise_ratio_db']} dB")
    print(f"  Subcortical Precision Score: {res2['subcortical_precision_score']} / 100")
    print(f"  Classification: {res2['classification']}")
    print(f"  Actionable Guidance: {res2['actionable_guidance']}")


if __name__ == "__main__":
    main()
