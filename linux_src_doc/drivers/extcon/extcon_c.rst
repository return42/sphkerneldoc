.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/extcon/extcon.c

.. _`extcon_cable`:

struct extcon_cable
===================

.. c:type:: struct extcon_cable

    An internal data for each cable of extcon device.

.. _`extcon_cable.definition`:

Definition
----------

.. code-block:: c

    struct extcon_cable {
        struct extcon_dev *edev;
        int cable_index;
        struct attribute_group attr_g;
        struct device_attribute attr_name;
        struct device_attribute attr_state;
        struct attribute  *attrs[3];
        union extcon_property_value usb_propval[EXTCON_PROP_USB_CNT];
        union extcon_property_value chg_propval[EXTCON_PROP_CHG_CNT];
        union extcon_property_value jack_propval[EXTCON_PROP_JACK_CNT];
        union extcon_property_value disp_propval[EXTCON_PROP_DISP_CNT];
        unsigned long usb_bits[BITS_TO_LONGS(EXTCON_PROP_USB_CNT)];
        unsigned long chg_bits[BITS_TO_LONGS(EXTCON_PROP_CHG_CNT)];
        unsigned long jack_bits[BITS_TO_LONGS(EXTCON_PROP_JACK_CNT)];
        unsigned long disp_bits[BITS_TO_LONGS(EXTCON_PROP_DISP_CNT)];
    }

.. _`extcon_cable.members`:

Members
-------

edev
    The extcon device

cable_index
    Index of this cable in the edev

attr_g
    Attribute group for the cable

attr_name
    "name" sysfs entry

attr_state
    "state" sysfs entry

attrs
    Array pointing to attr_name and attr_state for attr_g

.. _`check_mutually_exclusive`:

check_mutually_exclusive
========================

.. c:function:: int check_mutually_exclusive(struct extcon_dev *edev, u32 new_state)

    Check if new_state violates mutually_exclusive condition.

    :param struct extcon_dev \*edev:
        the extcon device

    :param u32 new_state:
        new cable attach status for \ ``edev``\ 

.. _`check_mutually_exclusive.description`:

Description
-----------

Returns 0 if nothing violates. Returns the index + 1 for the first
violated condition.

.. _`extcon_sync`:

extcon_sync
===========

.. c:function:: int extcon_sync(struct extcon_dev *edev, unsigned int id)

    Synchronize the states for both the attached/detached

    :param struct extcon_dev \*edev:
        the extcon device that has the cable.

    :param unsigned int id:
        *undescribed*

.. _`extcon_sync.description`:

Description
-----------

This function send a notification to synchronize the all states of a
specific external connector

.. _`extcon_get_state`:

extcon_get_state
================

.. c:function:: int extcon_get_state(struct extcon_dev *edev, const unsigned int id)

    Get the state of a external connector.

    :param struct extcon_dev \*edev:
        the extcon device that has the cable.

    :param const unsigned int id:
        the unique id of each external connector in extcon enumeration.

.. _`extcon_set_state`:

extcon_set_state
================

.. c:function:: int extcon_set_state(struct extcon_dev *edev, unsigned int id, bool cable_state)

    Set the state of a external connector. without a notification.

    :param struct extcon_dev \*edev:
        the extcon device that has the cable.

    :param unsigned int id:
        the unique id of each external connector
        in extcon enumeration.

    :param bool cable_state:
        *undescribed*

.. _`extcon_set_state.description`:

Description
-----------

This function only set the state of a external connector without
a notification. To synchronize the data of a external connector,
use \ :c:func:`extcon_set_state_sync`\  and \ :c:func:`extcon_sync`\ .

.. _`extcon_set_state_sync`:

extcon_set_state_sync
=====================

.. c:function:: int extcon_set_state_sync(struct extcon_dev *edev, unsigned int id, bool cable_state)

    Set the state of a external connector with a notification.

    :param struct extcon_dev \*edev:
        the extcon device that has the cable.

    :param unsigned int id:
        the unique id of each external connector
        in extcon enumeration.

    :param bool cable_state:
        *undescribed*

.. _`extcon_set_state_sync.description`:

Description
-----------

This function set the state of external connector and synchronize the data
by usning a notification.

.. _`extcon_get_property`:

extcon_get_property
===================

.. c:function:: int extcon_get_property(struct extcon_dev *edev, unsigned int id, unsigned int prop, union extcon_property_value *prop_val)

    Get the property value of a specific cable.

    :param struct extcon_dev \*edev:
        the extcon device that has the cable.

    :param unsigned int id:
        the unique id of each external connector
        in extcon enumeration.

    :param unsigned int prop:
        the property id among enum extcon_property.

    :param union extcon_property_value \*prop_val:
        the pointer which store the value of property.

.. _`extcon_get_property.description`:

Description
-----------

When getting the property value of external connector, the external connector
should be attached. If detached state, function just return 0 without
property value. Also, the each property should be included in the list of
supported properties according to the type of external connectors.

Returns 0 if success or error number if fail

.. _`extcon_set_property`:

extcon_set_property
===================

.. c:function:: int extcon_set_property(struct extcon_dev *edev, unsigned int id, unsigned int prop, union extcon_property_value prop_val)

    Set the property value of a specific cable.

    :param struct extcon_dev \*edev:
        the extcon device that has the cable.

    :param unsigned int id:
        the unique id of each external connector
        in extcon enumeration.

    :param unsigned int prop:
        the property id among enum extcon_property.

    :param union extcon_property_value prop_val:
        the pointer including the new value of property.

.. _`extcon_set_property.description`:

Description
-----------

The each property should be included in the list of supported properties
according to the type of external connectors.

Returns 0 if success or error number if fail

.. _`extcon_set_property_sync`:

extcon_set_property_sync
========================

.. c:function:: int extcon_set_property_sync(struct extcon_dev *edev, unsigned int id, unsigned int prop, union extcon_property_value prop_val)

    Set the property value of a specific cable

    :param struct extcon_dev \*edev:
        *undescribed*

    :param unsigned int id:
        *undescribed*

    :param unsigned int prop:
        *undescribed*

    :param union extcon_property_value prop_val:
        the pointer including the new value of property.

.. _`extcon_set_property_sync.description`:

Description
-----------

When setting the property value of external connector, the external connector
should be attached. The each property should be included in the list of
supported properties according to the type of external connectors.

Returns 0 if success or error number if fail

.. _`extcon_get_property_capability`:

extcon_get_property_capability
==============================

.. c:function:: int extcon_get_property_capability(struct extcon_dev *edev, unsigned int id, unsigned int prop)

    Get the capability of property of an external connector.

    :param struct extcon_dev \*edev:
        the extcon device that has the cable.

    :param unsigned int id:
        the unique id of each external connector
        in extcon enumeration.

    :param unsigned int prop:
        the property id among enum extcon_property.

.. _`extcon_get_property_capability.description`:

Description
-----------

Returns 1 if the property is available or 0 if not available.

.. _`extcon_set_property_capability`:

extcon_set_property_capability
==============================

.. c:function:: int extcon_set_property_capability(struct extcon_dev *edev, unsigned int id, unsigned int prop)

    Set the capability of a property of an external connector.

    :param struct extcon_dev \*edev:
        the extcon device that has the cable.

    :param unsigned int id:
        the unique id of each external connector
        in extcon enumeration.

    :param unsigned int prop:
        the property id among enum extcon_property.

.. _`extcon_set_property_capability.description`:

Description
-----------

This function set the capability of a property for an external connector
to mark the bit in capability bitmap which mean the available state of
a property.

Returns 0 if success or error number if fail

.. _`extcon_get_extcon_dev`:

extcon_get_extcon_dev
=====================

.. c:function:: struct extcon_dev *extcon_get_extcon_dev(const char *extcon_name)

    Get the extcon device instance from the name

    :param const char \*extcon_name:
        The extcon name provided with \ :c:func:`extcon_dev_register`\ 

.. _`extcon_register_notifier`:

extcon_register_notifier
========================

.. c:function:: int extcon_register_notifier(struct extcon_dev *edev, unsigned int id, struct notifier_block *nb)

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

.. c:function:: int extcon_unregister_notifier(struct extcon_dev *edev, unsigned int id, struct notifier_block *nb)

    Unregister a notifiee from the extcon device.

    :param struct extcon_dev \*edev:
        the extcon device that has the external connecotr.

    :param unsigned int id:
        the unique id of each external connector in extcon enumeration.

    :param struct notifier_block \*nb:
        a notifier block to be registered.

.. _`extcon_register_notifier_all`:

extcon_register_notifier_all
============================

.. c:function:: int extcon_register_notifier_all(struct extcon_dev *edev, struct notifier_block *nb)

    Register a notifier block for all connectors

    :param struct extcon_dev \*edev:
        the extcon device that has the external connecotr.

    :param struct notifier_block \*nb:
        a notifier block to be registered.

.. _`extcon_register_notifier_all.description`:

Description
-----------

This fucntion registers a notifier block in order to receive the state
change of all supported external connectors from extcon device.
And The second parameter given to the callback of nb (val) is
the current state and third parameter is the edev pointer.

Returns 0 if success or error number if fail

.. _`extcon_unregister_notifier_all`:

extcon_unregister_notifier_all
==============================

.. c:function:: int extcon_unregister_notifier_all(struct extcon_dev *edev, struct notifier_block *nb)

    Unregister a notifier block from extcon.

    :param struct extcon_dev \*edev:
        the extcon device that has the external connecotr.

    :param struct notifier_block \*nb:
        a notifier block to be registered.

.. _`extcon_unregister_notifier_all.description`:

Description
-----------

Returns 0 if success or error number if fail

.. _`extcon_dev_register`:

extcon_dev_register
===================

.. c:function:: int extcon_dev_register(struct extcon_dev *edev)

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

.. c:function:: void extcon_dev_unregister(struct extcon_dev *edev)

    Unregister the extcon device.

    :param struct extcon_dev \*edev:
        the extcon device instance to be unregistered.

.. _`extcon_dev_unregister.description`:

Description
-----------

Note that this does not call kfree(edev) because edev was not allocated
by this class.

.. _`extcon_get_edev_name`:

extcon_get_edev_name
====================

.. c:function:: const char *extcon_get_edev_name(struct extcon_dev *edev)

    Get the name of the extcon device.

    :param struct extcon_dev \*edev:
        the extcon device

.. This file was automatic generated / don't edit.

