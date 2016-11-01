.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/input/input-polldev.c

.. _`input_allocate_polled_device`:

input_allocate_polled_device
============================

.. c:function:: struct input_polled_dev *input_allocate_polled_device( void)

    allocate memory for polled device

    :param  void:
        no arguments

.. _`input_allocate_polled_device.description`:

Description
-----------

The function allocates memory for a polled device and also
for an input device associated with this polled device.

.. _`devm_input_allocate_polled_device`:

devm_input_allocate_polled_device
=================================

.. c:function:: struct input_polled_dev *devm_input_allocate_polled_device(struct device *dev)

    allocate managed polled device

    :param struct device \*dev:
        device owning the polled device being created

.. _`devm_input_allocate_polled_device.description`:

Description
-----------

Returns prepared \ :c:type:`struct input_polled_dev <input_polled_dev>`\  or \ ``NULL``\ .

Managed polled input devices do not need to be explicitly unregistered
or freed as it will be done automatically when owner device unbinds
from * its driver (or binding fails). Once such managed polled device
is allocated, it is ready to be set up and registered in the same
fashion as regular polled input devices (using
\ :c:func:`input_register_polled_device`\  function).

If you want to manually unregister and free such managed polled devices,
it can be still done by calling \ :c:func:`input_unregister_polled_device`\  and
\ :c:func:`input_free_polled_device`\ , although it is rarely needed.

.. _`devm_input_allocate_polled_device.note`:

NOTE
----

the owner device is set up as parent of input device and users
should not override it.

.. _`input_free_polled_device`:

input_free_polled_device
========================

.. c:function:: void input_free_polled_device(struct input_polled_dev *dev)

    free memory allocated for polled device

    :param struct input_polled_dev \*dev:
        device to free

.. _`input_free_polled_device.description`:

Description
-----------

The function frees memory allocated for polling device and drops
reference to the associated input device.

.. _`input_register_polled_device`:

input_register_polled_device
============================

.. c:function:: int input_register_polled_device(struct input_polled_dev *dev)

    register polled device

    :param struct input_polled_dev \*dev:
        device to register

.. _`input_register_polled_device.description`:

Description
-----------

The function registers previously initialized polled input device
with input layer. The device should be allocated with call to
\ :c:func:`input_allocate_polled_device`\ . Callers should also set up \ :c:func:`poll`\ 
method and set up capabilities (id, name, phys, bits) of the
corresponding input_dev structure.

.. _`input_unregister_polled_device`:

input_unregister_polled_device
==============================

.. c:function:: void input_unregister_polled_device(struct input_polled_dev *dev)

    unregister polled device

    :param struct input_polled_dev \*dev:
        device to unregister

.. _`input_unregister_polled_device.description`:

Description
-----------

The function unregisters previously registered polled input
device from input layer. Polling is stopped and device is
ready to be freed with call to \ :c:func:`input_free_polled_device`\ .

.. This file was automatic generated / don't edit.

