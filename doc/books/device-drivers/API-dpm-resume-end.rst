
.. _API-dpm-resume-end:

==============
dpm_resume_end
==============

*man dpm_resume_end(9)*

*4.6.0-rc1*

Execute “resume” callbacks and complete system transition.


Synopsis
========

.. c:function:: void dpm_resume_end( pm_message_t state )

Arguments
=========

``state``
    PM transition of the system being carried out.


Description
===========

Execute “resume” callbacks for all devices and complete the PM transition of the system.
