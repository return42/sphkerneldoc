
.. _API-napi-schedule-prep:

==================
napi_schedule_prep
==================

*man napi_schedule_prep(9)*

*4.6.0-rc1*

check if NAPI can be scheduled


Synopsis
========

.. c:function:: bool napi_schedule_prep( struct napi_struct * n )

Arguments
=========

``n``
    NAPI context


Description
===========

Test if NAPI routine is already running, and if not mark it as running. This is used as a condition variable to insure only one NAPI poll instance runs. We also make sure there is
no pending NAPI disable.
