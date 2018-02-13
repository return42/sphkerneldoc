.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/sfc/falcon/rx.c

.. _`ef4_init_rx_buffers`:

ef4_init_rx_buffers
===================

.. c:function:: int ef4_init_rx_buffers(struct ef4_rx_queue *rx_queue, bool atomic)

    create EF4_RX_BATCH page-based RX buffers

    :param struct ef4_rx_queue \*rx_queue:
        Efx RX queue

    :param bool atomic:
        *undescribed*

.. _`ef4_init_rx_buffers.description`:

Description
-----------

This allocates a batch of pages, maps them for DMA, and populates
struct ef4_rx_buffers for each one. Return a negative error code or
0 on success. If a single page can be used for multiple buffers,
then the page will either be inserted fully, or not at all.

.. _`ef4_fast_push_rx_descriptors`:

ef4_fast_push_rx_descriptors
============================

.. c:function:: void ef4_fast_push_rx_descriptors(struct ef4_rx_queue *rx_queue, bool atomic)

    push new RX descriptors quickly

    :param struct ef4_rx_queue \*rx_queue:
        RX descriptor queue

    :param bool atomic:
        *undescribed*

.. _`ef4_fast_push_rx_descriptors.description`:

Description
-----------

This will aim to fill the RX descriptor queue up to
\ ``rx_queue``\ ->@max_fill. If there is insufficient atomic
memory to do so, a slow fill will be scheduled.

The caller must provide serialisation (none is used here). In practise,
this means this function must run from the NAPI handler, or be called
when NAPI is disabled.

.. _`ef4_filter_is_mc_recipient`:

ef4_filter_is_mc_recipient
==========================

.. c:function:: bool ef4_filter_is_mc_recipient(const struct ef4_filter_spec *spec)

    test whether spec is a multicast recipient

    :param const struct ef4_filter_spec \*spec:
        Specification to test

.. _`ef4_filter_is_mc_recipient.return`:

Return
------

\ ``true``\  if the specification is a non-drop RX filter that
matches a local MAC address I/G bit value of 1 or matches a local
IPv4 or IPv6 address value in the respective multicast address
range.  Otherwise \ ``false``\ .

.. This file was automatic generated / don't edit.

