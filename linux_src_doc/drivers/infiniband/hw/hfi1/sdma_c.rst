.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/sdma.c

.. _`sdma_state_name`:

sdma_state_name
===============

.. c:function:: const char *sdma_state_name(enum sdma_states state)

    return state string from enum

    :param state:
        state
    :type state: enum sdma_states

.. _`sdma_get_descq_cnt`:

sdma_get_descq_cnt
==================

.. c:function:: u16 sdma_get_descq_cnt( void)

    called when device probed

    :param void:
        no arguments
    :type void: 

.. _`sdma_get_descq_cnt.description`:

Description
-----------

Return a validated descq count.

This is currently only used in the verbs initialization to build the tx
list.

This will probably be deleted in favor of a more scalable approach to
alloc tx's.

.. _`sdma_engine_get_vl`:

sdma_engine_get_vl
==================

.. c:function:: int sdma_engine_get_vl(struct sdma_engine *sde)

    return vl for a given sdma engine

    :param sde:
        sdma engine
    :type sde: struct sdma_engine \*

.. _`sdma_engine_get_vl.description`:

Description
-----------

This function returns the vl mapped to a given engine, or an error if
the mapping can't be found. The mapping fields are protected by RCU.

.. _`sdma_select_engine_vl`:

sdma_select_engine_vl
=====================

.. c:function:: struct sdma_engine *sdma_select_engine_vl(struct hfi1_devdata *dd, u32 selector, u8 vl)

    select sdma engine

    :param dd:
        devdata
    :type dd: struct hfi1_devdata \*

    :param selector:
        a spreading factor
    :type selector: u32

    :param vl:
        this vl
    :type vl: u8

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

    :param dd:
        devdata
    :type dd: struct hfi1_devdata \*

    :param selector:
        a spreading factor
    :type selector: u32

    :param sc5:
        the 5 bit sc
    :type sc5: u8

.. _`sdma_select_engine_sc.description`:

Description
-----------


This function returns an engine based on the selector and an sc.

.. _`sdma_seqfile_dump_cpu_list`:

sdma_seqfile_dump_cpu_list
==========================

.. c:function:: void sdma_seqfile_dump_cpu_list(struct seq_file *s, struct hfi1_devdata *dd, unsigned long cpuid)

    debugfs dump the cpu to sdma mappings

    :param s:
        seq file
    :type s: struct seq_file \*

    :param dd:
        hfi1_devdata
    :type dd: struct hfi1_devdata \*

    :param cpuid:
        cpu id
    :type cpuid: unsigned long

.. _`sdma_seqfile_dump_cpu_list.description`:

Description
-----------

This routine dumps the process to sde mappings per cpu

.. _`sdma_map_init`:

sdma_map_init
=============

.. c:function:: int sdma_map_init(struct hfi1_devdata *dd, u8 port, u8 num_vls, u8 *vl_engines)

    called when # vls change

    :param dd:
        hfi1_devdata
    :type dd: struct hfi1_devdata \*

    :param port:
        port number
    :type port: u8

    :param num_vls:
        number of vls
    :type num_vls: u8

    :param vl_engines:
        per vl engine mapping (optional)
    :type vl_engines: u8 \*

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

.. _`sdma_clean`:

sdma_clean
==========

.. c:function:: void sdma_clean(struct hfi1_devdata *dd, size_t num_engines)

    :param dd:
        struct hfi1_devdata
    :type dd: struct hfi1_devdata \*

    :param num_engines:
        num sdma engines
    :type num_engines: size_t

.. _`sdma_clean.description`:

Description
-----------

This routine can be called regardless of the success of
\ :c:func:`sdma_init`\ 

.. _`sdma_init`:

sdma_init
=========

.. c:function:: int sdma_init(struct hfi1_devdata *dd, u8 port)

    called when device probed

    :param dd:
        hfi1_devdata
    :type dd: struct hfi1_devdata \*

    :param port:
        port number (currently only zero)
    :type port: u8

.. _`sdma_init.description`:

Description
-----------

Initializes each sde and its csrs.
Interrupts are not required to be enabled.

.. _`sdma_init.return`:

Return
------

0 - success, -errno on failure

.. _`sdma_all_running`:

sdma_all_running
================

.. c:function:: void sdma_all_running(struct hfi1_devdata *dd)

    called when the link goes up

    :param dd:
        hfi1_devdata
    :type dd: struct hfi1_devdata \*

.. _`sdma_all_running.description`:

Description
-----------

This routine moves all engines to the running state.

.. _`sdma_all_idle`:

sdma_all_idle
=============

.. c:function:: void sdma_all_idle(struct hfi1_devdata *dd)

    called when the link goes down

    :param dd:
        hfi1_devdata
    :type dd: struct hfi1_devdata \*

.. _`sdma_all_idle.description`:

Description
-----------

This routine moves all engines to the idle state.

.. _`sdma_start`:

sdma_start
==========

.. c:function:: void sdma_start(struct hfi1_devdata *dd)

    called to kick off state processing for all engines

    :param dd:
        hfi1_devdata
    :type dd: struct hfi1_devdata \*

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

    :param dd:
        hfi1_devdata
    :type dd: struct hfi1_devdata \*

.. _`__sdma_txclean`:

\__sdma_txclean
===============

.. c:function:: void __sdma_txclean(struct hfi1_devdata *dd, struct sdma_txreq *tx)

    clean tx of mappings, descp \*kmalloc's

    :param dd:
        hfi1_devdata for unmapping
    :type dd: struct hfi1_devdata \*

    :param tx:
        tx request to clean
    :type tx: struct sdma_txreq \*

.. _`__sdma_txclean.description`:

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

    :param sde:
        sdma engine
    :type sde: struct sdma_engine \*

    :param status:
        sdma interrupt reason
    :type status: u64

.. _`sdma_seqfile_dump_sde`:

sdma_seqfile_dump_sde
=====================

.. c:function:: void sdma_seqfile_dump_sde(struct seq_file *s, struct sdma_engine *sde)

    debugfs dump of sde

    :param s:
        seq file
    :type s: struct seq_file \*

    :param sde:
        send dma engine to dump
    :type sde: struct sdma_engine \*

.. _`sdma_seqfile_dump_sde.description`:

Description
-----------

This routine dumps the sde to the indicated seq file.

.. _`sdma_send_txreq`:

sdma_send_txreq
===============

.. c:function:: int sdma_send_txreq(struct sdma_engine *sde, struct iowait_work *wait, struct sdma_txreq *tx, bool pkts_sent)

    submit a tx req to ring

    :param sde:
        sdma engine to use
    :type sde: struct sdma_engine \*

    :param wait:
        SE wait structure to use when full (may be NULL)
    :type wait: struct iowait_work \*

    :param tx:
        sdma_txreq to submit
    :type tx: struct sdma_txreq \*

    :param pkts_sent:
        has any packet been sent yet?
    :type pkts_sent: bool

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

.. c:function:: int sdma_send_txlist(struct sdma_engine *sde, struct iowait_work *wait, struct list_head *tx_list, u16 *count_out)

    submit a list of tx req to ring

    :param sde:
        sdma engine to use
    :type sde: struct sdma_engine \*

    :param wait:
        SE wait structure to use when full (may be NULL)
    :type wait: struct iowait_work \*

    :param tx_list:
        list of sdma_txreqs to submit
    :type tx_list: struct list_head \*

    :param count_out:
        *undescribed*
    :type count_out: u16 \*

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

0 - Success,
-EINVAL - sdma_txreq incomplete, -EBUSY - no space in ring (wait == NULL)
-EIOCBQUEUED - tx queued to iowait, -ECOMM bad sdma state

.. _`sdma_ahg_alloc`:

sdma_ahg_alloc
==============

.. c:function:: int sdma_ahg_alloc(struct sdma_engine *sde)

    allocate an AHG entry

    :param sde:
        engine to allocate from
    :type sde: struct sdma_engine \*

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

    :param sde:
        engine to return AHG entry
    :type sde: struct sdma_engine \*

    :param ahg_index:
        index to free
    :type ahg_index: int

.. _`sdma_ahg_free.description`:

Description
-----------

This routine frees the indicate AHG entry.

.. _`_sdma_engine_progress_schedule`:

\_sdma_engine_progress_schedule
===============================

.. c:function:: void _sdma_engine_progress_schedule(struct sdma_engine *sde)

    schedule progress on engine

    :param sde:
        sdma_engine to schedule progress
    :type sde: struct sdma_engine \*

.. This file was automatic generated / don't edit.

