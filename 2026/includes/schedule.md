# Program

| Time | Speaker(s) | Talk |
|------|------------|------|
| 09:00 |  | [Opening](#opening) |
| 09:10 | [Natalie Kilber](#natalie-kilber) | [Keynote: Secrets don’t age well: Cyber, Kyber, Quantum and the encryption time bombs](#keynote-secrets-dont-age-well-cyber-kyber-quantum-and-the-encryption-time-bombs) |
| 09:55 | [Leon Rickert](#leon-rickert) | [Harvest Now, Decrypt Later: Bringing Post-Quantum Cryptography to SSH](#harvest-now-decrypt-later-bringing-post-quantum-cryptography-to-ssh) |
| 10:25 |  | [Morning break](#morning-break) |
| 10:50 | [Michael Reimsbach](#michael-reimsbach), [Rishi (@rxerium)](#rishi-rxerium) | [Ghost in the Hiring Machine: Catch Fake Personas Before They’re Hired](#ghost-in-the-hiring-machine-catch-fake-personas-before-theyre-hired) |
| 11:20 | [Robin Kirchner](#robin-kirchner) | ['We Have Always Been at War With Eastasia': Attacks Against Web Archives](#we-have-always-been-at-war-with-eastasia-attacks-against-web-archives) |
| 11:50 | [René Lößner](#rené-lößner) | [When Trust Breaks Under Pressure](#when-trust-breaks-under-pressure) |
| 12:20 | [Julian (dead1nfluence)](#julian-dead1nfluence) | [Let Him Cook! Hacking the Meatmeet BBQ Probe](#let-him-cook-hacking-the-meatmeet-bbq-probe) |
| 12:50 |  | [Lunch](#lunch) |
| 13:50 | [Michael Helwig](#michael-helwig) | [The Map of Artificial Treasures: What to Automate in Security - and Why?](#the-map-of-artificial-treasures-what-to-automate-in-security---and-why) |
| 14:20 | [André Lima](#andré-lima) | [Pull the Plug: Kernel-Level Surgery to Blind EDRs](#pull-the-plug-kernel-level-surgery-to-blind-edrs) |
| 14:50 | [Nithin Ravi](#nithin-ravi) | [I Let My Pi5 Hack: Building a 0$ AI Pentesting Agent](#i-let-my-pi5-hack-building-a-0-ai-pentesting-agent) |
| 15:20 |  | [Afternoon break](#afternoon-break) |
| 15:45 | [Lisa Froehlich](#lisa-froehlich) | [Your Traffic Is Lying to You](#your-traffic-is-lying-to-you) |
| 16:15 | [Younes Ahmadzei](#younes-ahmadzei) | [Still Out of Sight? The NIS-2 Reality Check in German SMEs](#still-out-of-sight-the-nis-2-reality-check-in-german-smes) |
| 16:45 | [Juliane Reimann](#juliane-reimann) | [The Illusion of Finishability](#the-illusion-of-finishability) |
| 17:15 | [Brian Hein](#brian-hein), [Constantin Jacob](#constantin-jacob) | [Keynote: Who comes next?](#keynote-who-comes-next) |
| 17:45 |  | [Closing](#closing) |
| 18:00 |  | [Networking hours](#networking-hours) |

## Speakers

[André Lima](#andré-lima), [Brian Hein](#brian-hein), [Constantin Jacob](#constantin-jacob), [Julian (dead1nfluence)](#julian-dead1nfluence), [Juliane Reimann](#juliane-reimann), [Leon Rickert](#leon-rickert), [Lisa Froehlich](#lisa-froehlich), [Michael Helwig](#michael-helwig), [Michael Reimsbach](#michael-reimsbach), [Michel Messerschmidt](#michel-messerschmidt), [Natalie Kilber](#natalie-kilber), [Nithin Ravi](#nithin-ravi), [René Lößner](#rené-lößner), [Rishi (@rxerium)](#rishi-rxerium), [Robin Kirchner](#robin-kirchner), [Younes Ahmadzei](#younes-ahmadzei)

## Talks

## Opening
- **Time:** 09:00 - 09:10

**Abstract:**
Conference opening
<div style="clear: both;"></div>

---

## Keynote: Secrets don’t age well: Cyber, Kyber, Quantum and the encryption time bombs
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
- ![LinkedIn](/assets/icons/linkedin-icon.svg){:width="18px" :height="18px" style="vertical-align: middle;"}: [https://www.linkedin.com/company/hastesec/](https://www.linkedin.com/company/hastesec/)
- ![Website](/assets/icons/www-icon.svg){:width="18px" :height="18px" style="vertical-align: middle;"}: [https://hastesecurity.com/](https://hastesecurity.com/)

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
- ![LinkedIn](/assets/icons/linkedin-icon.svg){:width="18px" :height="18px" style="vertical-align: middle;"}: [https://linkedin.com/in/mreimsbach](https://linkedin.com/in/mreimsbach)

#### Rishi (@rxerium)

![Rishi (@rxerium)](/assets/2026/avatars/BUFJAD_qqqayWL.webp){:width="30%" style="padding: 10px; float: right;"}
Rishi is a London-based security researcher with experience in vulnerability research, threat intelligence, and enterprise risk analysis. His work focuses on identifying zero-day vulnerabilities and emerging CVEs, with a particular interest in building detection logic before threats are publicly weaponised.

He works across both offensive and defensive disciplines, developing threat models grounded in real-world TTPs, writing detection rules, and automating reconnaissance to uncover exposed assets at scale. Attack surface management and OSINT are areas he keeps coming back to, specifically the challenge of mapping exposure that organisations often don't know exists.

Outside of his day job, Rishi contributes to open source security tooling through Project Discovery and OWASP, part of the leadership team of the UK OSINT Community, and occasionally speaks at community events including DEF CON and BSides.

**Social Media:**
- ![X](/assets/icons/x-icon.svg){:width="18px" :height="18px" style="vertical-align: middle;"}: [https://x.com/rxerium](https://x.com/rxerium)
- ![LinkedIn](/assets/icons/linkedin-icon.svg){:width="18px" :height="18px" style="vertical-align: middle;"}: [https://linkedin.com/in/rxerium](https://linkedin.com/in/rxerium)
- bsky: [https://bsky.app/profile/rxerium.com](https://bsky.app/profile/rxerium.com)
- ![Mastodon](/assets/icons/mastodon-icon.svg){:width="18px" :height="18px" style="vertical-align: middle;"}: [https://infosec.exchange/@rxerium](https://infosec.exchange/@rxerium)
- ![Discord](/assets/icons/discord-icon.svg){:width="18px" :height="18px" style="vertical-align: middle;"}: [https://discord.com/users/1015266410332700755](https://discord.com/users/1015266410332700755)
- ![Website](/assets/icons/www-icon.svg){:width="18px" :height="18px" style="vertical-align: middle;"}: [https://rxerium.com](https://rxerium.com)
- github: [https://github.com/rxerium](https://github.com/rxerium)

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

![Robin Kirchner](/assets/2026/avatars/CBJW3B_UmQTa6O.webp){:width="30%" style="padding: 10px; float: right;"}
Robin is a senior Phd student at TU Braunschweig with an interest in secure systems and large-scale web scanning. His research focuses on the security and integrity of complex web-based systems, including the discovery of hard-to-find flaws and vulnerabilities in web archives, and on defending web systems against attacks.

**Social Media:**
- ![LinkedIn](/assets/icons/linkedin-icon.svg){:width="18px" :height="18px" style="vertical-align: middle;"}: [https://www.linkedin.com/in/robin-kirchner-3073971a3/](https://www.linkedin.com/in/robin-kirchner-3073971a3/)
- ![Website](/assets/icons/www-icon.svg){:width="18px" :height="18px" style="vertical-align: middle;"}: [https://robinkirchner.de](https://robinkirchner.de)
- github: [https://github.com/robinki](https://github.com/robinki)

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
  - [Julian (dead1nfluence)](#julian-dead1nfluence)

**Abstract:**
With grilling season quickly approaching, each and every grillmaster is eagerly preparing their tools… but little do some know, their “smart” meat probes may have some glaring vulnerabilities. In this 30 minute presentation we will disassemble, dump the flash, and decompile the mobile application of the Meatmeet BBQ probes to find countless vulnerabilities. 

From an open S3 bucket with the profile photo of every grill master, to never-before-seen devices, and even remote code execution, Julian will walk you through each vulnerability he found. This presentation will illustrate the importance of IoT security measures, because the last thing you want is for your beautiful BBQ to be burnt to a crisp!
### Speakers

#### Julian (dead1nfluence)
As a Penetration Tester at Software Secured, Julian hunts for vulnerabilities across a range of clients and products. Off hours, he spends his time performing vulnerability research against IoT devices and FOSS, amassing over 50 CVEs in the past several years. Previous work includes exploiting the Furbo devices, to find 20+ vulnerabilities, discovering [more than 130,000 Claude, Grok, ChatGPT, and Other LLM Chats Readable on Archive.org](https://www.404media.co/more-than-130-000-claude-grok-chatgpt-and-other-llm-chats-readable-on-archive-org/), as well as being featured by 404Media in the article: [ Grok Exposes Underlying Prompts for Its AI Personas: ‘EVEN PUTTING THINGS IN YOUR ***’](https://www.404media.co/grok-exposes-underlying-prompts-for-its-ai-personas-even-putting-things-in-your-ass/)

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

## Pull the Plug: Kernel-Level Surgery to Blind EDRs
- **Time:** 14:20 - 14:50
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

## I Let My Pi5 Hack: Building a 0$ AI Pentesting Agent
- **Time:** 14:50 - 15:20
- **Speakers:**
  - [Nithin Ravi](#nithin-ravi)

**Abstract:**
AI and automation are often used interchangeably, but they solve very different problems. But what if they can be used together to solve a single problem? This talk dives into lessons the presenter has learned while building a $0, fully self-hosted AI-assisted pentesting and bug bounty agent using a Raspberry Pi 5.

Attendees will see how local hardware can be scaled without a VPS and how recon and testing workflows can be stitched together using various open-sourced tools. It also explores using a local LLM with Ollama to triage, prioritize, and reason through results instead of relying on blind automation. Common assumptions, and areas of failure are shared along the way and there is a clear distinction to what exactly can a 0$ model do and where you need to pay.

The session is designed for all experience levels, with a focus on mid-level hackers and developers who want practical, cost-efficient ways to build AI-assisted security workflows.
### Speakers

#### Nithin Ravi

![Nithin Ravi](/assets/2026/avatars/97K8WJ_K6YgCJp.webp){:width="30%" style="padding: 10px; float: right;"}
Nithin Ravi is a security researcher and offensive security specialist working at Centripetal, Ireland. He holds multiple industry relevant certifications such as the Certified Red Team Professional (CRTP), a double masters in computer science and information systems management, 3 year work experience in cybersecurity and a published research paper to his name.

He is also a speaker at various conferences and meetups such as BSides Galway, DevFest Ireland, IWCON, GDG Galway and does bug bounty hunting for fun and profit. He is currently invested and working on leveraging AI for offensive security.

Outside work, Nithin plays chess, does photography and is a big time fiction reader.

**Social Media:**
- ![X](/assets/icons/x-icon.svg){:width="18px" :height="18px" style="vertical-align: middle;"}: [https://x.com/thebinarybot](https://x.com/thebinarybot)
- ![LinkedIn](/assets/icons/linkedin-icon.svg){:width="18px" :height="18px" style="vertical-align: middle;"}: [https://www.linkedin.com/in/nithinravi10/](https://www.linkedin.com/in/nithinravi10/)
- ![Website](/assets/icons/www-icon.svg){:width="18px" :height="18px" style="vertical-align: middle;"}: [https://nithinr.com/](https://nithinr.com/)

<div style="clear: both;"></div>

---

## Afternoon break
- **Time:** 15:20 - 15:45
<div style="clear: both;"></div>

---

## Your Traffic Is Lying to You
- **Time:** 15:45 - 16:15
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

## Still Out of Sight? The NIS-2 Reality Check in German SMEs
- **Time:** 16:15 - 16:45
- **Speakers:**
  - [Younes Ahmadzei](#younes-ahmadzei)

**Abstract:**
The NIS-2 directive aims to elevate European cybersecurity, but its implementation often clashes with the reality of understaffed SME IT departments and organizational inertia.

In my Phase 1 research (conducted before the law passed), reaching out to 1,800 SMEs yielded only 17 interviews, highlighting a widespread "wait-and-see" attitude. Now, as of December 2025, NIS-2 is active national law in Germany, including executive liability. Did this finally trigger the necessary compliance efforts in the German Mittelstand?

This talk presents the findings of my Phase 2 longitudinal follow-up study (Q1 2026). Based on quantitative data and qualitative interviews with CISOs and IT leads, we will explore the current implementation barriers. The data shows that SMEs struggle significantly less with technical complexity than with the massive burden of proof and documentation.

Furthermore, we will discuss why complex, state-sponsored standard frameworks often fail in practice. Instead, I will demonstrate how a pragmatic, Excel-based self-assessment tool, mapped to established standards like ISO 27001 and TISAX, helped companies overcome their initial compliance paralysis. Expect empirical data, real-world quotes from IT professionals, and actionable takeaways on how the InfoSec community can better support SMEs.
### Speakers

#### Younes Ahmadzei

![Younes Ahmadzei](/assets/2026/avatars/CHVHRC_u8yLfgf.webp){:width="30%" style="padding: 10px; float: right;"}
Younes Ahmadzei is an Information Systems student at the Technical University of Munich (TUM) and an Information Security Consultant. His research centers around the EU's NIS-2 Directive and its real-world implications for mid-sized German companies.

As part of his initial research, he created a pragmatic NIS-2 self-assessment tool, mapped the directive's requirements to ISO 27001, TISAX, and BSI IT-Grundschutz, and conducted a massive empirical outreach to 1,800 SMEs. He is currently extending this work through a longitudinal Phase 2 study (Q1 2026) to analyze the actual market reality and compliance barriers now that the national NIS-2 law is actively in effect.

**Social Media:**
- ![LinkedIn](/assets/icons/linkedin-icon.svg){:width="18px" :height="18px" style="vertical-align: middle;"}: [https://de.linkedin.com/in/younes-ahmadzei-7536b42a3](https://de.linkedin.com/in/younes-ahmadzei-7536b42a3)

<div style="clear: both;"></div>

---

## The Illusion of Finishability
- **Time:** 16:45 - 17:15
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

## Keynote: Who comes next?
- **Time:** 17:15 - 17:45
- **Speakers:**
  - [Brian Hein](#brian-hein)
  - [Constantin Jacob](#constantin-jacob)

**Abstract:**
We solved what to share. We solved how fast to share it. We did not solve who comes next.
Threat intelligence has run for two decades on an iron principle — KMT: Know, Met, Trust — enforced by physics. You had to be in the room. Then COVID closed the room. The room reopened. The travel budgets did not. The next generation is being raised by agentic tools that give them every answer except one: who do I call?
Picking up the line that started in Montreal (Trust → Action) and continued in Munich (Action → Impact), this talk argues the next evolution is bench depth. Two calls to arms, a feeder-team model borrowed from professional sports, and a single demand: stop fighting like a Rolodex. Start fighting like an army.
### Speakers

#### Brian Hein

![Brian Hein](/assets/2026/avatars/MMYYJG_2M4P41v.webp){:width="30%" style="padding: 10px; float: right;"}
Brian Hein is Principal Threat Researcher at DNSFilter, Case Lead at the World Economic Forum’s Cybercrime Atlas, a FIRST.org Liaison Member, and sits on the National Council of ISACs. Two decades of community-driven disruption work across HP, Flashpoint, DTAG, and Silobreaker. Co-authored How NOT to Be Your Adversary’s Best Friend at FIRST CTI 2026 in Munich.

**Social Media:**
- ![LinkedIn](/assets/icons/linkedin-icon.svg){:width="18px" :height="18px" style="vertical-align: middle;"}: [https://linkedin.com/in/heinbrian](https://linkedin.com/in/heinbrian)
- bsky: [https://bsky.app/profile/heinbrian.bsky.social](https://bsky.app/profile/heinbrian.bsky.social)

#### Constantin Jacob

![Constantin Jacob](/assets/2026/avatars/RM8EDR_cCzOBcG.webp){:width="30%" style="padding: 10px; float: right;"}
Constantin Jacob (CJ) is a software engineering manager at DNSFilter focused on protecting the privacy of multiple hundred thousand customers of the Guardian Firewall + VPN service and their OEM partners. CJ spent the last 8 years building the skills to operate and maintain secure & reliable core technologies which route multiple petabytes of customer traffic every week across a global network of public VPN servers, accessible to customers with a single tap through deep platform integrations

<div style="clear: both;"></div>

---

## Closing
- **Time:** 17:45 - 17:50

**Abstract:**
Closing Remarks
<div style="clear: both;"></div>

---

## Networking hours
- **Time:** 18:00 - 20:00
<div style="clear: both;"></div>

---


---

## Backup Speakers

#### Michel Messerschmidt
Michel Messerschmidt is a Senior Key Expert for Product Cybersecurity at Siemens Gamesa Renewable Energy.
<div style="clear: both;"></div>

---

