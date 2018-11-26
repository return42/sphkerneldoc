.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soundwire/bus.c

.. _`sdw_add_bus_master`:

sdw_add_bus_master
==================

.. c:function:: int sdw_add_bus_master(struct sdw_bus *bus)

    add a bus Master instance

    :param bus:
        bus instance
    :type bus: struct sdw_bus \*

.. _`sdw_add_bus_master.description`:

Description
-----------

Initializes the bus instance, read properties and create child
devices.

.. _`sdw_delete_bus_master`:

sdw_delete_bus_master
=====================

.. c:function:: void sdw_delete_bus_master(struct sdw_bus *bus)

    delete the bus master instance

    :param bus:
        bus to be deleted
    :type bus: struct sdw_bus \*

.. _`sdw_delete_bus_master.description`:

Description
-----------

Remove the instance, delete the child devices.

.. _`sdw_transfer`:

sdw_transfer
============

.. c:function:: int sdw_transfer(struct sdw_bus *bus, struct sdw_msg *msg)

    Synchronous transfer message to a SDW Slave device

    :param bus:
        SDW bus
    :type bus: struct sdw_bus \*

    :param msg:
        SDW message to be xfered
    :type msg: struct sdw_msg \*

.. _`sdw_transfer_defer`:

sdw_transfer_defer
==================

.. c:function:: int sdw_transfer_defer(struct sdw_bus *bus, struct sdw_msg *msg, struct sdw_defer *defer)

    Asynchronously transfer message to a SDW Slave device

    :param bus:
        SDW bus
    :type bus: struct sdw_bus \*

    :param msg:
        SDW message to be xfered
    :type msg: struct sdw_msg \*

    :param defer:
        Defer block for signal completion
    :type defer: struct sdw_defer \*

.. _`sdw_transfer_defer.description`:

Description
-----------

Caller needs to hold the msg_lock lock while calling this

.. _`sdw_nread`:

sdw_nread
=========

.. c:function:: int sdw_nread(struct sdw_slave *slave, u32 addr, size_t count, u8 *val)

    Read "n" contiguous SDW Slave registers

    :param slave:
        SDW Slave
    :type slave: struct sdw_slave \*

    :param addr:
        Register address
    :type addr: u32

    :param count:
        length
    :type count: size_t

    :param val:
        Buffer for values to be read
    :type val: u8 \*

.. _`sdw_nwrite`:

sdw_nwrite
==========

.. c:function:: int sdw_nwrite(struct sdw_slave *slave, u32 addr, size_t count, u8 *val)

    Write "n" contiguous SDW Slave registers

    :param slave:
        SDW Slave
    :type slave: struct sdw_slave \*

    :param addr:
        Register address
    :type addr: u32

    :param count:
        length
    :type count: size_t

    :param val:
        Buffer for values to be read
    :type val: u8 \*

.. _`sdw_read`:

sdw_read
========

.. c:function:: int sdw_read(struct sdw_slave *slave, u32 addr)

    Read a SDW Slave register

    :param slave:
        SDW Slave
    :type slave: struct sdw_slave \*

    :param addr:
        Register address
    :type addr: u32

.. _`sdw_write`:

sdw_write
=========

.. c:function:: int sdw_write(struct sdw_slave *slave, u32 addr, u8 value)

    Write a SDW Slave register

    :param slave:
        SDW Slave
    :type slave: struct sdw_slave \*

    :param addr:
        Register address
    :type addr: u32

    :param value:
        Register value
    :type value: u8

.. _`sdw_handle_slave_status`:

sdw_handle_slave_status
=======================

.. c:function:: int sdw_handle_slave_status(struct sdw_bus *bus, enum sdw_slave_status status)

    Handle Slave status

    :param bus:
        SDW bus instance
    :type bus: struct sdw_bus \*

    :param status:
        Status for all Slave(s)
    :type status: enum sdw_slave_status

.. This file was automatic generated / don't edit.

