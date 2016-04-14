.. -*- coding: utf-8; mode: rst -*-

====
rx.c
====

.. _`packet-alignment`:

Packet alignment
================

Drivers always need to pass packets that are aligned to two-byte boundaries
to the stack.

Additionally, should, if possible, align the payload data in a way that
guarantees that the contained IP header is aligned to a four-byte
boundary. In the case of regular frames, this simply means aligning the
payload to a four-byte boundary (because either the IP header is directly
contained, or IV/RFC1042 headers that have a length divisible by four are
in front of it).  If the payload data is not properly aligned and the
architecture doesn't support efficient unaligned operations, mac80211
will align the data.

With A-MSDU frames, however, the payload data address must yield two modulo
four because there are 14-byte 802.3 headers within the A-MSDU frames that
push the IP header further back to a multiple of four again. Thankfully, the
specs were sane enough this time around to require padding each A-MSDU
subframe to a length that is a multiple of four.

Padding like Atheros hardware adds which is between the 802.11 header and
the payload is not supported, the driver is required to move the 802.11
header to be directly in front of the payload in that case.

