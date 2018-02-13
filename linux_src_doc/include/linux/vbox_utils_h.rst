.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/vbox_utils.h

.. _`__printf`:

\__printf
=========

.. c:function::  __printf( 1,  2)

    the equivalent kernel pr_foo function.

    :param  1:
        *undescribed*

    :param  2:
        *undescribed*

.. _`vbg_req_alloc`:

vbg_req_alloc
=============

.. c:function:: void *vbg_req_alloc(size_t len, enum vmmdev_request_type req_type)

    :param size_t len:
        Size of memory block required for the request.

    :param enum vmmdev_request_type req_type:
        The generic request type.

.. _`vbg_req_alloc.return`:

Return
------

the allocated memory

.. _`vbg_req_perform`:

vbg_req_perform
===============

.. c:function:: int vbg_req_perform(struct vbg_dev *gdev, void *req)

    :param struct vbg_dev \*gdev:
        The Guest extension device.

    :param void \*req:
        Pointer to the request structure.

.. _`vbg_req_perform.return`:

Return
------

VBox status code

.. _`vbg_status_code_to_errno`:

vbg_status_code_to_errno
========================

.. c:function:: int vbg_status_code_to_errno(int rc)

    :param int rc:
        VirtualBox status code to convert.

.. _`vbg_status_code_to_errno.return`:

Return
------

0 or negative errno value.

.. _`vbg_get_gdev`:

vbg_get_gdev
============

.. c:function:: struct vbg_dev *vbg_get_gdev( void)

    :param  void:
        no arguments

.. _`vbg_get_gdev.return`:

Return
------

a pointer to the gdev; or a ERR_PTR value on error.

.. _`vbg_put_gdev`:

vbg_put_gdev
============

.. c:function:: void vbg_put_gdev(struct vbg_dev *gdev)

    :param struct vbg_dev \*gdev:
        Reference returned by vbg_get_gdev to put.

.. This file was automatic generated / don't edit.

