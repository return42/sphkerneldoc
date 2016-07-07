.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/perf/ui/util.c

.. _`perf_error__register`:

perf_error__register
====================

.. c:function:: int perf_error__register(struct perf_error_ops *eops)

    Register error logging functions

    :param struct perf_error_ops \*eops:
        The pointer to error logging function struct

.. _`perf_error__register.description`:

Description
-----------

Register UI-specific error logging functions. Before calling this,
other logging functions should be unregistered, if any.

.. _`perf_error__unregister`:

perf_error__unregister
======================

.. c:function:: int perf_error__unregister(struct perf_error_ops *eops)

    Unregister error logging functions

    :param struct perf_error_ops \*eops:
        The pointer to error logging function struct

.. _`perf_error__unregister.description`:

Description
-----------

Unregister already registered error logging functions.

.. This file was automatic generated / don't edit.

