.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/base/devcon.c

.. _`define_mutex`:

DEFINE_MUTEX
============

.. c:function::  DEFINE_MUTEX( devcon_lock)

    :param devcon_lock:
        *undescribed*
    :type devcon_lock: 

.. _`define_mutex.description`:

Description
-----------

Copyright (C) 2018 Intel Corporation
Author: Heikki Krogerus <heikki.krogerus@linux.intel.com>

.. _`device_connection_find_match`:

device_connection_find_match
============================

.. c:function:: void *device_connection_find_match(struct device *dev, const char *con_id, void *data, void *(*match)(struct device_connection *con, int ep, void *data))

    Find physical connection to a device

    :param dev:
        Device with the connection
    :type dev: struct device \*

    :param con_id:
        Identifier for the connection
    :type con_id: const char \*

    :param data:
        Data for the match function
    :type data: void \*

    :param void \*(\*match)(struct device_connection \*con, int ep, void \*data):
        Function to check and convert the connection description

.. _`device_connection_find_match.description`:

Description
-----------

Find a connection with unique identifier \ ``con_id``\  between \ ``dev``\  and another
device. \ ``match``\  will be used to convert the connection description to data the
caller is expecting to be returned.

.. _`device_connection_find`:

device_connection_find
======================

.. c:function:: struct device *device_connection_find(struct device *dev, const char *con_id)

    Find two devices connected together

    :param dev:
        Device with the connection
    :type dev: struct device \*

    :param con_id:
        Identifier for the connection
    :type con_id: const char \*

.. _`device_connection_find.description`:

Description
-----------

Find a connection with unique identifier \ ``con_id``\  between \ ``dev``\  and
another device. On success returns handle to the device that is connected
to \ ``dev``\ , with the reference count for the found device incremented. Returns
NULL if no matching connection was found, or ERR_PTR(-EPROBE_DEFER) when a
connection was found but the other device has not been enumerated yet.

.. _`device_connection_add`:

device_connection_add
=====================

.. c:function:: void device_connection_add(struct device_connection *con)

    Register a connection description

    :param con:
        The connection description to be registered
    :type con: struct device_connection \*

.. _`device_connection_remove`:

device_connection_remove
========================

.. c:function:: void device_connection_remove(struct device_connection *con)

    Unregister connection description

    :param con:
        The connection description to be unregistered
    :type con: struct device_connection \*

.. This file was automatic generated / don't edit.

