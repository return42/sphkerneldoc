
.. _API-dpm-suspend-start:

=================
dpm_suspend_start
=================

*man dpm_suspend_start(9)*

*4.6.0-rc1*

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

Prepare all non-sysdev devices for system PM transition and execute “suspend” callbacks for them.
