.. -*- coding: utf-8; mode: rst -*-

.. _API---audit-mq-notify:

=================
__audit_mq_notify
=================

*man __audit_mq_notify(9)*

*4.6.0-rc5*

record audit data for a POSIX MQ notify


Synopsis
========

.. c:function:: void __audit_mq_notify( mqd_t mqdes, const struct sigevent * notification )

Arguments
=========

``mqdes``
    MQ descriptor

``notification``
    Notification event


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
