.. -*- coding: utf-8; mode: rst -*-

=============
am437x-vpfe.c
=============



.. _xref_vpfe_schedule_next_buffer:

vpfe_schedule_next_buffer
=========================

.. c:function:: void vpfe_schedule_next_buffer (struct vpfe_device * vpfe)

    

    :param struct vpfe_device * vpfe:
        ptr to vpfe device



Description
-----------

This function will get next buffer from the dma queue and
set the buffer address in the vpfe register for capture.
the buffer is marked active


Assumes caller is holding vpfe->dma_queue_lock already


