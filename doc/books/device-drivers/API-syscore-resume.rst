.. -*- coding: utf-8; mode: rst -*-

.. _API-syscore-resume:

==============
syscore_resume
==============

*man syscore_resume(9)*

*4.6.0-rc5*

Execute all the registered system core resume callbacks.


Synopsis
========

.. c:function:: void syscore_resume( void )

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
