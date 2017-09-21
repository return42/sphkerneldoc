.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/typec/ucsi/ucsi.c

.. _`ucsi_notify`:

ucsi_notify
===========

.. c:function:: void ucsi_notify(struct ucsi *ucsi)

    PPM notification handler

    :param struct ucsi \*ucsi:
        Source UCSI Interface for the notifications

.. _`ucsi_notify.description`:

Description
-----------

Handle notifications from PPM of \ ``ucsi``\ .

.. _`ucsi_register_ppm`:

ucsi_register_ppm
=================

.. c:function:: struct ucsi *ucsi_register_ppm(struct device *dev, struct ucsi_ppm *ppm)

    Register UCSI PPM Interface

    :param struct device \*dev:
        Device interface to the PPM

    :param struct ucsi_ppm \*ppm:
        The PPM interface

.. _`ucsi_register_ppm.description`:

Description
-----------

Allocates UCSI instance, associates it with \ ``ppm``\  and returns it to the
caller, and schedules initialization of the interface.

.. _`ucsi_unregister_ppm`:

ucsi_unregister_ppm
===================

.. c:function:: void ucsi_unregister_ppm(struct ucsi *ucsi)

    Unregister UCSI PPM Interface

    :param struct ucsi \*ucsi:
        struct ucsi associated with the PPM

.. _`ucsi_unregister_ppm.description`:

Description
-----------

Unregister UCSI PPM that was created with \ :c:func:`ucsi_register`\ .

.. This file was automatic generated / don't edit.

