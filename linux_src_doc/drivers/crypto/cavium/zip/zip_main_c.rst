.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/cavium/zip/zip_main.c

.. _`zip_get_device`:

zip_get_device
==============

.. c:function:: struct zip_device *zip_get_device(int node)

    Get ZIP device based on node id of cpu

    :param node:
        Node id of the current cpu
    :type node: int

.. _`zip_get_device.return`:

Return
------

Pointer to Zip device structure

.. _`zip_get_node_id`:

zip_get_node_id
===============

.. c:function:: int zip_get_node_id( void)

    Get the node id of the current cpu

    :param void:
        no arguments
    :type void: 

.. _`zip_get_node_id.return`:

Return
------

Node id of the current cpu

.. This file was automatic generated / don't edit.

