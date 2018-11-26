.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/char/tpm/tpm_crb.c

.. _`__crb_go_idle`:

\__crb_go_idle
==============

.. c:function:: int __crb_go_idle(struct device *dev, struct crb_priv *priv)

    request tpm crb device to go the idle state

    :param dev:
        crb device
    :type dev: struct device \*

    :param priv:
        crb private data
    :type priv: struct crb_priv \*

.. _`__crb_go_idle.description`:

Description
-----------

Write CRB_CTRL_REQ_GO_IDLE to TPM_CRB_CTRL_REQ
The device should respond within TIMEOUT_C by clearing the bit.
Anyhow, we do not wait here as a consequent CMD_READY request
will be handled correctly even if idle was not completed.

The function does nothing for devices with ACPI-start method
or SMC-start method.

.. _`__crb_go_idle.return`:

Return
------

0 always

.. _`__crb_cmd_ready`:

\__crb_cmd_ready
================

.. c:function:: int __crb_cmd_ready(struct device *dev, struct crb_priv *priv)

    request tpm crb device to enter ready state

    :param dev:
        crb device
    :type dev: struct device \*

    :param priv:
        crb private data
    :type priv: struct crb_priv \*

.. _`__crb_cmd_ready.description`:

Description
-----------

Write CRB_CTRL_REQ_CMD_READY to TPM_CRB_CTRL_REQ
and poll till the device acknowledge it by clearing the bit.
The device should respond within TIMEOUT_C.

The function does nothing for devices with ACPI-start method
or SMC-start method.

.. _`__crb_cmd_ready.return`:

Return
------

0 on success -ETIME on timeout;

.. This file was automatic generated / don't edit.

