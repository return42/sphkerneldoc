.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/rpmsg/rpmsg_internal.h

.. _`rpmsg_device_ops`:

struct rpmsg_device_ops
=======================

.. c:type:: struct rpmsg_device_ops

    indirection table for the rpmsg_device operations

.. _`rpmsg_device_ops.definition`:

Definition
----------

.. code-block:: c

    struct rpmsg_device_ops {
        struct rpmsg_endpoint *(*create_ept)(struct rpmsg_device *rpdev,rpmsg_rx_cb_t cb, void *priv,struct rpmsg_channel_info chinfo);
        int (*announce_create)(struct rpmsg_device *ept);
        int (*announce_destroy)(struct rpmsg_device *ept);
    }

.. _`rpmsg_device_ops.members`:

Members
-------

create_ept
    create backend-specific endpoint, requried

announce_create
    announce presence of new channel, optional

announce_destroy
    announce destruction of channel, optional

.. _`rpmsg_device_ops.description`:

Description
-----------

Indirection table for the operations that a rpmsg backend should implement.
\ ``announce_create``\  and \ ``announce_destroy``\  are optional as the backend might
advertise new channels implicitly by creating the endpoints.

.. _`rpmsg_endpoint_ops`:

struct rpmsg_endpoint_ops
=========================

.. c:type:: struct rpmsg_endpoint_ops

    indirection table for rpmsg_endpoint operations

.. _`rpmsg_endpoint_ops.definition`:

Definition
----------

.. code-block:: c

    struct rpmsg_endpoint_ops {
        void (*destroy_ept)(struct rpmsg_endpoint *ept);
        int (*send)(struct rpmsg_endpoint *ept, void *data, int len);
        int (*sendto)(struct rpmsg_endpoint *ept, void *data, int len, u32 dst);
        int (*send_offchannel)(struct rpmsg_endpoint *ept, u32 src, u32 dst,void *data, int len);
        int (*trysend)(struct rpmsg_endpoint *ept, void *data, int len);
        int (*trysendto)(struct rpmsg_endpoint *ept, void *data, int len, u32 dst);
        int (*trysend_offchannel)(struct rpmsg_endpoint *ept, u32 src, u32 dst,void *data, int len);
    }

.. _`rpmsg_endpoint_ops.members`:

Members
-------

destroy_ept
    destroy the given endpoint, required

send
    see \ ``rpmsg_send``\ (), required

sendto
    see \ ``rpmsg_sendto``\ (), optional

send_offchannel
    see \ ``rpmsg_send_offchannel``\ (), optional

trysend
    see \ ``rpmsg_trysend``\ (), required

trysendto
    see \ ``rpmsg_trysendto``\ (), optional

trysend_offchannel
    see \ ``rpmsg_trysend_offchannel``\ (), optional

.. _`rpmsg_endpoint_ops.description`:

Description
-----------

Indirection table for the operations that a rpmsg backend should implement.
In addition to \ ``destroy_ept``\ , the backend must at least implement \ ``send``\  and
\ ``trysend``\ , while the variants sending data off-channel are optional.

.. This file was automatic generated / don't edit.

