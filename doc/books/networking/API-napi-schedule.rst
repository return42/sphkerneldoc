.. -*- coding: utf-8; mode: rst -*-

.. _API-napi-schedule:

=============
napi_schedule
=============

*man napi_schedule(9)*

*4.6.0-rc5*

schedule NAPI poll


Synopsis
========

.. c:function:: void napi_schedule( struct napi_struct * n )

Arguments
=========

``n``
    NAPI context


Description
===========

Schedule NAPI poll routine to be called if it is not already running.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
