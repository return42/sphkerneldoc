.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/aic94xx/aic94xx_scb.c

.. _`asd_get_attached_sas_addr`:

asd_get_attached_sas_addr
=========================

.. c:function:: void asd_get_attached_sas_addr(struct asd_phy *phy, u8 *sas_addr)

    - extract/generate attached SAS address

    :param phy:
        *undescribed*
    :type phy: struct asd_phy \*

    :param sas_addr:
        *undescribed*
    :type sas_addr: u8 \*

.. _`asd_get_attached_sas_addr.phy`:

phy
---

pointer to asd_phy

.. _`asd_get_attached_sas_addr.sas_addr`:

sas_addr
--------

pointer to buffer where the SAS address is to be written

This function extracts the SAS address from an IDENTIFY frame
received.  If OOB is SATA, then a SAS address is generated from the
HA tables.

.. _`asd_get_attached_sas_addr.locking`:

LOCKING
-------

the frame_rcvd_lock needs to be held since this parses the frame
buffer.

.. _`asd_invalidate_edb`:

asd_invalidate_edb
==================

.. c:function:: void asd_invalidate_edb(struct asd_ascb *ascb, int edb_id)

    - invalidate an EDB and if necessary post the ESCB

    :param ascb:
        pointer to Empty SCB
    :type ascb: struct asd_ascb \*

    :param edb_id:
        index [0,6] to the empty data buffer which is to be invalidated
    :type edb_id: int

.. _`asd_invalidate_edb.description`:

Description
-----------

After an EDB has been invalidated, if all EDBs in this ESCB have been
invalidated, the ESCB is posted back to the sequencer.
Context is tasklet/IRQ.

.. _`control_phy_tasklet_complete`:

control_phy_tasklet_complete
============================

.. c:function:: void control_phy_tasklet_complete(struct asd_ascb *ascb, struct done_list_struct *dl)

    - tasklet complete for CONTROL PHY ascb

    :param ascb:
        pointer to an ascb
    :type ascb: struct asd_ascb \*

    :param dl:
        pointer to the done list entry
    :type dl: struct done_list_struct \*

.. _`control_phy_tasklet_complete.description`:

Description
-----------

This function completes a CONTROL PHY scb and frees the ascb.

.. _`control_phy_tasklet_complete.a-note-on-leds`:

A note on LEDs
--------------

- an LED blinks if there is IO though it,
- if a device is connected to the LED, it is lit,
- if no device is connected to the LED, is is dimmed (off).

.. _`asd_build_control_phy`:

asd_build_control_phy
=====================

.. c:function:: void asd_build_control_phy(struct asd_ascb *ascb, int phy_id, u8 subfunc)

    - build a CONTROL PHY SCB

    :param ascb:
        pointer to an ascb
    :type ascb: struct asd_ascb \*

    :param phy_id:
        phy id to control, integer
    :type phy_id: int

    :param subfunc:
        subfunction, what to actually to do the phy
    :type subfunc: u8

.. _`asd_build_control_phy.description`:

Description
-----------

This function builds a CONTROL PHY scb.  No allocation of any kind
is performed. \ ``ascb``\  is allocated with the list function.
The caller can override the ascb->tasklet_complete to point
to its own callback function.  It must call \ :c:func:`asd_ascb_free`\ 
at its tasklet complete function.
See the default implementation.

.. _`asd_ascb_timedout`:

asd_ascb_timedout
=================

.. c:function:: void asd_ascb_timedout(struct timer_list *t)

    - called when a pending SCB's timer has expired

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`asd_ascb_timedout.description`:

Description
-----------

This is the default timeout function which does the most necessary.
Upper layers can implement their own timeout function, say to free
resources they have with this SCB, and then call this one at the
end of their timeout function.  To do this, one should initialize
the ascb->timer.{function, expires} prior to calling the post
function. The timer is started by the post function.

.. This file was automatic generated / don't edit.

