
.. _API-syscore-resume:

==============
syscore_resume
==============

*man syscore_resume(9)*

*4.6.0-rc1*

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
