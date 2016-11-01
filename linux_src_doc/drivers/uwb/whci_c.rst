.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/uwb/whci.c

.. _`whci_wait_for`:

whci_wait_for
=============

.. c:function:: int whci_wait_for(struct device *dev, u32 __iomem *reg, u32 mask, u32 result, unsigned long max_ms, const char *tag)

    wait for a WHCI register to be set

    :param struct device \*dev:
        *undescribed*

    :param u32 __iomem \*reg:
        *undescribed*

    :param u32 mask:
        *undescribed*

    :param u32 result:
        *undescribed*

    :param unsigned long max_ms:
        *undescribed*

    :param const char \*tag:
        *undescribed*

.. _`whci_wait_for.description`:

Description
-----------

Polls (for at most \ ``max_ms``\  ms) until '\*@reg & \ ``mask``\  == \ ``result``\ '.

.. This file was automatic generated / don't edit.

