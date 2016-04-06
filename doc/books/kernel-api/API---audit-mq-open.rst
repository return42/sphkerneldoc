
.. _API---audit-mq-open:

===============
__audit_mq_open
===============

*man __audit_mq_open(9)*

*4.6.0-rc1*

record audit data for a POSIX MQ open


Synopsis
========

.. c:function:: void __audit_mq_open( int oflag, umode_t mode, struct mq_attr * attr )

Arguments
=========

``oflag``
    open flag

``mode``
    mode bits

``attr``
    queue attributes
