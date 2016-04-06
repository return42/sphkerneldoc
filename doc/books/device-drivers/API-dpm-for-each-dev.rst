
.. _API-dpm-for-each-dev:

================
dpm_for_each_dev
================

*man dpm_for_each_dev(9)*

*4.6.0-rc1*

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

Iterate over devices in dpm_list, and call ``fn`` for each device, passing it ``data``.
