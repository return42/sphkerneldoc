
.. _API-blk-attempt-plug-merge:

======================
blk_attempt_plug_merge
======================

*man blk_attempt_plug_merge(9)*

*4.6.0-rc1*

try to merge with ``current``'s plugged list


Synopsis
========

.. c:function:: bool blk_attempt_plug_merge( struct request_queue * q, struct bio * bio, unsigned int * request_count, struct request ** same_queue_rq )

Arguments
=========

``q``
    request_queue new bio is being queued at

``bio``
    new bio being queued

``request_count``
    out parameter for number of traversed plugged requests

``same_queue_rq``
    pointer to ``struct request`` that gets filled in when another request associated with ``q`` is found on the plug list (optional, may be ``NULL``)


Description
===========

Determine whether ``bio`` being queued on ``q`` can be merged with a request on ``current``'s plugged list. Returns ``true`` if merge was successful, otherwise ``false``.

Plugging coalesces IOs from the same issuer for the same purpose without going through ``q``->queue_lock. As such it's more of an issuing mechanism than scheduling, and the
request, while may have elvpriv data, is not added on the elevator at this point. In addition, we don't have reliable access to the elevator outside queue lock. Only check basic
merging parameters without querying the elevator.

Caller must ensure !blk_queue_nomerges(q) beforehand.
