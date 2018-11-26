.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/fpga/dfl-fme.h

.. _`dfl_fme`:

struct dfl_fme
==============

.. c:type:: struct dfl_fme

    dfl fme private data

.. _`dfl_fme.definition`:

Definition
----------

.. code-block:: c

    struct dfl_fme {
        struct platform_device *mgr;
        struct list_head region_list;
        struct list_head bridge_list;
        struct dfl_feature_platform_data *pdata;
    }

.. _`dfl_fme.members`:

Members
-------

mgr
    FME's FPGA manager platform device.

region_list
    linked list of FME's FPGA regions.

bridge_list
    linked list of FME's FPGA bridges.

pdata
    fme platform device's pdata.

.. This file was automatic generated / don't edit.

