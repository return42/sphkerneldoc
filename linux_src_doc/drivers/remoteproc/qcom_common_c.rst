.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/remoteproc/qcom_common.c

.. _`qcom_add_glink_subdev`:

qcom_add_glink_subdev
=====================

.. c:function:: void qcom_add_glink_subdev(struct rproc *rproc, struct qcom_rproc_glink *glink)

    try to add a GLINK subdevice to rproc

    :param struct rproc \*rproc:
        rproc handle to parent the subdevice

    :param struct qcom_rproc_glink \*glink:
        reference to a GLINK subdev context

.. _`qcom_remove_glink_subdev`:

qcom_remove_glink_subdev
========================

.. c:function:: void qcom_remove_glink_subdev(struct rproc *rproc, struct qcom_rproc_glink *glink)

    remove a GLINK subdevice from rproc

    :param struct rproc \*rproc:
        rproc handle

    :param struct qcom_rproc_glink \*glink:
        reference to a GLINK subdev context

.. _`qcom_register_dump_segments`:

qcom_register_dump_segments
===========================

.. c:function:: int qcom_register_dump_segments(struct rproc *rproc, const struct firmware *fw)

    register segments for coredump

    :param struct rproc \*rproc:
        remoteproc handle

    :param const struct firmware \*fw:
        firmware header

.. _`qcom_register_dump_segments.description`:

Description
-----------

Register all segments of the ELF in the remoteproc coredump segment list

.. _`qcom_register_dump_segments.return`:

Return
------

0 on success, negative errno on failure.

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

.. _`qcom_register_ssr_notifier`:

qcom_register_ssr_notifier
==========================

.. c:function:: int qcom_register_ssr_notifier(struct notifier_block *nb)

    register SSR notification handler

    :param struct notifier_block \*nb:
        notifier_block to notify for restart notifications

.. _`qcom_register_ssr_notifier.description`:

Description
-----------

Returns 0 on success, negative errno on failure.

This register the \ ``notify``\  function as handler for restart notifications. As
remote processors are stopped this function will be called, with the SSR
name passed as a parameter.

.. _`qcom_unregister_ssr_notifier`:

qcom_unregister_ssr_notifier
============================

.. c:function:: void qcom_unregister_ssr_notifier(struct notifier_block *nb)

    unregister SSR notification handler

    :param struct notifier_block \*nb:
        notifier_block to unregister

.. _`qcom_add_ssr_subdev`:

qcom_add_ssr_subdev
===================

.. c:function:: void qcom_add_ssr_subdev(struct rproc *rproc, struct qcom_rproc_ssr *ssr, const char *ssr_name)

    register subdevice as restart notification source

    :param struct rproc \*rproc:
        rproc handle

    :param struct qcom_rproc_ssr \*ssr:
        SSR subdevice handle

    :param const char \*ssr_name:
        identifier to use for notifications originating from \ ``rproc``\ 

.. _`qcom_add_ssr_subdev.description`:

Description
-----------

As the \ ``ssr``\  is registered with the \ ``rproc``\  SSR events will be sent to all
registered listeners in the system as the remoteproc is shut down.

.. _`qcom_remove_ssr_subdev`:

qcom_remove_ssr_subdev
======================

.. c:function:: void qcom_remove_ssr_subdev(struct rproc *rproc, struct qcom_rproc_ssr *ssr)

    remove subdevice as restart notification source

    :param struct rproc \*rproc:
        rproc handle

    :param struct qcom_rproc_ssr \*ssr:
        SSR subdevice handle

.. This file was automatic generated / don't edit.

