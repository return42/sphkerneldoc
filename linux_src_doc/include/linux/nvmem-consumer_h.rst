.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/nvmem-consumer.h

.. _`nvmem_cell_lookup`:

struct nvmem_cell_lookup
========================

.. c:type:: struct nvmem_cell_lookup

    cell lookup entry

.. _`nvmem_cell_lookup.definition`:

Definition
----------

.. code-block:: c

    struct nvmem_cell_lookup {
        const char *nvmem_name;
        const char *cell_name;
        const char *dev_id;
        const char *con_id;
        struct list_head node;
    }

.. _`nvmem_cell_lookup.members`:

Members
-------

nvmem_name
    Name of the provider.

cell_name
    Name of the nvmem cell as defined in the name field of
    struct nvmem_cell_info.

dev_id
    Name of the consumer device that will be associated with
    this cell.

con_id
    Connector id for this cell lookup.

node
    *undescribed*

.. This file was automatic generated / don't edit.

