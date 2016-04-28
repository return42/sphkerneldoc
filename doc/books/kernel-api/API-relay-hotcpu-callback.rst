.. -*- coding: utf-8; mode: rst -*-

.. _API-relay-hotcpu-callback:

=====================
relay_hotcpu_callback
=====================

*man relay_hotcpu_callback(9)*

*4.6.0-rc5*

CPU hotplug callback


Synopsis
========

.. c:function:: int relay_hotcpu_callback( struct notifier_block * nb, unsigned long action, void * hcpu )

Arguments
=========

``nb``
    notifier block

``action``
    hotplug action to take

``hcpu``
    CPU number


Description
===========

Returns the success/failure of the operation. (``NOTIFY_OK``,
``NOTIFY_BAD``)


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
