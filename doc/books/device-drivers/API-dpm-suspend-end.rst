
.. _API-dpm-suspend-end:

===============
dpm_suspend_end
===============

*man dpm_suspend_end(9)*

*4.6.0-rc1*

Execute “late” and “noirq” device suspend callbacks.


Synopsis
========

.. c:function:: int dpm_suspend_end( pm_message_t state )

Arguments
=========

``state``
    PM transition of the system being carried out.
