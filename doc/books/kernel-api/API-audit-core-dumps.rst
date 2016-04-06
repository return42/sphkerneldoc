
.. _API-audit-core-dumps:

================
audit_core_dumps
================

*man audit_core_dumps(9)*

*4.6.0-rc1*

record information about processes that end abnormally


Synopsis
========

.. c:function:: void audit_core_dumps( long signr )

Arguments
=========

``signr``
    signal value


Description
===========

If a process ends with a core dump, something fishy is going on and we should record the event for investigation.
