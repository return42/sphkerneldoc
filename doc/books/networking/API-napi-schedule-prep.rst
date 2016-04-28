.. -*- coding: utf-8; mode: rst -*-

.. _API-napi-schedule-prep:

==================
napi_schedule_prep
==================

*man napi_schedule_prep(9)*

*4.6.0-rc5*

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

Test if NAPI routine is already running, and if not mark it as running.
This is used as a condition variable to insure only one NAPI poll
instance runs. We also make sure there is no pending NAPI disable.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
