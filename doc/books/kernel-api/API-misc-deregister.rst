.. -*- coding: utf-8; mode: rst -*-

.. _API-misc-deregister:

===============
misc_deregister
===============

*man misc_deregister(9)*

*4.6.0-rc5*

unregister a miscellaneous device


Synopsis
========

.. c:function:: void misc_deregister( struct miscdevice * misc )

Arguments
=========

``misc``
    device to unregister


Description
===========

Unregister a miscellaneous device that was previously successfully
registered with ``misc_register``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
