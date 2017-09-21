.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/power/supply/bq27xxx_battery.c

.. _`bq27xxx_dm_buf`:

struct bq27xxx_dm_buf
=====================

.. c:type:: struct bq27xxx_dm_buf

    chip data memory buffer

.. _`bq27xxx_dm_buf.definition`:

Definition
----------

.. code-block:: c

    struct bq27xxx_dm_buf {
        u8 class;
        u8 block;
        u8 data;
        bool has_data;
        bool dirty;
    }

.. _`bq27xxx_dm_buf.members`:

Members
-------

class
    data memory subclass_id

block
    data memory block number

data
    data from/for the block

has_data
    true if data has been filled by read

dirty
    true if data has changed since last read/write

.. _`bq27xxx_dm_buf.description`:

Description
-----------

Encapsulates info required to manage chip data memory blocks.

.. This file was automatic generated / don't edit.

