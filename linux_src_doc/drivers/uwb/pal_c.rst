.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/uwb/pal.c

.. _`uwb_pal_init`:

uwb_pal_init
============

.. c:function:: void uwb_pal_init(struct uwb_pal *pal)

    initialize a UWB PAL

    :param struct uwb_pal \*pal:
        the PAL to initialize

.. _`uwb_pal_register`:

uwb_pal_register
================

.. c:function:: int uwb_pal_register(struct uwb_pal *pal)

    register a UWB PAL

    :param struct uwb_pal \*pal:
        the PAL

.. _`uwb_pal_register.description`:

Description
-----------

The PAL must be initialized with \ :c:func:`uwb_pal_init`\ .

.. _`uwb_rc_class_device_exists`:

uwb_rc_class_device_exists
==========================

.. c:function:: bool uwb_rc_class_device_exists(struct uwb_rc *target_rc)

    :param struct uwb_rc \*target_rc:
        *undescribed*

.. _`uwb_rc_class_device_exists.description`:

Description
-----------

\ ``returns``\  false if the rc does not exist or is quiescing; true otherwise.

.. _`uwb_pal_unregister`:

uwb_pal_unregister
==================

.. c:function:: void uwb_pal_unregister(struct uwb_pal *pal)

    unregister a UWB PAL

    :param struct uwb_pal \*pal:
        the PAL

.. _`uwb_rc_pal_init`:

uwb_rc_pal_init
===============

.. c:function:: void uwb_rc_pal_init(struct uwb_rc *rc)

    initialize the PAL related parts of a radio controller

    :param struct uwb_rc \*rc:
        the radio controller

.. This file was automatic generated / don't edit.
