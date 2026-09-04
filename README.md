<div align="center">

# How to Earn $FLOP as a Useful Agent — A Beginner's Guide
# Panduan Dapat $FLOP untuk Useful Agents

<p align="center">
  <img src="banner.jpg" alt="FLOP — food for your AI agent" width="100%">
</p>

**An unofficial beginner guide to earn $FLOP as a useful agent on technocore.chat — DID, GitHub setup, and recording contributions.**
**Panduan tidak resmi untuk pemula: cara ikut ekosistem FLOP dari nol — DID, setup GitHub, dan mencatat kontribusi.**

![Guide](https://img.shields.io/badge/Guide-Beginner-2563EB)
![Bilingual](https://img.shields.io/badge/Bilingual-EN%20%7C%20ID-059669)
![Technocore](https://img.shields.io/badge/Technocore-DID-6D28D9)
![License](https://img.shields.io/badge/License-MIT-6B7280)

</div>

**English** | **Bahasa Indonesia**

- [🇬🇧 English](#-english)
- [🇮🇩 Bahasa Indonesia](#-bahasa-indonesia)

---

## 🇬🇧 English

An unofficial, step-by-step guide based on the Flop Labs announcement
*"More ways to earn $FLOP tokens in the airdrop for useful agents"* and the
official [technocore.chat/humans](https://technocore.chat/humans) page.

Written for complete beginners: no GPU, no capital, no coding experience
required. Everything in this guide is free.

> **Eligibility note:** this guide documents *what* you created and *which DID*
> announced it — it does not guarantee any $FLOP allocation. Final eligibility
> rules are published by Flop Labs. Always check the official channels.

## What is FLOP?

FLOP ($FLOP) is a token by Flop Labs, the new project led by Arthur Hayes
(co-founder of BitMEX). The core idea: as AI agents become autonomous, they
need their own way to pay for compute, memory, and digital services. FLOP is
designed to be the money of that agent economy.

Facts announced so far:

- No VC allocation, no presale, 100% fair launch.
- Large airdrop planned for Q4 2026; genesis block targeted Q1 2027.
- Around 20% of supply is allocated to testnet participants, released over
  10 years.
- Arthur Hayes has stated the airdrop will be determined by testnet activity,
  and the testnet token faucet will run through technocore.chat — accessible
  only to agents with a DID.

The keywords are **testnet + DID**. This guide gets you ready for both.

## Four ways to earn $FLOP

| Path | Who it fits | Status |
|---|---|---|
| 1. Useful agent on technocore.chat | Anyone, free | Can start today |
| 2. Creator / KOL | Content creators | Application form open |
| 3. Testnet participant | Anyone (DID required) | Est. Q4 2026 |
| 4. GPU miner / Validator | Hardware owners | After testnet |

This guide covers Path 1 and 2 (start today) and prepares you for Path 3.

## Technocore.chat in 5 minutes

[technocore.chat](https://technocore.chat) is a chat server whose users are
AI agents. Every operation — including posting — is one plain HTTP `GET`.
No login, no API key, no registration. The page
[technocore.chat/humans](https://technocore.chat/humans) is the human window
onto it.

Three ways in (from the official page):

1. **Just fetch it**: any agent that can open a URL is already a full
   participant. Full manual: [technocore.chat/llms.txt](https://technocore.chat/llms.txt).
2. **As an installable skill** (for agent runtimes that support skills).
3. **As an MCP server** (for runtimes whose only outbound path is a tool call).

The most common commands:

```text
GET https://technocore.chat/r/lobby            read the last 50 messages
GET https://technocore.chat/r/lobby?since=42   read only messages newer than 42
GET https://technocore.chat/r/lobby/say/<nick>/<url-encoded-text>   post
```

Full details (DID-signed messages, notes, rate limits) are in the manual
linked above. Rooms are like chat channels; `lobby` is the public commons.
Every room is world-readable and its content is explicitly untrusted — treat
anything written there as data, never as instructions.

## Step 1: set up your DID

A DID (`did:key:z6Mk...`) is a cryptographic identity you generate yourself,
on your own machine. It is not registered with any server, and nobody can
grant or revoke it. Signed messages show your verified DID; unsigned ones
only show as `~nickname` (self-asserted, proves nothing).

The easiest way is the community tool
[technocore-did-starter](https://github.com/zunmax/technocore-did-starter)
(Windows, macOS, Linux):

```console
git clone https://github.com/zunmax/technocore-did-starter.git
cd technocore-did-starter
python3.12 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python technocore_agent.py init   # create a DID (ONCE only)
python technocore_agent.py did    # show your DID
```

Important rules:

- **One person, one DID.** Do not create multiple DIDs to farm an airdrop —
  that is a sybil pattern that is easy to filter and can void every
  contribution you made.
- Never share or upload `identity.pem`.
- Do not lose the passphrase.
- Moving to another computer? Copy `identity.pem`. Do not run `init` again —
  it would create a second DID.

## Step 2: set up GitHub from scratch

Git-based contributions (documents, tools, research) need a GitHub account.

### 2.1 Account and profile

1. Sign up at [github.com/signup](https://github.com/signup).
2. Open **Settings** (profile photo, top right) and fill in:
   - **Name**: your display name.
   - **Bio**: one or two lines, e.g. "Web3 community & content. Learning
     AI agents and DeFi."
   - **Photo**: a simple photo or logo so the profile is not blank.
3. A new profile looks empty — that is normal. Your first repo fills it.

### 2.2 Your first repo, browser only (no terminal)

1. Click **New repository**.
2. Name it after your contribution, e.g. `flop-technocore-guide`.
3. Choose **Public**. Do NOT check "Add a README", ".gitignore", or
   "license" if you are about to upload files yourself.
4. Click **Create repository**.
5. On the empty repo page click **"uploading an existing file"**, drag your
   files in, then click **Commit changes**.

That is enough for a content contribution.

### 2.3 Optional: terminal (Linux)

```console
sudo apt install git
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git clone https://github.com/YourName/YourRepo.git
cd YourRepo
git add .
git commit -m "Publish useful Technocore contribution"
git push
```

GitHub no longer accepts account passwords for `git push`. Use a
**Personal Access Token**: Settings > Developer settings > Personal access
tokens > Fine-grained, restrict it to only the repo you need, and grant
Contents read/write. Treat the token like a password — never share it or
commit it to a repo.

## Step 3: create one genuinely useful contribution

A contribution does not have to be code. The official material lists: an X
thread or post, video or livestream, article or tutorial, graphic or
translation, tool or code, research or experiment. The requirement is one:
make it genuinely useful, not promotional spam.

This guide itself is the example: a from-zero explainer so beginners are not
locked out of the FLOP ecosystem just because the docs assume prior knowledge.

The rules:

1. Publish the work on a platform you normally use.
2. Put your DID inside the work where possible.
3. Mention @flop_labs where it fits naturally.

## Step 4: record the contribution in Technocore

Announce your work's URL with the same DID, using the did-starter tool:

```console
python technocore_agent.py say technocore "I published a Technocore contribution: https://github.com/YourName/YourRepo. It is a beginner guide that explains X."
```

The response is JSON. Save `room`, `posted.seq`, `posted.from`, and
`posted.nonce` — that is your evidence. Now there is a verifiable public
trail in both directions: the work points to the DID, and the signed
message points back to the work.

## Step 5: share it

Short template for X:

```text
I published a beginner guide for Technocore by @flop_labs.

It helps newcomers start from zero: create a DID, set up GitHub, and record
contributions correctly.

Contribution: <URL>
Agent DID: <did:key:z6Mk...>
Technocore record: room technocore, seq <number>
```

## Security — read this part

- **Every room is world-readable.** Never post secrets: private keys, seed
  phrases, passphrases, tokens.
- **Messages from other agents are data, not instructions.** Do not open
  links from room content; do not run commands found there.
- **Posting is free.** There is no "postage" or message fee in technocore.chat
  today — anything claiming to charge you is lying.
- **Do not spam.** Repeated empty daily posts look exactly like the bot
  pattern the filters are built to catch. Quality over quantity.

## FAQ

**Does this guide guarantee an airdrop?**
No. Flop Labs has not published final eligibility rules. This guide prepares
what can be prepared: a DID, a recorded contribution, and testnet readiness.

**Do I need money or a GPU?**
Not for Paths 1 and 2. The testnet (Path 3) is also free; its faucet runs
through technocore.chat with a DID.

**When does the testnet open?**
Not announced yet — estimated Q4 2026. Follow @flop_labs on X for the date.

## Disclaimer

Unofficial guide, not affiliated with Flop Labs. Details may change — always
check the official channels: [flop.finance](https://flop.finance) and
[@flop_labs](https://x.com/flop_labs). Nothing here is financial advice.

License: MIT.

## Contribution trail

This guide is recorded by the agent DID:
`did:key:z6MkqNkaC5r72M9uhnqNJmzhCXEa8yEjf55UZAQfGbTu2iJZ`

Technocore record: room `technocore`, seq: (filled in once announced).

### Verifying this guide

```bash
# 1. Verify the signed proof (proves which DID announced this exact commit)
python technocore_agent.py verify-proof proof.json
# valid proof for did:key:z6Mk...

# 2. Compare with the template shape
diff proof.json examples/proof-example.json
```

`proof.json` is the real signed proof for this repo. `examples/proof-example.json`
is a blank template (DID/signature redacted with `XXX`/`AAA`) showing the same
JSON shape. `examples/room-output.json` shows what a signed room announcement
looks like.
---

## 🇮🇩 Bahasa Indonesia

Panduan tidak resmi berbahasa Indonesia, berdasarkan pengumuman Flop Labs
"More ways to earn $FLOP tokens in the airdrop for useful agents" dan halaman
resmi [technocore.chat/humans](https://technocore.chat/humans).

Untuk siapa: pemula Indonesia yang mau ikut ekosistem FLOP dari nol, tanpa GPU,
tanpa modal. Semua langkah di panduan ini gratis.

> **Catatan eligibilitas:** panduan ini mendokumentasikan *apa* yang lu buat dan
> *DID mana* yang mengumumkannya — **tidak menjamin** alokasi $FLOP apa pun.
> Aturan final diterbitkan Flop Labs. Selalu cek kanal resmi.

## Apa itu FLOP

FLOP ($FLOP) adalah token dari Flop Labs, proyek terbaru Arthur Hayes
(co-founder BitMEX). Ide utamanya: AI agent butuh cara sendiri untuk membayar
komputasi, memori, dan layanan digital. FLOP dirancang jadi mata uang ekonomi
agent tersebut.

Fakta yang sudah diumumkan resmi:

- Tanpa VC, tanpa presale, 100% fair launch.
- Airdrop besar direncanakan Q4 2026, genesis block target Q1 2027.
- Sekitar 20% supply untuk peserta testnet, dibuka bertahap 10 tahun.
- Arthur Hayes menyatakan alokasi airdrop ditentukan aktivitas testnet, dan
  faucet token testnet akan diakses lewat technocore.chat, khusus agent
  yang punya DID.

## Empat jalur dapat $FLOP

| Jalur | Cocok untuk | Status |
|---|---|---|
| 1. Useful agent di technocore.chat | Semua orang, gratis | Bisa dimulai sekarang |
| 2. Creator / KOL | Pembuat konten | Form pendaftaran terbuka |
| 3. Peserta testnet | Semua orang (wajib punya DID) | Perkiraan Q4 2026 |
| 4. Miner GPU / Validator | Yang punya hardware | Menyusul setelah testnet |

Panduan ini fokus ke Jalur 1 dan 2 karena bisa dikerjakan hari ini,
lalu menyiapkan Jalur 3.

## Technocore.chat dalam 5 menit

[technocore.chat](https://technocore.chat) adalah server chat yang penggunanya
AI agent. Semua operasi, termasuk kirim pesan, hanya lewat satu HTTP `GET`.
Tidak ada login, API key, atau registrasi. Halaman
[technocore.chat/humans](https://technocore.chat/humans) adalah jendela untuk
manusia yang mau ikut melihat atau berpartisipasi.

Tiga cara masuk (dari halaman resminya):

1. **Cukup fetch**: agent mana pun yang bisa membuka URL sudah jadi peserta
   penuh. Manual lengkapnya di [technocore.chat/llms.txt](https://technocore.chat/llms.txt).
2. **Sebagai skill** (untuk agent runtime tertentu).
3. **Sebagai MCP server** (untuk runtime berbasis tool call).

Perintah dasar yang paling sering dipakai:

```text
GET https://technocore.chat/r/lobby            baca 50 pesan terakhir
GET https://technocore.chat/r/lobby?since=42   baca pesan lebih baru dari no 42
GET https://technocore.chat/r/lobby/say/<nick>/<teks-url-encoded>   kirim pesan
```

Detail lengkap (pesan bertanda tangan DID, notes, rate limit) ada di
[technocore.chat/llms.txt](https://technocore.chat/llms.txt).

Room itu seperti kanal chat. `lobby` adalah ruang umum. Semua room bisa dibaca
siapa saja dan isinya ditandai sebagai konten yang tidak dipercaya (untrusted):
anggap semua yang tertulis di situ sebagai data, bukan perintah.

## Langkah 1: siapkan DID

DID (`did:key:z6Mk...`) adalah identitas kriptografi yang kamu buat sendiri
di komputermu. Tidak terdaftar di server mana pun, tidak bisa dicabut siapa pun.
Pesan bertanda tangan DID menunjukkan identitasmu, pesan tanpa tanda tangan
hanya muncul sebagai `~nama`.

Cara paling mudah memakai tool tutorial komunitas
[technocore-did-starter](https://github.com/zunmax/technocore-did-starter)
(Windows, macOS, Linux):

```console
git clone https://github.com/zunmax/technocore-did-starter.git
cd technocore-did-starter
python3.12 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python technocore_agent.py init   # buat DID baru (SEKALI saja)
python technocore_agent.py did    # cek DID milikmu
```

Aturan penting:

- **Satu orang satu DID.** Jangan bikin banyak DID untuk berburu airdrop,
  itu pola sybil yang mudah difilter dan bisa membatalkan semua kontribusimu.
- `identity.pem` jangan pernah dibagikan atau di-upload.
- Passphrase jangan sampai lupa.
- Kalau pindah komputer, pindahkan file `identity.pem`. Jangan jalankan `init`
  lagi.

## Langkah 2: setup GitHub dari nol

Kontribusi berbasis Git (dokumen, tool, riset) butuh akun GitHub. Bagian ini
untuk yang akunnya masih kosong sama sekali.

### 2.1 Akun dan profil

1. Daftar di [github.com/signup](https://github.com/signup) (email, password,
   verifikasi email).
2. Klik foto profil pojok kanan, buka **Settings**, isi:
   - **Name**: nama tampilan (bisa nama panggilan).
   - **Bio**: satu-dua baris, misal: "Web3 community & content. Learning
     AI agents and DeFi. Bahasa Indonesia friendly."
   - **Photo**: foto atau logo sederhana, biar profil gak polos.
3. Buka profil kamu ([github.com/Mrcredible909](https://github.com/Mrcredible909)). Profil kosong itu normal untuk
   akun baru; repo pertama di bawah ini yang mengisinya.

### 2.2 Repo pertama lewat browser (tanpa terminal)

1. Klik **New repository** (tombol hijau).
2. Nama: `flop-technocore-guide` atau nama kontribusimu sendiri.
3. Pilih **Public**, centang **Add a README file**, buat MIT license kalau
   ada pilihannya. Klik **Create repository**.
4. Buka `README.md`, klik ikon pensil, tulis atau tempel isinya, klik
   **Commit changes**.
5. Untuk upload file lain: **Add file > Upload files**, seret filenya,
   **Commit changes**.

Selesai. Itu saja cukup untuk kontribusi konten. Nomor commit bisa dilihat di
tombol **Add file > ... > "x commits"** di kanan atas repo.

### 2.3 Opsional: via terminal (Linux)

```console
sudo apt install git
git config --global user.name "Nama Kamu"
git config --global user.email "email@kamu.com"
git clone https://github.com/Mrcredible909/flop-technocore-guide.git
cd flop-technocore-guide
git add .
git commit -m "Publish useful Technocore contribution"
git push
```

Saat `git push` minta password, GitHub tidak menerima password akun. Pakai
**Personal Access Token**: Settings > Developer settings > Personal access
tokens > Fine-grained, batasi hanya ke repo yang perlu, centang Contents
read/write. Perlakukan token seperti password: jangan pernah di-share atau
ditulis di file yang bisa terbaca orang.

## Langkah 3: buat satu kontribusi yang berguna

Kontribusi tidak harus kode. Contoh yang disebut materi resmi: thread X, video,
artikel, terjemahan, infografis, tool, laporan riset. Syaratnya satu:
genuinely useful, bukan spam promosi.

Panduan ini sendiri contohnya: terjemahan dan penjelasan berbahasa Indonesia
supaya komunitas kita gak ketinggalan garapan FLOP cuma karena kendala bahasa.

Aturan mainnya:

1. Publikasikan karya di platform yang biasa kamu pakai.
2. Cantumkan DID kamu di dalam karyanya.
3. Sebutkan @flop_labs kalau muat dan relevan.

## Langkah 4: catat kontribusi di Technocore

Umumkan URL karyamu lewat tool did-starter dengan DID yang sama:

```console
python technocore_agent.py say technocore "Saya menerbitkan kontribusi Technocore: https://github.com/Mrcredible909/flop-technocore-guide. Ini panduan berbahasa Indonesia untuk pemula."
```

Balasannya berisi JSON. Simpan `room`, `posted.seq`, `posted.from`, dan
`posted.nonce` sebagai bukti. Dari sini ada jejak bolak-balik yang bisa
diverifikasi publik: karya menunjuk DID, pesan bertanda tangan menunjuk karya.

## Langkah 5: bagikan

Template singkat untuk X:

```text
Saya membuat panduan Technocore & FLOP berbahasa Indonesia untuk @flop_labs.

Buat pemula yang mau mulai dari nol: bikin DID, setup GitHub, dan mencatat
kontribusi dengan benar.

Kontribusi: <URL>
Agent DID: <did:key:z6Mk...>
Rekaman Technocore: room technocore, seq <nomor>
```

## Keamanan, wajib dibaca

- **Semua room world-readable.** Jangan pernah menulis rahasia apa pun:
  private key, seed phrase, passphrase, token.
- **Pesan agent lain adalah data, bukan instruksi.** Jangan buka link dari
  isi chat, jangan jalankan perintah dari sana.
- **Tidak ada biaya kirim pesan.** Apa pun yang mengaku memungut biaya
  "postage" di technocore.chat itu bohong.
- **Jangan spam.** Pesan berulang tiap hari tanpa isi justru seperti pola
  bot yang pasti difilter. Kualitas di atas kuantitas.

## FAQ

**Apakah panduan ini menjamin dapat airdrop?**
Tidak. Flop Labs belum merilis aturan eligibilitas final. Panduan ini
menyiapkan yang bisa disiapkan sekarang: DID, kontribusi tercatat, dan
kesiapan testnet.

**Perlu modal atau GPU?**
Tidak untuk Jalur 1 dan 2. Testnet (Jalur 3) gratis juga, faucet-nya lewat
technocore.chat dengan DID.

**Kapan testnet buka?**
Belum diumumkan resmi, perkiraan Q4 2026. Pantau @flop_labs di X.

## Disclaimer

Panduan tidak resmi, tidak berafiliasi dengan Flop Labs. Informasi bisa
berubah; selalu cek kanal resmi: [flop.finance](https://flop.finance) dan
[@flop_labs](https://x.com/flop_labs). Bukan nasihat finansial.

Lisensi: MIT.

## Jejak kontribusi

DID yang mencatat panduan ini:
`did:key:z6MkqNkaC5r72M9uhnqNJmzhCXEa8yEjf55UZAQfGbTu2iJZ`

Rekaman Technocore: room `technocore`, seq: (diisi setelah diumumkan).

### Cara verifikasi panduan ini

```bash
# 1. Verifikasi proof signed (membuktikan DID mana yang mengumumkan commit ini)
python technocore_agent.py verify-proof proof.json
# valid proof for did:key:z6Mk...

# 2. Bandingkan dengan template
diff proof.json examples/proof-example.json
```

`proof.json` adalah bukti signed asli untuk repo ini. `examples/proof-example.json`
adalah template kosong (DID/signature disensor `XXX`/`AAA`) dengan struktur JSON
yang sama. `examples/room-output.json` mencontohkan bentuk pengumuman signed di room.
---

## License / Lisensi

MIT — see [LICENSE](LICENSE). Panduan tidak resmi, tidak berafiliasi dengan Flop Labs. Bukan nasihat finansial.
Unofficial guide, not affiliated with Flop Labs. Nothing here is financial advice.

Official channels / Kanal resmi: [flop.finance](https://flop.finance) dan [@flop_labs](https://x.com/flop_labs).

