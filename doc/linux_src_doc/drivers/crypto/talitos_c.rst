.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/talitos.c

.. _`talitos_submit`:

talitos_submit
==============

.. c:function:: int talitos_submit(struct device *dev, int ch, struct talitos_desc *desc, void (*) callback (struct device *dev, struct talitos_desc *desc, void *context, int error, void *context)

    submits a descriptor to the device for processing

    :param struct device \*dev:
        the SEC device to be used

    :param int ch:
        the SEC device channel to be used

    :param struct talitos_desc \*desc:
        the descriptor to be processed by the device

    :param (void (\*) callback (struct device \*dev, struct talitos_desc \*desc, void \*context, int error):
        whom to call when processing is complete

    :param void \*context:
        a handle for use by caller (optional)

.. _`talitos_submit.description`:

Description
-----------

desc must contain valid dma-mapped (bus physical) address pointers.
callback must check err and feedback in descriptor header
for device processing status.

.. This file was automatic generated / don't edit.

