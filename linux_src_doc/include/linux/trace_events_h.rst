.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/trace_events.h

.. _`trace_trigger_soft_disabled`:

trace_trigger_soft_disabled
===========================

.. c:function:: bool trace_trigger_soft_disabled(struct trace_event_file *file)

    do triggers and test if soft disabled

    :param file:
        The file pointer of the event to test
    :type file: struct trace_event_file \*

.. _`trace_trigger_soft_disabled.description`:

Description
-----------

If any triggers without filters are attached to this event, they
will be called here. If the event is soft disabled and has no
triggers that require testing the fields, it will return true,
otherwise false.

.. This file was automatic generated / don't edit.

