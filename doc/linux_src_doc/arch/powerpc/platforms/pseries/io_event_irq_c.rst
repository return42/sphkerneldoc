.. -*- coding: utf-8; mode: rst -*-

==============
io_event_irq.c
==============


.. _`ioei_find_event`:

ioei_find_event
===============

.. c:function:: struct pseries_io_event *ioei_find_event (struct rtas_error_log *elog)

    :param struct rtas_error_log \*elog:
        RTAS error/event log.



.. _`ioei_find_event.return`:

Return
------

pointer to a valid IO event section data. NULL if not found.

