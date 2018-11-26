.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/gcov/base.c

.. _`gcov_enable_events`:

gcov_enable_events
==================

.. c:function:: void gcov_enable_events( void)

    enable event reporting through \ :c:func:`gcov_event`\ 

    :param void:
        no arguments
    :type void: 

.. _`gcov_enable_events.description`:

Description
-----------

Turn on reporting of profiling data load/unload-events through the
\ :c:func:`gcov_event`\  callback. Also replay all previous events once. This function
is needed because some events are potentially generated too early for the
callback implementation to handle them initially.

.. This file was automatic generated / don't edit.

