import curses

def all_in_one_preview():
    return f"""
               ALL IN ONE                                          


    ARP  -->   IP  -->   PORT  -->  MAP                                
   SWEEP     Sweep      SCANNER    NETWORK                          
                                                                   
     │          │          │          │                         
     v          v          v          v                           
   HOSTS      ALIVE      PORTS     TOPOLOGY                         
"""

def arp_sweep_preview():
    return f"""
               ARP SWEEP
               
               
   Protocol  : ARP (RFC 826)
   Scope     : Local L2 broadcast domain
   Method    : ARP probe per host; reply = alive
   Output    : IP–MAC table
   Note      : Unaffected by ICMP filtering

"""
def ip_sweep_preview():
    return f"""
               IP SWEEP


   Protocol  : ICMP Echo / TCP SYN
   Scope     : Target subnet (e.g. 192.168.1.0/24)
   Method    : Ping sweep; response = alive
   Output    : List of live IPs
   Note      : Fallback to TCP 443 if ICMP filtered
"""

def port_scanner_preview():
    return f"""
               PORT SCANNER


   Protocol  : TCP SYN / Connect
   Scope     : Live hosts from previous stage
   Method    : Sequential or threaded port scan
   Output    : Open ports + service fingerprint
   Note      : Top 1000 / full 65535 / custom range
"""

def network_map_preview():
    return f"""
               NETWORK MAP


   Input     : Hosts, ports, services from pipeline
   Scope     : Full topology view
   Method    : Graph rendering (ASCII / TUI)
   Output    : Nodes = hosts, Edges = connections
   Note      : Shows gateway, subnets, services at a glance
"""

#def Bootingscreen():
    #return f"""                   
    