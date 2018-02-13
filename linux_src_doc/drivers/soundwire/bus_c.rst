.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soundwire/bus.c

.. _`sdw_add_bus_master`:

sdw_add_bus_master
==================

.. c:function:: int sdw_add_bus_master(struct sdw_bus *bus)

    add a bus Master instance

    :param struct sdw_bus \*bus:
        bus instance

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

    :param struct sdw_bus \*bus:
        bus to be deleted

.. _`sdw_delete_bus_master.description`:

Description
-----------

Remove the instance, delete the child devices.

.. _`sdw_transfer`:

sdw_transfer
============

.. c:function:: int sdw_transfer(struct sdw_bus *bus, struct sdw_msg *msg)

    Synchronous transfer message to a SDW Slave device

    :param struct sdw_bus \*bus:
        SDW bus

    :param struct sdw_msg \*msg:
        SDW message to be xfered

.. _`sdw_transfer_defer`:

sdw_transfer_defer
==================

.. c:function:: int sdw_transfer_defer(struct sdw_bus *bus, struct sdw_msg *msg, struct sdw_defer *defer)

    Asynchronously transfer message to a SDW Slave device

    :param struct sdw_bus \*bus:
        SDW bus

    :param struct sdw_msg \*msg:
        SDW message to be xfered

    :param struct sdw_defer \*defer:
        Defer block for signal completion

.. _`sdw_transfer_defer.description`:

Description
-----------

Caller needs to hold the msg_lock lock while calling this

.. _`sdw_nread`:

sdw_nread
=========

.. c:function:: int sdw_nread(struct sdw_slave *slave, u32 addr, size_t count, u8 *val)

    Read "n" contiguous SDW Slave registers

    :param struct sdw_slave \*slave:
        SDW Slave

    :param u32 addr:
        Register address

    :param size_t count:
        length

    :param u8 \*val:
        Buffer for values to be read

.. _`sdw_nwrite`:

sdw_nwrite
==========

.. c:function:: int sdw_nwrite(struct sdw_slave *slave, u32 addr, size_t count, u8 *val)

    Write "n" contiguous SDW Slave registers

    :param struct sdw_slave \*slave:
        SDW Slave

    :param u32 addr:
        Register address

    :param size_t count:
        length

    :param u8 \*val:
        Buffer for values to be read

.. _`sdw_read`:

sdw_read
========

.. c:function:: int sdw_read(struct sdw_slave *slave, u32 addr)

    Read a SDW Slave register

    :param struct sdw_slave \*slave:
        SDW Slave

    :param u32 addr:
        Register address

.. _`sdw_write`:

sdw_write
=========

.. c:function:: int sdw_write(struct sdw_slave *slave, u32 addr, u8 value)

    Write a SDW Slave register

    :param struct sdw_slave \*slave:
        SDW Slave

    :param u32 addr:
        Register address

    :param u8 value:
        Register value

.. _`sdw_handle_slave_status`:

sdw_handle_slave_status
=======================

.. c:function:: int sdw_handle_slave_status(struct sdw_bus *bus, enum sdw_slave_status status)

    Handle Slave status

    :param struct sdw_bus \*bus:
        SDW bus instance

    :param enum sdw_slave_status status:
        Status for all Slave(s)

.. This file was automatic generated / don't edit.

