.. -*- coding: utf-8; mode: rst -*-

.. _API-idr-init:

========
idr_init
========

*man idr_init(9)*

*4.6.0-rc5*

initialize idr handle


Synopsis
========

.. c:function:: void idr_init( struct idr * idp )

Arguments
=========

``idp``
    idr handle


Description
===========

This function is use to set up the handle (``idp``) that you will pass
to the rest of the functions.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
