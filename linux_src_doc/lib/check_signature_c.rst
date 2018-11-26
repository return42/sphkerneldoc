.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/check_signature.c

.. _`check_signature`:

check_signature
===============

.. c:function:: int check_signature(const volatile void __iomem *io_addr, const unsigned char *signature, int length)

    find BIOS signatures

    :param io_addr:
        mmio address to check
    :type io_addr: const volatile void __iomem \*

    :param signature:
        signature block
    :type signature: const unsigned char \*

    :param length:
        length of signature
    :type length: int

.. _`check_signature.description`:

Description
-----------

Perform a signature comparison with the mmio address io_addr. This
address should have been obtained by ioremap.
Returns 1 on a match.

.. This file was automatic generated / don't edit.

