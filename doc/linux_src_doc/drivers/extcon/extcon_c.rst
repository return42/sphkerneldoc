.. -*- coding: utf-8; mode: rst -*-

========
extcon.c
========


.. _`check_mutually_exclusive`:

check_mutually_exclusive
========================

.. c:function:: int check_mutually_exclusive (struct extcon_dev *edev, u32 new_state)

    Check if new_state violates mutually_exclusive condition.

    :param struct extcon_dev \*edev:
        the extcon device

    :param u32 new_state:
        new cable attach status for ``edev``



.. _`check_mutually_exclusive.description`:

Description
-----------

Returns 0 if nothing violates. Returns the index + 1 for the first
violated condition.



.. _`extcon_update_state`:

extcon_update_state
===================

.. c:function:: int extcon_update_state (struct extcon_dev *edev, u32 mask, u32 state)

    Update the cable attach states of the extcon device only for the masked bits.

    :param struct extcon_dev \*edev:
        the extcon device

    :param u32 mask:
        the bit mask to designate updated bits.

    :param u32 state:
        new cable attach status for ``edev``



.. _`extcon_update_state.description`:

Description
-----------

Changing the state sends uevent with environment variable containing
the name of extcon device (envp[0]) and the state output (envp[1]).
Tizen uses this format for extcon device to get events from ports.
Android uses this format as well.

Note that the notifier provides which bits are changed in the state
variable with the val parameter (second) to the callback.



.. _`extcon_set_state`:

extcon_set_state
================

.. c:function:: int extcon_set_state (struct extcon_dev *edev, u32 state)

    Set the cable attach states of the extcon device.

    :param struct extcon_dev \*edev:
        the extcon device

    :param u32 state:
        new cable attach status for ``edev``



.. _`extcon_set_state.description`:

Description
-----------

Note that notifier provides which bits are changed in the state
variable with the val parameter (second) to the callback.



.. _`extcon_get_cable_state_`:

extcon_get_cable_state_
=======================

.. c:function:: int extcon_get_cable_state_ (struct extcon_dev *edev, const unsigned int id)

    Get the status of a specific cable.

    :param struct extcon_dev \*edev:
        the extcon device that has the cable.

    :param const unsigned int id:
        the unique id of each external connector in extcon enumeration.



.. _`extcon_get_cable_state`:

extcon_get_cable_state
======================

.. c:function:: int extcon_get_cable_state (struct extcon_dev *edev, const char *cable_name)

    Get the status of a specific cable.

    :param struct extcon_dev \*edev:
        the extcon device that has the cable.

    :param const char \*cable_name:
        cable name.



.. _`extcon_get_cable_state.description`:

Description
-----------

Note that this is slower than extcon_get_cable_state_.



.. _`extcon_set_cable_state_`:

extcon_set_cable_state_
=======================

.. c:function:: int extcon_set_cable_state_ (struct extcon_dev *edev, unsigned int id, bool cable_state)

    Set the status of a specific cable.

    :param struct extcon_dev \*edev:
        the extcon device that has the cable.

    :param unsigned int id:
        the unique id of each external connector
        in extcon enumeration.

    :param bool cable_state:

        *undescribed*



.. _`extcon_set_cable_state_.true`:

true
----

attached / false: detached.



.. _`extcon_set_cable_state`:

extcon_set_cable_state
======================

.. c:function:: int extcon_set_cable_state (struct extcon_dev *edev, const char *cable_name, bool cable_state)

    Set the status of a specific cable.

    :param struct extcon_dev \*edev:
        the extcon device that has the cable.

    :param const char \*cable_name:
        cable name.

    :param bool cable_state:
        the new cable status. The default semantics is



.. _`extcon_set_cable_state.true`:

true
----

attached / false: detached.

Note that this is slower than extcon_set_cable_state_.



.. _`extcon_get_extcon_dev`:

extcon_get_extcon_dev
=====================

.. c:function:: struct extcon_dev *extcon_get_extcon_dev (const char *extcon_name)

    Get the extcon device instance from the name

    :param const char \*extcon_name:
        The extcon name provided with :c:func:`extcon_dev_register`



.. _`extcon_register_interest`:

extcon_register_interest
========================

.. c:function:: int extcon_register_interest (struct extcon_specific_cable_nb *obj, const char *extcon_name, const char *cable_name, struct notifier_block *nb)

    Register a notifier for a state change of a specific cable, not an entier set of cables of a extcon device.

    :param struct extcon_specific_cable_nb \*obj:
        an empty extcon_specific_cable_nb object to be returned.

    :param const char \*extcon_name:
        the name of extcon device.
        if NULL, extcon_register_interest will register
        every cable with the target cable_name given.

    :param const char \*cable_name:
        the target cable name.

    :param struct notifier_block \*nb:
        the notifier block to get notified.



.. _`extcon_register_interest.description`:

Description
-----------

Provide an empty extcon_specific_cable_nb. :c:func:`extcon_register_interest` sets
the struct for you.

extcon_register_interest is a helper function for those who want to get
notification for a single specific cable's status change. If a user wants
to get notification for any changes of all cables of a extcon device,
he/she should use the general :c:func:`extcon_register_notifier`.

Note that the second parameter given to the callback of nb (val) is
"old_state", not the current state. The current state can be retrieved
by looking at the third pameter (edev pointer)'s state value.



.. _`extcon_unregister_interest`:

extcon_unregister_interest
==========================

.. c:function:: int extcon_unregister_interest (struct extcon_specific_cable_nb *obj)

    Unregister the notifier registered by extcon_register_interest().

    :param struct extcon_specific_cable_nb \*obj:
        the extcon_specific_cable_nb object returned by
        :c:func:`extcon_register_interest`.



.. _`extcon_register_notifier`:

extcon_register_notifier
========================

.. c:function:: int extcon_register_notifier (struct extcon_dev *edev, unsigned int id, struct notifier_block *nb)

    Register a notifiee to get notified by any attach status changes from the extcon.

    :param struct extcon_dev \*edev:
        the extcon device that has the external connecotr.

    :param unsigned int id:
        the unique id of each external connector in extcon enumeration.

    :param struct notifier_block \*nb:
        a notifier block to be registered.



.. _`extcon_register_notifier.description`:

Description
-----------

Note that the second parameter given to the callback of nb (val) is
"old_state", not the current state. The current state can be retrieved
by looking at the third pameter (edev pointer)'s state value.



.. _`extcon_unregister_notifier`:

extcon_unregister_notifier
==========================

.. c:function:: int extcon_unregister_notifier (struct extcon_dev *edev, unsigned int id, struct notifier_block *nb)

    Unregister a notifiee from the extcon device.

    :param struct extcon_dev \*edev:
        the extcon device that has the external connecotr.

    :param unsigned int id:
        the unique id of each external connector in extcon enumeration.

    :param struct notifier_block \*nb:
        a notifier block to be registered.



.. _`devm_extcon_dev_allocate`:

devm_extcon_dev_allocate
========================

.. c:function:: struct extcon_dev *devm_extcon_dev_allocate (struct device *dev, const unsigned int *supported_cable)

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



.. _`extcon_dev_register`:

extcon_dev_register
===================

.. c:function:: int extcon_dev_register (struct extcon_dev *edev)

    Register a new extcon device

    :param struct extcon_dev \*edev:
        the new extcon device (should be allocated before calling)



.. _`extcon_dev_register.description`:

Description
-----------

Among the members of edev struct, please set the "user initializing data"
in any case and set the "optional callbacks" if required. However, please
do not set the values of "internal data", which are initialized by
this function.



.. _`extcon_dev_unregister`:

extcon_dev_unregister
=====================

.. c:function:: void extcon_dev_unregister (struct extcon_dev *edev)

    Unregister the extcon device.

    :param struct extcon_dev \*edev:
        the extcon device instance to be unregistered.



.. _`extcon_dev_unregister.description`:

Description
-----------

Note that this does not call kfree(edev) because edev was not allocated
by this class.



.. _`devm_extcon_dev_register`:

devm_extcon_dev_register
========================

.. c:function:: int devm_extcon_dev_register (struct device *dev, struct extcon_dev *edev)

    Resource-managed extcon_dev_register()

    :param struct device \*dev:
        device to allocate extcon device

    :param struct extcon_dev \*edev:
        the new extcon device to register



.. _`devm_extcon_dev_register.description`:

Description
-----------

Managed :c:func:`extcon_dev_register` function. If extcon device is attached with
this function, that extcon device is automatically unregistered on driver
detach. Internally this function calls :c:func:`extcon_dev_register` function.
To get more information, refer that function.

If extcon device is registered with this function and the device needs to be
unregistered separately, :c:func:`devm_extcon_dev_unregister` should be used.

Returns 0 if success or negaive error number if failure.



.. _`devm_extcon_dev_unregister`:

devm_extcon_dev_unregister
==========================

.. c:function:: void devm_extcon_dev_unregister (struct device *dev, struct extcon_dev *edev)

    Resource-managed extcon_dev_unregister()

    :param struct device \*dev:
        device the extcon belongs to

    :param struct extcon_dev \*edev:
        the extcon device to unregister



.. _`devm_extcon_dev_unregister.description`:

Description
-----------

Unregister extcon device that is registered with :c:func:`devm_extcon_dev_register`
function.



.. _`extcon_get_edev_name`:

extcon_get_edev_name
====================

.. c:function:: const char *extcon_get_edev_name (struct extcon_dev *edev)

    Get the name of the extcon device.

    :param struct extcon_dev \*edev:
        the extcon device

