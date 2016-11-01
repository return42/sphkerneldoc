.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/input/rmi4/rmi_i2c.c

.. _`rmi_i2c_xport`:

struct rmi_i2c_xport
====================

.. c:type:: struct rmi_i2c_xport

    stores information for i2c communication

.. _`rmi_i2c_xport.definition`:

Definition
----------

.. code-block:: c

    struct rmi_i2c_xport {
        struct rmi_transport_dev xport;
        struct i2c_client *client;
        struct mutex page_mutex;
        int page;
        int irq;
        u8 *tx_buf;
        size_t tx_buf_size;
        struct regulator_bulk_data supplies[2];
        u32 startup_delay;
    }

.. _`rmi_i2c_xport.members`:

Members
-------

xport
    The transport interface structure

client
    *undescribed*

page_mutex
    Locks current page to avoid changing pages in unexpected ways.

page
    Keeps track of the current virtual page

irq
    *undescribed*

tx_buf
    Buffer used for transmitting data to the sensor over i2c.

tx_buf_size
    Size of the buffer

startup_delay
    *undescribed*

.. This file was automatic generated / don't edit.

