.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/char/hw_random/pseries-rng.c

.. _`pseries_rng_get_desired_dma`:

pseries_rng_get_desired_dma
===========================

.. c:function:: unsigned long pseries_rng_get_desired_dma(struct vio_dev *vdev)

    Return desired DMA allocate for CMO operations

    :param vdev:
        *undescribed*
    :type vdev: struct vio_dev \*

.. _`pseries_rng_get_desired_dma.description`:

Description
-----------

This is a required function for a driver to operate in a CMO environment
but this device does not make use of DMA allocations, return 0.

.. _`pseries_rng_get_desired_dma.return-value`:

Return value
------------

Number of bytes of IO data the driver will need to perform well -> 0

.. This file was automatic generated / don't edit.

