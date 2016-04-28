.. -*- coding: utf-8; mode: rst -*-

.. _API-v4l2-ctrl-get-name:

==================
v4l2_ctrl_get_name
==================

*man v4l2_ctrl_get_name(9)*

*4.6.0-rc5*

Get the name of the control


Synopsis
========

.. c:function:: const char * v4l2_ctrl_get_name( u32 id )

Arguments
=========

``id``
    The control ID.


Description
===========

This function returns the name of the given control ID or NULL if it
isn't a known control.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
