.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/trace/events/ipi.h

.. _`trace_ipi_raise`:

trace_ipi_raise
===============

.. c:function:: void trace_ipi_raise(const struct cpumask *mask, const char *reason)

    called when a smp cross call is made

    :param mask:
        mask of recipient CPUs for the IPI
    :type mask: const struct cpumask \*

    :param reason:
        string identifying the IPI purpose
    :type reason: const char \*

.. _`trace_ipi_raise.description`:

Description
-----------

It is necessary for \ ``reason``\  to be a static string declared with
\__tracepoint_string.

.. _`trace_ipi_entry`:

trace_ipi_entry
===============

.. c:function:: void trace_ipi_entry(const char *reason)

    called immediately before the IPI handler

    :param reason:
        string identifying the IPI purpose
    :type reason: const char \*

.. _`trace_ipi_entry.description`:

Description
-----------

It is necessary for \ ``reason``\  to be a static string declared with
\__tracepoint_string, ideally the same as used with trace_ipi_raise
for that IPI.

.. _`trace_ipi_exit`:

trace_ipi_exit
==============

.. c:function:: void trace_ipi_exit(const char *reason)

    called immediately after the IPI handler returns

    :param reason:
        string identifying the IPI purpose
    :type reason: const char \*

.. _`trace_ipi_exit.description`:

Description
-----------

It is necessary for \ ``reason``\  to be a static string declared with
\__tracepoint_string, ideally the same as used with trace_ipi_raise for
that IPI.

.. This file was automatic generated / don't edit.

