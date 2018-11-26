.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/uwb/whci.c

.. _`whci_wait_for`:

whci_wait_for
=============

.. c:function:: int whci_wait_for(struct device *dev, u32 __iomem *reg, u32 mask, u32 result, unsigned long max_ms, const char *tag)

    wait for a WHCI register to be set

    :param dev:
        *undescribed*
    :type dev: struct device \*

    :param reg:
        *undescribed*
    :type reg: u32 __iomem \*

    :param mask:
        *undescribed*
    :type mask: u32

    :param result:
        *undescribed*
    :type result: u32

    :param max_ms:
        *undescribed*
    :type max_ms: unsigned long

    :param tag:
        *undescribed*
    :type tag: const char \*

.. _`whci_wait_for.description`:

Description
-----------

Polls (for at most \ ``max_ms``\  ms) until '\*@reg & \ ``mask``\  == \ ``result``\ '.

.. This file was automatic generated / don't edit.

