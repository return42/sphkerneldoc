.. -*- coding: utf-8; mode: rst -*-

.. _API---audit-mq-getsetattr:

=====================
__audit_mq_getsetattr
=====================

*man __audit_mq_getsetattr(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
