.. -*- coding: utf-8; mode: rst -*-

.. _API-dpm-for-each-dev:

================
dpm_for_each_dev
================

*man dpm_for_each_dev(9)*

*4.6.0-rc5*

device iterator.


Synopsis
========

.. c:function:: void dpm_for_each_dev( void * data, void (*fn) struct device *, void * )

Arguments
=========

``data``
    data for the callback.

``fn``
    function to be called for each device.


Description
===========

Iterate over devices in dpm_list, and call ``fn`` for each device,
passing it ``data``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
