.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/atmdev.h

.. _`register_atm_ioctl`:

register_atm_ioctl
==================

.. c:function:: void register_atm_ioctl(struct atm_ioctl *)

    register handler for ioctl operations

    :param struct atm_ioctl \*:
        *undescribed*

.. _`register_atm_ioctl.description`:

Description
-----------

Special (non-device) handlers of ioctl's should
register here. If you're a normal device, you should
set .ioctl in your atmdev_ops instead.

.. _`deregister_atm_ioctl`:

deregister_atm_ioctl
====================

.. c:function:: void deregister_atm_ioctl(struct atm_ioctl *)

    remove the ioctl handler

    :param struct atm_ioctl \*:
        *undescribed*

.. This file was automatic generated / don't edit.

