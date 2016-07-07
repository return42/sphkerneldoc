.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/qat/qat_common/adf_vf2pf_msg.c

.. _`adf_vf2pf_init`:

adf_vf2pf_init
==============

.. c:function:: int adf_vf2pf_init(struct adf_accel_dev *accel_dev)

    send init msg to PF

    :param struct adf_accel_dev \*accel_dev:
        Pointer to acceleration VF device.

.. _`adf_vf2pf_init.description`:

Description
-----------

Function sends an init messge from the VF to a PF

.. _`adf_vf2pf_init.return`:

Return
------

0 on success, error code otherwise.

.. _`adf_vf2pf_shutdown`:

adf_vf2pf_shutdown
==================

.. c:function:: void adf_vf2pf_shutdown(struct adf_accel_dev *accel_dev)

    send shutdown msg to PF

    :param struct adf_accel_dev \*accel_dev:
        Pointer to acceleration VF device.

.. _`adf_vf2pf_shutdown.description`:

Description
-----------

Function sends a shutdown messge from the VF to a PF

.. _`adf_vf2pf_shutdown.return`:

Return
------

void

.. This file was automatic generated / don't edit.

