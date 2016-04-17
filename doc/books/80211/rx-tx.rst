
.. _rx-tx:

===============================
Receive and transmit processing
===============================


what should be here
===================

TBD

This should describe the receive and transmit paths in mac80211/the drivers as well as transmit status handling.


Frame format
============

As a general rule, when frames are passed between mac80211 and the driver, they start with the IEEE 802.11 header and include the same octets that are sent over the air except for
the FCS which should be calculated by the hardware.

There are, however, various exceptions to this rule for advanced features:

The first exception is for hardware encryption and decryption offload where the IV/ICV may or may not be generated in hardware.

Secondly, when the hardware handles fragmentation, the frame handed to the driver from mac80211 is the MSDU, not the MPDU.


Packet alignment
================

Drivers always need to pass packets that are aligned to two-byte boundaries to the stack.

Additionally, should, if possible, align the payload data in a way that guarantees that the contained IP header is aligned to a four-byte boundary. In the case of regular frames,
this simply means aligning the payload to a four-byte boundary (because either the IP header is directly contained, or IV/RFC1042 headers that have a length divisible by four are
in front of it). If the payload data is not properly aligned and the architecture doesn't support efficient unaligned operations, mac80211 will align the data.

With A-MSDU frames, however, the payload data address must yield two modulo four because there are 14-byte 802.3 headers within the A-MSDU frames that push the IP header further
back to a multiple of four again. Thankfully, the specs were sane enough this time around to require padding each A-MSDU subframe to a length that is a multiple of four.

Padding like Atheros hardware adds which is between the 802.11 header and the payload is not supported, the driver is required to move the 802.11 header to be directly in front of
the payload in that case.


Calling into mac80211 from interrupts
=====================================

Only ``ieee80211_tx_status_irqsafe`` and ``ieee80211_rx_irqsafe`` can be called in hardware interrupt context. The low-level driver must not call any other functions in hardware
interrupt context. If there is a need for such call, the low-level driver should first ACK the interrupt and perform the IEEE 802.11 code call after this, e.g. from a scheduled
workqueue or even tasklet function.

NOTE: If the driver opts to use the ``_irqsafe`` functions, it may not also use the non-IRQ-safe functions!


functions/definitions
=====================


.. toctree::
    :maxdepth: 1

    API-struct-ieee80211-rx-status
    API-enum-mac80211-rx-flags
    API-enum-mac80211-tx-info-flags
    API-enum-mac80211-tx-control-flags
    API-enum-mac80211-rate-control-flags
    API-struct-ieee80211-tx-rate
    API-struct-ieee80211-tx-info
    API-ieee80211-tx-info-clear-status
    API-ieee80211-rx
    API-ieee80211-rx-ni
    API-ieee80211-rx-irqsafe
    API-ieee80211-tx-status
    API-ieee80211-tx-status-ni
    API-ieee80211-tx-status-irqsafe
    API-ieee80211-rts-get
    API-ieee80211-rts-duration
    API-ieee80211-ctstoself-get
    API-ieee80211-ctstoself-duration
    API-ieee80211-generic-frame-duration
    API-ieee80211-wake-queue
    API-ieee80211-stop-queue
    API-ieee80211-wake-queues
    API-ieee80211-stop-queues
    API-ieee80211-queue-stopped
