.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/extcon/devres.c

.. _`devm_extcon_dev_allocate`:

devm_extcon_dev_allocate
========================

.. c:function:: struct extcon_dev *devm_extcon_dev_allocate(struct device *dev, const unsigned int *supported_cable)

    Allocate managed extcon device

    :param dev:
        the device owning the extcon device being created
    :type dev: struct device \*

    :param supported_cable:
        the array of the supported external connectors
        ending with EXTCON_NONE.
    :type supported_cable: const unsigned int \*

.. _`devm_extcon_dev_allocate.description`:

Description
-----------

This function manages automatically the memory of extcon device using device
resource management and simplify the control of freeing the memory of extcon
device.

Returns the pointer memory of allocated extcon_dev if success
or ERR_PTR(err) if fail

.. _`devm_extcon_dev_free`:

devm_extcon_dev_free
====================

.. c:function:: void devm_extcon_dev_free(struct device *dev, struct extcon_dev *edev)

    Resource-managed \ :c:func:`extcon_dev_unregister`\ 

    :param dev:
        the device owning the extcon device being created
    :type dev: struct device \*

    :param edev:
        the extcon device to be freed
    :type edev: struct extcon_dev \*

.. _`devm_extcon_dev_free.description`:

Description
-----------

Free the memory that is allocated with \ :c:func:`devm_extcon_dev_allocate`\ 
function.

.. _`devm_extcon_dev_register`:

devm_extcon_dev_register
========================

.. c:function:: int devm_extcon_dev_register(struct device *dev, struct extcon_dev *edev)

    Resource-managed \ :c:func:`extcon_dev_register`\ 

    :param dev:
        the device owning the extcon device being created
    :type dev: struct device \*

    :param edev:
        the extcon device to be registered
    :type edev: struct extcon_dev \*

.. _`devm_extcon_dev_register.description`:

Description
-----------

this function, that extcon device is automatically unregistered on driver
detach. Internally this function calls \ :c:func:`extcon_dev_register`\  function.
To get more information, refer that function.

If extcon device is registered with this function and the device needs to be
unregistered separately, \ :c:func:`devm_extcon_dev_unregister`\  should be used.

Returns 0 if success or negaive error number if failure.

.. _`devm_extcon_dev_unregister`:

devm_extcon_dev_unregister
==========================

.. c:function:: void devm_extcon_dev_unregister(struct device *dev, struct extcon_dev *edev)

    Resource-managed \ :c:func:`extcon_dev_unregister`\ 

    :param dev:
        the device owning the extcon device being created
    :type dev: struct device \*

    :param edev:
        the extcon device to unregistered
    :type edev: struct extcon_dev \*

.. _`devm_extcon_dev_unregister.description`:

Description
-----------

Unregister extcon device that is registered with \ :c:func:`devm_extcon_dev_register`\ 
function.

.. _`devm_extcon_register_notifier`:

devm_extcon_register_notifier
=============================

.. c:function:: int devm_extcon_register_notifier(struct device *dev, struct extcon_dev *edev, unsigned int id, struct notifier_block *nb)

    Resource-managed \ :c:func:`extcon_register_notifier`\ 

    :param dev:
        the device owning the extcon device being created
    :type dev: struct device \*

    :param edev:
        the extcon device
    :type edev: struct extcon_dev \*

    :param id:
        the unique id among the extcon enumeration
    :type id: unsigned int

    :param nb:
        a notifier block to be registered
    :type nb: struct notifier_block \*

.. _`devm_extcon_register_notifier.description`:

Description
-----------

This function manages automatically the notifier of extcon device using
device resource management and simplify the control of unregistering
the notifier of extcon device.

Note that the second parameter given to the callback of nb (val) is
"old_state", not the current state. The current state can be retrieved
by looking at the third pameter (edev pointer)'s state value.

Returns 0 if success or negaive error number if failure.

.. _`devm_extcon_unregister_notifier`:

devm_extcon_unregister_notifier
===============================

.. c:function:: void devm_extcon_unregister_notifier(struct device *dev, struct extcon_dev *edev, unsigned int id, struct notifier_block *nb)

    :param dev:
        the device owning the extcon device being created
    :type dev: struct device \*

    :param edev:
        the extcon device
    :type edev: struct extcon_dev \*

    :param id:
        the unique id among the extcon enumeration
    :type id: unsigned int

    :param nb:
        a notifier block to be registered
    :type nb: struct notifier_block \*

.. _`devm_extcon_register_notifier_all`:

devm_extcon_register_notifier_all
=================================

.. c:function:: int devm_extcon_register_notifier_all(struct device *dev, struct extcon_dev *edev, struct notifier_block *nb)

    - Resource-managed \ :c:func:`extcon_register_notifier_all`\ 

    :param dev:
        the device owning the extcon device being created
    :type dev: struct device \*

    :param edev:
        the extcon device
    :type edev: struct extcon_dev \*

    :param nb:
        a notifier block to be registered
    :type nb: struct notifier_block \*

.. _`devm_extcon_register_notifier_all.description`:

Description
-----------

This function manages automatically the notifier of extcon device using
device resource management and simplify the control of unregistering
the notifier of extcon device. To get more information, refer that function.

Returns 0 if success or negaive error number if failure.

.. _`devm_extcon_unregister_notifier_all`:

devm_extcon_unregister_notifier_all
===================================

.. c:function:: void devm_extcon_unregister_notifier_all(struct device *dev, struct extcon_dev *edev, struct notifier_block *nb)

    - Resource-managed \ :c:func:`extcon_unregister_notifier_all`\ 

    :param dev:
        the device owning the extcon device being created
    :type dev: struct device \*

    :param edev:
        the extcon device
    :type edev: struct extcon_dev \*

    :param nb:
        a notifier block to be registered
    :type nb: struct notifier_block \*

.. This file was automatic generated / don't edit.

