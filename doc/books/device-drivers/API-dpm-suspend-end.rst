.. -*- coding: utf-8; mode: rst -*-

.. _API-dpm-suspend-end:

===============
dpm_suspend_end
===============

*man dpm_suspend_end(9)*

*4.6.0-rc5*

Execute “late” and “noirq” device suspend callbacks.


Synopsis
========

.. c:function:: int dpm_suspend_end( pm_message_t state )

Arguments
=========

``state``
    PM transition of the system being carried out.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
