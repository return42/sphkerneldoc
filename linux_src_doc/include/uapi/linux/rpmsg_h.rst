.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/rpmsg.h

.. _`rpmsg_endpoint_info`:

struct rpmsg_endpoint_info
==========================

.. c:type:: struct rpmsg_endpoint_info

    endpoint info representation

.. _`rpmsg_endpoint_info.definition`:

Definition
----------

.. code-block:: c

    struct rpmsg_endpoint_info {
        char name[32];
        __u32 src;
        __u32 dst;
    }

.. _`rpmsg_endpoint_info.members`:

Members
-------

name
    name of service

src
    local address

dst
    destination address

.. This file was automatic generated / don't edit.

