.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soc/ux500/ux500-soc-id.c

.. _`dbx500_asic_id`:

struct dbx500_asic_id
=====================

.. c:type:: struct dbx500_asic_id

    fields of the ASIC ID

.. _`dbx500_asic_id.definition`:

Definition
----------

.. code-block:: c

    struct dbx500_asic_id {
        u16 partnumber;
        u8 revision;
        u8 process;
    }

.. _`dbx500_asic_id.members`:

Members
-------

partnumber
    hithereto 0x8500 for DB8500

revision
    version code in the series

process
    the manufacturing process, 0x40 is 40 nm 0x00 is "standard"

.. This file was automatic generated / don't edit.

