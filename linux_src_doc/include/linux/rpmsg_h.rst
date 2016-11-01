.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/rpmsg.h

.. _`rpmsg_channel_info`:

struct rpmsg_channel_info
=========================

.. c:type:: struct rpmsg_channel_info

    channel info representation

.. _`rpmsg_channel_info.definition`:

Definition
----------

.. code-block:: c

    struct rpmsg_channel_info {
        char name[RPMSG_NAME_SIZE];
        u32 src;
        u32 dst;
    }

.. _`rpmsg_channel_info.members`:

Members
-------

name
    name of service

src
    local address

dst
    destination address

.. _`rpmsg_endpoint`:

struct rpmsg_endpoint
=====================

.. c:type:: struct rpmsg_endpoint

    binds a local rpmsg address to its user

.. _`rpmsg_endpoint.definition`:

Definition
----------

.. code-block:: c

    struct rpmsg_endpoint {
        struct rpmsg_device *rpdev;
        struct kref refcount;
        rpmsg_rx_cb_t cb;
        struct mutex cb_lock;
        u32 addr;
        void *priv;
        const struct rpmsg_endpoint_ops *ops;
    }

.. _`rpmsg_endpoint.members`:

Members
-------

rpdev
    rpmsg channel device

refcount
    when this drops to zero, the ept is deallocated

cb
    rx callback handler

cb_lock
    must be taken before accessing/changing \ ``cb``\ 

addr
    local rpmsg address

priv
    private data for the driver's use

ops
    *undescribed*

.. _`rpmsg_endpoint.description`:

Description
-----------

In essence, an rpmsg endpoint represents a listener on the rpmsg bus, as
it binds an rpmsg address with an rx callback handler.

Simple rpmsg drivers shouldn't use this struct directly, because

.. _`rpmsg_endpoint.things-just-work`:

things just work
----------------

every rpmsg driver provides an rx callback upon
registering to the bus, and that callback is then bound to its rpmsg
address when the driver is probed. When relevant inbound messages arrive
(i.e. messages which their dst address equals to the src address of
the rpmsg channel), the driver's handler is invoked to process it.

More complicated drivers though, that do need to allocate additional rpmsg
addresses, and bind them to different rx callbacks, must explicitly
create additional endpoints by themselves (see \ :c:func:`rpmsg_create_ept`\ ).

.. _`rpmsg_driver`:

struct rpmsg_driver
===================

.. c:type:: struct rpmsg_driver

    rpmsg driver struct

.. _`rpmsg_driver.definition`:

Definition
----------

.. code-block:: c

    struct rpmsg_driver {
        struct device_driver drv;
        const struct rpmsg_device_id *id_table;
        int (*probe)(struct rpmsg_device *dev);
        void (*remove)(struct rpmsg_device *dev);
        int (*callback)(struct rpmsg_device *, void *, int, void *, u32);
    }

.. _`rpmsg_driver.members`:

Members
-------

drv
    underlying device driver

id_table
    rpmsg ids serviced by this driver

probe
    invoked when a matching rpmsg channel (i.e. device) is found

remove
    invoked when the rpmsg channel is removed

callback
    invoked when an inbound message is received on the channel

.. _`module_rpmsg_driver`:

module_rpmsg_driver
===================

.. c:function::  module_rpmsg_driver( __rpmsg_driver)

    Helper macro for registering an rpmsg driver

    :param  __rpmsg_driver:
        rpmsg_driver struct

.. _`module_rpmsg_driver.description`:

Description
-----------

Helper macro for rpmsg drivers which do not do anything special in module
init/exit. This eliminates a lot of boilerplate.  Each module may only
use this macro once, and calling it replaces \ :c:func:`module_init`\  and \ :c:func:`module_exit`\ 

.. This file was automatic generated / don't edit.

