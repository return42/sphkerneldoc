.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-imx/tzic.c

.. _`tzic_enable_wake`:

tzic_enable_wake
================

.. c:function:: int tzic_enable_wake( void)

    enable wakeup interrupt

    :param  void:
        no arguments

.. _`tzic_enable_wake.description`:

Description
-----------

@return                      0 if successful; non-zero otherwise

This function provides an interrupt synchronization point that is required
by tzic enabled platforms before entering imx specific low power modes (ie,
those low power modes beyond the WAIT_CLOCKED basic ARM WFI only mode).

.. This file was automatic generated / don't edit.

