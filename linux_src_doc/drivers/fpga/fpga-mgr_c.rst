.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/fpga/fpga-mgr.c

.. _`fpga_image_info_alloc`:

fpga_image_info_alloc
=====================

.. c:function:: struct fpga_image_info *fpga_image_info_alloc(struct device *dev)

    Allocate a FPGA image info struct

    :param dev:
        owning device
    :type dev: struct device \*

.. _`fpga_image_info_alloc.return`:

Return
------

struct fpga_image_info or NULL

.. _`fpga_image_info_free`:

fpga_image_info_free
====================

.. c:function:: void fpga_image_info_free(struct fpga_image_info *info)

    Free a FPGA image info struct

    :param info:
        FPGA image info struct to free
    :type info: struct fpga_image_info \*

.. _`fpga_mgr_buf_load_sg`:

fpga_mgr_buf_load_sg
====================

.. c:function:: int fpga_mgr_buf_load_sg(struct fpga_manager *mgr, struct fpga_image_info *info, struct sg_table *sgt)

    load fpga from image in buffer from a scatter list

    :param mgr:
        fpga manager
    :type mgr: struct fpga_manager \*

    :param info:
        fpga image specific information
    :type info: struct fpga_image_info \*

    :param sgt:
        scatterlist table
    :type sgt: struct sg_table \*

.. _`fpga_mgr_buf_load_sg.description`:

Description
-----------

Step the low level fpga manager through the device-specific steps of getting
an FPGA ready to be configured, writing the image to it, then doing whatever
post-configuration steps necessary.  This code assumes the caller got the
mgr pointer from \ :c:func:`of_fpga_mgr_get`\  or \ :c:func:`fpga_mgr_get`\  and checked that it is
not an error code.

This is the preferred entry point for FPGA programming, it does not require
any contiguous kernel memory.

.. _`fpga_mgr_buf_load_sg.return`:

Return
------

0 on success, negative error code otherwise.

.. _`fpga_mgr_buf_load`:

fpga_mgr_buf_load
=================

.. c:function:: int fpga_mgr_buf_load(struct fpga_manager *mgr, struct fpga_image_info *info, const char *buf, size_t count)

    load fpga from image in buffer

    :param mgr:
        fpga manager
    :type mgr: struct fpga_manager \*

    :param info:
        fpga image info
    :type info: struct fpga_image_info \*

    :param buf:
        buffer contain fpga image
    :type buf: const char \*

    :param count:
        byte count of buf
    :type count: size_t

.. _`fpga_mgr_buf_load.description`:

Description
-----------

Step the low level fpga manager through the device-specific steps of getting
an FPGA ready to be configured, writing the image to it, then doing whatever
post-configuration steps necessary.  This code assumes the caller got the
mgr pointer from \ :c:func:`of_fpga_mgr_get`\  and checked that it is not an error code.

.. _`fpga_mgr_buf_load.return`:

Return
------

0 on success, negative error code otherwise.

.. _`fpga_mgr_firmware_load`:

fpga_mgr_firmware_load
======================

.. c:function:: int fpga_mgr_firmware_load(struct fpga_manager *mgr, struct fpga_image_info *info, const char *image_name)

    request firmware and load to fpga

    :param mgr:
        fpga manager
    :type mgr: struct fpga_manager \*

    :param info:
        fpga image specific information
    :type info: struct fpga_image_info \*

    :param image_name:
        name of image file on the firmware search path
    :type image_name: const char \*

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

.. _`fpga_mgr_load`:

fpga_mgr_load
=============

.. c:function:: int fpga_mgr_load(struct fpga_manager *mgr, struct fpga_image_info *info)

    load FPGA from scatter/gather table, buffer, or firmware

    :param mgr:
        fpga manager
    :type mgr: struct fpga_manager \*

    :param info:
        fpga image information.
    :type info: struct fpga_image_info \*

.. _`fpga_mgr_load.description`:

Description
-----------

Load the FPGA from an image which is indicated in \ ``info``\ .  If successful, the
FPGA ends up in operating mode.

.. _`fpga_mgr_load.return`:

Return
------

0 on success, negative error code otherwise.

.. _`fpga_mgr_get`:

fpga_mgr_get
============

.. c:function:: struct fpga_manager *fpga_mgr_get(struct device *dev)

    Given a device, get a reference to a fpga mgr.

    :param dev:
        parent device that fpga mgr was registered with
    :type dev: struct device \*

.. _`fpga_mgr_get.return`:

Return
------

fpga manager struct or \ :c:func:`IS_ERR`\  condition containing error code.

.. _`of_fpga_mgr_get`:

of_fpga_mgr_get
===============

.. c:function:: struct fpga_manager *of_fpga_mgr_get(struct device_node *node)

    Given a device node, get a reference to a fpga mgr.

    :param node:
        device node
    :type node: struct device_node \*

.. _`of_fpga_mgr_get.return`:

Return
------

fpga manager struct or \ :c:func:`IS_ERR`\  condition containing error code.

.. _`fpga_mgr_put`:

fpga_mgr_put
============

.. c:function:: void fpga_mgr_put(struct fpga_manager *mgr)

    release a reference to a fpga manager

    :param mgr:
        fpga manager structure
    :type mgr: struct fpga_manager \*

.. _`fpga_mgr_lock`:

fpga_mgr_lock
=============

.. c:function:: int fpga_mgr_lock(struct fpga_manager *mgr)

    Lock FPGA manager for exclusive use

    :param mgr:
        fpga manager
    :type mgr: struct fpga_manager \*

.. _`fpga_mgr_lock.description`:

Description
-----------

Given a pointer to FPGA Manager (from \ :c:func:`fpga_mgr_get`\  or
\ :c:func:`of_fpga_mgr_put`\ ) attempt to get the mutex. The user should call
\ :c:func:`fpga_mgr_lock`\  and verify that it returns 0 before attempting to
program the FPGA.  Likewise, the user should call fpga_mgr_unlock
when done programming the FPGA.

.. _`fpga_mgr_lock.return`:

Return
------

0 for success or -EBUSY

.. _`fpga_mgr_unlock`:

fpga_mgr_unlock
===============

.. c:function:: void fpga_mgr_unlock(struct fpga_manager *mgr)

    Unlock FPGA manager after done programming

    :param mgr:
        fpga manager
    :type mgr: struct fpga_manager \*

.. _`fpga_mgr_create`:

fpga_mgr_create
===============

.. c:function:: struct fpga_manager *fpga_mgr_create(struct device *dev, const char *name, const struct fpga_manager_ops *mops, void *priv)

    create and initialize a FPGA manager struct

    :param dev:
        fpga manager device from pdev
    :type dev: struct device \*

    :param name:
        fpga manager name
    :type name: const char \*

    :param mops:
        pointer to structure of fpga manager ops
    :type mops: const struct fpga_manager_ops \*

    :param priv:
        fpga manager private data
    :type priv: void \*

.. _`fpga_mgr_create.description`:

Description
-----------

The caller of this function is responsible for freeing the struct with
\ :c:func:`fpga_mgr_free`\ .  Using \ :c:func:`devm_fpga_mgr_create`\  instead is recommended.

.. _`fpga_mgr_create.return`:

Return
------

pointer to struct fpga_manager or NULL

.. _`fpga_mgr_free`:

fpga_mgr_free
=============

.. c:function:: void fpga_mgr_free(struct fpga_manager *mgr)

    free a FPGA manager created with \ :c:func:`fpga_mgr_create`\ 

    :param mgr:
        fpga manager struct
    :type mgr: struct fpga_manager \*

.. _`devm_fpga_mgr_create`:

devm_fpga_mgr_create
====================

.. c:function:: struct fpga_manager *devm_fpga_mgr_create(struct device *dev, const char *name, const struct fpga_manager_ops *mops, void *priv)

    create and initialize a managed FPGA manager struct

    :param dev:
        fpga manager device from pdev
    :type dev: struct device \*

    :param name:
        fpga manager name
    :type name: const char \*

    :param mops:
        pointer to structure of fpga manager ops
    :type mops: const struct fpga_manager_ops \*

    :param priv:
        fpga manager private data
    :type priv: void \*

.. _`devm_fpga_mgr_create.description`:

Description
-----------

This function is intended for use in a FPGA manager driver's probe function.
After the manager driver creates the manager struct with
\ :c:func:`devm_fpga_mgr_create`\ , it should register it with \ :c:func:`fpga_mgr_register`\ .  The
manager driver's remove function should call \ :c:func:`fpga_mgr_unregister`\ .  The
manager struct allocated with this function will be freed automatically on
driver detach.  This includes the case of a probe function returning error
before calling \ :c:func:`fpga_mgr_register`\ , the struct will still get cleaned up.

.. _`devm_fpga_mgr_create.return`:

Return
------

pointer to struct fpga_manager or NULL

.. _`fpga_mgr_register`:

fpga_mgr_register
=================

.. c:function:: int fpga_mgr_register(struct fpga_manager *mgr)

    register a FPGA manager

    :param mgr:
        fpga manager struct
    :type mgr: struct fpga_manager \*

.. _`fpga_mgr_register.return`:

Return
------

0 on success, negative error code otherwise.

.. _`fpga_mgr_unregister`:

fpga_mgr_unregister
===================

.. c:function:: void fpga_mgr_unregister(struct fpga_manager *mgr)

    unregister a FPGA manager

    :param mgr:
        fpga manager struct
    :type mgr: struct fpga_manager \*

.. _`fpga_mgr_unregister.description`:

Description
-----------

This function is intended for use in a FPGA manager driver's remove function.

.. This file was automatic generated / don't edit.

