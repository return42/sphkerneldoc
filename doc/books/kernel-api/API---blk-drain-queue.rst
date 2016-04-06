
.. _API---blk-drain-queue:

=================
__blk_drain_queue
=================

*man __blk_drain_queue(9)*

*4.6.0-rc1*

drain requests from request_queue


Synopsis
========

.. c:function:: void __blk_drain_queue( struct request_queue * q, bool drain_all )

Arguments
=========

``q``
    queue to drain

``drain_all``
    whether to drain all requests or only the ones w/ ELVPRIV


Description
===========

Drain requests from ``q``. If ``drain_all`` is set, all requests are drained. If not, only ELVPRIV requests are drained. The caller is responsible for ensuring that no new requests
which need to be drained are queued.
