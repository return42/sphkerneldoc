.. -*- coding: utf-8; mode: rst -*-

.. _API-dpm-suspend-start:

=================
dpm_suspend_start
=================

*man dpm_suspend_start(9)*

*4.6.0-rc5*

Prepare devices for PM transition and suspend them.


Synopsis
========

.. c:function:: int dpm_suspend_start( pm_message_t state )

Arguments
=========

``state``
    PM transition of the system being carried out.


Description
===========

Prepare all non-sysdev devices for system PM transition and execute
“suspend” callbacks for them.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
