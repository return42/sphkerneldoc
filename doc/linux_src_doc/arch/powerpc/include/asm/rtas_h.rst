.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/include/asm/rtas.h

.. _`rtas_config_addr`:

rtas_config_addr
================

.. c:function:: u32 rtas_config_addr(int busno, int devfn, int reg)

    Format a busno, devfn and reg for RTAS.

    :param int busno:
        The bus number.

    :param int devfn:
        The device and function number as encoded by \ :c:func:`PCI_DEVFN`\ .

    :param int reg:
        The register number.

.. _`rtas_config_addr.description`:

Description
-----------

This function encodes the given busno, devfn and register number as
required for RTAS calls that take a "config_addr" parameter.
See PAPR requirement 7.3.4-1 for more info.

.. This file was automatic generated / don't edit.

