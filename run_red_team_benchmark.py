"""
PromptShield-AI: Red-Team Benchmark Runner Shortcut
Executes the comparative evaluation against all 30 test cases and outputs to benchmark_results.json.
Bennett University - Milestone 2
"""

import os
import sys
import json

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from pipeline import PromptShieldPipeline

if __name__ == "__main__":
    benchmark_path = os.path.join("experiments", "benchmark_test_cases.json")
    pipeline = PromptShieldPipeline(benchmark_file=benchmark_path)
    print("=" * 60)
    print(" PromptShield-AI: Automated Red-Team Benchmark Execution")
    print("=" * 60)
    
    # Run full comparative audit
    results = pipeline.run_full_comparative_audit(
        "prompts/v1_baseline/customer_support.txt",
        "prompts/v4_adaptive_shield/customer_support_v4.txt"
    )
    
    # Also write to root benchmark_results.json as referenced in submission package
    out_file = "benchmark_results.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
        
    print(f"\n[SUCCESS] Benchmark completed across {len(pipeline.test_cases)} scenarios!")
    print(f"[METRICS] Baseline ASR: {results['metrics']['baseline_asr']}% -> Hardened ASR: {results['metrics']['hardened_asr']}%")
    print(f"[OUTPUT] Telemetry saved to '{out_file}' and 'experiments/baseline_vs_hardened_results.json'.")
