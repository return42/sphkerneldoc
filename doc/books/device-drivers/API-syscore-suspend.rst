.. -*- coding: utf-8; mode: rst -*-

.. _API-syscore-suspend:

===============
syscore_suspend
===============

*man syscore_suspend(9)*

*4.6.0-rc5*

Execute all the registered system core suspend callbacks.


Synopsis
========

.. c:function:: int syscore_suspend( void )

Arguments
=========

``void``
    no arguments


Description
===========

This function is executed with one CPU on-line and disabled interrupts.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
