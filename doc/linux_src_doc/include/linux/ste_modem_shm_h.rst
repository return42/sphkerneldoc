.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/ste_modem_shm.h

.. _`ste_modem_dev_cb`:

struct ste_modem_dev_cb
=======================

.. c:type:: struct ste_modem_dev_cb

    Callbacks for modem initiated events.

.. _`ste_modem_dev_cb.definition`:

Definition
----------

.. code-block:: c

    struct ste_modem_dev_cb {
        void (* kick) (struct ste_modem_device *mdev, int notify_id);
    }

.. _`ste_modem_dev_cb.members`:

Members
-------

kick
    Called when the modem kicks the host.

.. _`ste_modem_dev_cb.description`:

Description
-----------

This structure contains callbacks for actions triggered by the modem.

.. _`ste_modem_dev_ops`:

struct ste_modem_dev_ops
========================

.. c:type:: struct ste_modem_dev_ops

    Functions to control modem and modem interface.

.. _`ste_modem_dev_ops.definition`:

Definition
----------

.. code-block:: c

    struct ste_modem_dev_ops {
        int (* power) (struct ste_modem_device *mdev, bool on);
        int (* kick) (struct ste_modem_device *mdev, int notify_id);
        int (* kick_subscribe) (struct ste_modem_device *mdev, int notify_id);
        int (* setup) (struct ste_modem_device *mdev,struct ste_modem_dev_cb *cfg);
    }

.. _`ste_modem_dev_ops.members`:

Members
-------

power
    Main power switch, used for cold-start or complete power off.

kick
    Kick the modem.

kick_subscribe
    Subscribe for notifications from the modem.

setup
    Provide callback functions to modem device.

.. _`ste_modem_dev_ops.description`:

Description
-----------

This structure contains functions used by the ste remoteproc driver
to manage the modem.

.. _`ste_modem_device`:

struct ste_modem_device
=======================

.. c:type:: struct ste_modem_device

    represent the STE modem device

.. _`ste_modem_device.definition`:

Definition
----------

.. code-block:: c

    struct ste_modem_device {
        struct platform_device pdev;
        struct ste_modem_dev_ops ops;
        void *drv_data;
    }

.. _`ste_modem_device.members`:

Members
-------

pdev
    Reference to platform device

ops
    Operations used to manage the modem.

drv_data
    Driver private data.

.. This file was automatic generated / don't edit.

