.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/md/raid5.c

.. _`scribble_alloc`:

scribble_alloc
==============

.. c:function:: struct flex_array *scribble_alloc(int num, int cnt, gfp_t flags)

    return the required size of the scribble region \ ``num``\  - total number of disks in the array

    :param int num:
        *undescribed*

    :param int cnt:
        *undescribed*

    :param gfp_t flags:
        *undescribed*

.. _`scribble_alloc.the-size-must-be-enough-to-contain`:

The size must be enough to contain
----------------------------------

1/ a struct page pointer for each device in the array +2
2/ room to convert each entry in (1) to its corresponding dma
(\ :c:func:`dma_map_page`\ ) or page (\ :c:func:`page_address`\ ) address.

.. _`scribble_alloc.note`:

Note
----

the +2 is for the destination buffers of the ddf/raid6 case where we
calculate over all devices (not just the data blocks), using zeros in place
of the P and Q blocks.

.. _`handle_stripe_fill`:

handle_stripe_fill
==================

.. c:function:: void handle_stripe_fill(struct stripe_head *sh, struct stripe_head_state *s, int disks)

    read or compute data to satisfy pending requests.

    :param struct stripe_head \*sh:
        *undescribed*

    :param struct stripe_head_state \*s:
        *undescribed*

    :param int disks:
        *undescribed*

.. This file was automatic generated / don't edit.

