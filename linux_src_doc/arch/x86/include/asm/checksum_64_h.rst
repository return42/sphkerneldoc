.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/include/asm/checksum_64.h

.. _`csum_fold`:

csum_fold
=========

.. c:function:: __sum16 csum_fold(__wsum sum)

    Fold and invert a 32bit checksum.

    :param sum:
        *undescribed*
    :type sum: __wsum

.. _`csum_fold.sum`:

sum
---

32bit unfolded sum

Fold a 32bit running checksum to 16bit and invert it. This is usually
the last step before putting a checksum into a packet.
Make sure not to mix with 64bit checksums.

.. _`ip_fast_csum`:

ip_fast_csum
============

.. c:function:: __sum16 ip_fast_csum(const void *iph, unsigned int ihl)

    Compute the IPv4 header checksum efficiently.

    :param iph:
        *undescribed*
    :type iph: const void \*

    :param ihl:
        *undescribed*
    :type ihl: unsigned int

.. _`ip_fast_csum.iph`:

iph
---

ipv4 header

.. _`ip_fast_csum.ihl`:

ihl
---

length of header / 4

.. _`csum_tcpudp_nofold`:

csum_tcpudp_nofold
==================

.. c:function:: __wsum csum_tcpudp_nofold(__be32 saddr, __be32 daddr, __u32 len, __u8 proto, __wsum sum)

    Compute an IPv4 pseudo header checksum.

    :param saddr:
        source address
    :type saddr: __be32

    :param daddr:
        destination address
    :type daddr: __be32

    :param len:
        length of packet
    :type len: __u32

    :param proto:
        ip protocol of packet
    :type proto: __u8

    :param sum:
        initial sum to be added in (32bit unfolded)
    :type sum: __wsum

.. _`csum_tcpudp_nofold.description`:

Description
-----------

Returns the pseudo header checksum the input data. Result is
32bit unfolded.

.. _`csum_tcpudp_magic`:

csum_tcpudp_magic
=================

.. c:function:: __sum16 csum_tcpudp_magic(__be32 saddr, __be32 daddr, __u32 len, __u8 proto, __wsum sum)

    Compute an IPv4 pseudo header checksum.

    :param saddr:
        source address
    :type saddr: __be32

    :param daddr:
        destination address
    :type daddr: __be32

    :param len:
        length of packet
    :type len: __u32

    :param proto:
        ip protocol of packet
    :type proto: __u8

    :param sum:
        initial sum to be added in (32bit unfolded)
    :type sum: __wsum

.. _`csum_tcpudp_magic.description`:

Description
-----------

Returns the 16bit pseudo header checksum the input data already
complemented and ready to be filled in.

.. _`csum_partial`:

csum_partial
============

.. c:function:: __wsum csum_partial(const void *buff, int len, __wsum sum)

    Compute an internet checksum.

    :param buff:
        buffer to be checksummed
    :type buff: const void \*

    :param len:
        length of buffer.
    :type len: int

    :param sum:
        initial sum to be added in (32bit unfolded)
    :type sum: __wsum

.. _`csum_partial.description`:

Description
-----------

Returns the 32bit unfolded internet checksum of the buffer.
Before filling it in it needs to be \ :c:func:`csum_fold`\ 'ed.
buff should be aligned to a 64bit boundary if possible.

.. _`ip_compute_csum`:

ip_compute_csum
===============

.. c:function:: __sum16 ip_compute_csum(const void *buff, int len)

    Compute an 16bit IP checksum.

    :param buff:
        buffer address.
    :type buff: const void \*

    :param len:
        length of buffer.
    :type len: int

.. _`ip_compute_csum.description`:

Description
-----------

Returns the 16bit folded/inverted checksum of the passed buffer.
Ready to fill in.

.. This file was automatic generated / don't edit.

