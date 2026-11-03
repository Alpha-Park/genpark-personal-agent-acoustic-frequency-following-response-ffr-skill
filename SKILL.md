---
name: genpark-personal-agent-acoustic-frequency-following-response-ffr-skill
version: 1.0.0
description: Zero-dependency sovereign personal agent skill for calculating Auditory Brainstem Frequency Following Response (FFR) Phase-Locking Value (PLV), SNR, and subcortical temporal envelope encoding fidelity.
author: AlphaPark Inc.
license: Apache-2.0
tags:
  - personal-agent
  - ai-agent
  - openclaw
  - genpark
  - mcp
  - mcp-server
  - model-context-protocol
  - python
  - zero-dependency
  - wellness
  - productivity
  - production-ready
metadata:
  openclaw_compatible: true
  hermes_compatible: true
  zero_dependency: true
---

# Acoustic Frequency Following Response (FFR) Skill

A sovereign personal agent capability for evaluating auditory brainstem electrophysiology, inferior colliculus phase-locked periodicity, Phase-Locking Value ($PLV$), fundamental frequency ($F_0$) pitch tracking, and speech perception in noisy open-plan work environments.

## Core Capabilities
- **Subcortical Phase-Locking Value (PLV)**: Quantifies neural phase coherence ($PLV$, normative: $0.65 - 0.90$) across repeated acoustic fundamental periods.
- **FFR Amplitude & SNR Formulation**: Measures microvolt-level evoked potential peak amplitude ($0.20 - 0.65\text{ }\mu\text{V}$) and signal-to-noise ratio ($> 6.0\text{ dB}$).
- **Cochlear Synaptopathy & Hidden Hearing Loss Screening**: Identifies subclinical temporal encoding jitter despite normal pure-tone audiograms.
- **Acoustic Workstation Hygiene**: Prescribes active noise cancellation profiles and quiet recharge breaks to prevent listening exhaustion.

## Fast Invocation
```python
from client import AcousticFrequencyFollowingResponseClient

client = AcousticFrequencyFollowingResponseClient()
res = client.evaluate_ffr(
    stimulus_fundamental_freq_hz=150.0,
    ffr_amplitude_uv=0.42,
    phase_locking_value=0.79,
    signal_to_noise_ratio_db=9.4
)
print("Phase-Locking Value:", res["phase_locking_value"])
print("Precision Score:", res["subcortical_precision_score"], "/ 100")
```
