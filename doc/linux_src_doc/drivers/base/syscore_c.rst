.. -*- coding: utf-8; mode: rst -*-

=========
syscore.c
=========



.. _xref_register_syscore_ops:

register_syscore_ops
====================

.. c:function:: void register_syscore_ops (struct syscore_ops * ops)

    Register a set of system core operations.

    :param struct syscore_ops * ops:
        System core operations to register.




.. _xref_unregister_syscore_ops:

unregister_syscore_ops
======================

.. c:function:: void unregister_syscore_ops (struct syscore_ops * ops)

    Unregister a set of system core operations.

    :param struct syscore_ops * ops:
        System core operations to unregister.




.. _xref_syscore_suspend:

syscore_suspend
===============

.. c:function:: int syscore_suspend ( void)

    Execute all the registered system core suspend callbacks.

    :param void:
        no arguments



Description
-----------



This function is executed with one CPU on-line and disabled interrupts.




.. _xref_syscore_resume:

syscore_resume
==============

.. c:function:: void syscore_resume ( void)

    Execute all the registered system core resume callbacks.

    :param void:
        no arguments



Description
-----------



This function is executed with one CPU on-line and disabled interrupts.




.. _xref_syscore_shutdown:

syscore_shutdown
================

.. c:function:: void syscore_shutdown ( void)

    Execute all the registered system core shutdown callbacks.

    :param void:
        no arguments


