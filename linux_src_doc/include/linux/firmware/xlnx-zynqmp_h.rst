.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/firmware/xlnx-zynqmp.h

.. _`zynqmp_pm_query_data`:

struct zynqmp_pm_query_data
===========================

.. c:type:: struct zynqmp_pm_query_data

    PM query data

.. _`zynqmp_pm_query_data.definition`:

Definition
----------

.. code-block:: c

    struct zynqmp_pm_query_data {
        u32 qid;
        u32 arg1;
        u32 arg2;
        u32 arg3;
    }

.. _`zynqmp_pm_query_data.members`:

Members
-------

qid
    query ID

arg1
    Argument 1 of query data

arg2
    Argument 2 of query data

arg3
    Argument 3 of query data

.. This file was automatic generated / don't edit.

