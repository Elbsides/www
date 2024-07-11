---
title: "Programme"
layout: page
permalink: /2019/programme/

---

**The conference and workshop date is 16th of September, 2019.**

All conference talks will be in the [Elbe](/2019/venue#elbe) room.

| Time   |                | Title                    | Speaker  |
| ------ | ------ |:-------------|:------|
| 08:00 | 09:00      | registration        |              |
| 09:00 | 09:10      | intro                   |              |
| 09:10 | 10:10      | [Keynote: The Past, Present, and Future of DNS Resolution](#keynote-the-past-present-and-future-of-dns-resolution) | [Paul Vixie](#paul-vixie) |
| 10:10 | 10:55      | [DNS privacy and how DNS-over-HTTPS may fix it](#dns-privacy-and-how-dns-over-https-may-fix-it) | [Ole Michaelis](#ole-michaelis) |
| 10:55 | 11:15      | break     |     |
| 11:15 | 12:00      | [Privacy Attacks Against Machine Learning Systems](#privacy-attacks-against-machine-learning-systems)  |  [Katharine Jarmul](#katharine-jarmul) |
| 12:00 | 12:25      | [Improving the Performance and Privacy of TCP Fast Open, TLS 1.3, and QUIC](#improving-the-performance-and-privacy-of-tcp-fast-open-tls-13-and-quic) | [Erik Sy](#erik-sy) |
| 12:25 | 12:50      | [Exploring Emotet, an Elaborate Everyday Enigma](#exploring-emotet-an-elaborate-everyday-enigma) | [Luca Nagy](#luca-nagy) |
| 12:50 | 13:50      | lunch     |     |
| 13:50 | 14:35      | [Defending BLE Beacon Applications Against Common Attacks](#defending-ble-beacon-applications-against-common-attacks) | [Christoph Peglow](#christoph-peglow), [Malte Stoffers](#malte-stoffers) and [Thore Tiemann](#thore-tiemann)|
| 14:35 | 15:20      | [When Your Biggest Threat is on Your Payroll: Drivers & Enablers of Insider Threat Activity](#when-your-biggest-threat-is-on-your-payroll-drivers--enablers-of-insider-threat-activity) | [Christina Lekati](#christina-lekati) |
| 15:20 | 15:40      | break     |     |
| 15:40 | 16:25      | [Securing Software at Scale - The crazy world of modern application security programs](#securing-software-at-scale---the-crazy-world-of-modern-application-security-programs) | [Michael Helwig](#michael-helwig) |
| 16:25 | 17:10      | [Continuous Security at the Next Level](#continuous-security-at-the-next-level) | [Martin Reinhardt](#martin-reinhardt) |
| 17:10 | 17:55      | [Credential Stuffing Attacks! What is it and how you can protect your Web Application!](#credential-stuffing-attacks-what-is-it-and-how-you-can-protect-your-web-application) | [Samy Makki](#samy-makki) |
| 17:55 | 18:00      | closing     |     |

Reserve paper: [A brief introduction to Digital Forensics](#a-brief-introduction-to-digital-forensics) - [Tim Eggert](#tim-eggert)

# Workshop Programme #

The Workshops take place on the first floor and there are two rooms: [Alster](/2019/venue#alster)  and  [Bille](/2019/venue#bille). Take the stairs or the elevator up one floor from the entrance area (or three floors from the main space).

## Workshops in room [Alster](/2019/venue#alster)  ##

|------- | -----+--------------------------------+---------------|
| Time      |            | Title                                                         | Speaker       |
| ------ | ------| :----------------------------- |:--------------|
| 08:00    | 09:00  |      Registration  will be outside room  [Elbe](/2019/venue#elbe)   |
|------- | -----+--------------------------------+---------------|
| 11:00     | 12:55  |  [From source code to the final end - The way of an encryption trojan from attacker to your company](#from-source-code-to-the-final-end---the-way-of-an-encryption-trojan-from-attacker-to-your-company) | [Constantin Zankl ](#constantin-zankl), [Clemens Rambow](#clemens-rambow) |
|------- | -------+-----------+--------------------------------+---------------|
| 13:50     | 17:50  |  [Elbsides vs. Juice Shop](#elbsides-vs-juice-shop) | [Björn Kimminich](#björn-kimminich) |
|------- | -----+-------------------------------------------+---------------|

## Workshops in room [Bille](/2019/venue#bille) ##

|------- | -----------------+--------------------------------+---------------|
| Time      |             | Title                          | Speaker       |
| ------ | ------ |:---------| :----------------------------- |:--------------|
| 08:00    | 09:00   |    Registration  will be outside room  [Elbe](/2019/venue#elbe)                       |               |
|------- | -------+-----------+--------------------------------+---------------|
| 11:00    | 12:55   | [Bettercap: exploring the local network](#bettercap-exploring-the-local-network) | [Christoph Eicke](#christoph-eicke) |
|------- | ------------------+--------------------------------+---------------|
| 13:50    | 17:50   | [Introduction to Binary Reversing and Exploitation with radare2](#introduction-to-binary-reversing-and-exploitation-with-radare2) | [Richard Sammet](#richard-sammet) |
|------- | ------------------+--------------------------------+---------------|

-------------------------------------------------------------------------------

# Presentations #

## Keynote: The Past, Present, and Future of DNS Resolution ##

* Speaker: [Paul Vixie](#paul-vixie)
* Time: 9:10
* Length: 1h
* Room: [Elbe](/2019/venue#elbe)

The Domain Name System has been a critical enabler of Internet growth
since its inception in 1987. In the decades since then, the DNS
resolution process has evolved from the LAN to the WAN, and to
Anycast; it now includes DNSSEC validation, Extended DNS (EDNS) Client
Subnet, larger message sizes, and I18N. The resolution processs has
also been abused for surveillance, advertising insertion, and
exfiltration. Today the DNS resolution process is poorly understood,
and yet under forced revision. The trend is for DNS to be carried
inside HTTPS where it cannot be monitored or controlled except by
servers and clients themselves, and the dangers this will yield must
be studied and discussed while the future remains flexible. Dr. Vixie
will describe the past and present of DNS, and discuss its likely near
term future.


## DNS privacy and how DNS-over-HTTPS may fix it ##
* Speaker: [Ole Michaelis](#ole-michaelis)
* Time: 10:10
* Length: 45 min
* Room: [Elbe](/2019/venue#elbe)

DNS is a protocol as old as the Internet. Yet we only notice it when it’s not working, or when some company acquires a cool IP to run their own resolvers. But lately, there’s a new, cool kid in town: DNS-over-HTTP, or DoH. In this talk, I want to answer the question you all had when you read it the first time: Why? Why would anyone really want to do this? After we explore the motivation behind this, we’ll look a bit into the implementation details and the current status of the effort.

## Privacy Attacks Against Machine Learning Systems ##
* Speaker: [Katharine Jarmul](#katharine-jarmul)
* Time: 11:15
* Length: 45 min
* Room: [Elbe](/2019/venue#elbe)

Research in the past several years has shown that machine learning models can expose personal information present in their training data. This vulnerability exposes sensitive user information to attackers savvy enough to learn how to hack a machine learning API. In this talk, we'll explore the details of several privacy attacks against machine learning models and provide some potential solutions for this growing security issue.


## Improving the Performance and Privacy of TCP Fast Open, TLS 1.3, and QUIC ##
* Speaker: [Erik Sy](#erik-sy)
* Time: 12:00
* Length: 25 min
* Room: [Elbe](/2019/venue#elbe)

The delay of the connection establishment of modern HTTPS protocol stacks presents a performance bottleneck for web browsing. Furthermore, performance-optimizations such as TLS session resumption present a performance versus user privacy tradeoff. In this talk, we discuss severe privacy issues of state-of-the-art HTTPS protocols stacks such as the kernel-based tracking mechanism using TCP Fast Open cookies.
Subsequently, we present evaluation results indicating mechanisms such as out-of-band address validation tokens for QUIC that allow further performance improvements for the connection establishment on the web.


## Exploring Emotet, an Elaborate Everyday Enigma ##
* Speaker: [Luca Nagy](#luca-nagy)
* Time: 12:25
* Length: 25 min
* Room: [Elbe](/2019/venue#elbe)

Based on Sophos detection numbers the Emotet Trojan is the most widespread malware family in the wild. It has been, and is still, the most notorious and costly malware since its appearance more than five years ago. Emotet owes its reputation to its constant state of evolution and change. The malware's rapid advancement helps support its highly sophisticated operation. This presentation will discuss the reverse engineering of its component, the capabilities and features of Emotet: a detailed overview of its multilayered operation, starting with the spam lure, the malicious attachments (and their evolution); and the malware executable itself, from its highly sophisticated packer, to its C2 server communications.

Emotet is well-known for its modular architecture, worm-like propagation, and highly skilled persistence techniques. The recent versions spread rapidly using multiple methods. Besides its capability to spread by brute forcing using its own password lists, it can harvest email addresses and email contents from victims, then spread through spam. Its diverse module list hides different malicious intentions, such as information stealing including credentials from web browsers or email clients, spreading capabilities, or delivering other malwares as well as ransomware or other banking Trojans. Finally, I will dissect the background operations of the payload modules. I will also present statistics from Sophos about its global reach.

## Defending BLE Beacon Applications Against Common Attacks ##
* Speakers: [Christoph Peglow](#christoph-peglow), [Malte Stoffers](#malte-stoffers) and [Thore Tiemann](#thore-tiemann)
* Time: 13:50
* Length: 45 min
* Room: [Elbe](/2019/venue#elbe)

Bluetooth Low Energy (BLE) is a wireless network technology that is often used in IoT scenarios like indoor navigation, proximity marketing, automatic check-in or contactless payment. These usually use broadcast messages, so called BLE beacons, which by default have no protection mechanisms against attackers. Anyone with a Bluetooth receiver device can see these beacons and their content and thus can copy, manipulate and replay them anywhere at any time [3]. Therefore no confidential data should be transmitted using beacons. Furthermore location determination and authentication based on beacons is not to be trusted.

Common beacon developers like Google(1), kontact.io(2), and Estimote(3) use UUID shuffling to defend their beacons against such attacks. This means that the beacon UUID is shuffled depending on a seed and a shuffling algorithm. The seed and the algorithm are to be kept in the cloud and the beacon only to ensure attackers cannot gain any knowledge by reverse engineering the corresponding app. This setup brings two problems: (a) a constant cloud connection is required to decode beacons and (b) keeping the shuffling algorithm secret is security by obscurity and therefore cannot be trusted [2].

We present a solution to defend BLE beacon applications against common attacks like manipulation, data extraction, replay, and cloning attacks. There are two main results: (a) a structure for BLE beacons that protect the confidentiality, integrity and authenticity of the payload and (b) a prototype infrastructure, which fulfills all the preconditions needed to achieve (a). Our beacon relies on well researched cryptographic primitives such AES encryption, which today is supported in hardware by commodity low-energy BLE chips, SHA256 hmac and Curve25519 [1]. Additionally no constant cloud connection is needed to decode beacons.

To test our secure beacon we developed prototype Android application, which receives theses beacons from a microcontroller. The payload consists of arbitrary data that is AES-encrypted and also provides integrity checks and replay protection. The disadvantage in this version is the usage of a shared key for encryption. The key must be available on the Android device on startup, which means it has to be hardcoded in the application. To solve this problem, we extend our prototype in a second version by a registration phase. Before sending beacons, a beacon device must register itself to the system. This registration process is protected using the asymmetric authentication protocol ISO/IEC9798-3 extended by a public key infrastructure (PKI) and key exchange using elliptic-curve Diffie-Hellmann.

We show how beacon protection can be achieved and proposes to standardize a format for secure beacons.

---
Footnotes:
- (1) https://developers.google.com/beacons/eddystone-eid
- (2) https://support.kontakt.io/hc/en-gb/articles/206762009-Kontakt-io-Secure-Shuffeling
- (3) https://community.estimote.com/hc/en-us/articles/201371053

References:
- [1] Bernstein, D.J.: Curve25519: new diffie-hellman speed records. In: International Workshop on Public Key Cryptography. pp. 207-228. Springer (2006)
- [2] Schneier, B.: Applied Cryptography: Protocols, Algorithms, and Source Code in C. John Wiley & Sons (2007)
- [3] Tay, H.J., Tan, J., Narasimhan, P.: A survey of security vulnerabilities in bluetooth low energy beacons. Carnegie Mellon University Parallel Data Lab Technical Report CMU-PDL-16-109 (2016)

## Securing Software at Scale - The crazy world of modern application security programs ##
* Speaker: [Michael Helwig](#michael-helwig)
* Time:  15:40
* Length: 45 min
* Room: [Elbe](/2019/venue#elbe)

With agile development and DevOps on the rise, the speed of modern software development increases rapidly. Software has long become a vital part of many businesses (sometimes to their own surprise), but news about application related data breaches won't stop. Security teams in many organizations hardly managed to keep up with application security in a waterfall world, let alone during the now ongoing adoption of cloud and container based technologies with agile and independent DevOps teams. As application security is also gaining increasing attention from management, security teams need to react - but what to do when your resources are limited and the number of projects isn't? How can you build - and scale - your application security strategy in a large organization? Shift-Left and DevSecOps to the rescue, together with a chain of modern security tools like SAST, DAST, IAST and OSA. But can finding thousands of security bugs really help? And should you train your developers for security awareness - or just expand your application security team? (Spoiler: Better do both.)
This talk is a journey through bootstrapping application security programs in small organizations and large enterprises, the challenge of keeping management and development teams happy, while trying to (not make things worse) improve security - and a self-critical reflection on what worked well and what didn't.

## Continuous Security at the Next Level ##
* Speaker: [Martin Reinhardt](#martin-reinhardt)
* Time: 16:25
* Length: 45 min
* Room: [Elbe](/2019/venue#elbe)

Automated unit, integration and acceptance tests are essential quality controls in running a reliable continuous integration or continuous delivery pipeline. Too often, security tests are left out of this process because of the erroneous belief that security testing is solely the domain of leather-jacket-wearing security experts. The talk covers how easy it could be to integrate security aspects into a continuous delivery livecycle.

## Credential Stuffing Attacks! What is it and how you can protect your Web Application! ##
* Speaker: [Samy Makki](#samy-makki)
* Time:  17:10
* Length: 45 min
* Room: [Elbe](/2019/venue#elbe)

Every web application will see them on their site... Bots. But what are they doing? WebScraping, Content Aggregation, Credential Stuffing and DDoS Attacks are some examples of bad bot attacks. But there are also good bots like search engine bots, SEO and Marketing Bots and Partner Bots. So, how can we detect and mitigate them? Why is simply IP Blocking and Rate Limiting not working anymore?

In this talk I will especially talk about attacks targeting the login of a site. Learn about how a typical credential stuffing attack works and ways how to detect and mitigate them.

## When Your Biggest Threat is on Your Payroll: Drivers & Enablers of Insider Threat Activity ##
* Speaker: [Christina Lekati](#christina-lekati)
* Time: 14:35
* Length: 45 min
* Company: [Cyber Risk GmbH](https://www.cyber-risk-gmbh.com/)

It is often an irony in organizational security: Although so much capital is invested in the protection of the organizational assets against external threats, some of the largest compromises have instead occurred as a result of insider threats, sometimes resulting in irrecoverable damage. This type of threat carries an especially high-risk factor for organizations in the sector of critical infrastructure and industries where intellectual property and the protection of sensitive information are essential for the healthy continuation of their operations.

Employees in security-focused environments learn to treat outsiders with suspicion and to maintain trust boundaries. However, it is often the case that once an “outsider” enters the payroll of an organization they given a "carte blanche" in terms of trust and disclosure of information. They are now treated as the "insiders" that they are; members of the same tribe, fighting and working towards the same goals and using their skills to benefit their organization...until at some point one of them decides to use them differently. Or, until one of them realizes that the exploitation of organizational weaknesses would be a low-risk and high-reward activity.
This talk aims to shed some light on the threat of insider activity. It will discuss the motives that lead employees to insider activity, such as the unauthorized disclosure of sensitive information, process corruption, electronic sabotage, and/or the facilitation of third-party access to organizational assets. Research has repeatedly found a clear link between insider activity taking place and exploitable weaknesses in an organization’s security and management processes. Therefore, this talk will go on discussing the organizational factors enabling insider threat operations as well as countermeasures against them, by combining the lessons learned on insider activity prevention from the fields of counterintelligence, psychology, and cyber-security.

## A brief introduction to Digital Forensics ##

* Speaker: [Tim Eggert](#tim-eggert)
* Time: n/a (reserve talk)
* Length: 45m
* Room: [Elbe](/2019/venue#elbe)

In the last ten years cybercrime has evolved into a profitable business for the attackers, which led to more sophisticated attacks, new "underground business models" and a strong desire to collaborate to reach their goals.

Meanwhile the defenders struggle with the complexity of their own it-infrastructures, the processes and forget to share their knowledge about how to investigate in a case of an attack.

To help defenders to catch up with the attackers, this talk should shed some light on the basics of an investigative method called Digital Forensics, which is part of the overall approach called DFIR (Digital Forensics & Incident Response).

In short:

* A brief Introduction to Digital Forensics
* The talk is about the different phases/stages of a digital forensics and the tasks which will arise.
* It will also mention some real life problems during a digital forensic and approaches how to address them.


# Workshop descriptions #

## Elbsides vs. Juice Shop ##

* Speaker: [Björn Kimminich](#björn-kimminich)
* Time: 13:30-17:30
* Length: 4h
* Room: [Alster](/2019/venue#alster)

In this workshop you can test your skills in hacking modern
web applications against the OWASP Juice Shop! There are 85+
hacking challenges that are waiting to be solved, ranging from
simple functional problems and the usual XSS/SQLi issues over
severe authentication flaws up to multi-step and multi-path
attacks!

The workshop will consist of multiple short teasers to specific
vulnerabilities and lots of time for hacking! You can then stick
to the teasered topic or go into free-roaming mode and just try to
beat as many challenges as possible. Your pace is entirely up to
you! Some of the more mindboggling challenges can optionally be
tackled in a "swarm-hacking" style together on the big
screen. Over the entire duration of the training you can get
first-hand hints by the creator of the Juice Shop in case you get
stuck on any challenge.

Please bring the following prerequisites to this workshop:

* Laptop with OWASP Juice Shop already installed
* Your favorite Internet browser (obviously not IE)
* Some API testing app like PostMan (optional)
* Any pentesting toys and tools you like (optional)

## Bettercap: exploring the local network ##
* Speaker: [Christoph Eicke](#christoph-eicke)
* Time: 11:00
* Length: 2h
* Room: [Bille](/2019/venue#bille)

This workshop gives an introduction into doing MITM attacks on your local ethernet network. I will demonstrate how to direct all traffic in an ethernet switched network to your machine, analyze the traffic for certain patterns (e.g. URLs) and forward that traffic so that the victim machines do not notice your MITM attack.

All of this is done with the Bettercap tool, the better and more modern successor to ettercap. We will briefly look at a high level overview of the tool and then dive into a practical application by doing the above described MITM attack.

Please bring your own laptop to this workshop. We will be using a wired ethernet connection, so please make sure that you have an ethernet network port. I advise you to not use your personal or work laptop that emits information over the network, as we will be actively sniffing the network and spoofing connections! Maybe it is a good idea to boot from a live DVD or live USB thumbdrive for this workshop. Ubuntu or Debian preferred, but we can probably deal with any flavor of Unix.

## Introduction to Binary Reversing and Exploitation with radare2 ##
* Speaker: [Richard Sammet](#richard-sammet)
* Time: 13:50
* Length: 4h
* Room: [Bille](/2019/venue#bille)

Attendees will learn how to use radare2 in order to reverse engineer and exploit binary applications on Linux. This includes disassembling applications and working with the assembler for manipulation and patching, debugging applications and identifying vulnerabilities as well as crafting exploits.

Agenda:
- (80 minutes) Disassembling, reverse engineering and binary manipulation/patching
- 10 min break
- (80 minutes) Debugging and and exploiting vulnerable applications (memory corruption/manipulation, buffer overflows, execution flow manipulation as well as writing simple fuzzers with r2pipe and python)
- 10 min break
- (1 hour) Reverse engineering of a Linux malware (static, dynamic and using malware sandboxes) and identifying ways to contain and eradicate an infection globally

What attendees need to bring/know:
- A laptop with either Linux or a VM running your favorite Linux distribution (64 bit)
- A working docker (version  18+) environment in said Linux/VM
Working installation of the following tools:
- radare2, objdump, strings, strace, wireshark/tshark/tcpdump, python, your favorite web browser and text editor
- Basic experience with running/using Linux based systems and working on the shell/cli
- Basic experience with docker (what is a Dockerfile, how to build a container, how to run/stop it)
- Basic understanding of TCP/IP networking, basic understanding of HTTP/1.1
- Basic understanding of x86_64 assembler
- Basic scripting/programming experience in any language that can be used to automate basic tasks on Linux


## From source code to the final end - The way of an encryption trojan from attacker to your company ##
* Speakers: [Constantin Zankl ](#constantin-zankl), [Clemens Rambow](#clemens-rambow)
* Length: 2h
* Time: 11:00
* Room: [Alster](/2019/venue#alster)

Agenda

- General:
  - Functionality and targets of a ransomware attack
- Phase 1: Preparation
  - How do I create my own ransomware?
  - Where can I find suitable frameworks?
  - What adjustments are necessary and how complex are they?
  - What can the trojan do after the adjustments?
- Phase 2: The attack
  - Performing the attack via phishing email
  - Presentation of the attack from the victim's point of view
  - Presentation of the dissemination mechanism
- Phase 3: Analyses and countermeasures - Discussion
  - What can one do in such an attack?
  - Which log files should I evaluate?
  - Which immediate measures can help to contain the damage?
- Phase 4: Evaluation of the attack
  - What information does the attacker receive?

# Speakers #

## Paul Vixie ##

![Paul Vixie](/assets/2019/photos/Paul-Vixie.jpg)

* Company: [Farsight Security, Inc.](https://www.farsightsecurity.com)
* Twitter: [@paulvixie](https://twitter.com/paulvixie)

[Paul Vixie](https://en.wikipedia.org/wiki/Paul_Vixie) was responsible
for BIND from 1989 to 1999, and is the
author of a dozen or so IETF RFC documents about DNS. He also started
the first anti-spam company (MAPS) where he co-invented the DNS RBL
(Realtime Blackhole List) that now protects all e-mail planet-wide,
and was the founder and later president of the first U.S.-based
commercial Internet Exchange (PAIX). Today he serves as CEO of
Farsight Security, home of the Security Information Exchange
([SIE Europe UG](http://sie-europe.net/)) and
the world's leading Passive DNS database (DNSDB). He managed the
F-root DNS server from 1996 to 2012, and wrote the Cron software used
on all UNIX-type computers today. He is also co-inventor of the DNS
Response Rate Limiting (RRL) and Response Policy Zone (RPZ)
feature-sets now in wide use to protect the operational Internet
Domain Name System against online attacks. He received his Ph.D. from
Keio University in 2011, and was inducted into the Internet Hall of
Fame in 2014.

## Björn Kimminich ##
<img src="/assets/2019/photos/Bjoern-avatar.png" alt="Björn Kimminich" width="200" height="200"/>
* Workshop: [Elbsides vs. Juice Shop](#elbsides-vs-juice-shop)
* Company: [Kuehne + Nagel (AG & Co.) KG](https://kuehne-nagel.com/)
* GitHub: [github.com/bkimminich](https://github.com/bkimminich)
* Twitter: [@bkimminich](https://twitter.com/bkimminich)

Björn Kimminich is responsible for global IT architecture and application security at [Kuehne + Nagel](https://kuehne-nagel.com/). On the side, he gives IT security lectures at the non-profit private university [Nordakademie](https://www.nordakademie.de/). Björn also is the project leader of the [OWASP Juice Shop](http://owasp-juice.shop/) and a board member for the [German OWASP chapter](https://www.owasp.org/index.php/Germany).

## Christoph Eicke ##
<img src="/assets/2019/photos/christoph-eicke.jpg" alt="Christoph Eicke" width="200" height="200"/>
* Workshop: [Bettercap: exploring the local network](#bettercap-exploring-the-local-network)
* Company: [XING SE](https://www.xing.com)

## Richard Sammet ##
<img src="/assets/2019/photos/richard-sammet.jpg" alt="Richard Sammet" width="200" height="200"/>

* Workshop: [Introduction to Binary Reversing and Exploitation with radare2](#introduction-to-binary-reversing-and-exploitation-with-radare2)
* Website: [mytty.org/about/](https://mytty.org/about/)
* Twitter: [@RichardSammet](https://twitter.com/RichardSammet)

Hey there, I’m Richard. I’m busy disassembling technology and software since 1991. Around 1995 I started with what most of you would call “hacking”. And since 2003 I’m working in information, IT and cyber security. I’ve been working in security R&D, as a consultant, consulting (senior-) manager, team lead, head of cyber/information security and director of cyber/information security. All the way from Germany, over Reykjavik (Iceland) to London (UK).

## Constantin Zankl  ##
* Workshop: [From source code to the final end - The way of an encryption trojan from attacker to your company](#from-source-code-to-the-final-end---the-way-of-an-encryption-trojan-from-attacker-to-your-company)
* Company: [Allgeier CORE GmbH](https://www.allgeier-core.com/)

## Clemens Rambow ##
* Workshop: [From source code to the final end - The way of an encryption trojan from attacker to your company](#from-source-code-to-the-final-end---the-way-of-an-encryption-trojan-from-attacker-to-your-company)
* Company: [Allgeier CORE GmbH](https://www.allgeier-core.com/)

## Ole Michaelis ##
<img src="/assets/2019/photos/ole-michaelis.jpg" alt="Ole Michaelis" width="200" height="200"/>

* Talk: [DNS privacy and how DNS-over-HTTPS may fix it](#dns-privacy-and-how-dns-over-https-may-fix-it)
* Time: 10:10
* Company: [DNSimple](https://dnsimple.com)
* Website: [ole.mchls.works](http://ole.mchls.works)
* Twitter: [@OleMchls](https://twitter.com/OleMchls)
* Github: [github.com/olemchls](https://github.com/olemchls)

## Katharine Jarmul ##
<img src="/assets/2019/photos/katharine-jarmul.jpg" alt="Katharine Jarmul" width="200" height="200"/>
* Talk: [Privacy Attacks Against Machine Learning Systems](#privacy-attacks-against-machine-learning-systems)
* Time: 11:15
* Company: [Kjamistan](https://kjamistan.com/)
* Country: Germany
* Twitter: [@kjam](https://twitter.com/kjam)

Katharine Jarmul has been working with computers and code since her early years, and is passionate about spreading knowledge on tools used in the open source community. She works with Python daily since 2008 and has a background in C++ and Java. Her exposure to board activities and funding at several start ups gives her a business-minded approach to technical problem solving -- introducing practical solutions and keeping business-interests first.

## Erik Sy ##
* Talk: [Improving the Performance and Privacy of TCP Fast Open, TLS 1.3, and QUIC](#improving-the-performance-and-privacy-of-tcp-fast-open-tls-13-and-quic)
* Time: 12:00
* Organization: [University of Hamburg](https://www.uni-hamburg.de)
* Country: Germany

## Luca Nagy ##
<img src="/assets/2019/photos/luca-nagy.jpg" alt="Luca Nagy" width="200" height="200"/>
* Talk: [Exploring Emotet, an Elaborate Everyday Enigma](#exploring-emotet-an-elaborate-everyday-enigma)
* Time: 12:25
* Company: Sophos
* Country: Hungary
* Twitter: [@luca_nagy_](https://twitter.com/luca_nagy_)

## Christoph Peglow ##
* Talk: [Defending BLE Beacon Applications Against Common Attacks](#defending-ble-beacon-applications-against-common-attacks)
* Time: 13:50
* Organization: [University of Lübeck](https://www.uni-luebeck.de)
* Country: Germany

## Malte Stoffers ##
* Talk: [Defending BLE Beacon Applications Against Common Attacks](#defending-ble-beacon-applications-against-common-attacks)
* Time: 13:50
* Organization: [University of Lübeck](https://www.uni-luebeck.de)
* Country: Germany

## Thore Tiemann ##
* Talk: [Defending BLE Beacon Applications Against Common Attacks](#defending-ble-beacon-applications-against-common-attacks)
* Time: 13:50
* Organization: [University of Lübeck](https://www.uni-luebeck.de)
* Country: Germany

## Michael Helwig ##
<img src="/assets/2019/photos/michael-helwig.jpg" alt="Michael Helwig" width="200" height="200"/>
* Time: 15:40
* Talk: [Securing Software at Scale - The crazy world of modern application security programs](#securing-software-at-scale---the-crazy-world-of-modern-application-security-programs)
* Company: [Codemetrix GmbH](https://www.codemetrix.io/)
* Country: Germany
* Twitter: [@c0dmtr1x](https://twitter.com/c0dmtr1x)

## Martin Reinhardt ##

<img src="/assets/2019/photos/martin-reinhardt.jpg" alt="Martin Reinhardt" width="200" height="200"/>
* Title: Ambassador of Software Craftsmanship and Secure {Code} Catalyst
* Time: 16:25
* Talk: [Continuous Security at the Next Level](#continuous-security-at-the-next-level)
* Twitter: [@mreinhardt](https://twitter.com/mreinhardt)

Martin Reinhardt is working as architect at Holisticon AG, a management and IT consulting company. He is in charge for the architecture of complex distributed systems, modern web architectures and build management. Martin is involved in the software-craftsmanship movement. He has been active in the field of Java and web development for several years. In addition, he is primarily involved in automation in various technologies, JavaScript projects and is also several OpenSource projects.

## Samy Makki ##

<img src="/assets/2019/photos/samy-makki.jpg" alt="Samy Makki" width="200" height="200"/>

* Talk: [Credential Stuffing Attacks! What is it and how you can protect your Web Application!](#credential-stuffing-attacks-what-is-it-and-how-you-can-protect-your-web-application)
* Time: 17:10
* Company: Akamai
* Country: Germany
* Twitter: [@SamyMakki](https://twitter.com/SamyMakki)

## Christina Lekati ##

<img src="/assets/2019/photos/christina-lekati.jpg" alt="Christina Lekati" width="200" height="200"/>

* Talk: [When Your Biggest Threat is on Your Payroll: Drivers & Enablers of Insider Threat Activity](#when-your-biggest-threat-is-on-your-payroll-drivers--enablers-of-insider-threat-activity)
* Time: 14:35
* Company: [Cyber Risk GmbH](https://www.cyber-risk-gmbh.com/)
* Country: Switzerland
* Twitter: [@ChristinaLekati](https://twitter.com/ChristinaLekati)

Christina Lekati is a psychologist and a social engineer.

With her background and degree in psychology, she learned the mechanisms of behavior, motivation, decision making, as well as manipulation and deceit. She became particularly interested in human dynamics and passionate about social engineering.

She pursued later a master’s degree in International Business. True to her passion, her thesis on social engineering strategies earned her a distinction during her master studies.

Contrary to typical career paths, her history and involvement in the cybersecurity field started quite early in her life. Being raised by George Lekatis, a sought-after cyber security expert, she found herself magnetized by the security field at a very young age. Growing up, she was able to get involved in different projects that were often beyond her age, that gave her an edge in her own knowledge and experience.

Christina has participated among other things in penetration tests, in training to companies and organizations, and in needs and vulnerability assessments.

She is working with Cyber Risk GmbH as a social engineering expert and trainer.

Christina is the main developer of the social engineering training programs provided by Cyber Risk GmbH. Those programs are intertwining the lessons learned from real life cases and previous experiences with the fields of cybersecurity, psychology and counterintelligence. They often cover unique aspects while their main goal is to inspire delegates with a sense of responsibility and a better relationship with security.

Being committed to sharing knowledge and expertise, Christina is also a speaker. She participates in a variety of cyber security events, raising awareness and educating people on social engineering techniques and the psychological elements involved in human hacking.

## Tim Eggert ##

* Talk: [A brief introduction to Digital Forensics](#a-brief-introduction-to-digital-forensics) (Reserve talk)
* Company: Otto Group
* Role: Principal Cybercrime Investigator
* Country: Germany
* Twitter: [@min0r_changes](https://twitter.com/min0r_changes)

After studying informatics at the University of Lübeck, I spent many years in the working fields of DFIR (Digital Forensics & Incident Response), Cyber Threat Intelligence, Penetration Testing, Malware Analysis and Information Security. I am always keen on learning something new and gladly share my knowledge about security topics. That‘s why i also dedicate a part of my working time to teach people about DFIR.
