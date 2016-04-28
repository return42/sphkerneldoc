.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-send-doorbell:

=================
rio_send_doorbell
=================

*man rio_send_doorbell(9)*

*4.6.0-rc5*

Send a doorbell message to a device


Synopsis
========

.. c:function:: int rio_send_doorbell( struct rio_dev * rdev, u16 data )

Arguments
=========

``rdev``
    RIO device

``data``
    Doorbell message data


Description
===========

Send a doorbell message to a RIO device. The doorbell message has a
16-bit info field provided by the ``data`` argument.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
