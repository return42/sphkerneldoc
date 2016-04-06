
.. _API---audit-mq-getsetattr:

=====================
__audit_mq_getsetattr
=====================

*man __audit_mq_getsetattr(9)*

*4.6.0-rc1*

record audit data for a POSIX MQ get/set attribute


Synopsis
========

.. c:function:: void __audit_mq_getsetattr( mqd_t mqdes, struct mq_attr * mqstat )

Arguments
=========

``mqdes``
    MQ descriptor

``mqstat``
    MQ flags
