.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/um/asm/checksum.h

.. _`csum_fold`:

csum_fold
=========

.. c:function:: __sum16 csum_fold(__wsum sum)

    Fold and invert a 32bit checksum.

    :param __wsum sum:
        *undescribed*

.. _`csum_fold.sum`:

sum
---

32bit unfolded sum

Fold a 32bit running checksum to 16bit and invert it. This is usually
the last step before putting a checksum into a packet.
Make sure not to mix with 64bit checksums.

.. _`csum_tcpudp_nofold`:

csum_tcpudp_nofold
==================

.. c:function:: __wsum csum_tcpudp_nofold(__be32 saddr, __be32 daddr, __u32 len, __u8 proto, __wsum sum)

    Compute an IPv4 pseudo header checksum.

    :param __be32 saddr:
        source address

    :param __be32 daddr:
        destination address

    :param __u32 len:
        length of packet

    :param __u8 proto:
        ip protocol of packet

    :param __wsum sum:
        initial sum to be added in (32bit unfolded)

.. _`csum_tcpudp_nofold.description`:

Description
-----------

Returns the pseudo header checksum the input data. Result is
32bit unfolded.

.. _`ip_fast_csum`:

ip_fast_csum
============

.. c:function:: __sum16 ip_fast_csum(const void *iph, unsigned int ihl)

    Compute the IPv4 header checksum efficiently.

    :param const void \*iph:
        *undescribed*

    :param unsigned int ihl:
        *undescribed*

.. _`ip_fast_csum.iph`:

iph
---

ipv4 header

.. _`ip_fast_csum.ihl`:

ihl
---

length of header / 4

.. This file was automatic generated / don't edit.

