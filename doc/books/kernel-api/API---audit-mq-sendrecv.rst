.. -*- coding: utf-8; mode: rst -*-

.. _API---audit-mq-sendrecv:

===================
__audit_mq_sendrecv
===================

*man __audit_mq_sendrecv(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
