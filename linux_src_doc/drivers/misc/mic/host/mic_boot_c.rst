.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mic/host/mic_boot.c

.. _`mic_request_dma_chans`:

mic_request_dma_chans
=====================

.. c:function:: int mic_request_dma_chans(struct mic_device *mdev)

    Request DMA channels

    :param mdev:
        pointer to mic_device instance
    :type mdev: struct mic_device \*

.. _`mic_request_dma_chans.description`:

Description
-----------

returns number of DMA channels acquired

.. _`mic_free_dma_chans`:

mic_free_dma_chans
==================

.. c:function:: void mic_free_dma_chans(struct mic_device *mdev)

    release DMA channels

    :param mdev:
        pointer to mic_device instance
    :type mdev: struct mic_device \*

.. _`mic_free_dma_chans.description`:

Description
-----------

returns none

.. _`_mic_start`:

\_mic_start
===========

.. c:function:: int _mic_start(struct cosm_device *cdev, int id)

    Start the MIC.

    :param cdev:
        pointer to cosm_device instance
    :type cdev: struct cosm_device \*

    :param id:
        MIC device id/index provided by COSM used in other drivers like SCIF
    :type id: int

.. _`_mic_start.description`:

Description
-----------

This function prepares an MIC for boot and initiates boot.

.. _`_mic_start.return`:

Return
------

An appropriate -ERRNO error value on error, or zero for success.

For all cosm_hw_ops the caller holds a mutex to ensure serialization.

.. _`_mic_stop`:

\_mic_stop
==========

.. c:function:: void _mic_stop(struct cosm_device *cdev, bool force)

    Prepare the MIC for reset and trigger reset.

    :param cdev:
        pointer to cosm_device instance
    :type cdev: struct cosm_device \*

    :param force:
        force a MIC to reset even if it is already offline.
    :type force: bool

.. _`_mic_stop.return`:

Return
------

None.

.. This file was automatic generated / don't edit.

