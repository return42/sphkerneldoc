.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/fpga/fpga-mgr.c

.. _`fpga_mgr_buf_load`:

fpga_mgr_buf_load
=================

.. c:function:: int fpga_mgr_buf_load(struct fpga_manager *mgr, struct fpga_image_info *info, const char *buf, size_t count)

    load fpga from image in buffer

    :param struct fpga_manager \*mgr:
        fpga manager

    :param struct fpga_image_info \*info:
        fpga image specific information

    :param const char \*buf:
        buffer contain fpga image

    :param size_t count:
        byte count of buf

.. _`fpga_mgr_buf_load.description`:

Description
-----------

Step the low level fpga manager through the device-specific steps of getting
an FPGA ready to be configured, writing the image to it, then doing whatever
post-configuration steps necessary.  This code assumes the caller got the
mgr pointer from \ :c:func:`of_fpga_mgr_get`\  or \ :c:func:`fpga_mgr_get`\  and checked that it is
not an error code.

.. _`fpga_mgr_buf_load.return`:

Return
------

0 on success, negative error code otherwise.

.. _`fpga_mgr_firmware_load`:

fpga_mgr_firmware_load
======================

.. c:function:: int fpga_mgr_firmware_load(struct fpga_manager *mgr, struct fpga_image_info *info, const char *image_name)

    request firmware and load to fpga

    :param struct fpga_manager \*mgr:
        fpga manager

    :param struct fpga_image_info \*info:
        fpga image specific information

    :param const char \*image_name:
        name of image file on the firmware search path

.. _`fpga_mgr_firmware_load.description`:

Description
-----------

Request an FPGA image using the firmware class, then write out to the FPGA.
Update the state before each step to provide info on what step failed if
there is a failure.  This code assumes the caller got the mgr pointer
from \ :c:func:`of_fpga_mgr_get`\  or \ :c:func:`fpga_mgr_get`\  and checked that it is not an error
code.

.. _`fpga_mgr_firmware_load.return`:

Return
------

0 on success, negative error code otherwise.

.. _`fpga_mgr_get`:

fpga_mgr_get
============

.. c:function:: struct fpga_manager *fpga_mgr_get(struct device *dev)

    get an exclusive reference to a fpga mgr

    :param struct device \*dev:
        parent device that fpga mgr was registered with

.. _`fpga_mgr_get.description`:

Description
-----------

Given a device, get an exclusive reference to a fpga mgr.

.. _`fpga_mgr_get.return`:

Return
------

fpga manager struct or \ :c:func:`IS_ERR`\  condition containing error code.

.. _`of_fpga_mgr_get`:

of_fpga_mgr_get
===============

.. c:function:: struct fpga_manager *of_fpga_mgr_get(struct device_node *node)

    get an exclusive reference to a fpga mgr

    :param struct device_node \*node:
        device node

.. _`of_fpga_mgr_get.description`:

Description
-----------

Given a device node, get an exclusive reference to a fpga mgr.

.. _`of_fpga_mgr_get.return`:

Return
------

fpga manager struct or \ :c:func:`IS_ERR`\  condition containing error code.

.. _`fpga_mgr_put`:

fpga_mgr_put
============

.. c:function:: void fpga_mgr_put(struct fpga_manager *mgr)

    release a reference to a fpga manager

    :param struct fpga_manager \*mgr:
        fpga manager structure

.. _`fpga_mgr_register`:

fpga_mgr_register
=================

.. c:function:: int fpga_mgr_register(struct device *dev, const char *name, const struct fpga_manager_ops *mops, void *priv)

    register a low level fpga manager driver

    :param struct device \*dev:
        fpga manager device from pdev

    :param const char \*name:
        fpga manager name

    :param const struct fpga_manager_ops \*mops:
        pointer to structure of fpga manager ops

    :param void \*priv:
        fpga manager private data

.. _`fpga_mgr_register.return`:

Return
------

0 on success, negative error code otherwise.

.. _`fpga_mgr_unregister`:

fpga_mgr_unregister
===================

.. c:function:: void fpga_mgr_unregister(struct device *dev)

    unregister a low level fpga manager driver

    :param struct device \*dev:
        fpga manager device from pdev

.. This file was automatic generated / don't edit.

