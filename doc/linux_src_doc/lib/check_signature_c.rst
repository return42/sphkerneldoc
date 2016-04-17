.. -*- coding: utf-8; mode: rst -*-

=================
check_signature.c
=================


.. _`check_signature`:

check_signature
===============

.. c:function:: int check_signature (const volatile void __iomem *io_addr, const unsigned char *signature, int length)

    find BIOS signatures

    :param const volatile void __iomem \*io_addr:
        mmio address to check

    :param const unsigned char \*signature:
        signature block

    :param int length:
        length of signature



.. _`check_signature.description`:

Description
-----------

Perform a signature comparison with the mmio address io_addr. This
address should have been obtained by ioremap.
Returns 1 on a match.

