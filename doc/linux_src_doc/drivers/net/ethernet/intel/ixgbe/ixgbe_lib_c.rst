.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ixgbe/ixgbe_lib.c

.. _`ixgbe_cache_ring_dcb_sriov`:

ixgbe_cache_ring_dcb_sriov
==========================

.. c:function:: bool ixgbe_cache_ring_dcb_sriov(struct ixgbe_adapter *adapter)

    Descriptor ring to register mapping for SR-IOV

    :param struct ixgbe_adapter \*adapter:
        board private structure to initialize

.. _`ixgbe_cache_ring_dcb_sriov.description`:

Description
-----------

Cache the descriptor ring offsets for SR-IOV to the assigned rings.  It
will also try to cache the proper offsets if RSS/FCoE are enabled along
with VMDq.

.. _`ixgbe_cache_ring_dcb`:

ixgbe_cache_ring_dcb
====================

.. c:function:: bool ixgbe_cache_ring_dcb(struct ixgbe_adapter *adapter)

    Descriptor ring to register mapping for DCB

    :param struct ixgbe_adapter \*adapter:
        board private structure to initialize

.. _`ixgbe_cache_ring_dcb.description`:

Description
-----------

Cache the descriptor ring offsets for DCB to the assigned rings.

.. _`ixgbe_cache_ring_sriov`:

ixgbe_cache_ring_sriov
======================

.. c:function:: bool ixgbe_cache_ring_sriov(struct ixgbe_adapter *adapter)

    Descriptor ring to register mapping for sriov

    :param struct ixgbe_adapter \*adapter:
        board private structure to initialize

.. _`ixgbe_cache_ring_sriov.description`:

Description
-----------

SR-IOV doesn't use any descriptor rings but changes the default if
no other mapping is used.

.. _`ixgbe_cache_ring_rss`:

ixgbe_cache_ring_rss
====================

.. c:function:: bool ixgbe_cache_ring_rss(struct ixgbe_adapter *adapter)

    Descriptor ring to register mapping for RSS

    :param struct ixgbe_adapter \*adapter:
        board private structure to initialize

.. _`ixgbe_cache_ring_rss.description`:

Description
-----------

Cache the descriptor ring offsets for RSS to the assigned rings.

.. _`ixgbe_cache_ring_register`:

ixgbe_cache_ring_register
=========================

.. c:function:: void ixgbe_cache_ring_register(struct ixgbe_adapter *adapter)

    Descriptor ring to register mapping

    :param struct ixgbe_adapter \*adapter:
        board private structure to initialize

.. _`ixgbe_cache_ring_register.description`:

Description
-----------

Once we know the feature-set enabled for the device, we'll cache
the register offset the descriptor ring is assigned to.

Note, the order the various feature calls is important.  It must start with
the "most" features enabled at the same time, then trickle down to the
least amount of features turned on at once.

.. _`ixgbe_set_dcb_sriov_queues`:

ixgbe_set_dcb_sriov_queues
==========================

.. c:function:: bool ixgbe_set_dcb_sriov_queues(struct ixgbe_adapter *adapter)

    Allocate queues for SR-IOV devices w/ DCB

    :param struct ixgbe_adapter \*adapter:
        board private structure to initialize

.. _`ixgbe_set_dcb_sriov_queues.description`:

Description
-----------

When SR-IOV (Single Root IO Virtualiztion) is enabled, allocate queues
and VM pools where appropriate.  Also assign queues based on DCB
priorities and map accordingly..

.. _`ixgbe_set_sriov_queues`:

ixgbe_set_sriov_queues
======================

.. c:function:: bool ixgbe_set_sriov_queues(struct ixgbe_adapter *adapter)

    Allocate queues for SR-IOV devices

    :param struct ixgbe_adapter \*adapter:
        board private structure to initialize

.. _`ixgbe_set_sriov_queues.description`:

Description
-----------

When SR-IOV (Single Root IO Virtualiztion) is enabled, allocate queues
and VM pools where appropriate.  If RSS is available, then also try and
enable RSS and map accordingly.

.. _`ixgbe_set_rss_queues`:

ixgbe_set_rss_queues
====================

.. c:function:: bool ixgbe_set_rss_queues(struct ixgbe_adapter *adapter)

    Allocate queues for RSS

    :param struct ixgbe_adapter \*adapter:
        board private structure to initialize

.. _`ixgbe_set_rss_queues.description`:

Description
-----------

This is our "base" multiqueue mode.  RSS (Receive Side Scaling) will try
to allocate one Rx queue per CPU, and if available, one Tx queue per CPU.

.. _`ixgbe_set_num_queues`:

ixgbe_set_num_queues
====================

.. c:function:: void ixgbe_set_num_queues(struct ixgbe_adapter *adapter)

    Allocate queues for device, feature dependent

    :param struct ixgbe_adapter \*adapter:
        board private structure to initialize

.. _`ixgbe_set_num_queues.description`:

Description
-----------

This is the top level queue allocation routine.  The order here is very
important, starting with the "most" number of features turned on at once,
and ending with the smallest set of features.  This way large combinations
can be allocated if they're turned on, and smaller combinations are the
fallthrough conditions.

.. _`ixgbe_acquire_msix_vectors`:

ixgbe_acquire_msix_vectors
==========================

.. c:function:: int ixgbe_acquire_msix_vectors(struct ixgbe_adapter *adapter)

    acquire MSI-X vectors

    :param struct ixgbe_adapter \*adapter:
        board private structure

.. _`ixgbe_acquire_msix_vectors.description`:

Description
-----------

Attempts to acquire a suitable range of MSI-X vector interrupts. Will
return a negative error code if unable to acquire MSI-X vectors for any
reason.

.. _`ixgbe_alloc_q_vector`:

ixgbe_alloc_q_vector
====================

.. c:function:: int ixgbe_alloc_q_vector(struct ixgbe_adapter *adapter, int v_count, int v_idx, int txr_count, int txr_idx, int rxr_count, int rxr_idx)

    Allocate memory for a single interrupt vector

    :param struct ixgbe_adapter \*adapter:
        board private structure to initialize

    :param int v_count:
        q_vectors allocated on adapter, used for ring interleaving

    :param int v_idx:
        index of vector in adapter struct

    :param int txr_count:
        total number of Tx rings to allocate

    :param int txr_idx:
        index of first Tx ring to allocate

    :param int rxr_count:
        total number of Rx rings to allocate

    :param int rxr_idx:
        index of first Rx ring to allocate

.. _`ixgbe_alloc_q_vector.description`:

Description
-----------

We allocate one q_vector.  If allocation fails we return -ENOMEM.

.. _`ixgbe_free_q_vector`:

ixgbe_free_q_vector
===================

.. c:function:: void ixgbe_free_q_vector(struct ixgbe_adapter *adapter, int v_idx)

    Free memory allocated for specific interrupt vector

    :param struct ixgbe_adapter \*adapter:
        board private structure to initialize

    :param int v_idx:
        Index of vector to be freed

.. _`ixgbe_free_q_vector.description`:

Description
-----------

This function frees the memory allocated to the q_vector.  In addition if
NAPI is enabled it will delete any references to the NAPI struct prior
to freeing the q_vector.

.. _`ixgbe_alloc_q_vectors`:

ixgbe_alloc_q_vectors
=====================

.. c:function:: int ixgbe_alloc_q_vectors(struct ixgbe_adapter *adapter)

    Allocate memory for interrupt vectors

    :param struct ixgbe_adapter \*adapter:
        board private structure to initialize

.. _`ixgbe_alloc_q_vectors.description`:

Description
-----------

We allocate one q_vector per queue interrupt.  If allocation fails we
return -ENOMEM.

.. _`ixgbe_free_q_vectors`:

ixgbe_free_q_vectors
====================

.. c:function:: void ixgbe_free_q_vectors(struct ixgbe_adapter *adapter)

    Free memory allocated for interrupt vectors

    :param struct ixgbe_adapter \*adapter:
        board private structure to initialize

.. _`ixgbe_free_q_vectors.description`:

Description
-----------

This function frees the memory allocated to the q_vectors.  In addition if
NAPI is enabled it will delete any references to the NAPI struct prior
to freeing the q_vector.

.. _`ixgbe_set_interrupt_capability`:

ixgbe_set_interrupt_capability
==============================

.. c:function:: void ixgbe_set_interrupt_capability(struct ixgbe_adapter *adapter)

    set MSI-X or MSI if supported

    :param struct ixgbe_adapter \*adapter:
        board private structure to initialize

.. _`ixgbe_set_interrupt_capability.description`:

Description
-----------

Attempt to configure the interrupts using the best available
capabilities of the hardware and the kernel.

.. _`ixgbe_init_interrupt_scheme`:

ixgbe_init_interrupt_scheme
===========================

.. c:function:: int ixgbe_init_interrupt_scheme(struct ixgbe_adapter *adapter)

    Determine proper interrupt scheme

    :param struct ixgbe_adapter \*adapter:
        board private structure to initialize

.. _`ixgbe_init_interrupt_scheme.description`:

Description
-----------

We determine which interrupt scheme to use based on...
- Kernel support (MSI, MSI-X)
- which can be user-defined (via MODULE_PARAM)
- Hardware queue count (num\_\*\_queues)
- defined by miscellaneous hardware support/features (RSS, etc.)

.. _`ixgbe_clear_interrupt_scheme`:

ixgbe_clear_interrupt_scheme
============================

.. c:function:: void ixgbe_clear_interrupt_scheme(struct ixgbe_adapter *adapter)

    Clear the current interrupt scheme settings

    :param struct ixgbe_adapter \*adapter:
        board private structure to clear interrupt scheme on

.. _`ixgbe_clear_interrupt_scheme.description`:

Description
-----------

We go through and clear interrupt specific resources and reset the structure
to pre-load conditions

.. This file was automatic generated / don't edit.

