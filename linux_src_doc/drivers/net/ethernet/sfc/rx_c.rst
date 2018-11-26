.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/sfc/rx.c

.. _`efx_init_rx_buffers`:

efx_init_rx_buffers
===================

.. c:function:: int efx_init_rx_buffers(struct efx_rx_queue *rx_queue, bool atomic)

    create EFX_RX_BATCH page-based RX buffers

    :param rx_queue:
        Efx RX queue
    :type rx_queue: struct efx_rx_queue \*

    :param atomic:
        *undescribed*
    :type atomic: bool

.. _`efx_init_rx_buffers.description`:

Description
-----------

This allocates a batch of pages, maps them for DMA, and populates
struct efx_rx_buffers for each one. Return a negative error code or
0 on success. If a single page can be used for multiple buffers,
then the page will either be inserted fully, or not at all.

.. _`efx_fast_push_rx_descriptors`:

efx_fast_push_rx_descriptors
============================

.. c:function:: void efx_fast_push_rx_descriptors(struct efx_rx_queue *rx_queue, bool atomic)

    push new RX descriptors quickly

    :param rx_queue:
        RX descriptor queue
    :type rx_queue: struct efx_rx_queue \*

    :param atomic:
        *undescribed*
    :type atomic: bool

.. _`efx_fast_push_rx_descriptors.description`:

Description
-----------

This will aim to fill the RX descriptor queue up to
\ ``rx_queue``\ ->@max_fill. If there is insufficient atomic
memory to do so, a slow fill will be scheduled.

The caller must provide serialisation (none is used here). In practise,
this means this function must run from the NAPI handler, or be called
when NAPI is disabled.

.. _`efx_filter_is_mc_recipient`:

efx_filter_is_mc_recipient
==========================

.. c:function:: bool efx_filter_is_mc_recipient(const struct efx_filter_spec *spec)

    test whether spec is a multicast recipient

    :param spec:
        Specification to test
    :type spec: const struct efx_filter_spec \*

.. _`efx_filter_is_mc_recipient.return`:

Return
------

\ ``true``\  if the specification is a non-drop RX filter that
matches a local MAC address I/G bit value of 1 or matches a local
IPv4 or IPv6 address value in the respective multicast address
range.  Otherwise \ ``false``\ .

.. This file was automatic generated / don't edit.

