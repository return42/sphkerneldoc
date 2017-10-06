.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/nand/nandsim.c

.. _`nandsim_debugfs_create`:

nandsim_debugfs_create
======================

.. c:function:: int nandsim_debugfs_create(struct nandsim *dev)

    initialize debugfs

    :param struct nandsim \*dev:
        nandsim device description object

.. _`nandsim_debugfs_create.description`:

Description
-----------

This function creates all debugfs files for UBI device \ ``ubi``\ . Returns zero in
case of success and a negative error code in case of failure.

.. This file was automatic generated / don't edit.

