# Acoustic Frequency Following Response (FFR) Skill

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/zero--dependencies-standard--lib-brightgreen.svg)](requirements.txt)
[![MCP Protocol Ready](https://img.shields.io/badge/mcp-protocol--ready-orange.svg)](mcp_server.py)
[![OpenClaw Certified](https://img.shields.io/badge/openclaw-certified-purple.svg)](SKILL.md)

Zero-dependency sovereign personal agent skill for non-invasive evaluation of Auditory Brainstem Frequency Following Response (FFR) Phase-Locking Value (PLV), SNR, and subcortical temporal envelope encoding fidelity.

```mermaid
flowchart TD
    PeriodicSound["Periodic Speech Vowel / Pitch Stimulus (F0 100-300 Hz)"] --> Cochlea["Cochlear Afferent Synchrony & Auditory Nerve Fibers"]
    Cochlea --> InferiorColliculus["Upper Brainstem Inferior Colliculus Phase-Locking"]
    InferiorColliculus --> FFR_Signal["Continuous Scalp-Recorded FFR Potential (Microvolts)"]
    FFR_Signal --> PhaseCoherence["Phase-Locking Value (PLV) & Signal-to-Noise Ratio (SNR)"]
    PhaseCoherence --> TemporalScore["Subcortical Auditory Fidelity & Speech-in-Noise Score"]
    TemporalScore --> Agent["OpenClaw / Hermes Personal Agent Sound Masking Protection"]
```

## Features
- **Deterministic Math**: Pure Python standard library implementation with zero external dependencies.
- **Auditory Electrophysiology Standards**: Implements validated equations for brainstem FFR amplitude, inter-trial phase-locking value (PLV), and stimulus cross-correlation.
- **Hidden Hearing Loss & Synaptopathy Shield**: Sensitive detection of auditory brainstem temporal jitter prior to pure-tone threshold loss.
- **Model Context Protocol (MCP)**: Native JSON-RPC tool integration for LLMs and autonomous agents.

## Quickstart

```python
from client import AcousticFrequencyFollowingResponseClient

client = AcousticFrequencyFollowingResponseClient()
result = client.evaluate_ffr(
    stimulus_fundamental_freq_hz=150.0,
    ffr_amplitude_uv=0.42,
    phase_locking_value=0.79,
    signal_to_noise_ratio_db=9.4
)
print("Phase-Locking Value:", result["phase_locking_value"])
print("Precision Score:", result["subcortical_precision_score"])
print("Classification:", result["classification"])
```

## License
Apache-2.0
