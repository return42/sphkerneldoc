.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soundwire/bus.h

.. _`sdw_msg`:

struct sdw_msg
==============

.. c:type:: struct sdw_msg

    Message structure

.. _`sdw_msg.definition`:

Definition
----------

.. code-block:: c

    struct sdw_msg {
        u16 addr;
        u16 len;
        u8 dev_num;
        u8 addr_page1;
        u8 addr_page2;
        u8 flags;
        u8 *buf;
        bool ssp_sync;
        bool page;
    }

.. _`sdw_msg.members`:

Members
-------

addr
    Register address accessed in the Slave

len
    number of messages

dev_num
    Slave device number

addr_page1
    SCP address page 1 Slave register

addr_page2
    SCP address page 2 Slave register

flags
    transfer flags, indicate if xfer is read or write

buf
    message data buffer

ssp_sync
    Send message at SSP (Stream Synchronization Point)

page
    address requires paging

.. This file was automatic generated / don't edit.

