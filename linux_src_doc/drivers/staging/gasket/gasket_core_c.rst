.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/gasket/gasket_core.c

.. _`gasket_num_name_lookup`:

gasket_num_name_lookup
======================

.. c:function:: const char *gasket_num_name_lookup(uint num, const struct gasket_num_name *table)

    :param num:
        Number to lookup.
    :type num: uint

    :param table:
        Array of num_name structures, the table for the lookup.
    :type table: const struct gasket_num_name \*

.. _`gasket_num_name_lookup.description`:

Description
-----------

Searches for num in the table.  If found, the
corresponding name is returned; otherwise NULL
is returned.

The table must have a NULL name pointer at the end.

.. _`gasket_wait_with_reschedule`:

gasket_wait_with_reschedule
===========================

.. c:function:: int gasket_wait_with_reschedule(struct gasket_dev *gasket_dev, int bar, u64 offset, u64 mask, u64 val, uint max_retries, u64 delay_ms)

    :param gasket_dev:
        Device struct.
    :type gasket_dev: struct gasket_dev \*

    :param bar:
        Bar
    :type bar: int

    :param offset:
        Register offset
    :type offset: u64

    :param mask:
        Register mask
    :type mask: u64

    :param val:
        Expected value
    :type val: u64

    :param max_retries:
        number of sleep periods
    :type max_retries: uint

    :param delay_ms:
        Timeout in milliseconds
    :type delay_ms: u64

.. _`gasket_wait_with_reschedule.description`:

Description
-----------

Busy waits for a specific combination of bits to be set on a
Gasket register.

.. This file was automatic generated / don't edit.

