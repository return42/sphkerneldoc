.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clocksource/timer-ti-dm.c

.. _`omap_dm_timer_read_reg`:

omap_dm_timer_read_reg
======================

.. c:function:: u32 omap_dm_timer_read_reg(struct omap_dm_timer *timer, u32 reg)

    read timer registers in posted and non-posted mode

    :param struct omap_dm_timer \*timer:
        timer pointer over which read operation to perform

    :param u32 reg:
        lowest byte holds the register offset

.. _`omap_dm_timer_read_reg.description`:

Description
-----------

The posted mode bit is encoded in reg. Note that in posted mode write
pending bit must be checked. Otherwise a read of a non completed write
will produce an error.

.. _`omap_dm_timer_write_reg`:

omap_dm_timer_write_reg
=======================

.. c:function:: void omap_dm_timer_write_reg(struct omap_dm_timer *timer, u32 reg, u32 value)

    write timer registers in posted and non-posted mode

    :param struct omap_dm_timer \*timer:
        timer pointer over which write operation is to perform

    :param u32 reg:
        lowest byte holds the register offset

    :param u32 value:
        data to write into the register

.. _`omap_dm_timer_write_reg.description`:

Description
-----------

The posted mode bit is encoded in reg. Note that in posted mode the write
pending bit must be checked. Otherwise a write on a register which has a
pending write will be lost.

.. _`omap_dm_timer_request_by_cap`:

omap_dm_timer_request_by_cap
============================

.. c:function:: struct omap_dm_timer *omap_dm_timer_request_by_cap(u32 cap)

    Request a timer by capability

    :param u32 cap:
        Bit mask of capabilities to match

.. _`omap_dm_timer_request_by_cap.description`:

Description
-----------

Find a timer based upon capabilities bit mask. Callers of this function
should use the definitions found in the plat/dmtimer.h file under the
comment "timer capabilities used in hwmod database". Returns pointer to
timer handle on success and a NULL pointer on failure.

.. _`omap_dm_timer_request_by_node`:

omap_dm_timer_request_by_node
=============================

.. c:function:: struct omap_dm_timer *omap_dm_timer_request_by_node(struct device_node *np)

    Request a timer by device-tree node

    :param struct device_node \*np:
        Pointer to device-tree timer node

.. _`omap_dm_timer_request_by_node.description`:

Description
-----------

Request a timer based upon a device node pointer. Returns pointer to
timer handle on success and a NULL pointer on failure.

.. _`omap_dm_timer_modify_idlect_mask`:

omap_dm_timer_modify_idlect_mask
================================

.. c:function:: __u32 omap_dm_timer_modify_idlect_mask(__u32 inputmask)

    Check if any running timers use ARMXOR

    :param __u32 inputmask:
        current value of idlect mask

.. _`omap_dm_timer_set_int_disable`:

omap_dm_timer_set_int_disable
=============================

.. c:function:: int omap_dm_timer_set_int_disable(struct omap_dm_timer *timer, u32 mask)

    disable timer interrupts

    :param struct omap_dm_timer \*timer:
        pointer to timer handle

    :param u32 mask:
        bit mask of interrupts to be disabled

.. _`omap_dm_timer_set_int_disable.description`:

Description
-----------

Disables the specified timer interrupts for a timer.

.. _`omap_dm_timer_probe`:

omap_dm_timer_probe
===================

.. c:function:: int omap_dm_timer_probe(struct platform_device *pdev)

    probe function called for every registered device

    :param struct platform_device \*pdev:
        pointer to current timer platform device

.. _`omap_dm_timer_probe.description`:

Description
-----------

Called by driver framework at the end of device registration for all
timer devices.

.. _`omap_dm_timer_remove`:

omap_dm_timer_remove
====================

.. c:function:: int omap_dm_timer_remove(struct platform_device *pdev)

    cleanup a registered timer device

    :param struct platform_device \*pdev:
        pointer to current timer platform device

.. _`omap_dm_timer_remove.description`:

Description
-----------

Called by driver framework whenever a timer device is unregistered.
In addition to freeing platform resources it also deletes the timer
entry from the local list.

.. This file was automatic generated / don't edit.

