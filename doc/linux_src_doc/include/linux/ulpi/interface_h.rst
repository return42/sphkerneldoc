.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/ulpi/interface.h

.. _`ulpi_ops`:

struct ulpi_ops
===============

.. c:type:: struct ulpi_ops

    ULPI register access

.. _`ulpi_ops.definition`:

Definition
----------

.. code-block:: c

    struct ulpi_ops {
        struct device *dev;
        int (* read) (struct ulpi_ops *ops, u8 addr);
        int (* write) (struct ulpi_ops *ops, u8 addr, u8 val);
    }

.. _`ulpi_ops.members`:

Members
-------

dev
    the interface provider

read
    read operation for ULPI register access

write
    write operation for ULPI register access

.. This file was automatic generated / don't edit.

