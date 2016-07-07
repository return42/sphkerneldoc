.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/sdma.c

.. _`sdma_state_name`:

sdma_state_name
===============

.. c:function:: const char *sdma_state_name(enum sdma_states state)

    return state string from enum

    :param enum sdma_states state:
        state

.. _`sdma_get_descq_cnt`:

sdma_get_descq_cnt
==================

.. c:function:: u16 sdma_get_descq_cnt( void)

    called when device probed

    :param  void:
        no arguments

.. _`sdma_get_descq_cnt.description`:

Description
-----------

Return a validated descq count.

This is currently only used in the verbs initialization to build the tx
list.

This will probably be deleted in favor of a more scalable approach to
alloc tx's.

.. _`sdma_select_engine_vl`:

sdma_select_engine_vl
=====================

.. c:function:: struct sdma_engine *sdma_select_engine_vl(struct hfi1_devdata *dd, u32 selector, u8 vl)

    select sdma engine

    :param struct hfi1_devdata \*dd:
        devdata

    :param u32 selector:
        a spreading factor

    :param u8 vl:
        this vl

.. _`sdma_select_engine_vl.description`:

Description
-----------


This function returns an engine based on the selector and a vl.  The
mapping fields are protected by RCU.

.. _`sdma_select_engine_sc`:

sdma_select_engine_sc
=====================

.. c:function:: struct sdma_engine *sdma_select_engine_sc(struct hfi1_devdata *dd, u32 selector, u8 sc5)

    select sdma engine

    :param struct hfi1_devdata \*dd:
        devdata

    :param u32 selector:
        a spreading factor

    :param u8 sc5:
        the 5 bit sc

.. _`sdma_select_engine_sc.description`:

Description
-----------


This function returns an engine based on the selector and an sc.

.. _`sdma_map_init`:

sdma_map_init
=============

.. c:function:: int sdma_map_init(struct hfi1_devdata *dd, u8 port, u8 num_vls, u8 *vl_engines)

    called when # vls change

    :param struct hfi1_devdata \*dd:
        hfi1_devdata

    :param u8 port:
        port number

    :param u8 num_vls:
        number of vls

    :param u8 \*vl_engines:
        per vl engine mapping (optional)

.. _`sdma_map_init.description`:

Description
-----------

This routine changes the mapping based on the number of vls.

vl_engines is used to specify a non-uniform vl/engine loading. NULL
implies auto computing the loading and giving each VLs a uniform
distribution of engines per VL.

The auto algorithm computes the sde_per_vl and the number of extra
engines.  Any extra engines are added from the last VL on down.

rcu locking is used here to control access to the mapping fields.

If either the num_vls or num_sdma are non-power of 2, the array sizes
in the struct sdma_vl_map and the struct sdma_map_elem are rounded
up to the next highest power of 2 and the first entry is reused
in a round robin fashion.

If an error occurs the map change is not done and the mapping is
not changed.

.. _`sdma_init`:

sdma_init
=========

.. c:function:: int sdma_init(struct hfi1_devdata *dd, u8 port)

    called when device probed

    :param struct hfi1_devdata \*dd:
        hfi1_devdata

    :param u8 port:
        port number (currently only zero)

.. _`sdma_init.description`:

Description
-----------

sdma_init initializes the specified number of engines.

The code initializes each sde, its csrs.  Interrupts
are not required to be enabled.

.. _`sdma_init.return`:

Return
------

0 - success, -errno on failure

.. _`sdma_all_running`:

sdma_all_running
================

.. c:function:: void sdma_all_running(struct hfi1_devdata *dd)

    called when the link goes up

    :param struct hfi1_devdata \*dd:
        hfi1_devdata

.. _`sdma_all_running.description`:

Description
-----------

This routine moves all engines to the running state.

.. _`sdma_all_idle`:

sdma_all_idle
=============

.. c:function:: void sdma_all_idle(struct hfi1_devdata *dd)

    called when the link goes down

    :param struct hfi1_devdata \*dd:
        hfi1_devdata

.. _`sdma_all_idle.description`:

Description
-----------

This routine moves all engines to the idle state.

.. _`sdma_start`:

sdma_start
==========

.. c:function:: void sdma_start(struct hfi1_devdata *dd)

    called to kick off state processing for all engines

    :param struct hfi1_devdata \*dd:
        hfi1_devdata

.. _`sdma_start.description`:

Description
-----------

This routine is for kicking off the state processing for all required
sdma engines.  Interrupts need to be working at this point.

.. _`sdma_exit`:

sdma_exit
=========

.. c:function:: void sdma_exit(struct hfi1_devdata *dd)

    used when module is removed

    :param struct hfi1_devdata \*dd:
        hfi1_devdata

.. _`sdma_txclean`:

sdma_txclean
============

.. c:function:: void sdma_txclean(struct hfi1_devdata *dd, struct sdma_txreq *tx)

    clean tx of mappings, descp \*kmalloc's

    :param struct hfi1_devdata \*dd:
        hfi1_devdata for unmapping

    :param struct sdma_txreq \*tx:
        tx request to clean

.. _`sdma_txclean.description`:

Description
-----------

This is used in the progress routine to clean the tx or
by the ULP to toss an in-process tx build.

The code can be called multiple times without issue.

.. _`sdma_engine_error`:

sdma_engine_error
=================

.. c:function:: void sdma_engine_error(struct sdma_engine *sde, u64 status)

    error handler for engine

    :param struct sdma_engine \*sde:
        sdma engine

    :param u64 status:
        sdma interrupt reason

.. _`sdma_seqfile_dump_sde`:

sdma_seqfile_dump_sde
=====================

.. c:function:: void sdma_seqfile_dump_sde(struct seq_file *s, struct sdma_engine *sde)

    debugfs dump of sde

    :param struct seq_file \*s:
        seq file

    :param struct sdma_engine \*sde:
        send dma engine to dump

.. _`sdma_seqfile_dump_sde.description`:

Description
-----------

This routine dumps the sde to the indicated seq file.

.. _`sdma_send_txreq`:

sdma_send_txreq
===============

.. c:function:: int sdma_send_txreq(struct sdma_engine *sde, struct iowait *wait, struct sdma_txreq *tx)

    submit a tx req to ring

    :param struct sdma_engine \*sde:
        sdma engine to use

    :param struct iowait \*wait:
        wait structure to use when full (may be NULL)

    :param struct sdma_txreq \*tx:
        sdma_txreq to submit

.. _`sdma_send_txreq.description`:

Description
-----------

The call submits the tx into the ring.  If a iowait structure is non-NULL
the packet will be queued to the list in wait.

.. _`sdma_send_txreq.return`:

Return
------

0 - Success, -EINVAL - sdma_txreq incomplete, -EBUSY - no space in
ring (wait == NULL)
-EIOCBQUEUED - tx queued to iowait, -ECOMM bad sdma state

.. _`sdma_send_txlist`:

sdma_send_txlist
================

.. c:function:: int sdma_send_txlist(struct sdma_engine *sde, struct iowait *wait, struct list_head *tx_list)

    submit a list of tx req to ring

    :param struct sdma_engine \*sde:
        sdma engine to use

    :param struct iowait \*wait:
        wait structure to use when full (may be NULL)

    :param struct list_head \*tx_list:
        list of sdma_txreqs to submit

.. _`sdma_send_txlist.description`:

Description
-----------

The call submits the list into the ring.

If the iowait structure is non-NULL and not equal to the iowait list
the unprocessed part of the list  will be appended to the list in wait.

In all cases, the tx_list will be updated so the head of the tx_list is
the list of descriptors that have yet to be transmitted.

The intent of this call is to provide a more efficient
way of submitting multiple packets to SDMA while holding the tail
side locking.

.. _`sdma_send_txlist.return`:

Return
------

> 0 - Success (value is number of sdma_txreq's submitted),
-EINVAL - sdma_txreq incomplete, -EBUSY - no space in ring (wait == NULL)
-EIOCBQUEUED - tx queued to iowait, -ECOMM bad sdma state

.. _`sdma_ahg_alloc`:

sdma_ahg_alloc
==============

.. c:function:: int sdma_ahg_alloc(struct sdma_engine *sde)

    allocate an AHG entry

    :param struct sdma_engine \*sde:
        engine to allocate from

.. _`sdma_ahg_alloc.return`:

Return
------

0-31 when successful, -EOPNOTSUPP if AHG is not enabled,
-ENOSPC if an entry is not available

.. _`sdma_ahg_free`:

sdma_ahg_free
=============

.. c:function:: void sdma_ahg_free(struct sdma_engine *sde, int ahg_index)

    free an AHG entry

    :param struct sdma_engine \*sde:
        engine to return AHG entry

    :param int ahg_index:
        index to free

.. _`sdma_ahg_free.description`:

Description
-----------

This routine frees the indicate AHG entry.

.. _`_sdma_engine_progress_schedule`:

_sdma_engine_progress_schedule
==============================

.. c:function:: void _sdma_engine_progress_schedule(struct sdma_engine *sde)

    schedule progress on engine

    :param struct sdma_engine \*sde:
        sdma_engine to schedule progress

.. This file was automatic generated / don't edit.

