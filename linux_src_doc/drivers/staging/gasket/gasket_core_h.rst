.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/gasket/gasket_core.h

.. _`gasket_num_name`:

struct gasket_num_name
======================

.. c:type:: struct gasket_num_name

    Map numbers to names.

.. _`gasket_num_name.definition`:

Definition
----------

.. code-block:: c

    struct gasket_num_name {
        uint snn_num;
        const char *snn_name;
    }

.. _`gasket_num_name.members`:

Members
-------

snn_num
    *undescribed*

snn_name
    *undescribed*

.. _`gasket_num_name.description`:

Description
-----------

This structure maps numbers to names. It is used to provide printable enum
names, e.g {0, "DEAD"} or {1, "ALIVE"}.

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

.. This file was automatic generated / don't edit.

