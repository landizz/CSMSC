# CSMSC
Cisco SMS Configuration

Missing internet access when you quickly need to configure or shut down your network during an attack can be a big problem, since all remote access normally takes place via SSH and VPN over WAN. This application deals with a method of providing secure access to a local network by sending commands or inquiries via text message over the GSM network to thereby extend the scope of remote access in cases where IP communication is not available.

This current implementation is using HTTPS to communicate with a GSM gateway provider, the application can easily be modified to be used with a local GSM gateway so that the application truly is free of IP communication over WAN.

We have built a solution that is easy to set up and that does not require any major financial investments.

TL;DR:
A python application for configuring network units over GSM network.
