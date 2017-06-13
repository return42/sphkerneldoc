.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/extcon/devres.c

.. _`devm_extcon_dev_allocate`:

devm_extcon_dev_allocate
========================

.. c:function:: struct extcon_dev *devm_extcon_dev_allocate(struct device *dev, const unsigned int *supported_cable)

    Allocate managed extcon device

    :param struct device \*dev:
        device owning the extcon device being created

    :param const unsigned int \*supported_cable:
        Array of supported extcon ending with EXTCON_NONE.
        If supported_cable is NULL, cable name related APIs
        are disabled.

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

    :param struct device \*dev:
        device the extcon belongs to

    :param struct extcon_dev \*edev:
        the extcon device to unregister

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

    :param struct device \*dev:
        device to allocate extcon device

    :param struct extcon_dev \*edev:
        the new extcon device to register

.. _`devm_extcon_dev_register.description`:

Description
-----------

Managed \ :c:func:`extcon_dev_register`\  function. If extcon device is attached with
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

    :param struct device \*dev:
        device the extcon belongs to

    :param struct extcon_dev \*edev:
        the extcon device to unregister

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

    :param struct device \*dev:
        device to allocate extcon device

    :param struct extcon_dev \*edev:
        the extcon device that has the external connecotr.

    :param unsigned int id:
        the unique id of each external connector in extcon enumeration.

    :param struct notifier_block \*nb:
        a notifier block to be registered.

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

    :param struct device \*dev:
        device to allocate extcon device

    :param struct extcon_dev \*edev:
        the extcon device that has the external connecotr.

    :param unsigned int id:
        the unique id of each external connector in extcon enumeration.

    :param struct notifier_block \*nb:
        a notifier block to be registered.

.. _`devm_extcon_register_notifier_all`:

devm_extcon_register_notifier_all
=================================

.. c:function:: int devm_extcon_register_notifier_all(struct device *dev, struct extcon_dev *edev, struct notifier_block *nb)

    - Resource-managed \ :c:func:`extcon_register_notifier_all`\ 

    :param struct device \*dev:
        device to allocate extcon device

    :param struct extcon_dev \*edev:
        the extcon device that has the external connecotr.

    :param struct notifier_block \*nb:
        a notifier block to be registered.

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

    :param struct device \*dev:
        device to allocate extcon device

    :param struct extcon_dev \*edev:
        the extcon device that has the external connecotr.

    :param struct notifier_block \*nb:
        a notifier block to be registered.

.. This file was automatic generated / don't edit.

