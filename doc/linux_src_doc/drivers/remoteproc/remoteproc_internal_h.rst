.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/remoteproc/remoteproc_internal.h

.. _`rproc_fw_ops`:

struct rproc_fw_ops
===================

.. c:type:: struct rproc_fw_ops

    firmware format specific operations.

.. _`rproc_fw_ops.definition`:

Definition
----------

.. code-block:: c

    struct rproc_fw_ops {
        struct resource_table *(* find_rsc_table) (struct rproc *rproc,const struct firmware *fw,int *tablesz);
        struct resource_table *(* find_loaded_rsc_table) (struct rproc *rproc,const struct firmware *fw);
        int (* load) (struct rproc *rproc, const struct firmware *fw);
        int (* sanity_check) (struct rproc *rproc, const struct firmware *fw);
        u32 (* get_boot_addr) (struct rproc *rproc, const struct firmware *fw);
    }

.. _`rproc_fw_ops.members`:

Members
-------

find_rsc_table
    find the resource table inside the firmware image

find_loaded_rsc_table
    find the loaded resouce table

load
    load firmeware to memory, where the remote processor
    expects to find it

sanity_check
    sanity check the fw image

get_boot_addr
    get boot address to entry point specified in firmware

.. This file was automatic generated / don't edit.

