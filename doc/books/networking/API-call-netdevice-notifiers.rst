.. -*- coding: utf-8; mode: rst -*-

.. _API-call-netdevice-notifiers:

========================
call_netdevice_notifiers
========================

*man call_netdevice_notifiers(9)*

*4.6.0-rc5*

call all network notifier blocks


Synopsis
========

.. c:function:: int call_netdevice_notifiers( unsigned long val, struct net_device * dev )

Arguments
=========

``val``
    value passed unmodified to notifier function

``dev``
    net_device pointer passed unmodified to notifier function


Description
===========

Call all network notifier blocks. Parameters and return value are as for
``raw_notifier_call_chain``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
