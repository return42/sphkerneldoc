
.. _API-syscore-suspend:

===============
syscore_suspend
===============

*man syscore_suspend(9)*

*4.6.0-rc1*

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
