.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/am437x/am437x-vpfe.c

.. _`vpfe_schedule_next_buffer`:

vpfe_schedule_next_buffer
=========================

.. c:function:: void vpfe_schedule_next_buffer(struct vpfe_device *vpfe)

    set next buffer address for capture

    :param vpfe:
        ptr to vpfe device
    :type vpfe: struct vpfe_device \*

.. _`vpfe_schedule_next_buffer.description`:

Description
-----------

This function will get next buffer from the dma queue and
set the buffer address in the vpfe register for capture.
the buffer is marked active

Assumes caller is holding vpfe->dma_queue_lock already

.. This file was automatic generated / don't edit.

