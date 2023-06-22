---
layout: page
permalink: /2021/programm/timpanton/
---

<iframe width="560" height="315" src="https://www.youtube.com/embed/AiIfgyZP05o" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# Speaker

Tim Panton

# Abstract

This talk describes the process of designing and building a secure remote access device which can be plugged into servers and other devices, using off the shelf hobby hardware. We will cover:

- Why use an external device rather than known software like VNC. What is the risk/benefit from a security point of view?
- Emulating a keyboard and mouse with a Raspberry pi. (This may be of interest to Red Teamers!)
- Capturing realtime hdmi graphics cheaply.
- Novel access control using a self signed PKI and Trust on first use (we will cover both initial pairing and subsequent lend/borrow transactions)
- Secure access to the device from a browser via webRTC (We will discuss the trade offs in using a browser as an access method vs a dedicated app/protocol) We will describe the limited network exposure of the device (How we keep no open ports, how we can ignore unauthorised traffic) We will discuss the design and implementation of the software and the steps taken to improve its security such as programming language choice, risky idioms we avoided and supply chain dependency risk minimisation.
The talk will have some thing for everyone, red teamers, blue teamers, network security folks and software developers can all learn from our experience in building this device because security had to be considered in every layer of the process.

# Speaker information

Tim Panton

[@steely_glint](https://twitter.com/steely_glint)

Tim is a software developer with a keen interest in security. Many years ago he founded an internet security business, then got distracted by VoIP for a few years. Recently he’s combined the two and has built a secure software stack for cameras and other IoT devices based on a proprietary implementation of the webRTC standard and patented authentication methods. (which he mis-used to host robot football games in his living room during lockdown).

He’s a frequent speaker at IoT, WebRTC and security events. He’s a fan of B-sides as a great place to learn about the world of computer security.
