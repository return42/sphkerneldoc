.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/host1x.h

.. _`host1x_client_ops`:

struct host1x_client_ops
========================

.. c:type:: struct host1x_client_ops

    host1x client operations

.. _`host1x_client_ops.definition`:

Definition
----------

.. code-block:: c

    struct host1x_client_ops {
        int (*init)(struct host1x_client *client);
        int (*exit)(struct host1x_client *client);
    }

.. _`host1x_client_ops.members`:

Members
-------

init
    host1x client initialization code

exit
    host1x client tear down code

.. _`host1x_client`:

struct host1x_client
====================

.. c:type:: struct host1x_client

    host1x client structure

.. _`host1x_client.definition`:

Definition
----------

.. code-block:: c

    struct host1x_client {
        struct list_head list;
        struct device *parent;
        struct device *dev;
        const struct host1x_client_ops *ops;
        enum host1x_class class;
        struct host1x_channel *channel;
        struct host1x_syncpt **syncpts;
        unsigned int num_syncpts;
    }

.. _`host1x_client.members`:

Members
-------

list
    list node for the host1x client

parent
    pointer to struct device representing the host1x controller

dev
    pointer to struct device backing this host1x client

ops
    host1x client operations

class
    host1x class represented by this client

channel
    host1x channel associated with this client

syncpts
    array of syncpoints requested for this client

num_syncpts
    number of syncpoints requested for this client

.. _`host1x_driver`:

struct host1x_driver
====================

.. c:type:: struct host1x_driver

    host1x logical device driver

.. _`host1x_driver.definition`:

Definition
----------

.. code-block:: c

    struct host1x_driver {
        struct device_driver driver;
        const struct of_device_id *subdevs;
        struct list_head list;
        int (*probe)(struct host1x_device *device);
        int (*remove)(struct host1x_device *device);
        void (*shutdown)(struct host1x_device *device);
    }

.. _`host1x_driver.members`:

Members
-------

driver
    core driver

subdevs
    table of OF device IDs matching subdevices for this driver

list
    list node for the driver

probe
    called when the host1x logical device is probed

remove
    called when the host1x logical device is removed

shutdown
    called when the host1x logical device is shut down

.. This file was automatic generated / don't edit.

