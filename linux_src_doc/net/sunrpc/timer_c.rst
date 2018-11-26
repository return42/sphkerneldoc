.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sunrpc/timer.c

.. _`rpc_init_rtt`:

rpc_init_rtt
============

.. c:function:: void rpc_init_rtt(struct rpc_rtt *rt, unsigned long timeo)

    Initialize an RPC RTT estimator context

    :param rt:
        context to initialize
    :type rt: struct rpc_rtt \*

    :param timeo:
        initial timeout value, in jiffies
    :type timeo: unsigned long

.. _`rpc_update_rtt`:

rpc_update_rtt
==============

.. c:function:: void rpc_update_rtt(struct rpc_rtt *rt, unsigned int timer, long m)

    Update an RPC RTT estimator context

    :param rt:
        context to update
    :type rt: struct rpc_rtt \*

    :param timer:
        timer array index (request type)
    :type timer: unsigned int

    :param m:
        recent actual RTT, in jiffies
    :type m: long

.. _`rpc_update_rtt.description`:

Description
-----------

NB: When computing the smoothed RTT and standard deviation,
be careful not to produce negative intermediate results.

.. _`rpc_calc_rto`:

rpc_calc_rto
============

.. c:function:: unsigned long rpc_calc_rto(struct rpc_rtt *rt, unsigned int timer)

    Provide an estimated timeout value

    :param rt:
        context to use for calculation
    :type rt: struct rpc_rtt \*

    :param timer:
        timer array index (request type)
    :type timer: unsigned int

.. _`rpc_calc_rto.description`:

Description
-----------

Estimate RTO for an NFS RPC sent via an unreliable datagram.  Use
the mean and mean deviation of RTT for the appropriate type of RPC
for frequently issued RPCs, and a fixed default for the others.

The justification for doing "other" this way is that these RPCs
happen so infrequently that timer estimation would probably be
stale.  Also, since many of these RPCs are non-idempotent, a
conservative timeout is desired.

getattr, lookup,
read, write, commit     - A+4D
other                   - timeo

.. This file was automatic generated / don't edit.

