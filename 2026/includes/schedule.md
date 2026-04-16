# Program

| Time | Speaker(s) | Talk |
|------|------------|------|
| 09:00 |  | [Opening](#opening) |
| 09:10 | [Natalie Kilber](#natalie-kilber) | [Secrets don’t age well: Cyber, Kyber, Quantum and the encryption time bombs](#secrets-dont-age-well-cyber-kyber-quantum-and-the-encryption-time-bombs) |
| 09:55 | [Leon Rickert](#leon-rickert) | [Harvest Now, Decrypt Later: Bringing Post-Quantum Cryptography to SSH](#harvest-now-decrypt-later-bringing-post-quantum-cryptography-to-ssh) |
| 10:25 |  | [Morning break](#morning-break) |
| 10:50 | [Michael Reimsbach](#michael-reimsbach), [Rishi (@rxerium)](#rishi-rxerium) | [Ghost in the Hiring Machine: Catch Fake Personas Before They’re Hired](#ghost-in-the-hiring-machine-catch-fake-personas-before-theyre-hired) |
| 11:20 | [Robin Kirchner](#robin-kirchner) | ['We Have Always Been at War With Eastasia': Attacks Against Web Archives](#we-have-always-been-at-war-with-eastasia-attacks-against-web-archives) |
| 11:50 | [René Lößner](#rené-lößner) | [When Trust Breaks Under Pressure](#when-trust-breaks-under-pressure) |
| 12:20 | [dead1nfluence](#dead1nfluence) | [Let Him Cook! Hacking the Meatmeet BBQ Probe](#let-him-cook-hacking-the-meatmeet-bbq-probe) |
| 12:50 |  | [Lunch](#lunch) |
| 13:50 | [Michael Helwig](#michael-helwig) | [The Map of Artificial Treasures: What to Automate in Security - and Why?](#the-map-of-artificial-treasures-what-to-automate-in-security---and-why) |
| 14:20 | [Blessen Thomas](#blessen-thomas), [Wojciech Poparda](#wojciech-poparda) | [Safe Power Grid Pentest, Practitioner's Guide to Security Without Operational Downtime](#safe-power-grid-pentest-practitioners-guide-to-security-without-operational-downtime) |
| 14:50 | [Nithin Ravi](#nithin-ravi) | [I Let My Pi5 Hack: Building a 0$ AI Pentesting Agent](#i-let-my-pi5-hack-building-a-0-ai-pentesting-agent) |
| 15:20 |  | [Afternoon break](#afternoon-break) |
| 15:45 | [Juliane Reimann](#juliane-reimann) | [The Illusion of Finishability](#the-illusion-of-finishability) |
| 16:15 | [André Lima](#andré-lima) | [Pull the Plug: Kernel-Level Surgery to Blind EDRs](#pull-the-plug-kernel-level-surgery-to-blind-edrs) |
| 16:45 | [Lisa Froehlich](#lisa-froehlich) | [Your Traffic Is Lying to You](#your-traffic-is-lying-to-you) |
| 17:45 |  | [Closing](#closing) |

## Speakers

[André Lima](#andré-lima), [Blessen Thomas](#blessen-thomas), [Juliane Reimann](#juliane-reimann), [Kaan Tolunay Kilic](#kaan-tolunay-kilic), [Leon Rickert](#leon-rickert), [Lisa Froehlich](#lisa-froehlich), [Michael Helwig](#michael-helwig), [Michael Reimsbach](#michael-reimsbach), [Michel Messerschmidt](#michel-messerschmidt), [Natalie Kilber](#natalie-kilber), [Nithin Ravi](#nithin-ravi), [René Lößner](#rené-lößner), [Rishi (@rxerium)](#rishi-rxerium), [Robin Kirchner](#robin-kirchner), [Wojciech Poparda](#wojciech-poparda), [dead1nfluence](#dead1nfluence)

## Talks

## Opening
- **Time:** 09:00 - 09:10

**Abstract:**
Conference opening
<div style="clear: both;"></div>

---

## Secrets don’t age well: Cyber, Kyber, Quantum and the encryption time bombs
- **Time:** 09:10 - 09:55
- **Speakers:**
  - [Natalie Kilber](#natalie-kilber)

**Abstract:**
Quantum is no longer a research topic for us; it is now a benchmark regulators and courts can compare us against. As NIST finalizes quantum‑safe standards and regulators begin referencing them in guidance and sectoral rules, security leaders are expected to manage the emerging cryptographic threats. This talk explains what the quantum threat really is (and is not), why it matters now for long‑lived sensitive data and critical infrastructure, and how it intersects with existing obligations under risk, compliance, and sectoral regulation. We will outline a practical PQC roadmap built around three steps: creating a cryptographic inventory and mapping it to data lifetimes, designing for crypto‑agility in architectures and vendor requirements, and planning targeted PQC pilots in high‑value systems. The goal is to reframe PQC as a no‑regrets crypto‑governance program that reduces future regulatory, operational, and reputational risk—without succumbing to quantum hype. As this is a roadmap problem, not a fire-drill, it also puts AI, LLMS and how it interacts with keys, tokens and signatures, into our perspective.
### Speakers

#### Natalie Kilber

![Natalie Kilber](/assets/2026/avatars/V7Z3QU_BIhoVXh.webp){:width="30%" style="padding: 10px; float: right;"}
Natalie Kilber is a quantum industry pioneer, former enterprise cybersecurity leader and CEO of Haste, securing the future of compute. As a researcher and technology advisor on quantum, AI and cybersecurity; she leads innovations fusing emergent technology defenses for hybrid compute ecosystems.

**Social Media:**
- ![LinkedIn](/assets/icons/linkedin-icon.svg){:width="18px" :height="18px" style="vertical-align: middle;"}: https://www.linkedin.com/company/hastesec/
- ![Website](/assets/icons/www-icon.svg){:width="18px" :height="18px" style="vertical-align: middle;"}: https://hastesecurity.com/

<div style="clear: both;"></div>

---

## Harvest Now, Decrypt Later: Bringing Post-Quantum Cryptography to SSH
- **Time:** 09:55 - 10:25
- **Speakers:**
  - [Leon Rickert](#leon-rickert)

**Abstract:**
Cryptographically relevant quantum computers may not be here yet — but with hardware milestones accelerating and adversaries already collecting encrypted traffic today, waiting to decrypt it later, the window for a safe migration is closing. This "harvest now, decrypt later" (HNDL) strategy makes acting now a security necessity, not a future concern.

NIST finalized ML-KEM (Kyber) and ML-DSA (Dilithium) as FIPS 203 and FIPS 204 in August 2024. OpenSSH 9.9 shipped ML-KEM hybrid key exchange shortly after. The algorithm standards are settled — but most SSH infrastructure hasn't moved yet, and the path from "supported" to "actually deployed everywhere" is longer than it looks.

This talk examines the practical state of PQC in SSH in 2026: how Shor's algorithm threatens today's SSH handshakes, what hybrid key exchange (X25519 + ML-KEM) actually looks like under the hood, and why SSH's modular architecture makes it well-suited for migration — yet adoption still lags. We'll also cover the attack surface that opens up during the transition itself: downgrade attacks on algorithm negotiation, side-channel risks in hybrid implementations, and where SSH and TLS differ fundamentally in their threat profiles and migration challenges.

You'll leave with a clear technical picture of where things stand today, which risks deserve attention first, and concrete steps to start hardening your infrastructure now.
### Speakers

#### Leon Rickert

![Leon Rickert](/assets/2026/avatars/KP7ZBG_9WV2ON7.webp){:width="30%" style="padding: 10px; float: right;"}
Leon Rickert is a Security Consultant at NVISO, where he specializes in vulnerability management and the development of security tooling. His current focus lies at the intersection of cryptographic protocol security and the practical challenge of migrating production infrastructure to post-quantum cryptography.

<div style="clear: both;"></div>

---

## Morning break
- **Time:** 10:25 - 10:50
<div style="clear: both;"></div>

---

## Ghost in the Hiring Machine: Catch Fake Personas Before They’re Hired
- **Time:** 10:50 - 11:20
- **Speakers:**
  - [Michael Reimsbach](#michael-reimsbach)
  - [Rishi (@rxerium)](#rishi-rxerium)

**Abstract:**
People are getting hired and trusted every day. Some of them do not exist at all, yet they still pass interviews, collect paychecks, and gain access to sensitive systems. Campaigns attributed to the DPRK have shown that this threat is very real. So how do you catch a ghost with a resume?
Attendees will learn practical OSINT techniques for spotting fake personas and receive a checklist for thorough background checks. They will see these methods applied through two cases based on a true story, illustrating how these personas succeeded, how one could have been prevented, and where OSINT reaches its limits.
These techniques not only help attendees detect fake personas but also provide practical ways to protect their own privacy and control what personal information is visible online.
### Speakers

#### Michael Reimsbach

![Michael Reimsbach](/assets/2026/avatars/VXJCB9_70NdTuv.webp){:width="30%" style="padding: 10px; float: right;"}
Michael is a Product Security Specialist at SAP, working with the SAP Cloud Infrastructure security team. His focus areas include vulnerability management, secrets management, and building secure internal services.
He obtained multiple industry certifications such as OSCP, GCPN, and CISSP. A healthy dose of paranoia led him to explore OSINT and the surprising power of publicly available information. Beyond his day-to-day work, Michael is an active member of the cybersecurity community and helps organize BSides Luxembourg.

**Social Media:**
- ![LinkedIn](/assets/icons/linkedin-icon.svg){:width="18px" :height="18px" style="vertical-align: middle;"}: https://linkedin.com/in/mreimsbach

#### Rishi (@rxerium)

![Rishi (@rxerium)](/assets/2026/avatars/BUFJAD_qqqayWL.webp){:width="30%" style="padding: 10px; float: right;"}
Rishi is a London-based security researcher with experience in vulnerability research, threat intelligence, and enterprise risk analysis. His work focuses on identifying zero-day vulnerabilities and emerging CVEs, with a particular interest in building detection logic before threats are publicly weaponised.
He works across both offensive and defensive disciplines, developing threat models grounded in real-world TTPs, writing detection rules, and automating reconnaissance to uncover exposed assets at scale. Attack surface management and OSINT are areas he keeps coming back to, specifically the challenge of mapping exposure that organisations often don't know exists.

Outside of his day job, Rishi contributes to open source security tooling through Project Discovery and OWASP, part of the leadership team of the UK OSINT Community, and occasionally speaks at community events including DEF CON and BSides.

<div style="clear: both;"></div>

---

## 'We Have Always Been at War With Eastasia': Attacks Against Web Archives
- **Time:** 11:20 - 11:50
- **Speakers:**
  - [Robin Kirchner](#robin-kirchner)

**Abstract:**
The Wayback Machine has just celebrated its 1 trillionth archived web page. Web archives have grown beyond their original purpose of simply preserving web content. They are now used by Supreme Court judges to preserve online evidence, by Wikipedia editors to maintain reliable sources, and by security researchers to study the evolution of JavaScript and tracking technologies. But can web archives live up to our expectations? 

In this talk, we challenge the assumption of *truthful preservation* by introducing five attacks within two new adversary models against web archives. We present the *evasive publisher* who can hide from web archives and selectively deceive them. But it gets worse... the *anachronistic publisher* can retroactively manipulate snapshots of their websites long after they have been archived. This talk will change the way you look at web archives, as we show that all eight of the popular web archives we studied were vulnerable to multiple of our attacks.
### Speakers

#### Robin Kirchner
Robin is a senior Phd student at TU Braunschweig with an interest in secure systems and large-scale web scanning. His research focuses on the security and integrity of complex web-based systems, including the discovery of hard-to-find flaws and vulnerabilities in web archives, and on defending web systems against attacks.

<div style="clear: both;"></div>

---

## When Trust Breaks Under Pressure
- **Time:** 11:50 - 12:20
- **Speakers:**
  - [René Lößner](#rené-lößner)

**Abstract:**
**Incident response depends on trust:** trust in sources, trust in evidence, and trust in what is real, current, and relevant. But during incidents and crises, teams increasingly face manipulated, recycled, or misleading content that creates pressure, confusion, and bad decisions.

This talk uses a guided mini-tabletop exercise to show how defenders can handle that problem in practice. Using a compact incident scenario, I will apply **FATE** - Focus, Authority, Tribal, Emotion - to explain why certain claims and media are persuasive, especially under pressure and then use **SIFT** to show how responders can quickly assess them before they distort triage, escalation, or crisis communications.

The goal is not perfect truth-detection. It is better operational judgment when trust is being actively manipulated.
### Speakers

#### René Lößner

![René Lößner](/assets/2026/avatars/KHA8DY_jWqroS6.webp){:width="30%" style="padding: 10px; float: right;"}
René works in IT security consulting with a focus on cyber resilience and incident readiness. He is particularly interested in threat intelligence, OSINT, and operational impact of manipulated or misleading information on incident and crisis response. His work explores how defenders can make better decision when trust, evidence, and narrative pressure collide.

<div style="clear: both;"></div>

---

## Let Him Cook! Hacking the Meatmeet BBQ Probe
- **Time:** 12:20 - 12:50
- **Speakers:**
  - [dead1nfluence](#dead1nfluence)

**Abstract:**
With grilling season quickly approaching, each and every grillmaster is eagerly preparing their tools… but little do some know, their “smart” meat probes may have some glaring vulnerabilities. In this 30 minute presentation we will disassemble, dump the flash, and decompile the mobile application of the Meatmeet BBQ probes to find countless vulnerabilities. 

From an open S3 bucket with the profile photo of every grill master, to never-before-seen devices, and even remote code execution, Julian will walk you through each vulnerability he found. This presentation will illustrate the importance of IoT security measures, because the last thing you want is for your beautiful BBQ to be burnt to a crisp!
### Speakers

#### dead1nfluence
As a Penetration Tester at Software Secured, Julian hunts for vulnerabilities across a range of clients and products. Off hours, he spends his time performing vulnerability research against IoT devices and FOSS, amassing over 40 CVEs in the past several years.

<div style="clear: both;"></div>

---

## Lunch
- **Time:** 12:50 - 13:50
<div style="clear: both;"></div>

---

## The Map of Artificial Treasures: What to Automate in Security - and Why?
- **Time:** 13:50 - 14:20
- **Speakers:**
  - [Michael Helwig](#michael-helwig)

**Abstract:**
With the rise of AI, especially large language models, it seems every security workflow will soon be automated or heavily supported by automation - from LLM-powered threat-intelligence enrichment or compliance mappings to AI-written threat models, codefixes and complete CISO roadmaps. But which processes will truly benefit, and in which cases will AI just increase the risk of adding cost and complexity? As security managers or leaders, how can we determine where to focus our efforts and investments upfront?

This talk presents a practical framework for evaluating the effectiveness of AI-driven automation in application security and related fields. First, we explore how to identify processes that are strong candidates for automation based on criteria such as repeatability, return on investment, and risk tolerance. Then, we map typical security processes to AI approaches, including large language models (LLMs), traditional machine learning, retrieval-augmented generation (RAG), and hybrid systems.

We will learn how these solutions are applied to critical security areas, such as vulnerability management, secure software development, threat detection, and compliance. We will explore an AI Capability Map, industry benchmarks, and real-world examples, such as the use of RAG-powered chatbots for security guidance and LLMs for compliance analysis. Our goal is to help you determine where AI would be a good fit for your organization and where you would likely see measurable value when applying it, so that you can make informed decisions. Also, we will examine the available data: In which areas of the industry is value already being recognized? We explore potential pitfalls, from fragile LLM implementations to poor risk modeling, and discuss how to avoid wasting resources.

Using industry data, real-world experience, and structured criteria, this talk provides security leaders and practitioners with more guidance in this rapidly evolving field.
### Speakers

#### Michael Helwig

![Michael Helwig](/assets/2026/avatars/VTB8G9_QAkfiRs.webp){:width="30%" style="padding: 10px; float: right;"}
I am a senior security consultant, founder and director at the Munich based company secureIO GmbH. With a strong background in application security and building and managing application security programs, I am passionate about all things related to AppSec and DevSecOps.

<div style="clear: both;"></div>

---

## Safe Power Grid Pentest, Practitioner's Guide to Security Without Operational Downtime
- **Time:** 14:20 - 14:50
- **Speakers:**
  - [Blessen Thomas](#blessen-thomas)
  - [Wojciech Poparda](#wojciech-poparda)

**Abstract:**
Pentesting critical infrastructure like a power grid is a high-stakes game where "move fast and break things" is a recipe for disaster. This session provides a transparent look on a regional grid, breaking down a repeatable, safety-first methodology that balances deep technical discovery with operational uptime.
We start at the beginning: the Rules of Engagement (RoE) workshop. You’ll learn how to work with site operators to map the environment using digital twins and mirrored test benches before a single packet is sent. From there, we move into the data: leveraging passive traffic analysis and protocol-specific inspection to identify firmware CVEs and insecure "clear-text" command paths without touching a live PLC.
The core of the talk demonstrates how to map the real-world effectiveness of the Purdue Model. We’ll walk through lateral movement scenarios—testing if guest or corporate Wi-Fi can jump the DMZ into Level 3,2,1,0 networks—and identify the "low-hanging fruit" that still plagues the grid, such as default credentials and unhardened ports.
By the end of this session, you’ll have a blueprint for conducting OT assessments that satisfy both security auditors and plant engineers. We will conclude with a walkthrough of traffic analysis techniques and architectural reviews that reveal the "crown jewels" of an ICS network without risking a blackout.
### Speakers

#### Blessen Thomas

![Blessen Thomas](/assets/2026/avatars/SXY7RD_pVHYBHi.webp){:width="30%" style="padding: 10px; float: right;"}
Blessen Thomas is an Independent Security Researcher. He has more than 13+ years of experience in Red Teaming, Appsec (Web, Thick, API & Mobile Apps), Smart Watch Wearable Application Penetration Testing, Mobile Penetration Test (iOS,Android,Windows platform), IoT,OT ,mainframes,SAP,SWIFT,RPA,Cloud,ATM,KIOSK,Vulnerability Assessment and Network Penetration Test,Physical Covert Entry,Wireless assessments,Telecom(2G,3G,USSD) etc. for several enterprise companies and financial institutions all across the globe.
He is a B.Tech in Information Technology from Anna University and holds industry certifications such as SANS GPEN,CRTO,OPST,CREST CRT(PEN),CREST CPSA,OSCP,CRTP,OSWP,C)PTE,CEH,CHFI. He has been listed and acknowledged in various “HALL OF FAMES” for various companies such as Oracle,Sony, Kayako, Appcelerator, Hotgloo, Meldium, Splunk and many more for responsible disclosure. He has been a bug bounty hunter and contributor for the OWASP Mobile Testing Guide Project(MSTG),Tamer OS, Seclists, OWASP top 10 API, OSSTMM, Awesome Mainframe Hacking,RvR,WAVSEP Benchmark sectool projects.
His research training/talks has been accepted into various security conferences like Hack in the Box-Dubai,Hacktivity -Hungary, CanSecWest -Canada,OWASP Appsec EU- London -UK,OWASP Appsec Europe-Italy, RootCon-Philippines ,OWASP PH,OWASP New Zealand Day, Infosec SouthWest,Austin,Texas, FSec-Croatia, Hackbeach, Hackfest, Shakacon,ITWeb-South Africa, Jordan Cyber Security Summit, HITCON-Taiwan, OWASP AppSec-Bucharest, OWASP Appsec Africa-Morocco, Bsides-London,CircleCityCon,OWASP Botswana,CactusCon and many more.
He has been invited as Speaker for Radio Talk Shows for All India Radio. He spends his leisure time playing drumkit and percussion.

#### Wojciech Poparda

![Wojciech Poparda](/assets/2026/avatars/3JBJGA_rQaE0Hw.webp){:width="30%" style="padding: 10px; float: right;"}
Wojciech Poparda is a cybersecurity consultant. He helps organizations proactively defend their digital infrastructure by thinking like an adversary. Leveraging a deep foundation in Offensive Security, he specializes in designing resilient Security Architectures that bridge the gap between complex attack vectors and enterprise defense, with a sharp focus on Cloud Security and Identity & Access Management (IAM).

His approach is backed by rigorous technical validation, holding industry-leading certifications including OSCP, CRTE, CRTP, CRTO, CPTS, CWES, and AWS Certified Solutions Architect - Associate. He is also an Associate of ISC2, having successfully passed the CISSP exam.

Beyond the terminal, he channels the discipline, focus, and resilience required for cybersecurity into his life as a triathlete. As an IRONMAN European and World Championships finisher, he brings the same endurance and dedication to solving complex security challenges as he does to the race course.

<div style="clear: both;"></div>

---

## I Let My Pi5 Hack: Building a 0$ AI Pentesting Agent
- **Time:** 14:50 - 15:20
- **Speakers:**
  - [Nithin Ravi](#nithin-ravi)

**Abstract:**
AI and automation are often used interchangeably, but they solve very different problems. But what if they can be used together to solve a single problem? This talk dives into lessons the presenter has learned while building a $0, fully self-hosted AI-assisted pentesting and bug bounty agent using a Raspberry Pi 5.

Attendees will see how local hardware can be scaled without a VPS and how recon and testing workflows can be stitched together using open-source orchestration tools like n8n, moltbot, and other open-source tools. It also explores using a local LLM with Ollama to triage, prioritize, and reason through results instead of relying on blind automation. Common assumptions, and areas of failure are shared along the way.

The session is designed for all experience levels, with a focus on mid-level hackers and developers who want practical, cost-efficient ways to build AI-assisted security workflows.
### Speakers

#### Nithin Ravi

![Nithin Ravi](/assets/2026/avatars/97K8WJ_cSva7Rp.webp){:width="30%" style="padding: 10px; float: right;"}
Nithin Ravi is a security researcher and offensive security specialist working at Centripetal, Ireland. He holds multiple industry relevant certifications such as the Certified Red Team Professional (CRTP), a double masters in computer science and information systems management, 3 year work experience in cybersecurity and a published research paper to his name.

He is also a speaker at various conferences and meetups such as BSides Galway, DevFest Ireland, IWCON, GDG Galway and does bug bounty hunting for fun and profit. He is currently invested and working on leveraging AI for offensive security.

Outside work, Nithin plays chess, does photography and is a big time fiction reader.

<div style="clear: both;"></div>

---

## Afternoon break
- **Time:** 15:20 - 15:45
<div style="clear: both;"></div>

---

## The Illusion of Finishability
- **Time:** 15:45 - 16:15
- **Speakers:**
  - [Juliane Reimann](#juliane-reimann)

**Abstract:**
As security people we live in a world of "it depends", probabilities, and never-ending risk. At the same time we as humans crave clear answers. So when someone asks, „Is it secure now?” and the honest answer is „No”, it creates psychological friction.

In this talk, we will explore the Need for Cognitive Closure, a psychological concept that explains why uncertainty is so uncomfortable and why teams often push for premature certainty in security decisions. We will take a close look at how this plays out in real life by rushing to close findings, over-trusting tools, or treating compliance checklists as proof of safety.

Drawing from practical examples, I will share ways to design security work with human psychology in mind: from better risk communication and structured decision frameworks to Security Champions programs that turn ongoing uncertainty into shared ownership. We will stop chasing the illusion of finishability and start building teams that stay effective even when security can’t give final answers.
### Speakers

#### Juliane Reimann

![Juliane Reimann](/assets/2026/avatars/VBBVRJ_jtIBNjI.webp){:width="30%" style="padding: 10px; float: right;"}
Juliane Reimann is a Founder & Security Community Expert @ FullCyrcle Security. She has worked as a cyber security consultant for large companies since 2019 with focus on DevSecOps and Community Building. Her expertise includes building security communities of software developers and establishing developer centric communication about secure software development topics. Before going into the field of Cyber Security she founded different companies in the area of web development. Due to her background in web development she has extensive knowledge of the software development life cycle. Since 2024, she has been a core member of the OWASP Security Champions Guide Community.

<div style="clear: both;"></div>

---

## Pull the Plug: Kernel-Level Surgery to Blind EDRs
- **Time:** 16:15 - 16:45
- **Speakers:**
  - [André Lima](#andré-lima)

**Abstract:**
Modern EDR solutions are only as effective as the telemetry they can collect. This talk takes a methodical, kernel-level approach to understanding (and dismantling) every major sensor an EDR relies on to detect malicious activity. From ETW providers feeding threat intelligence data, to kernel callbacks registering process and image events, to minifilter drivers intercepting filesystem I/O, and WFP callouts gating network telemetry: each one is a wire that can be cut.
This is not an attack on Microsoft. It's a surgical dissection of Windows' own defensive instrumentation, from the perspective of a Red Teamer who needs operational silence. Through live reverse engineering of Windows internals and hands-on demos, attendees will leave with a concrete, layered plan for achieving full "sensor deprivation" against EDR products.
### Speakers

#### André Lima

![André Lima](/assets/2026/avatars/E7K9B8_z3lJVrm.webp){:width="30%" style="padding: 10px; float: right;"}
Andre Lima is a Team Leader and Red Team operator doing it since 2011, who has worked in Portugal, Australia, and now leading the Red Team at Telenor CyberDefence in Oslo.
He is also a researcher and tries to publish as often as possible at his [Youtube channel](https://www.youtube.com/@0x4ndr3), and [blog](https://0x4ndr3.github.io/), while also doing presentations at [security conferences](https://github.com/0x4ndr3/Presentations).
His main areas of expertise are reverse engineering, exploit development, and malware development with a focus on EDR bypasses.
When not working, he enjoys playing basketball, tennis, or simply watching Formula1.

<div style="clear: both;"></div>

---

## Your Traffic Is Lying to You
- **Time:** 16:45 - 17:15
- **Speakers:**
  - [Lisa Froehlich](#lisa-froehlich)

**Abstract:**
Bots now generate more than half of global HTTP traffic. Many of these bots deliberately mimic legitimate users, spoof known crawlers, or operate just below every threshold that your monitoring system is calibrated for. As a result, the most damaging application-layer attacks today produce no bandwidth alert, payload anomaly, or obvious signature. They appear to be normal operation.
This talk will examine three real attack patterns:

1) A session flood that generates 16 million new sessions per minute against a single domain. This attack is invisible at the network layer, yet it is fatal to backend resources.
2) A multi-week, low-and-slow campaign that causes measurable revenue loss without ever triggering a security event.
3) A controlled reconnaissance attack that systematically maps defense response times ahead of a high-traffic sales period. This attack is not trying to cause an outage, but rather, it is preparing for one.

The common thread is not technical sophistication. It is the absence of a behavioral baseline. Organizations that have never profiled their own legitimate traffic cannot distinguish a bot campaign from a demand spike. Traffic volume, unique IP addresses, and request rates have become unreliable signals, and attackers know it.

The second half of the talk offers practical advice on what meaningful traffic profiling requires, where behavioral detection works and where it fails, and how to detect persistent application-layer pressure before it becomes a business problem.
### Speakers

#### Lisa Froehlich

![Lisa Froehlich](/assets/2026/avatars/RVQ899_pP2jxUe.webp){:width="30%" style="padding: 10px; float: right;"}
Lisa Fröhlich is Head of Corporate Communications at Link11, a European provider that specializes in DDoS mitigation and application-layer protection. With a background in science communication and over a decade of experience in technology public relations (PR), she translates complex threat data into actionable insights. Since 2023, she has hosted the IT security podcast Follow the White Rabbit. In 2025, she completed a professional cybersecurity program at the Eurobits Women Academy.

<div style="clear: both;"></div>

---

## Closing
- **Time:** 17:45 - 17:50

**Abstract:**
Closing Remarks
<div style="clear: both;"></div>

---


---

## Backup Speakers

#### Michel Messerschmidt
Michel Messerschmidt is a Senior Key Expert for Industrial Cybersecurity at Siemens Gamesa Renewable Energy.
<div style="clear: both;"></div>

---

#### Kaan Tolunay Kilic

![Kaan Tolunay Kilic](/assets/2026/avatars/M7J3WT_ERSs1Ni.webp){:width="30%" style="padding: 10px; float: right;"}
Kaan Tolunay Kilic is part of the cloud solutions and governance team and works at Otto Group one.O GmbH, where he is developing platform services for the product teams. He likes to learn and share his experience with others.
<div style="clear: both;"></div>

---

