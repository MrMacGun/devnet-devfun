#! /usr/bin/env python
"""
Learning Series: Network Programmability Basics
Author: Hank Preston <hapresto@cisco.com>

device_info.py
Illustrate the following concepts:
- Store device info for Sandbox Infrastructure used 
  in examples
"""


# DevNet Always-On IOS XE on CSR Recommended Code Sandbox Device
# https://devnetsandbox.cisco.com/RM/Diagram/Index/27d9747a-db48-4565-8d44-df318fce37ad?diagramType=Topology
ios_xe1 = {
             "address": "devnetsandboxiosxec9k.cisco.com",
             "port": 830,
             "username": "mflow43",
             "password": "X6Lt3-s3z_Sce"
           }

# DevNet Always-On IOS XE on CSR Latest Code Sandbox Device
# https://devnetsandbox.cisco.com/RM/Diagram/Index/38ded1f0-16ce-43f2-8df5-43a40ebf752e?diagramType=Topology
ios_xe_latest = {
             "address": "devnetsandboxiosxec9k.cisco.com",
             "port": 830,
             "username": "mflow43",
             "password": "X6Lt3-s3z_Sce"
          }          

# DevNet IOS XE Programmability Sandbox Device
# https://devnetsandbox.cisco.com/RM/Diagram/Index/cae403c2-27af-4c7d-b1e1-99b7d42f1504?diagramType=Topology
ios_xe2 = {
             "address": "devnetsandboxiosxec9k.cisco.com",
             "port": 830,
             "username": "mflow43",
             "password": "X6Lt3-s3z_Sce"
          }


# DevNet Always-On Sandbox APIC-EM
# https://devnetsandbox.cisco.com/RM/Diagram/Index/2e0f9525-5f46-4f46-973e-0f0c1bf934fa?diagramType=Topology
apicem = {
             "host": "devnetsandboxiosxec9k.cisco.com",
             "username": "mflow43",
             "password": "X6Lt3-s3z_Sce",
             "port": 443
         }

# DevNet Always-On Sandbox ACI APIC
# https://devnetsandbox.cisco.com/RM/Diagram/Index/5a229a7c-95d5-4cfd-a651-5ee9bc1b30e2?diagramType=Topology
apic = {
             "host": "devnetsandboxiosxec9k.cisco.com",
             "username": "mflow43",
             "password": "X6Lt3-s3z_Sce",
             "port": 443
         }