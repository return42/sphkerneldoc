
.. _API-call-netdevice-notifiers:

========================
call_netdevice_notifiers
========================

*man call_netdevice_notifiers(9)*

*4.6.0-rc1*

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

Call all network notifier blocks. Parameters and return value are as for ``raw_notifier_call_chain``.
