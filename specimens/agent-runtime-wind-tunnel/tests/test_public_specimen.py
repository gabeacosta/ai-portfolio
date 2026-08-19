from __future__ import annotations
import json, tempfile, unittest
from pathlib import Path
from wind_tunnel.core import EVIDENCE_FILES, gate, run_cell, tamper_copy, verify_bundle, verify_receipts
ROOT = Path(__file__).resolve().parents[1]

class PublicSpecimenTests(unittest.TestCase):
    def run_case(self, arm="native", scenario="baseline"):
        td=tempfile.TemporaryDirectory(); out=Path(td.name)/"run"; result=run_cell(ROOT,arm,scenario,out); return td,out,result
    def test_six_cell_matrix(self):
        expected={"baseline":"VERIFIED","context_reset":"VERIFIED","contradiction":"MISMATCH"}
        for arm in ("native","governed"):
            for scenario,verdict in expected.items():
                with self.subTest(arm=arm,scenario=scenario):
                    td,_,r=self.run_case(arm,scenario); self.addCleanup(td.cleanup); self.assertEqual(verdict,r["verdict"]["verdict"])
    def test_context_reset_recovers_from_durable(self):
        td,out,r=self.run_case("native","context_reset"); self.addCleanup(td.cleanup)
        fault=json.loads((out/"faults.jsonl").read_text()); self.assertIsNone(fault["transient_after"]); self.assertTrue(r["scorecard"]["recovered_from_durable"])
    def test_baseline_does_not_claim_recovery(self):
        td,_,r=self.run_case(); self.addCleanup(td.cleanup); self.assertFalse(r["scorecard"]["recovered_from_durable"])
    def test_contradiction_preserves_objective_continuity(self):
        td,_,r=self.run_case("governed","contradiction"); self.addCleanup(td.cleanup)
        self.assertTrue(r["verdict"]["checks"]["objective_continuity"]); self.assertEqual("DECLARED_EVIDENCE_CONTRADICTION",r["verdict"]["reason"])
    def test_native_and_governed_events_match(self):
        a,ao,_=self.run_case("native","context_reset"); b,bo,_=self.run_case("governed","context_reset"); self.addCleanup(a.cleanup); self.addCleanup(b.cleanup)
        self.assertEqual((ao/"normalized_events.jsonl").read_text(),(bo/"normalized_events.jsonl").read_text())
    def test_native_has_no_receipts(self):
        td,out,_=self.run_case(); self.addCleanup(td.cleanup); self.assertEqual("",(out/"receipts.jsonl").read_text())
    def test_governed_has_linked_receipts(self):
        td,out,_=self.run_case("governed"); self.addCleanup(td.cleanup); receipts=[json.loads(x) for x in (out/"receipts.jsonl").read_text().splitlines()]; self.assertTrue(verify_receipts(receipts))
    def test_gate_denies_unknown_capability(self): self.assertFalse(gate("delete:everything")["allowed"])
    def test_exact_eight_file_bundle(self):
        td,out,_=self.run_case(); self.addCleanup(td.cleanup); self.assertEqual(sorted(EVIDENCE_FILES),sorted(p.name for p in out.iterdir()))
    def test_existing_output_fails_closed(self):
        with tempfile.TemporaryDirectory() as td:
            out=Path(td)/"run"; out.mkdir()
            with self.assertRaises(FileExistsError): run_cell(ROOT,"native","baseline",out)
    def test_one_provider_call_and_effect(self):
        td,_,r=self.run_case("governed"); self.addCleanup(td.cleanup); self.assertEqual(1,r["scorecard"]["provider_calls"]); self.assertEqual(1,r["scorecard"]["emitted_effects"])
    def test_pristine_replay_verifies_without_effects(self):
        td,out,_=self.run_case("governed"); self.addCleanup(td.cleanup); r=verify_bundle(out); self.assertTrue(r["verified"]); self.assertFalse(r["side_effects_enabled"]); self.assertEqual(0,r["provider_calls"])
    def test_tamper_fails_replay(self):
        td,out,_=self.run_case("governed"); self.addCleanup(td.cleanup); tampered=Path(td.name)/"tampered"; tamper_copy(out,tampered); r=verify_bundle(tampered); self.assertFalse(r["verified"]); self.assertIn("normalized_events.jsonl",r["mismatches"])
    def test_receipt_chain_tamper_fails_replay(self):
        td,out,_=self.run_case("governed"); self.addCleanup(td.cleanup); lines=(out/"receipts.jsonl").read_text().splitlines(); r=json.loads(lines[1]); r["previous_hash"]="BAD"; lines[1]=json.dumps(r,sort_keys=True,separators=(',',':')); (out/"receipts.jsonl").write_text('\n'.join(lines)+'\n'); self.assertFalse(verify_bundle(out)["verified"])

if __name__ == "__main__": unittest.main()
