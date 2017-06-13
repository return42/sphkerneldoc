.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/input/rmi4/rmi_bus.h

.. _`rmi_function`:

struct rmi_function
===================

.. c:type:: struct rmi_function

    represents the implementation of an RMI4 function for a particular device (basically, a driver for that RMI4 function)

.. _`rmi_function.definition`:

Definition
----------

.. code-block:: c

    struct rmi_function {
        struct rmi_function_descriptor fd;
        struct rmi_device *rmi_dev;
        struct device dev;
        struct list_head node;
        unsigned int num_of_irqs;
        unsigned int irq_pos;
        unsigned long irq_mask;
    }

.. _`rmi_function.members`:

Members
-------

fd
    The function descriptor of the RMI function

rmi_dev
    Pointer to the RMI device associated with this function container

dev
    The device associated with this particular function.

node
    entry in device's list of functions

num_of_irqs
    The number of irqs needed by this function

irq_pos
    The position in the irq bitfield this function holds

irq_mask
    For convenience, can be used to mask IRQ bits off during ATTN
    interrupt handling.

.. _`rmi_function_handler`:

struct rmi_function_handler
===========================

.. c:type:: struct rmi_function_handler

    driver routines for a particular RMI function.

.. _`rmi_function_handler.definition`:

Definition
----------

.. code-block:: c

    struct rmi_function_handler {
        struct device_driver driver;
        u8 func;
        int (*probe)(struct rmi_function *fn);
        void (*remove)(struct rmi_function *fn);
        int (*config)(struct rmi_function *fn);
        int (*reset)(struct rmi_function *fn);
        int (*attention)(struct rmi_function *fn, unsigned long *irq_bits);
        int (*suspend)(struct rmi_function *fn);
        int (*resume)(struct rmi_function *fn);
    }

.. _`rmi_function_handler.members`:

Members
-------

driver
    *undescribed*

func
    The RMI function number

probe
    *undescribed*

remove
    *undescribed*

config
    Called when the function container is first initialized, and
    after a reset is detected.  This routine should write any necessary
    configuration settings to the device.

reset
    Called when a reset of the touch sensor is detected.  The routine
    should perform any out-of-the-ordinary reset handling that might be
    necessary.  Restoring of touch sensor configuration registers should be
    handled in the \ :c:func:`config`\  callback, below.

attention
    Called when the IRQ(s) for the function are set by the touch
    sensor.

suspend
    Should perform any required operations to suspend the particular
    function.

resume
    Should perform any required operations to resume the particular
    function.

.. _`rmi_function_handler.description`:

Description
-----------

All callbacks are expected to return 0 on success, error code on failure.

.. _`rmi_reset`:

rmi_reset
=========

.. c:function:: int rmi_reset(struct rmi_device *d)

    reset a RMI4 device

    :param struct rmi_device \*d:
        Pointer to an RMI device

.. _`rmi_reset.description`:

Description
-----------

Calls for a reset of each function implemented by a specific device.
Returns 0 on success or a negative error code.

.. _`rmi_read`:

rmi_read
========

.. c:function:: int rmi_read(struct rmi_device *d, u16 addr, u8 *buf)

    read a single byte

    :param struct rmi_device \*d:
        Pointer to an RMI device

    :param u16 addr:
        The address to read from

    :param u8 \*buf:
        The read buffer

.. _`rmi_read.description`:

Description
-----------

Reads a single byte of data using the underlying transport protocol
into memory pointed by \ ``buf``\ . It returns 0 on success or a negative
error code.

.. _`rmi_read_block`:

rmi_read_block
==============

.. c:function:: int rmi_read_block(struct rmi_device *d, u16 addr, void *buf, size_t len)

    read a block of bytes

    :param struct rmi_device \*d:
        Pointer to an RMI device

    :param u16 addr:
        The start address to read from

    :param void \*buf:
        The read buffer

    :param size_t len:
        Length of the read buffer

.. _`rmi_read_block.description`:

Description
-----------

Reads a block of byte data using the underlying transport protocol
into memory pointed by \ ``buf``\ . It returns 0 on success or a negative
error code.

.. _`rmi_write`:

rmi_write
=========

.. c:function:: int rmi_write(struct rmi_device *d, u16 addr, u8 data)

    write a single byte

    :param struct rmi_device \*d:
        Pointer to an RMI device

    :param u16 addr:
        The address to write to

    :param u8 data:
        The data to write

.. _`rmi_write.description`:

Description
-----------

Writes a single byte using the underlying transport protocol. It
returns zero on success or a negative error code.

.. _`rmi_write_block`:

rmi_write_block
===============

.. c:function:: int rmi_write_block(struct rmi_device *d, u16 addr, const void *buf, size_t len)

    write a block of bytes

    :param struct rmi_device \*d:
        Pointer to an RMI device

    :param u16 addr:
        The start address to write to

    :param const void \*buf:
        The write buffer

    :param size_t len:
        Length of the write buffer

.. _`rmi_write_block.description`:

Description
-----------

Writes a block of byte data from buf using the underlaying transport
protocol.  It returns the amount of bytes written or a negative error code.

.. This file was automatic generated / don't edit.

