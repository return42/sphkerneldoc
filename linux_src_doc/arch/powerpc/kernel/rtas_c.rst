.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/kernel/rtas.c

.. _`get_pseries_errorlog`:

get_pseries_errorlog
====================

.. c:function:: struct pseries_errorlog *get_pseries_errorlog(struct rtas_error_log *log, uint16_t section_id)

    :param log:
        RTAS error/event log
    :type log: struct rtas_error_log \*

    :param section_id:
        two character section identifier
    :type section_id: uint16_t

.. _`get_pseries_errorlog.description`:

Description
-----------

Returns a pointer to the specified errorlog or NULL if not found.

.. This file was automatic generated / don't edit.

