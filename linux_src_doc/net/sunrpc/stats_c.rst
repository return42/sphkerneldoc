.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sunrpc/stats.c

.. _`rpc_alloc_iostats`:

rpc_alloc_iostats
=================

.. c:function:: struct rpc_iostats *rpc_alloc_iostats(struct rpc_clnt *clnt)

    allocate an rpc_iostats structure

    :param clnt:
        RPC program, version, and xprt
    :type clnt: struct rpc_clnt \*

.. _`rpc_free_iostats`:

rpc_free_iostats
================

.. c:function:: void rpc_free_iostats(struct rpc_iostats *stats)

    release an rpc_iostats structure

    :param stats:
        doomed rpc_iostats structure
    :type stats: struct rpc_iostats \*

.. _`rpc_count_iostats_metrics`:

rpc_count_iostats_metrics
=========================

.. c:function:: void rpc_count_iostats_metrics(const struct rpc_task *task, struct rpc_iostats *op_metrics)

    tally up per-task stats

    :param task:
        completed rpc_task
    :type task: const struct rpc_task \*

    :param op_metrics:
        stat structure for OP that will accumulate stats from \ ``task``\ 
    :type op_metrics: struct rpc_iostats \*

.. _`rpc_count_iostats`:

rpc_count_iostats
=================

.. c:function:: void rpc_count_iostats(const struct rpc_task *task, struct rpc_iostats *stats)

    tally up per-task stats

    :param task:
        completed rpc_task
    :type task: const struct rpc_task \*

    :param stats:
        array of stat structures
    :type stats: struct rpc_iostats \*

.. _`rpc_count_iostats.description`:

Description
-----------

Uses the statidx from \ ``task``\ 

.. This file was automatic generated / don't edit.

