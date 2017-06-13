.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/fm10k/fm10k_main.c

.. _`fm10k_init_module`:

fm10k_init_module
=================

.. c:function:: int fm10k_init_module( void)

    Driver Registration Routine

    :param  void:
        no arguments

.. _`fm10k_init_module.description`:

Description
-----------

fm10k_init_module is the first routine called when the driver is
loaded.  All it does is register with the PCI subsystem.

.. _`fm10k_exit_module`:

fm10k_exit_module
=================

.. c:function:: void __exit fm10k_exit_module( void)

    Driver Exit Cleanup Routine

    :param  void:
        no arguments

.. _`fm10k_exit_module.description`:

Description
-----------

fm10k_exit_module is called just before the driver is removed
from memory.

.. _`fm10k_alloc_rx_buffers`:

fm10k_alloc_rx_buffers
======================

.. c:function:: void fm10k_alloc_rx_buffers(struct fm10k_ring *rx_ring, u16 cleaned_count)

    Replace used receive buffers

    :param struct fm10k_ring \*rx_ring:
        ring to place buffers on

    :param u16 cleaned_count:
        number of buffers to replace

.. _`fm10k_reuse_rx_page`:

fm10k_reuse_rx_page
===================

.. c:function:: void fm10k_reuse_rx_page(struct fm10k_ring *rx_ring, struct fm10k_rx_buffer *old_buff)

    page flip buffer and store it back on the ring

    :param struct fm10k_ring \*rx_ring:
        rx descriptor ring to store buffers on

    :param struct fm10k_rx_buffer \*old_buff:
        donor buffer to have page reused

.. _`fm10k_reuse_rx_page.description`:

Description
-----------

Synchronizes page for reuse by the interface

.. _`fm10k_add_rx_frag`:

fm10k_add_rx_frag
=================

.. c:function:: bool fm10k_add_rx_frag(struct fm10k_rx_buffer *rx_buffer, unsigned int size, union fm10k_rx_desc *rx_desc, struct sk_buff *skb)

    Add contents of Rx buffer to sk_buff

    :param struct fm10k_rx_buffer \*rx_buffer:
        buffer containing page to add

    :param unsigned int size:
        packet size from rx_desc

    :param union fm10k_rx_desc \*rx_desc:
        descriptor containing length of buffer written by hardware

    :param struct sk_buff \*skb:
        sk_buff to place the data into

.. _`fm10k_add_rx_frag.description`:

Description
-----------

This function will add the data contained in rx_buffer->page to the skb.
This is done either through a direct copy if the data in the buffer is
less than the skb header size, otherwise it will just attach the page as
a frag to the skb.

The function will then update the page offset if necessary and return
true if the buffer can be reused by the interface.

.. _`fm10k_process_skb_fields`:

fm10k_process_skb_fields
========================

.. c:function:: unsigned int fm10k_process_skb_fields(struct fm10k_ring *rx_ring, union fm10k_rx_desc *rx_desc, struct sk_buff *skb)

    Populate skb header fields from Rx descriptor

    :param struct fm10k_ring \*rx_ring:
        rx descriptor ring packet is being transacted on

    :param union fm10k_rx_desc \*rx_desc:
        pointer to the EOP Rx descriptor

    :param struct sk_buff \*skb:
        pointer to current skb being populated

.. _`fm10k_process_skb_fields.description`:

Description
-----------

This function checks the ring, descriptor, and packet information in
order to populate the hash, checksum, VLAN, timestamp, protocol, and
other fields within the skb.

.. _`fm10k_is_non_eop`:

fm10k_is_non_eop
================

.. c:function:: bool fm10k_is_non_eop(struct fm10k_ring *rx_ring, union fm10k_rx_desc *rx_desc)

    process handling of non-EOP buffers

    :param struct fm10k_ring \*rx_ring:
        Rx ring being processed

    :param union fm10k_rx_desc \*rx_desc:
        Rx descriptor for current buffer

.. _`fm10k_is_non_eop.description`:

Description
-----------

This function updates next to clean.  If the buffer is an EOP buffer
this function exits returning false, otherwise it will place the
sk_buff in the next buffer to be chained and return true indicating
that this is in fact a non-EOP buffer.

.. _`fm10k_cleanup_headers`:

fm10k_cleanup_headers
=====================

.. c:function:: bool fm10k_cleanup_headers(struct fm10k_ring *rx_ring, union fm10k_rx_desc *rx_desc, struct sk_buff *skb)

    Correct corrupted or empty headers

    :param struct fm10k_ring \*rx_ring:
        rx descriptor ring packet is being transacted on

    :param union fm10k_rx_desc \*rx_desc:
        pointer to the EOP Rx descriptor

    :param struct sk_buff \*skb:
        pointer to current skb being fixed

.. _`fm10k_cleanup_headers.description`:

Description
-----------

Address the case where we are pulling data in on pages only
and as such no data is present in the skb header.

In addition if skb is not at least 60 bytes we need to pad it so that
it is large enough to qualify as a valid Ethernet frame.

Returns true if an error was encountered and skb was freed.

.. _`fm10k_receive_skb`:

fm10k_receive_skb
=================

.. c:function:: void fm10k_receive_skb(struct fm10k_q_vector *q_vector, struct sk_buff *skb)

    helper function to handle rx indications

    :param struct fm10k_q_vector \*q_vector:
        structure containing interrupt and ring information

    :param struct sk_buff \*skb:
        packet to send up

.. _`fm10k_get_tx_pending`:

fm10k_get_tx_pending
====================

.. c:function:: u64 fm10k_get_tx_pending(struct fm10k_ring *ring, bool in_sw)

    how many Tx descriptors not processed

    :param struct fm10k_ring \*ring:
        the ring structure

    :param bool in_sw:
        is tx_pending being checked in SW or in HW?

.. _`fm10k_tx_timeout_reset`:

fm10k_tx_timeout_reset
======================

.. c:function:: void fm10k_tx_timeout_reset(struct fm10k_intfc *interface)

    initiate reset due to Tx timeout

    :param struct fm10k_intfc \*interface:
        driver private struct

.. _`fm10k_clean_tx_irq`:

fm10k_clean_tx_irq
==================

.. c:function:: bool fm10k_clean_tx_irq(struct fm10k_q_vector *q_vector, struct fm10k_ring *tx_ring, int napi_budget)

    Reclaim resources after transmit completes

    :param struct fm10k_q_vector \*q_vector:
        structure containing interrupt and ring information

    :param struct fm10k_ring \*tx_ring:
        tx ring to clean

    :param int napi_budget:
        Used to determine if we are in netpoll

.. _`fm10k_update_itr`:

fm10k_update_itr
================

.. c:function:: void fm10k_update_itr(struct fm10k_ring_container *ring_container)

    update the dynamic ITR value based on packet size

    :param struct fm10k_ring_container \*ring_container:
        Container for rings to have ITR updated

.. _`fm10k_update_itr.description`:

Description
-----------

Stores a new ITR value based on strictly on packet size.  The
divisors and thresholds used by this function were determined based
on theoretical maximum wire speed and testing data, in order to
minimize response time while increasing bulk throughput.

.. _`fm10k_set_qos_queues`:

fm10k_set_qos_queues
====================

.. c:function:: bool fm10k_set_qos_queues(struct fm10k_intfc *interface)

    Allocate queues for a QOS-enabled device

    :param struct fm10k_intfc \*interface:
        board private structure to initialize

.. _`fm10k_set_qos_queues.description`:

Description
-----------

When QoS (Quality of Service) is enabled, allocate queues for
each traffic class.  If multiqueue isn't available,then abort QoS
initialization.

This function handles all combinations of Qos and RSS.

.. _`fm10k_set_rss_queues`:

fm10k_set_rss_queues
====================

.. c:function:: bool fm10k_set_rss_queues(struct fm10k_intfc *interface)

    Allocate queues for RSS

    :param struct fm10k_intfc \*interface:
        board private structure to initialize

.. _`fm10k_set_rss_queues.description`:

Description
-----------

This is our "base" multiqueue mode.  RSS (Receive Side Scaling) will try
to allocate one Rx queue per CPU, and if available, one Tx queue per CPU.

.. _`fm10k_set_num_queues`:

fm10k_set_num_queues
====================

.. c:function:: void fm10k_set_num_queues(struct fm10k_intfc *interface)

    Allocate queues for device, feature dependent

    :param struct fm10k_intfc \*interface:
        board private structure to initialize

.. _`fm10k_set_num_queues.description`:

Description
-----------

This is the top level queue allocation routine.  The order here is very
important, starting with the "most" number of features turned on at once,
and ending with the smallest set of features.  This way large combinations
can be allocated if they're turned on, and smaller combinations are the
fallthrough conditions.

.. _`fm10k_reset_num_queues`:

fm10k_reset_num_queues
======================

.. c:function:: void fm10k_reset_num_queues(struct fm10k_intfc *interface)

    Reset the number of queues to zero

    :param struct fm10k_intfc \*interface:
        board private structure

.. _`fm10k_reset_num_queues.description`:

Description
-----------

This function should be called whenever we need to reset the number of
queues after an error condition.

.. _`fm10k_alloc_q_vector`:

fm10k_alloc_q_vector
====================

.. c:function:: int fm10k_alloc_q_vector(struct fm10k_intfc *interface, unsigned int v_count, unsigned int v_idx, unsigned int txr_count, unsigned int txr_idx, unsigned int rxr_count, unsigned int rxr_idx)

    Allocate memory for a single interrupt vector

    :param struct fm10k_intfc \*interface:
        board private structure to initialize

    :param unsigned int v_count:
        q_vectors allocated on interface, used for ring interleaving

    :param unsigned int v_idx:
        index of vector in interface struct

    :param unsigned int txr_count:
        total number of Tx rings to allocate

    :param unsigned int txr_idx:
        index of first Tx ring to allocate

    :param unsigned int rxr_count:
        total number of Rx rings to allocate

    :param unsigned int rxr_idx:
        index of first Rx ring to allocate

.. _`fm10k_alloc_q_vector.description`:

Description
-----------

We allocate one q_vector.  If allocation fails we return -ENOMEM.

.. _`fm10k_free_q_vector`:

fm10k_free_q_vector
===================

.. c:function:: void fm10k_free_q_vector(struct fm10k_intfc *interface, int v_idx)

    Free memory allocated for specific interrupt vector

    :param struct fm10k_intfc \*interface:
        board private structure to initialize

    :param int v_idx:
        Index of vector to be freed

.. _`fm10k_free_q_vector.description`:

Description
-----------

This function frees the memory allocated to the q_vector.  In addition if
NAPI is enabled it will delete any references to the NAPI struct prior
to freeing the q_vector.

.. _`fm10k_alloc_q_vectors`:

fm10k_alloc_q_vectors
=====================

.. c:function:: int fm10k_alloc_q_vectors(struct fm10k_intfc *interface)

    Allocate memory for interrupt vectors

    :param struct fm10k_intfc \*interface:
        board private structure to initialize

.. _`fm10k_alloc_q_vectors.description`:

Description
-----------

We allocate one q_vector per queue interrupt.  If allocation fails we
return -ENOMEM.

.. _`fm10k_free_q_vectors`:

fm10k_free_q_vectors
====================

.. c:function:: void fm10k_free_q_vectors(struct fm10k_intfc *interface)

    Free memory allocated for interrupt vectors

    :param struct fm10k_intfc \*interface:
        board private structure to initialize

.. _`fm10k_free_q_vectors.description`:

Description
-----------

This function frees the memory allocated to the q_vectors.  In addition if
NAPI is enabled it will delete any references to the NAPI struct prior
to freeing the q_vector.

.. _`fm10k_reset_msix_capability`:

fm10k_reset_msix_capability
===========================

.. c:function:: void fm10k_reset_msix_capability(struct fm10k_intfc *interface)

    reset MSI-X capability

    :param struct fm10k_intfc \*interface:
        board private structure to initialize

.. _`fm10k_reset_msix_capability.description`:

Description
-----------

Reset the MSI-X capability back to its starting state

.. _`fm10k_init_msix_capability`:

fm10k_init_msix_capability
==========================

.. c:function:: int fm10k_init_msix_capability(struct fm10k_intfc *interface)

    configure MSI-X capability

    :param struct fm10k_intfc \*interface:
        board private structure to initialize

.. _`fm10k_init_msix_capability.description`:

Description
-----------

Attempt to configure the interrupts using the best available
capabilities of the hardware and the kernel.

.. _`fm10k_cache_ring_qos`:

fm10k_cache_ring_qos
====================

.. c:function:: bool fm10k_cache_ring_qos(struct fm10k_intfc *interface)

    Descriptor ring to register mapping for QoS

    :param struct fm10k_intfc \*interface:
        Interface structure continaining rings and devices

.. _`fm10k_cache_ring_qos.description`:

Description
-----------

Cache the descriptor ring offsets for Qos

.. _`fm10k_cache_ring_rss`:

fm10k_cache_ring_rss
====================

.. c:function:: void fm10k_cache_ring_rss(struct fm10k_intfc *interface)

    Descriptor ring to register mapping for RSS

    :param struct fm10k_intfc \*interface:
        Interface structure continaining rings and devices

.. _`fm10k_cache_ring_rss.description`:

Description
-----------

Cache the descriptor ring offsets for RSS

.. _`fm10k_assign_rings`:

fm10k_assign_rings
==================

.. c:function:: void fm10k_assign_rings(struct fm10k_intfc *interface)

    Map rings to network devices

    :param struct fm10k_intfc \*interface:
        Interface structure containing rings and devices

.. _`fm10k_assign_rings.description`:

Description
-----------

This function is meant to go though and configure both the network
devices so that they contain rings, and configure the rings so that
they function with their network devices.

.. _`fm10k_init_queueing_scheme`:

fm10k_init_queueing_scheme
==========================

.. c:function:: int fm10k_init_queueing_scheme(struct fm10k_intfc *interface)

    Determine proper queueing scheme

    :param struct fm10k_intfc \*interface:
        board private structure to initialize

.. _`fm10k_init_queueing_scheme.description`:

Description
-----------

We determine which queueing scheme to use based on...
- Hardware queue count (num\_\*\_queues)
- defined by miscellaneous hardware support/features (RSS, etc.)

.. _`fm10k_clear_queueing_scheme`:

fm10k_clear_queueing_scheme
===========================

.. c:function:: void fm10k_clear_queueing_scheme(struct fm10k_intfc *interface)

    Clear the current queueing scheme settings

    :param struct fm10k_intfc \*interface:
        board private structure to clear queueing scheme on

.. _`fm10k_clear_queueing_scheme.description`:

Description
-----------

We go through and clear queueing specific resources and reset the structure
to pre-load conditions

.. This file was automatic generated / don't edit.

