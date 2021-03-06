.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iommu/iova.c

.. _`alloc_iova`:

alloc_iova
==========

.. c:function:: struct iova *alloc_iova(struct iova_domain *iovad, unsigned long size, unsigned long limit_pfn, bool size_aligned)

    allocates an iova

    :param iovad:
        - iova domain in question
    :type iovad: struct iova_domain \*

    :param size:
        - size of page frames to allocate
    :type size: unsigned long

    :param limit_pfn:
        - max limit address
    :type limit_pfn: unsigned long

    :param size_aligned:
        - set if size_aligned address range is required
        This function allocates an iova in the range iovad->start_pfn to limit_pfn,
        searching top-down from limit_pfn to iovad->start_pfn. If the size_aligned
        flag is set then the allocated address iova->pfn_lo will be naturally
        aligned on roundup_power_of_two(size).
    :type size_aligned: bool

.. _`find_iova`:

find_iova
=========

.. c:function:: struct iova *find_iova(struct iova_domain *iovad, unsigned long pfn)

    finds an iova for a given pfn

    :param iovad:
        - iova domain in question.
    :type iovad: struct iova_domain \*

    :param pfn:
        - page frame number
        This function finds and returns an iova belonging to the
        given doamin which matches the given pfn.
    :type pfn: unsigned long

.. _`__free_iova`:

\__free_iova
============

.. c:function:: void __free_iova(struct iova_domain *iovad, struct iova *iova)

    frees the given iova

    :param iovad:
        iova domain in question.
    :type iovad: struct iova_domain \*

    :param iova:
        iova in question.
        Frees the given iova belonging to the giving domain
    :type iova: struct iova \*

.. _`free_iova`:

free_iova
=========

.. c:function:: void free_iova(struct iova_domain *iovad, unsigned long pfn)

    finds and frees the iova for a given pfn

    :param iovad:
        - iova domain in question.
    :type iovad: struct iova_domain \*

    :param pfn:
        - pfn that is allocated previously
        This functions finds an iova for a given pfn and then
        frees the iova from that domain.
    :type pfn: unsigned long

.. _`alloc_iova_fast`:

alloc_iova_fast
===============

.. c:function:: unsigned long alloc_iova_fast(struct iova_domain *iovad, unsigned long size, unsigned long limit_pfn, bool flush_rcache)

    allocates an iova from rcache

    :param iovad:
        - iova domain in question
    :type iovad: struct iova_domain \*

    :param size:
        - size of page frames to allocate
    :type size: unsigned long

    :param limit_pfn:
        - max limit address
    :type limit_pfn: unsigned long

    :param flush_rcache:
        - set to flush rcache on regular allocation failure
        This function tries to satisfy an iova allocation from the rcache,
        and falls back to regular allocation on failure. If regular allocation
        fails too and the flush_rcache flag is set then the rcache will be flushed.
    :type flush_rcache: bool

.. _`free_iova_fast`:

free_iova_fast
==============

.. c:function:: void free_iova_fast(struct iova_domain *iovad, unsigned long pfn, unsigned long size)

    free iova pfn range into rcache

    :param iovad:
        - iova domain in question.
    :type iovad: struct iova_domain \*

    :param pfn:
        - pfn that is allocated previously
    :type pfn: unsigned long

    :param size:
        - # of pages in range
        This functions frees an iova range by trying to put it into the rcache,
        falling back to regular iova deallocation via \ :c:func:`free_iova`\  if this fails.
    :type size: unsigned long

.. _`put_iova_domain`:

put_iova_domain
===============

.. c:function:: void put_iova_domain(struct iova_domain *iovad)

    destroys the iova doamin

    :param iovad:
        - iova domain in question.
        All the iova's in that domain are destroyed.
    :type iovad: struct iova_domain \*

.. _`reserve_iova`:

reserve_iova
============

.. c:function:: struct iova *reserve_iova(struct iova_domain *iovad, unsigned long pfn_lo, unsigned long pfn_hi)

    reserves an iova in the given range

    :param iovad:
        - iova domain pointer
    :type iovad: struct iova_domain \*

    :param pfn_lo:
        - lower page frame address
    :type pfn_lo: unsigned long

    :param pfn_hi:
        - higher pfn adderss
        This function allocates reserves the address range from pfn_lo to pfn_hi so
        that this address is not dished out as part of alloc_iova.
    :type pfn_hi: unsigned long

.. _`copy_reserved_iova`:

copy_reserved_iova
==================

.. c:function:: void copy_reserved_iova(struct iova_domain *from, struct iova_domain *to)

    copies the reserved between domains

    :param from:
        - source doamin from where to copy
    :type from: struct iova_domain \*

    :param to:
        - destination domin where to copy
        This function copies reserved iova's from one doamin to
        other.
    :type to: struct iova_domain \*

.. This file was automatic generated / don't edit.

