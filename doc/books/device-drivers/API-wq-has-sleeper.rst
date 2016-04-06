
.. _API-wq-has-sleeper:

==============
wq_has_sleeper
==============

*man wq_has_sleeper(9)*

*4.6.0-rc1*

check if there are any waiting processes


Synopsis
========

.. c:function:: bool wq_has_sleeper( wait_queue_head_t * wq )

Arguments
=========

``wq``
    wait queue head


Description
===========

Returns true if wq has waiting processes

Please refer to the comment for waitqueue_active.
