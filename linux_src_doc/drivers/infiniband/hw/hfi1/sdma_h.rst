.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/sdma.h

.. _`sdma_engine`:

struct sdma_engine
==================

.. c:type:: struct sdma_engine

    Data pertaining to each SDMA engine.

.. _`sdma_engine.definition`:

Definition
----------

.. code-block:: c

    struct sdma_engine {
        struct hfi1_devdata *dd;
        struct hfi1_pportdata *ppd;
    }

.. _`sdma_engine.members`:

Members
-------

dd
    a back-pointer to the device data

ppd
    per port back-pointer

.. _`sdma_engine.description`:

Description
-----------

This structure has the state for each sdma_engine.

Accessing to non public fields are not supported
since the private members are subject to change.

.. _`sdma_empty`:

sdma_empty
==========

.. c:function:: int sdma_empty(struct sdma_engine *sde)

    idle engine test

    :param struct sdma_engine \*sde:
        *undescribed*

.. _`sdma_empty.description`:

Description
-----------

Currently used by verbs as a latency optimization.

.. _`sdma_empty.return`:

Return
------

1 - empty, 0 - non-empty

.. _`sdma_running`:

sdma_running
============

.. c:function:: int sdma_running(struct sdma_engine *engine)

    state suitability test

    :param struct sdma_engine \*engine:
        sdma engine

.. _`sdma_running.description`:

Description
-----------

sdma_running probes the internal state to determine if it is suitable
for submitting packets.

.. _`sdma_running.return`:

Return
------

1 - ok to submit, 0 - not ok to submit

.. _`sdma_txinit_ahg`:

sdma_txinit_ahg
===============

.. c:function:: int sdma_txinit_ahg(struct sdma_txreq *tx, u16 flags, u16 tlen, u8 ahg_entry, u8 num_ahg, u32 *ahg, u8 ahg_hlen, void (*cb)(struct sdma_txreq *, int))

    initialize an sdma_txreq struct with AHG

    :param struct sdma_txreq \*tx:
        tx request to initialize

    :param u16 flags:
        flags to key last descriptor additions

    :param u16 tlen:
        total packet length (pbc + headers + data)

    :param u8 ahg_entry:
        ahg entry to use  (0 - 31)

    :param u8 num_ahg:
        ahg descriptor for first descriptor (0 - 9)

    :param u32 \*ahg:
        array of AHG descriptors (up to 9 entries)

    :param u8 ahg_hlen:
        number of bytes from ASIC entry to use

    :param void (\*cb)(struct sdma_txreq \*, int):
        callback

.. _`sdma_txinit_ahg.description`:

Description
-----------

The allocation of the sdma_txreq and it enclosing structure is user
dependent.  This routine must be called to initialize the user independent
fields.

The currently supported flags are SDMA_TXREQ_F_URGENT,
SDMA_TXREQ_F_AHG_COPY, and SDMA_TXREQ_F_USE_AHG.

SDMA_TXREQ_F_URGENT is used for latency sensitive situations where the
completion is desired as soon as possible.

SDMA_TXREQ_F_AHG_COPY causes the header in the first descriptor to be
copied to chip entry. SDMA_TXREQ_F_USE_AHG causes the code to add in
the AHG descriptors into the first 1 to 3 descriptors.

Completions of submitted requests can be gotten on selected
txreqs by giving a completion routine callback to \ :c:func:`sdma_txinit`\  or
\ :c:func:`sdma_txinit_ahg`\ .  The environment in which the callback runs
can be from an ISR, a tasklet, or a thread, so no sleeping
kernel routines can be used.   Aspects of the sdma ring may
be locked so care should be taken with locking.

The callback pointer can be NULL to avoid any callback for the packet
being submitted. The callback will be provided this tx, a status, and a flag.

The status will be one of SDMA_TXREQ_S_OK, SDMA_TXREQ_S_SENDERROR,
SDMA_TXREQ_S_ABORTED, or SDMA_TXREQ_S_SHUTDOWN.

The flag, if the is the iowait had been used, indicates the iowait
sdma_busy count has reached zero.

user data portion of tlen should be precise.   The sdma_txadd\_\* entrances
will pad with a descriptor references 1 - 3 bytes when the number of bytes
specified in tlen have been supplied to the sdma_txreq.

ahg_hlen is used to determine the number of on-chip entry bytes to
use as the header.   This is for cases where the stored header is
larger than the header to be used in a packet.  This is typical
for verbs where an RDMA_WRITE_FIRST is larger than the packet in
and RDMA_WRITE_MIDDLE.

.. _`sdma_txinit`:

sdma_txinit
===========

.. c:function:: int sdma_txinit(struct sdma_txreq *tx, u16 flags, u16 tlen, void (*cb)(struct sdma_txreq *, int))

    initialize an sdma_txreq struct (no AHG)

    :param struct sdma_txreq \*tx:
        tx request to initialize

    :param u16 flags:
        flags to key last descriptor additions

    :param u16 tlen:
        total packet length (pbc + headers + data)

    :param void (\*cb)(struct sdma_txreq \*, int):
        callback pointer

.. _`sdma_txinit.description`:

Description
-----------

The allocation of the sdma_txreq and it enclosing structure is user
dependent.  This routine must be called to initialize the user
independent fields.

The currently supported flags is SDMA_TXREQ_F_URGENT.

SDMA_TXREQ_F_URGENT is used for latency sensitive situations where the
completion is desired as soon as possible.

Completions of submitted requests can be gotten on selected
txreqs by giving a completion routine callback to \ :c:func:`sdma_txinit`\  or
\ :c:func:`sdma_txinit_ahg`\ .  The environment in which the callback runs
can be from an ISR, a tasklet, or a thread, so no sleeping
kernel routines can be used.   The head size of the sdma ring may
be locked so care should be taken with locking.

The callback pointer can be NULL to avoid any callback for the packet
being submitted.

The callback, if non-NULL,  will be provided this tx and a status.  The
status will be one of SDMA_TXREQ_S_OK, SDMA_TXREQ_S_SENDERROR,
SDMA_TXREQ_S_ABORTED, or SDMA_TXREQ_S_SHUTDOWN.

.. _`sdma_txadd_page`:

sdma_txadd_page
===============

.. c:function:: int sdma_txadd_page(struct hfi1_devdata *dd, struct sdma_txreq *tx, struct page *page, unsigned long offset, u16 len)

    add a page to the sdma_txreq

    :param struct hfi1_devdata \*dd:
        the device to use for mapping

    :param struct sdma_txreq \*tx:
        tx request to which the page is added

    :param struct page \*page:
        page to map

    :param unsigned long offset:
        offset within the page

    :param u16 len:
        length in bytes

.. _`sdma_txadd_page.description`:

Description
-----------

This is used to add a page/offset/length descriptor.

The mapping/unmapping of the page/offset/len is automatically handled.

.. _`sdma_txadd_page.return`:

Return
------

0 - success, -ENOSPC - mapping fail, -ENOMEM - couldn't
extend/coalesce descriptor array

.. _`sdma_txadd_daddr`:

sdma_txadd_daddr
================

.. c:function:: int sdma_txadd_daddr(struct hfi1_devdata *dd, struct sdma_txreq *tx, dma_addr_t addr, u16 len)

    add a dma address to the sdma_txreq

    :param struct hfi1_devdata \*dd:
        the device to use for mapping

    :param struct sdma_txreq \*tx:
        sdma_txreq to which the page is added

    :param dma_addr_t addr:
        dma address mapped by caller

    :param u16 len:
        length in bytes

.. _`sdma_txadd_daddr.description`:

Description
-----------

This is used to add a descriptor for memory that is already dma mapped.

In this case, there is no unmapping as part of the progress processing for
this memory location.

.. _`sdma_txadd_daddr.return`:

Return
------

0 - success, -ENOMEM - couldn't extend descriptor array

.. _`sdma_txadd_kvaddr`:

sdma_txadd_kvaddr
=================

.. c:function:: int sdma_txadd_kvaddr(struct hfi1_devdata *dd, struct sdma_txreq *tx, void *kvaddr, u16 len)

    add a kernel virtual address to sdma_txreq

    :param struct hfi1_devdata \*dd:
        the device to use for mapping

    :param struct sdma_txreq \*tx:
        sdma_txreq to which the page is added

    :param void \*kvaddr:
        the kernel virtual address

    :param u16 len:
        length in bytes

.. _`sdma_txadd_kvaddr.description`:

Description
-----------

This is used to add a descriptor referenced by the indicated kvaddr and
len.

The mapping/unmapping of the kvaddr and len is automatically handled.

.. _`sdma_txadd_kvaddr.return`:

Return
------

0 - success, -ENOSPC - mapping fail, -ENOMEM - couldn't extend/coalesce
descriptor array

.. _`sdma_build_ahg_descriptor`:

sdma_build_ahg_descriptor
=========================

.. c:function:: u32 sdma_build_ahg_descriptor(u16 data, u8 dwindex, u8 startbit, u8 bits)

    build ahg descriptor \ ``data``\  \ ``dwindex``\  \ ``startbit``\  \ ``bits``\ 

    :param u16 data:
        *undescribed*

    :param u8 dwindex:
        *undescribed*

    :param u8 startbit:
        *undescribed*

    :param u8 bits:
        *undescribed*

.. _`sdma_build_ahg_descriptor.description`:

Description
-----------

Build and return a 32 bit descriptor.

.. _`sdma_progress`:

sdma_progress
=============

.. c:function:: unsigned sdma_progress(struct sdma_engine *sde, unsigned seq, struct sdma_txreq *tx)

    use seq number of detect head progress

    :param struct sdma_engine \*sde:
        sdma_engine to check

    :param unsigned seq:
        base seq count

    :param struct sdma_txreq \*tx:
        txreq for which we need to check descriptor availability

.. _`sdma_progress.description`:

Description
-----------

This is used in the appropriate spot in the sleep routine
to check for potential ring progress.  This routine gets the
seqcount before queuing the iowait structure for progress.

If the seqcount indicates that progress needs to be checked,
re-submission is detected by checking whether the descriptor
queue has enough descriptor for the txreq.

.. _`sdma_iowait_schedule`:

sdma_iowait_schedule
====================

.. c:function:: void sdma_iowait_schedule(struct sdma_engine *sde, struct iowait *wait)

    initialize wait structure

    :param struct sdma_engine \*sde:
        sdma_engine to schedule

    :param struct iowait \*wait:
        wait struct to schedule

.. _`sdma_iowait_schedule.description`:

Description
-----------

This function initializes the iowait
structure embedded in the QP or PQ.

.. _`sdma_map_elem`:

struct sdma_map_elem
====================

.. c:type:: struct sdma_map_elem

    mapping for a vl \ ``mask``\  - selector mask \ ``sde``\  - array of engines for this vl

.. _`sdma_map_elem.definition`:

Definition
----------

.. code-block:: c

    struct sdma_map_elem {
        u32 mask;
        struct sdma_engine  *sde;
    }

.. _`sdma_map_elem.members`:

Members
-------

mask
    *undescribed*

sde
    *undescribed*

.. _`sdma_map_elem.description`:

Description
-----------

The mask is used to "mod" the selector
to produce index into the trailing
array of sdes.

.. _`sdma_vl_map`:

struct sdma_vl_map
==================

.. c:type:: struct sdma_vl_map

    mapping for a vl \ ``engine_to_vl``\  - map of an engine to a vl \ ``list``\  - rcu head for free callback \ ``mask``\  - vl mask to "mod" the vl to produce an index to map array \ ``actual_vls``\  - number of vls \ ``vls``\  - number of vls rounded to next power of 2 \ ``map``\  - array of sdma_map_elem entries

.. _`sdma_vl_map.definition`:

Definition
----------

.. code-block:: c

    struct sdma_vl_map {
        s8 engine_to_vl;
        struct rcu_head list;
        u32 mask;
        u8 actual_vls;
        u8 vls;
        struct sdma_map_elem  *map;
    }

.. _`sdma_vl_map.members`:

Members
-------

engine_to_vl
    *undescribed*

list
    *undescribed*

mask
    *undescribed*

actual_vls
    *undescribed*

vls
    *undescribed*

map
    *undescribed*

.. _`sdma_vl_map.description`:

Description
-----------

This is the parent mapping structure.  The trailing
members of the struct point to sdma_map_elem entries, which
in turn point to an array of sde's for that vl.

.. _`sdma_engine_progress_schedule`:

sdma_engine_progress_schedule
=============================

.. c:function:: void sdma_engine_progress_schedule(struct sdma_engine *sde)

    schedule progress on engine

    :param struct sdma_engine \*sde:
        sdma_engine to schedule progress

.. _`sdma_engine_progress_schedule.description`:

Description
-----------

This is the fast path.

.. This file was automatic generated / don't edit.

