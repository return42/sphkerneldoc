.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/ibm/ibmveth.c

.. _`ibmveth_get_desired_dma`:

ibmveth_get_desired_dma
=======================

.. c:function:: unsigned long ibmveth_get_desired_dma(struct vio_dev *vdev)

    Calculate IO memory desired by the driver

    :param vdev:
        struct vio_dev for the device whose desired IO mem is to be returned
    :type vdev: struct vio_dev \*

.. _`ibmveth_get_desired_dma.return-value`:

Return value
------------

Number of bytes of IO data the driver will need to perform well.

.. This file was automatic generated / don't edit.

