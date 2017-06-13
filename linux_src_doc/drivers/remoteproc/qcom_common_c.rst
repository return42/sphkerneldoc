.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/remoteproc/qcom_common.c

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

.. _`qcom_add_smd_subdev`:

qcom_add_smd_subdev
===================

.. c:function:: void qcom_add_smd_subdev(struct rproc *rproc, struct qcom_rproc_subdev *smd)

    try to add a SMD subdevice to rproc

    :param struct rproc \*rproc:
        rproc handle to parent the subdevice

    :param struct qcom_rproc_subdev \*smd:
        reference to a Qualcomm subdev context

.. _`qcom_remove_smd_subdev`:

qcom_remove_smd_subdev
======================

.. c:function:: void qcom_remove_smd_subdev(struct rproc *rproc, struct qcom_rproc_subdev *smd)

    remove the smd subdevice from rproc

    :param struct rproc \*rproc:
        rproc handle

    :param struct qcom_rproc_subdev \*smd:
        the SMD subdevice to remove

.. This file was automatic generated / don't edit.

