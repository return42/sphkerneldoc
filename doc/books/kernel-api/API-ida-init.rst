.. -*- coding: utf-8; mode: rst -*-

.. _API-ida-init:

========
ida_init
========

*man ida_init(9)*

*4.6.0-rc5*

initialize ida handle


Synopsis
========

.. c:function:: void ida_init( struct ida * ida )

Arguments
=========

``ida``
    ida handle


Description
===========

This function is use to set up the handle (``ida``) that you will pass
to the rest of the functions.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
