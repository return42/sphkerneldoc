
.. _API---audit-mq-notify:

=================
__audit_mq_notify
=================

*man __audit_mq_notify(9)*

*4.6.0-rc1*

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
