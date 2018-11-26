.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/talitos.c

.. _`talitos_submit`:

talitos_submit
==============

.. c:function:: int talitos_submit(struct device *dev, int ch, struct talitos_desc *desc, void (*callback)(struct device *dev, struct talitos_desc *desc, void *context, int error), void *context)

    submits a descriptor to the device for processing

    :param dev:
        the SEC device to be used
    :type dev: struct device \*

    :param ch:
        the SEC device channel to be used
    :type ch: int

    :param desc:
        the descriptor to be processed by the device
    :type desc: struct talitos_desc \*

    :param void (\*callback)(struct device \*dev, struct talitos_desc \*desc, void \*context, int error):
        whom to call when processing is complete

    :param context:
        a handle for use by caller (optional)
    :type context: void \*

.. _`talitos_submit.description`:

Description
-----------

desc must contain valid dma-mapped (bus physical) address pointers.
callback must check err and feedback in descriptor header
for device processing status.

.. This file was automatic generated / don't edit.

