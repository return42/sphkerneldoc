.. -*- coding: utf-8; mode: rst -*-

======
rtas.c
======


.. _`get_pseries_errorlog`:

get_pseries_errorlog
====================

.. c:function:: struct pseries_errorlog *get_pseries_errorlog (struct rtas_error_log *log, uint16_t section_id)

    :param struct rtas_error_log \*log:
        RTAS error/event log

    :param uint16_t section_id:
        two character section identifier



.. _`get_pseries_errorlog.description`:

Description
-----------

Returns a pointer to the specified errorlog or NULL if not found.

