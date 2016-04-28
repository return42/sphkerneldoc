.. -*- coding: utf-8; mode: rst -*-

.. _API-v4l2-ctrl-get-menu:

==================
v4l2_ctrl_get_menu
==================

*man v4l2_ctrl_get_menu(9)*

*4.6.0-rc5*

Get the menu string array of the control


Synopsis
========

.. c:function:: const char * const * v4l2_ctrl_get_menu( u32 id )

Arguments
=========

``id``
    The control ID.


Description
===========

This function returns the NULL-terminated menu string array name of the
given control ID or NULL if it isn't a known menu control.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
