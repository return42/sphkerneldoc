.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hid/intel-ish-hid/ishtp/bus.h

.. _`ishtp_cl_device`:

struct ishtp_cl_device
======================

.. c:type:: struct ishtp_cl_device

    ISHTP device handle

.. _`ishtp_cl_device.definition`:

Definition
----------

.. code-block:: c

    struct ishtp_cl_device {
        struct device dev;
        struct ishtp_device *ishtp_dev;
        struct ishtp_fw_client *fw_client;
        struct list_head device_link;
        struct work_struct event_work;
        void *driver_data;
        int reference_count;
        void (*event_cb)(struct ishtp_cl_device *device);
    }

.. _`ishtp_cl_device.members`:

Members
-------

dev
    device pointer

ishtp_dev
    pointer to ishtp device structure to primarily to access
    hw device operation callbacks and properties

fw_client
    fw_client pointer to get fw information like protocol name
    max message length etc.

device_link
    Link to next client in the list on a bus

event_work
    Used to schedule rx event for client

driver_data
    Storage driver private data

reference_count
    Used for get/put device

event_cb
    Callback to driver to send events

.. _`ishtp_cl_device.description`:

Description
-----------

An ishtp_cl_device pointer is returned from \ :c:func:`ishtp_add_device`\ 
and links ISHTP bus clients to their actual host client pointer.
Drivers for ISHTP devices will get an ishtp_cl_device pointer
when being probed and shall use it for doing bus I/O.

.. _`ishtp_cl_driver`:

struct ishtp_cl_driver
======================

.. c:type:: struct ishtp_cl_driver

    ISHTP device handle

.. _`ishtp_cl_driver.definition`:

Definition
----------

.. code-block:: c

    struct ishtp_cl_driver {
        struct device_driver driver;
        const char *name;
        int (*probe)(struct ishtp_cl_device *dev);
        int (*remove)(struct ishtp_cl_device *dev);
        int (*reset)(struct ishtp_cl_device *dev);
        const struct dev_pm_ops *pm;
    }

.. _`ishtp_cl_driver.members`:

Members
-------

driver
    driver instance on a bus

name
    Name of the device for probe

probe
    driver callback for device probe

remove
    driver callback on device removal

reset
    *undescribed*

pm
    *undescribed*

.. _`ishtp_cl_driver.description`:

Description
-----------

Client drivers defines to get probed/removed for ISHTP client device.

.. This file was automatic generated / don't edit.

