
.. _API-dpm-resume-start:

================
dpm_resume_start
================

*man dpm_resume_start(9)*

*4.6.0-rc1*

Execute “noirq” and “early” device callbacks.


Synopsis
========

.. c:function:: void dpm_resume_start( pm_message_t state )

Arguments
=========

``state``
    PM transition of the system being carried out.
