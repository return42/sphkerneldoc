.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/aic94xx/aic94xx_hwi.c

.. _`asd_init_scbs`:

asd_init_scbs
=============

.. c:function:: int asd_init_scbs(struct asd_ha_struct *asd_ha)

    manually allocate the first SCB.

    :param struct asd_ha_struct \*asd_ha:
        pointer to host adapter structure

.. _`asd_init_scbs.description`:

Description
-----------

This allocates the very first SCB which would be sent to the
sequencer for execution.  Its bus address is written to
CSEQ_Q_NEW_POINTER, mode page 2, mode 8.  Since the bus address of
the \_next\_ scb to be DMA-ed to the host adapter is read from the last
SCB DMA-ed to the host adapter, we have to always stay one step
ahead of the sequencer and keep one SCB already allocated.

.. _`asd_init_escbs`:

asd_init_escbs
==============

.. c:function:: int asd_init_escbs(struct asd_ha_struct *asd_ha)

    - allocate and initialize empty scbs

    :param struct asd_ha_struct \*asd_ha:
        pointer to host adapter structure

.. _`asd_init_escbs.description`:

Description
-----------

An empty SCB has sg_elements of ASD_EDBS_PER_SCB (7) buffers.
They transport sense data, etc.

.. _`asd_chip_hardrst`:

asd_chip_hardrst
================

.. c:function:: int asd_chip_hardrst(struct asd_ha_struct *asd_ha)

    - hard reset the chip

    :param struct asd_ha_struct \*asd_ha:
        pointer to host adapter structure

.. _`asd_chip_hardrst.description`:

Description
-----------

This takes 16 cycles and is synchronous to CFCLK, which runs
at 200 MHz, so this should take at most 80 nanoseconds.

.. _`asd_init_chip`:

asd_init_chip
=============

.. c:function:: int asd_init_chip(struct asd_ha_struct *asd_ha)

    - initialize the chip

    :param struct asd_ha_struct \*asd_ha:
        pointer to host adapter structure

.. _`asd_init_chip.description`:

Description
-----------

Hard resets the chip, disables HA interrupts, downloads the sequnecer
microcode and starts the sequencers.  The caller has to explicitly
enable HA interrupts with asd_enable_ints(asd_ha).

.. _`asd_init_ctxmem`:

asd_init_ctxmem
===============

.. c:function:: int asd_init_ctxmem(struct asd_ha_struct *asd_ha)

    - initialize context memory

    :param struct asd_ha_struct \*asd_ha:
        *undescribed*

.. _`asd_init_ctxmem.asd_ha`:

asd_ha
------

pointer to host adapter structure

This function sets the maximum number of SCBs and
DDBs which can be used by the sequencer.  This is normally
512 and 128 respectively.  If support for more SCBs or more DDBs
is required then CMDCTXBASE, DEVCTXBASE and CTXDOMAIN are
initialized here to extend context memory to point to host memory,
thus allowing unlimited support for SCBs and DDBs -- only limited
by host memory.

.. _`asd_chip_reset`:

asd_chip_reset
==============

.. c:function:: void asd_chip_reset(struct asd_ha_struct *asd_ha)

    - reset the host adapter, etc

    :param struct asd_ha_struct \*asd_ha:
        pointer to host adapter structure of interest

.. _`asd_chip_reset.description`:

Description
-----------

Called from the ISR.  Hard reset the chip.  Let everything
timeout.  This should be no different than hot-unplugging the
host adapter.  Once everything times out we'll init the chip with
a call to \ :c:func:`asd_init_chip`\  and enable interrupts with \ :c:func:`asd_enable_ints`\ .
XXX finish.

.. _`asd_process_donelist_isr`:

asd_process_donelist_isr
========================

.. c:function:: void asd_process_donelist_isr(struct asd_ha_struct *asd_ha)

    - schedule processing of done list entries

    :param struct asd_ha_struct \*asd_ha:
        pointer to host adapter structure

.. _`asd_com_sas_isr`:

asd_com_sas_isr
===============

.. c:function:: void asd_com_sas_isr(struct asd_ha_struct *asd_ha)

    - process device communication interrupt (COMINT)

    :param struct asd_ha_struct \*asd_ha:
        pointer to host adapter structure

.. _`asd_dch_sas_isr`:

asd_dch_sas_isr
===============

.. c:function:: void asd_dch_sas_isr(struct asd_ha_struct *asd_ha)

    - process device channel interrupt (DEVINT)

    :param struct asd_ha_struct \*asd_ha:
        pointer to host adapter structure

.. _`asd_rbi_exsi_isr`:

asd_rbi_exsi_isr
================

.. c:function:: void asd_rbi_exsi_isr(struct asd_ha_struct *asd_ha)

    - process external system interface interrupt (INITERR)

    :param struct asd_ha_struct \*asd_ha:
        pointer to host adapter structure

.. _`asd_hst_pcix_isr`:

asd_hst_pcix_isr
================

.. c:function:: void asd_hst_pcix_isr(struct asd_ha_struct *asd_ha)

    - process host interface interrupts

    :param struct asd_ha_struct \*asd_ha:
        pointer to host adapter structure

.. _`asd_hst_pcix_isr.asserted-on-pcix-errors`:

Asserted on PCIX errors
-----------------------

target abort, etc.

.. _`asd_hw_isr`:

asd_hw_isr
==========

.. c:function:: irqreturn_t asd_hw_isr(int irq, void *dev_id)

    - host adapter interrupt service routine

    :param int irq:
        ignored

    :param void \*dev_id:
        pointer to host adapter structure

.. _`asd_hw_isr.description`:

Description
-----------

The ISR processes done list entries and level 3 error handling.

.. _`asd_ascb_alloc_list`:

asd_ascb_alloc_list
===================

.. c:function:: struct asd_ascb *asd_ascb_alloc_list(struct asd_ha_struct *asd_ha, int *num, gfp_t gfp_flags)

    - allocate a list of aSCBs

    :param struct asd_ha_struct \*asd_ha:
        pointer to host adapter structure

    :param int \*num:
        pointer to integer number of aSCBs

    :param gfp_t gfp_flags:
        GFP\_ flags.

.. _`asd_ascb_alloc_list.description`:

Description
-----------

This is the only function which is used to allocate aSCBs.
It can allocate one or many. If more than one, then they form

.. _`asd_ascb_alloc_list.a-linked-list-in-two-ways`:

a linked list in two ways
-------------------------

by their list field of the ascb struct
and by the next_scb field of the scb_header.

Returns NULL if no memory was available, else pointer to a list
of ascbs.  When this function returns, \ ``num``\  would be the number
of SCBs which were not able to be allocated, 0 if all requested
were able to be allocated.

.. _`asd_swap_head_scb`:

asd_swap_head_scb
=================

.. c:function:: void asd_swap_head_scb(struct asd_ha_struct *asd_ha, struct asd_ascb *ascb)

    - swap the head scb

    :param struct asd_ha_struct \*asd_ha:
        pointer to host adapter structure

    :param struct asd_ascb \*ascb:
        pointer to the head of an ascb list

.. _`asd_swap_head_scb.description`:

Description
-----------

The sequencer knows the DMA address of the next SCB to be DMAed to
the host adapter, from initialization or from the last list DMAed.
seq->next_scb keeps the address of this SCB.  The sequencer will
DMA to the host adapter this list of SCBs.  But the head (first
element) of this list is not known to the sequencer.  Here we swap
the head of the list with the known SCB (memcpy()).
Only one \ :c:func:`memcpy`\  is required per list so it is in our interest
to keep the list of SCB as long as possible so that the ratio
of number of memcpy calls to the number of SCB DMA-ed is as small
as possible.

.. _`asd_swap_head_scb.locking`:

LOCKING
-------

called with the pending list lock held.

.. _`asd_start_scb_timers`:

asd_start_scb_timers
====================

.. c:function:: void asd_start_scb_timers(struct list_head *list)

    - (add and) start timers of SCBs

    :param struct list_head \*list:
        pointer to struct list_head of the scbs

.. _`asd_start_scb_timers.description`:

Description
-----------

If an SCB in the \ ``list``\  has no timer function, assign the default
one,  then start the timer of the SCB.  This function is
intended to be called from \ :c:func:`asd_post_ascb_list`\ , just prior to
posting the SCBs to the sequencer.

.. _`asd_post_ascb_list`:

asd_post_ascb_list
==================

.. c:function:: int asd_post_ascb_list(struct asd_ha_struct *asd_ha, struct asd_ascb *ascb, int num)

    - post a list of 1 or more aSCBs to the host adapter

    :param struct asd_ha_struct \*asd_ha:
        pointer to a host adapter structure

    :param struct asd_ascb \*ascb:
        pointer to the first aSCB in the list

    :param int num:
        number of aSCBs in the list (to be posted)

.. _`asd_post_ascb_list.description`:

Description
-----------

See queueing comment in \ :c:func:`asd_post_escb_list`\ .

.. _`asd_post_ascb_list.additional-note-on-queuing`:

Additional note on queuing
--------------------------

In order to minimize the ratio of \ :c:func:`memcpy`\ 
to the number of ascbs sent, we try to batch-send as many ascbs as possible
in one go.

.. _`asd_post_ascb_list.two-cases-are-possible`:

Two cases are possible
----------------------

A) can_queue >= num,
B) can_queue < num.

.. _`asd_post_ascb_list.case-a`:

Case A
------

we can send the whole batch at once.  Increment "pending"
in the beginning of this function, when it is checked, in order to
eliminate races when this function is called by multiple processes.

.. _`asd_post_ascb_list.case-b`:

Case B
------

should never happen.

.. _`asd_post_escb_list`:

asd_post_escb_list
==================

.. c:function:: int asd_post_escb_list(struct asd_ha_struct *asd_ha, struct asd_ascb *ascb, int num)

    - post a list of 1 or more empty scb

    :param struct asd_ha_struct \*asd_ha:
        pointer to a host adapter structure

    :param struct asd_ascb \*ascb:
        pointer to the first empty SCB in the list

    :param int num:
        number of aSCBs in the list (to be posted)

.. _`asd_post_escb_list.description`:

Description
-----------

This is essentially the same as asd_post_ascb_list, but we do not
increment pending, add those to the pending list or get indexes.
See \ :c:func:`asd_init_escbs`\  and \ :c:func:`asd_init_post_escbs`\ .

Since sending a list of ascbs is a superset of sending a single
ascb, this function exists to generalize this.  More specifically,
when sending a list of those, we want to do only a \_single\_
\ :c:func:`memcpy`\  at swap head, as opposed to for each ascb sent (in the
case of sending them one by one).  That is, we want to minimize the
ratio of \ :c:func:`memcpy`\  operations to the number of ascbs sent.  The same
logic applies to \ :c:func:`asd_post_ascb_list`\ .

.. _`asd_turn_led`:

asd_turn_led
============

.. c:function:: void asd_turn_led(struct asd_ha_struct *asd_ha, int phy_id, int op)

    - turn on/off an LED

    :param struct asd_ha_struct \*asd_ha:
        pointer to host adapter structure

    :param int phy_id:
        the PHY id whose LED we want to manupulate

    :param int op:
        1 to turn on, 0 to turn off

.. _`asd_control_led`:

asd_control_led
===============

.. c:function:: void asd_control_led(struct asd_ha_struct *asd_ha, int phy_id, int op)

    - enable/disable an LED on the board

    :param struct asd_ha_struct \*asd_ha:
        pointer to host adapter structure

    :param int phy_id:
        integer, the phy id

    :param int op:
        integer, 1 to enable, 0 to disable the LED

.. _`asd_control_led.description`:

Description
-----------

First we output enable the LED, then we set the source
to be an external module.

.. This file was automatic generated / don't edit.

