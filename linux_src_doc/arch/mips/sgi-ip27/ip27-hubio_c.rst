.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/sgi-ip27/ip27-hubio.c

.. _`hub_pio_map`:

hub_pio_map
===========

.. c:function:: unsigned long hub_pio_map(cnodeid_t cnode, xwidgetnum_t widget, unsigned long xtalk_addr, size_t size)

    establish a HUB PIO mapping

    :param cnode:
        *undescribed*
    :type cnode: cnodeid_t

    :param widget:
        widget ID to perform PIO mapping for
    :type widget: xwidgetnum_t

    :param xtalk_addr:
        xtalk_address that needs to be mapped
    :type xtalk_addr: unsigned long

    :param size:
        size of the PIO mapping
    :type size: size_t

.. _`hub_set_piomode`:

hub_set_piomode
===============

.. c:function:: void hub_set_piomode(nasid_t nasid)

    set pio mode for a given hub

    :param nasid:
        physical node ID for the hub in question
    :type nasid: nasid_t

.. _`hub_set_piomode.description`:

Description
-----------

Put the hub into either "PIO conveyor belt" mode or "fire-and-forget" mode.
To do this, we have to make absolutely sure that no PIOs are in progress
so we turn off access to all widgets for the duration of the function.

XXX - This code should really check what kind of widget we're talking
to.  Bridges can only handle three requests, but XG will do more.
How many can crossbow handle to widget 0?  We're assuming 1.

XXX - There is a bug in the crossbow that link reset PIOs do not
return write responses.  The easiest solution to this problem is to
leave widget 0 (xbow) in fire-and-forget mode at all times.  This
only affects pio's to xbow registers, which should be rare.

.. This file was automatic generated / don't edit.

