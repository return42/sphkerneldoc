.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/qib/qib_driver.c

.. _`qib_wait_linkstate`:

qib_wait_linkstate
==================

.. c:function:: int qib_wait_linkstate(struct qib_pportdata *ppd, u32 state, int msecs)

    wait for an IB link state change to occur

    :param ppd:
        *undescribed*
    :type ppd: struct qib_pportdata \*

    :param state:
        the state to wait for
    :type state: u32

    :param msecs:
        the number of milliseconds to wait
    :type msecs: int

.. _`qib_wait_linkstate.description`:

Description
-----------

wait up to msecs milliseconds for IB link state change to occur for
now, take the easy polling route.  Currently used only by
qib_set_linkstate.  Returns 0 if state reached, otherwise
-ETIMEDOUT state can have multiple states set, for any of several
transitions.

.. _`qib_set_mtu`:

qib_set_mtu
===========

.. c:function:: int qib_set_mtu(struct qib_pportdata *ppd, u16 arg)

    set the MTU

    :param ppd:
        the perport data
    :type ppd: struct qib_pportdata \*

    :param arg:
        the new MTU
    :type arg: u16

.. _`qib_set_mtu.description`:

Description
-----------

We can handle "any" incoming size, the issue here is whether we
need to restrict our outgoing size.   For now, we don't do any
sanity checking on this, and we don't deal with what happens to
programs that are already running when the size changes.

.. _`qib_set_mtu.note`:

NOTE
----

changing the MTU will usually cause the IBC to go back to
link INIT state...

.. _`qib_reset_device`:

qib_reset_device
================

.. c:function:: int qib_reset_device(int unit)

    reset the chip if possible

    :param unit:
        the device to reset
    :type unit: int

.. _`qib_reset_device.description`:

Description
-----------

Whether or not reset is successful, we attempt to re-initialize the chip
(that is, much like a driver unload/reload).  We clear the INITTED flag
so that the various entry points will fail until we reinitialize.  For
now, we only allow this if no user contexts are open that use chip resources

.. This file was automatic generated / don't edit.

