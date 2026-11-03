"""
MCP Server for Acoustic Frequency Following Response (FFR) Skill.
Exposes JSON-RPC Model Context Protocol tools for evaluating FFR amplitude, Phase-Locking Value (PLV), and subcortical precision.
"""

import sys
import json
from typing import Dict, Any
from client import AcousticFrequencyFollowingResponseClient


def get_tools_manifest() -> Dict[str, Any]:
    return {
        "tools": [
            {
                "name": "evaluate_ffr",
                "description": "Calculates Auditory Brainstem Frequency Following Response (FFR) Phase-Locking Value (PLV), SNR (dB), and subcortical temporal precision score.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "stimulus_fundamental_freq_hz": {
                            "type": "number",
                            "description": "Fundamental frequency F0 of stimulus tone or vowel in Hz (e.g. 150.0 Hz)."
                        },
                        "ffr_amplitude_uv": {
                            "type": "number",
                            "description": "Peak FFR response amplitude in microvolts (e.g. 0.38 uV, normative 0.20-0.65 uV)."
                        },
                        "phase_locking_value": {
                            "type": "number",
                            "description": "Phase-Locking Value PLV between 0.0 and 1.0 (e.g. 0.78, normative 0.65-0.90)."
                        },
                        "signal_to_noise_ratio_db": {
                            "type": "number",
                            "description": "Signal-to-noise ratio in decibels (e.g. 8.5 dB, normative > 6.0 dB)."
                        },
                        "stimulus_cross_correlation": {
                            "type": "number",
                            "description": "Cross-correlation Pearson r between stimulus and brainstem response (default: 0.72).",
                            "default": 0.72
                        }
                    },
                    "required": ["stimulus_fundamental_freq_hz", "ffr_amplitude_uv", "phase_locking_value", "signal_to_noise_ratio_db"]
                }
            }
        ]
    }


def handle_request(client: AcousticFrequencyFollowingResponseClient, req: Dict[str, Any]) -> Dict[str, Any]:
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": get_tools_manifest()
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})

        if name == "evaluate_ffr":
            res = client.evaluate_ffr(
                stimulus_fundamental_freq_hz=float(args.get("stimulus_fundamental_freq_hz", 150.0)),
                ffr_amplitude_uv=float(args.get("ffr_amplitude_uv", 0.35)),
                phase_locking_value=float(args.get("phase_locking_value", 0.75)),
                signal_to_noise_ratio_db=float(args.get("signal_to_noise_ratio_db", 8.0)),
                stimulus_cross_correlation=float(args.get("stimulus_cross_correlation", 0.72))
            )
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(res, indent=2)
                        }
                    ]
                }
            }
        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32601,
                    "message": f"Method not found: {name}"
                }
            }
    else:
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {
                "code": -32600,
                "message": f"Invalid Request: Unsupported method {method}"
            }
        }


def main():
    client = AcousticFrequencyFollowingResponseClient()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(client, req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {
                    "code": -32700,
                    "message": f"Parse error or exception: {str(e)}"
                }
            }
            sys.stdout.write(json.dumps(err_resp) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
