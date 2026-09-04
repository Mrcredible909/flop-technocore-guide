#!/usr/bin/env python3
"""Verifikasi panduan flop-technocore-guide — by Mrcredible909.

Adaptasi bebas (MIT) dari pola proof Technocore community tooling:
cek struktur proof.json lokal, verifikasi signature Ed25519-nya,
dan bandingkan dengan template di examples/.

Beda dari contoh upstream:
- CLI bernama `flop-verify` (bukan verify-proof generik)
- Pesan error Bahasa Indonesia + Inggris
- Ngecek konsistensi artifact_url repo ini secara eksplisit
- Mode `--strict`: commit di proof.json harus == HEAD git lokal

Pakai:
    pip install -r requirements.txt
    python verify_guide.py                  # cek proof.json
    python verify_guide.py --strict         # + cocokkan commit == HEAD
    python verify_guide.py --proof path/ke/proof.json
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
EXPECTED_ARTIFACT = "https://github.com/Mrcredible909/flop-technocore-guide"
# NOTE: dua schema berbeda by design (lihat contribution_payload vs
# create_contribution_proof di technocore_agent.py):
# - FILE_SCHEMA: yg tertulis di proof.json
# - PAYLOAD_SCHEMA: yg ikut di-sign dalam canonical payload
FILE_SCHEMA = "technocore-contribution-proof-v1"
PAYLOAD_SCHEMA = "technocore-contribution-v1"

# Batas kewajaran biar error-nya kebaca manusia, bukan traceback mentah.
ARTIFACT_MAXLEN = 200
COMMIT_MAXLEN = 64
SIGNATURE_MAXLEN = 200


def fail(msg_id: str, msg_en: str) -> int:
    print(f"GAGAL: {msg_id}\nFAILED: {msg_en}", file=sys.stderr)
    return 1


def load_json(path: Path) -> dict | None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"GAGAL: file tidak ada: {path}\nFAILED: file not found: {path}",
              file=sys.stderr)
        return None
    except json.JSONDecodeError as exc:
        print(f"GAGAL: bukan JSON valid ({exc})\nFAILED: invalid JSON ({exc})",
              file=sys.stderr)
        return None
    if not isinstance(data, dict):
        print("GAGAL: isi JSON harus object {...}\nFAILED: JSON must be an object",
              file=sys.stderr)
        return None
    return data


def check_shape(proof: dict) -> int:
    if proof.get("schema") != FILE_SCHEMA:
        return fail(f"schema harus {FILE_SCHEMA!r}",
                    f"schema must be {FILE_SCHEMA!r}")
    for field in ("did", "artifact_url", "commit", "signature"):
        val = proof.get(field)
        if not isinstance(val, str) or not val:
            return fail(f"field {field!r} hilang/kosong",
                        f"field {field!r} missing/empty")
    if len(proof["artifact_url"]) > ARTIFACT_MAXLEN:
        return fail("artifact_url kepanjangan (>200 char), curiga",
                    "artifact_url too long (>200 chars), suspicious")
    if len(proof["commit"]) > COMMIT_MAXLEN:
        return fail("commit kepanjangan (>64 char), curiga",
                    "commit too long (>64 chars), suspicious")
    if len(proof["signature"]) > SIGNATURE_MAXLEN:
        return fail("signature kepanjangan (>200 char), curiga",
                    "signature too long (>200 chars), suspicious")
    if proof["artifact_url"] != EXPECTED_ARTIFACT:
        return fail(f"artifact_url harus {EXPECTED_ARTIFACT}",
                    f"artifact_url must be {EXPECTED_ARTIFACT}")
    if not proof["did"].startswith("did:key:z6Mk"):
        return fail("did harus diawali did:key:z6Mk (Ed25519)",
                    "did must start with did:key:z6Mk (Ed25519)")
    return 0


def verify_signature(proof_path: Path) -> int:
    """Verifikasi signature via cryptography langsung (tanpa tool eksternal)."""
    try:
        from cryptography.exceptions import InvalidSignature
    except ImportError:
        return fail("pip install -r requirements.txt dulu (cryptography belum ada)",
                    "run pip install -r requirements.txt first (missing cryptography)")
    proof = load_json(proof_path)
    if proof is None:
        return 1
    if (rc := check_shape(proof)) != 0:
        return rc
    try:
        import base64

        from cryptography.hazmat.primitives.asymmetric.ed25519 import (
            Ed25519PublicKey,
        )

        # did:key:z6Mk... = multibase-base58btc dari 0xed01 + 32-byte pubkey.
        # Decode base58btc dgn leading-zero handling yg benar (lihat
        # base58btc_decode di technocore_agent.py: hitung digit dulu,
        # byte-length dari bit_length, lalu prepend b"\x00" per leading "1").
        alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
        raw = proof["did"].removeprefix("did:key:z")
        num = 0
        for ch in raw:
            try:
                num = num * 58 + alphabet.index(ch)
            except ValueError:
                return fail(f"karakter base58 invalid: {ch!r}",
                            f"invalid base58 character: {ch!r}")
        decoded = num.to_bytes((num.bit_length() + 7) // 8, "big") if num else b""
        zeroes = len(raw) - len(raw.lstrip("1"))
        keybytes = b"\x00" * zeroes + decoded
        if len(keybytes) != 34 or keybytes[:2] != b"\xed\x01":
            return fail("DID bukan kunci ed25519-pub yg valid",
                        "DID is not a valid ed25519-pub key")
        pubkey = Ed25519PublicKey.from_public_bytes(keybytes[2:])

        record = {
            "artifact_url": proof["artifact_url"],
            "commit": proof["commit"].lower(),
            "schema": PAYLOAD_SCHEMA,
        }
        canonical = json.dumps(record, ensure_ascii=False,
                              sort_keys=True, separators=(",", ":"))
        sig = base64.urlsafe_b64decode(proof["signature"] + "==")
        pubkey.verify(sig, canonical.encode())
    except InvalidSignature:
        return fail("signature TIDAK valid untuk DID+commit ini",
                    "signature NOT valid for this DID+commit")
    except Exception as exc:  # noqa: BLE001 — pesan ramah, bukan traceback
        return fail(f"verifikasi error: {exc}", f"verification error: {exc}")
    print(f"OK: valid proof for {proof['did']} @ {proof['commit'][:7]}")
    return 0


def check_examples() -> int:
    """Pastikan template examples/ masih valid JSON + bentuknya sama."""
    for name in ("examples/proof-example.json", "examples/room-output.json",
                 "examples/tclk-offer-example.json"):
        p = HERE / name
        data = load_json(p)
        if data is None:
            return 1
    print("OK: examples/ valid (proof-example.json + room-output.json + tclk-offer-example.json)")
    return 0


def check_strict(proof_path: Path) -> int:
    """Mode --strict: commit di proof.json harus == HEAD git lokal."""
    proof = load_json(proof_path)
    if proof is None:
        return 1
    try:
        head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=HERE,
                              capture_output=True, text=True,
                              check=True).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return fail("git HEAD tidak kebaca (bukan repo git?)",
                    "cannot read git HEAD (not a git repo?)")
    if proof.get("commit", "").lower() != head.lower():
        return fail(
            f"commit proof ({proof.get('commit')}) != HEAD lokal ({head}). "
            "Bikin proof baru untuk commit terbaru.",
            f"proof commit ({proof.get('commit')}) != local HEAD ({head}). "
            "Create a new proof for the latest commit.")
    print(f"OK: commit proof == HEAD ({head[:7]})")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="flop-verify",
                                 description="Verifikasi proof.json panduan FLOP (by Mrcredible909).")
    ap.add_argument("--proof", default="proof.json", help="path proof.json (default: proof.json)")
    ap.add_argument("--strict", action="store_true",
                    help="wajibkan commit proof == HEAD git lokal")
    ap.add_argument("--skip-examples", action="store_true",
                    help="lewati cek examples/")
    args = ap.parse_args(argv)

    proof_path = (HERE / args.proof
                  if not Path(args.proof).is_absolute() else Path(args.proof))
    if (rc := verify_signature(proof_path)) != 0:
        return rc
    if not args.skip_examples and (rc := check_examples()) != 0:
        return rc
    if args.strict and (rc := check_strict(proof_path)) != 0:
        return rc
    print("Semua cek lolos. / All checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
