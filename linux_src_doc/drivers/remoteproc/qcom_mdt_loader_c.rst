.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/remoteproc/qcom_mdt_loader.c

.. _`qcom_mdt_find_rsc_table`:

qcom_mdt_find_rsc_table
=======================

.. c:function:: struct resource_table *qcom_mdt_find_rsc_table(struct rproc *rproc, const struct firmware *fw, int *tablesz)

    provide dummy resource table for remoteproc

    :param struct rproc \*rproc:
        remoteproc handle

    :param const struct firmware \*fw:
        firmware header

    :param int \*tablesz:
        outgoing size of the table

.. _`qcom_mdt_find_rsc_table.description`:

Description
-----------

Returns a dummy table.

.. _`qcom_mdt_parse`:

qcom_mdt_parse
==============

.. c:function:: int qcom_mdt_parse(const struct firmware *fw, phys_addr_t *fw_addr, size_t *fw_size, bool *fw_relocate)

    extract useful parameters from the mdt header

    :param const struct firmware \*fw:
        firmware handle

    :param phys_addr_t \*fw_addr:
        optional reference for base of the firmware's memory region

    :param size_t \*fw_size:
        optional reference for size of the firmware's memory region

    :param bool \*fw_relocate:
        optional reference for flagging if the firmware is relocatable

.. _`qcom_mdt_parse.description`:

Description
-----------

Returns 0 on success, negative errno otherwise.

.. _`qcom_mdt_load`:

qcom_mdt_load
=============

.. c:function:: int qcom_mdt_load(struct rproc *rproc, const struct firmware *fw, const char *firmware)

    load the firmware which header is defined in fw

    :param struct rproc \*rproc:
        rproc handle

    :param const struct firmware \*fw:
        frimware object for the header

    :param const char \*firmware:
        filename of the firmware, for building .bXX names

.. _`qcom_mdt_load.description`:

Description
-----------

Returns 0 on success, negative errno otherwise.

.. This file was automatic generated / don't edit.

