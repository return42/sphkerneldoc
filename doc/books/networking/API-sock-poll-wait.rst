
.. _API-sock-poll-wait:

==============
sock_poll_wait
==============

*man sock_poll_wait(9)*

*4.6.0-rc1*

place memory barrier behind the poll_wait call.


Synopsis
========

.. c:function:: void sock_poll_wait( struct file * filp, wait_queue_head_t * wait_address, poll_table * p )

Arguments
=========

``filp``
    file

``wait_address``
    socket wait queue

``p``
    poll_table


Description
===========

See the comments in the wq_has_sleeper function.
