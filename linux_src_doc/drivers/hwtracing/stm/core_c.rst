.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hwtracing/stm/core.c

.. _`stm_find_device`:

stm_find_device
===============

.. c:function:: struct stm_device *stm_find_device(const char *buf)

    find stm device by name

    :param const char \*buf:
        character buffer containing the name

.. _`stm_find_device.description`:

Description
-----------

This is called when either policy gets assigned to an stm device or an
stm_source device gets linked to an stm device.

This grabs device's reference (get_device()) and module reference, both
of which the calling path needs to make sure to drop with \ :c:func:`stm_put_device`\ .

.. _`stm_find_device.return`:

Return
------

stm device pointer or null if lookup failed.

.. _`stm_put_device`:

stm_put_device
==============

.. c:function:: void stm_put_device(struct stm_device *stm)

    drop references on the stm device

    :param struct stm_device \*stm:
        stm device, previously acquired by \ :c:func:`stm_find_device`\ 

.. _`stm_put_device.description`:

Description
-----------

This drops the module reference and device reference taken by
\ :c:func:`stm_find_device`\  or \ :c:func:`stm_char_open`\ .

.. _`stm_source_link_add`:

stm_source_link_add
===================

.. c:function:: int stm_source_link_add(struct stm_source_device *src, struct stm_device *stm)

    connect an stm_source device to an stm device

    :param struct stm_source_device \*src:
        stm_source device

    :param struct stm_device \*stm:
        stm device

.. _`stm_source_link_add.description`:

Description
-----------

This function establishes a link from stm_source to an stm device so that
the former can send out trace data to the latter.

.. _`stm_source_link_add.return`:

Return
------

0 on success, -errno otherwise.

.. _`__stm_source_link_drop`:

__stm_source_link_drop
======================

.. c:function:: int __stm_source_link_drop(struct stm_source_device *src, struct stm_device *stm)

    detach stm_source from an stm device

    :param struct stm_source_device \*src:
        stm_source device

    :param struct stm_device \*stm:
        stm device

.. _`__stm_source_link_drop.description`:

Description
-----------

If \ ``stm``\  is \ ``src``\ ::link, disconnect them from one another and put the
reference on the \ ``stm``\  device.

Caller must hold stm::link_mutex.

.. _`stm_source_link_drop`:

stm_source_link_drop
====================

.. c:function:: void stm_source_link_drop(struct stm_source_device *src)

    detach stm_source from its stm device

    :param struct stm_source_device \*src:
        stm_source device

.. _`stm_source_link_drop.description`:

Description
-----------

Unlinking means disconnecting from source's STM device; after this
writes will be unsuccessful until it is linked to a new STM device.

This will happen on "stm_source_link" sysfs attribute write to undo
the existing link (if any), or on linked STM device's de-registration.

.. _`stm_source_register_device`:

stm_source_register_device
==========================

.. c:function:: int stm_source_register_device(struct device *parent, struct stm_source_data *data)

    register an stm_source device

    :param struct device \*parent:
        parent device

    :param struct stm_source_data \*data:
        device description structure

.. _`stm_source_register_device.description`:

Description
-----------

This will create a device of stm_source class that can write
data to an stm device once linked.

.. _`stm_source_register_device.return`:

Return
------

0 on success, -errno otherwise.

.. _`stm_source_unregister_device`:

stm_source_unregister_device
============================

.. c:function:: void stm_source_unregister_device(struct stm_source_data *data)

    unregister an stm_source device

    :param struct stm_source_data \*data:
        device description that was used to register the device

.. _`stm_source_unregister_device.description`:

Description
-----------

This will remove a previously created stm_source device from the system.

.. This file was automatic generated / don't edit.

