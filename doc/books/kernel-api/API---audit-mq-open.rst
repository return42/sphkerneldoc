.. -*- coding: utf-8; mode: rst -*-

.. _API---audit-mq-open:

===============
__audit_mq_open
===============

*man __audit_mq_open(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
