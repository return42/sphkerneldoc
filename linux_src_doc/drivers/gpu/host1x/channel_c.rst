.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/host1x/channel.c

.. _`host1x_channel_get_index`:

host1x_channel_get_index
========================

.. c:function:: struct host1x_channel *host1x_channel_get_index(struct host1x *host, unsigned int index)

    Attempt to get channel reference by index

    :param host:
        Host1x device object
    :type host: struct host1x \*

    :param index:
        Index of channel
    :type index: unsigned int

.. _`host1x_channel_get_index.description`:

Description
-----------

If channel number \ ``index``\  is currently allocated, increase its refcount
and return a pointer to it. Otherwise, return NULL.

.. _`host1x_channel_request`:

host1x_channel_request
======================

.. c:function:: struct host1x_channel *host1x_channel_request(struct device *dev)

    Allocate a channel

    :param dev:
        *undescribed*
    :type dev: struct device \*

.. _`host1x_channel_request.description`:

Description
-----------

Allocates a new host1x channel for \ ``device``\ . May return NULL if CDMA
initialization fails.

.. This file was automatic generated / don't edit.

