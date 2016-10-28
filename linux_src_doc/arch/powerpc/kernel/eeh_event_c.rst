.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/kernel/eeh_event.c

.. _`eeh_event_handler`:

eeh_event_handler
=================

.. c:function:: int eeh_event_handler(void *dummy)

    Dispatch EEH events. \ ``dummy``\  - unused

    :param void \*dummy:
        *undescribed*

.. _`eeh_event_handler.description`:

Description
-----------

The detection of a frozen slot can occur inside an interrupt,
where it can be hard to do anything about it.  The goal of this
routine is to pull these detection events out of the context
of the interrupt handler, and re-dispatch them for processing
at a later time in a normal context.

.. _`eeh_event_init`:

eeh_event_init
==============

.. c:function:: int eeh_event_init( void)

    Start kernel thread to handle EEH events

    :param  void:
        no arguments

.. _`eeh_event_init.description`:

Description
-----------

This routine is called to start the kernel thread for processing
EEH event.

.. _`eeh_send_failure_event`:

eeh_send_failure_event
======================

.. c:function:: int eeh_send_failure_event(struct eeh_pe *pe)

    Generate a PCI error event

    :param struct eeh_pe \*pe:
        EEH PE

.. _`eeh_send_failure_event.description`:

Description
-----------

This routine can be called within an interrupt context;
the actual event will be delivered in a normal context
(from a workqueue).

.. _`eeh_remove_event`:

eeh_remove_event
================

.. c:function:: void eeh_remove_event(struct eeh_pe *pe, bool force)

    Remove EEH event from the queue

    :param struct eeh_pe \*pe:
        Event binding to the PE

    :param bool force:
        Event will be removed unconditionally

.. _`eeh_remove_event.description`:

Description
-----------

On PowerNV platform, we might have subsequent coming events
is part of the former one. For that case, those subsequent
coming events are totally duplicated and unnecessary, thus
they should be removed.

.. This file was automatic generated / don't edit.

