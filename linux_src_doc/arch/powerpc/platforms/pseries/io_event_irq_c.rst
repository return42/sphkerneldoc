.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/platforms/pseries/io_event_irq.c

.. _`ioei_find_event`:

ioei_find_event
===============

.. c:function:: struct pseries_io_event *ioei_find_event(struct rtas_error_log *elog)

    :param elog:
        RTAS error/event log.
    :type elog: struct rtas_error_log \*

.. _`ioei_find_event.return`:

Return
------

pointer to a valid IO event section data. NULL if not found.

.. This file was automatic generated / don't edit.

