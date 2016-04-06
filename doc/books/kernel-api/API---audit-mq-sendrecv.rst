
.. _API---audit-mq-sendrecv:

===================
__audit_mq_sendrecv
===================

*man __audit_mq_sendrecv(9)*

*4.6.0-rc1*

record audit data for a POSIX MQ timed send/receive


Synopsis
========

.. c:function:: void __audit_mq_sendrecv( mqd_t mqdes, size_t msg_len, unsigned int msg_prio, const struct timespec * abs_timeout )

Arguments
=========

``mqdes``
    MQ descriptor

``msg_len``
    Message length

``msg_prio``
    Message priority

``abs_timeout``
    Message timeout in absolute time
