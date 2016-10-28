.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/char/hmcdrv_dev.c

.. _`hmcdrv_dev_name`:

hmcdrv_dev_name
===============

.. c:function:: char *hmcdrv_dev_name(struct device *dev, umode_t *mode)

    provides a naming hint for a device node in /dev

    :param struct device \*dev:
        device for which the naming/mode hint is

    :param umode_t \*mode:
        file mode for device node created in /dev

.. _`hmcdrv_dev_name.see`:

See
---

devtmpfs.c, function \ :c:func:`devtmpfs_create_node`\ 

.. _`hmcdrv_dev_name.return`:

Return
------

recommended device file name in /dev

.. _`hmcdrv_dev_init`:

hmcdrv_dev_init
===============

.. c:function:: int hmcdrv_dev_init( void)

    creates a HMC drive CD/DVD device

    :param  void:
        no arguments

.. _`hmcdrv_dev_init.description`:

Description
-----------

This function creates a HMC drive CD/DVD kernel device and an associated
device under /dev, using a dynamically allocated major number.

.. _`hmcdrv_dev_init.return`:

Return
------

0 on success, else an error code.

.. _`hmcdrv_dev_exit`:

hmcdrv_dev_exit
===============

.. c:function:: void hmcdrv_dev_exit( void)

    destroys a HMC drive CD/DVD device

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

