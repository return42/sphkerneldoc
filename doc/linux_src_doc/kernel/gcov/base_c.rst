.. -*- coding: utf-8; mode: rst -*-

======
base.c
======


.. _`gcov_enable_events`:

gcov_enable_events
==================

.. c:function:: void gcov_enable_events ( void)

    enable event reporting through gcov_event()

    :param void:
        no arguments



.. _`gcov_enable_events.description`:

Description
-----------


Turn on reporting of profiling data load/unload-events through the
:c:func:`gcov_event` callback. Also replay all previous events once. This function
is needed because some events are potentially generated too early for the
callback implementation to handle them initially.

