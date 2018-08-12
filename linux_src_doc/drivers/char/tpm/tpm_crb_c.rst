.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/char/tpm/tpm_crb.c

.. _`crb_go_idle`:

crb_go_idle
===========

.. c:function:: int crb_go_idle(struct device *dev, struct crb_priv *priv)

    request tpm crb device to go the idle state

    :param struct device \*dev:
        crb device

    :param struct crb_priv \*priv:
        crb private data

.. _`crb_go_idle.description`:

Description
-----------

Write CRB_CTRL_REQ_GO_IDLE to TPM_CRB_CTRL_REQ
The device should respond within TIMEOUT_C by clearing the bit.
Anyhow, we do not wait here as a consequent CMD_READY request
will be handled correctly even if idle was not completed.

The function does nothing for devices with ACPI-start method
or SMC-start method.

.. _`crb_go_idle.return`:

Return
------

0 always

.. _`crb_cmd_ready`:

crb_cmd_ready
=============

.. c:function:: int crb_cmd_ready(struct device *dev, struct crb_priv *priv)

    request tpm crb device to enter ready state

    :param struct device \*dev:
        crb device

    :param struct crb_priv \*priv:
        crb private data

.. _`crb_cmd_ready.description`:

Description
-----------

Write CRB_CTRL_REQ_CMD_READY to TPM_CRB_CTRL_REQ
and poll till the device acknowledge it by clearing the bit.
The device should respond within TIMEOUT_C.

The function does nothing for devices with ACPI-start method
or SMC-start method.

.. _`crb_cmd_ready.return`:

Return
------

0 on success -ETIME on timeout;

.. This file was automatic generated / don't edit.

