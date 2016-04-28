.. -*- coding: utf-8; mode: rst -*-

.. _API-input-unregister-handle:

=======================
input_unregister_handle
=======================

*man input_unregister_handle(9)*

*4.6.0-rc5*

unregister an input handle


Synopsis
========

.. c:function:: void input_unregister_handle( struct input_handle * handle )

Arguments
=========

``handle``
    handle to unregister


Description
===========

This function removes input handle from device's and handler's lists.

This function is supposed to be called from handler's ``disconnect``
method.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
