.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/cavium/zip/zip_inflate.c

.. _`zip_inflate`:

zip_inflate
===========

.. c:function:: int zip_inflate(struct zip_operation *zip_ops, struct zip_state *s, struct zip_device *zip_dev)

    API to offload inflate operation to hardware

    :param zip_ops:
        Pointer to zip operation structure
    :type zip_ops: struct zip_operation \*

    :param s:
        Pointer to the structure representing zip state
    :type s: struct zip_state \*

    :param zip_dev:
        Pointer to zip device structure
    :type zip_dev: struct zip_device \*

.. _`zip_inflate.description`:

Description
-----------

This function prepares the zip inflate command and submits it to the zip
engine for processing.

.. _`zip_inflate.return`:

Return
------

0 if successful or error code

.. This file was automatic generated / don't edit.

