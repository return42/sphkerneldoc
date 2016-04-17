.. -*- coding: utf-8; mode: rst -*-

=============
events_base.c
=============


.. _`notify_remote_via_irq`:

notify_remote_via_irq
=====================

.. c:function:: void notify_remote_via_irq (int irq)

    send event to remote end of event channel via irq

    :param int irq:
        irq of event channel to send event to



.. _`notify_remote_via_irq.description`:

Description
-----------

Unlike :c:func:`notify_remote_via_evtchn`, this is safe to use across
save/restore. Notifications on a broken connection are silently
dropped.



.. _`xen_evtchn_nr_channels`:

xen_evtchn_nr_channels
======================

.. c:function:: unsigned xen_evtchn_nr_channels ( void)

    number of usable event channel ports

    :param void:
        no arguments



.. _`xen_evtchn_nr_channels.description`:

Description
-----------


This may be less than the maximum supported by the current
hypervisor ABI. Use :c:func:`xen_evtchn_max_channels` for the maximum
supported.



.. _`xen_set_irq_priority`:

xen_set_irq_priority
====================

.. c:function:: int xen_set_irq_priority (unsigned irq, unsigned priority)

    set an event channel priority.

    :param unsigned irq:
        irq bound to an event channel.

    :param unsigned priority:
        priority between XEN_IRQ_PRIORITY_MAX and XEN_IRQ_PRIORITY_MIN.

