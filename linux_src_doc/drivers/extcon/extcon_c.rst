.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/extcon/extcon.c

.. _`extcon_cable`:

struct extcon_cable
===================

.. c:type:: struct extcon_cable

    An internal data for an external connector.

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
        struct attribute *attrs[3];
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
    the extcon device

cable_index
    the index of this cable in the edev

attr_g
    the attribute group for the cable

attr_name
    "name" sysfs entry

attr_state
    "state" sysfs entry

attrs
    the array pointing to attr_name and attr_state for attr_g

usb_propval
    *undescribed*

chg_propval
    *undescribed*

jack_propval
    *undescribed*

disp_propval
    *undescribed*

usb_bits
    *undescribed*

chg_bits
    *undescribed*

jack_bits
    *undescribed*

disp_bits
    *undescribed*

.. _`extcon_sync`:

extcon_sync
===========

.. c:function:: int extcon_sync(struct extcon_dev *edev, unsigned int id)

    Synchronize the state for an external connector.

    :param struct extcon_dev \*edev:
        the extcon device

    :param unsigned int id:
        *undescribed*

.. _`extcon_sync.description`:

Description
-----------

Note that this function send a notification in order to synchronize
the state and property of an external connector.

Returns 0 if success or error number if fail.

.. _`extcon_get_state`:

extcon_get_state
================

.. c:function:: int extcon_get_state(struct extcon_dev *edev, const unsigned int id)

    Get the state of an external connector.

    :param struct extcon_dev \*edev:
        the extcon device

    :param const unsigned int id:
        the unique id indicating an external connector

.. _`extcon_get_state.description`:

Description
-----------

Returns 0 if success or error number if fail.

.. _`extcon_set_state`:

extcon_set_state
================

.. c:function:: int extcon_set_state(struct extcon_dev *edev, unsigned int id, bool state)

    Set the state of an external connector.

    :param struct extcon_dev \*edev:
        the extcon device

    :param unsigned int id:
        the unique id indicating an external connector

    :param bool state:
        the new state of an external connector.
        the default semantics is true: attached / false: detached.

.. _`extcon_set_state.description`:

Description
-----------

Note that this function set the state of an external connector without
a notification. To synchronize the state of an external connector,
have to use \ :c:func:`extcon_set_state_sync`\  and \ :c:func:`extcon_sync`\ .

Returns 0 if success or error number if fail.

.. _`extcon_set_state_sync`:

extcon_set_state_sync
=====================

.. c:function:: int extcon_set_state_sync(struct extcon_dev *edev, unsigned int id, bool state)

    Set the state of an external connector with sync.

    :param struct extcon_dev \*edev:
        the extcon device

    :param unsigned int id:
        the unique id indicating an external connector

    :param bool state:
        the new state of external connector.
        the default semantics is true: attached / false: detached.

.. _`extcon_set_state_sync.description`:

Description
-----------

Note that this function set the state of external connector
and synchronize the state by sending a notification.

Returns 0 if success or error number if fail.

.. _`extcon_get_property`:

extcon_get_property
===================

.. c:function:: int extcon_get_property(struct extcon_dev *edev, unsigned int id, unsigned int prop, union extcon_property_value *prop_val)

    Get the property value of an external connector.

    :param struct extcon_dev \*edev:
        the extcon device

    :param unsigned int id:
        the unique id indicating an external connector

    :param unsigned int prop:
        the property id indicating an extcon property

    :param union extcon_property_value \*prop_val:
        the pointer which store the value of extcon property

.. _`extcon_get_property.description`:

Description
-----------

Note that when getting the property value of external connector,
the external connector should be attached. If detached state, function
return 0 without property value. Also, the each property should be
included in the list of supported properties according to extcon type.

Returns 0 if success or error number if fail.

.. _`extcon_set_property`:

extcon_set_property
===================

.. c:function:: int extcon_set_property(struct extcon_dev *edev, unsigned int id, unsigned int prop, union extcon_property_value prop_val)

    Set the property value of an external connector.

    :param struct extcon_dev \*edev:
        the extcon device

    :param unsigned int id:
        the unique id indicating an external connector

    :param unsigned int prop:
        the property id indicating an extcon property

    :param union extcon_property_value prop_val:
        the pointer including the new value of extcon property

.. _`extcon_set_property.description`:

Description
-----------

Note that each property should be included in the list of supported
properties according to the extcon type.

Returns 0 if success or error number if fail.

.. _`extcon_set_property_sync`:

extcon_set_property_sync
========================

.. c:function:: int extcon_set_property_sync(struct extcon_dev *edev, unsigned int id, unsigned int prop, union extcon_property_value prop_val)

    Set property of an external connector with sync.

    :param struct extcon_dev \*edev:
        *undescribed*

    :param unsigned int id:
        *undescribed*

    :param unsigned int prop:
        *undescribed*

    :param union extcon_property_value prop_val:
        the pointer including the new value of extcon property

.. _`extcon_set_property_sync.description`:

Description
-----------

Note that when setting the property value of external connector,
the external connector should be attached. The each property should
be included in the list of supported properties according to extcon type.

Returns 0 if success or error number if fail.

.. _`extcon_get_property_capability`:

extcon_get_property_capability
==============================

.. c:function:: int extcon_get_property_capability(struct extcon_dev *edev, unsigned int id, unsigned int prop)

    Get the capability of the property for an external connector.

    :param struct extcon_dev \*edev:
        the extcon device

    :param unsigned int id:
        the unique id indicating an external connector

    :param unsigned int prop:
        the property id indicating an extcon property

.. _`extcon_get_property_capability.description`:

Description
-----------

Returns 1 if the property is available or 0 if not available.

.. _`extcon_set_property_capability`:

extcon_set_property_capability
==============================

.. c:function:: int extcon_set_property_capability(struct extcon_dev *edev, unsigned int id, unsigned int prop)

    Set the capability of the property for an external connector.

    :param struct extcon_dev \*edev:
        the extcon device

    :param unsigned int id:
        the unique id indicating an external connector

    :param unsigned int prop:
        the property id indicating an extcon property

.. _`extcon_set_property_capability.description`:

Description
-----------

Note that this function set the capability of the property
for an external connector in order to mark the bit in capability
bitmap which mean the available state of the property.

Returns 0 if success or error number if fail.

.. _`extcon_get_extcon_dev`:

extcon_get_extcon_dev
=====================

.. c:function:: struct extcon_dev *extcon_get_extcon_dev(const char *extcon_name)

    Get the extcon device instance from the name.

    :param const char \*extcon_name:
        the extcon name provided with \ :c:func:`extcon_dev_register`\ 

.. _`extcon_get_extcon_dev.description`:

Description
-----------

Return the pointer of extcon device if success or ERR_PTR(err) if fail.

.. _`extcon_register_notifier`:

extcon_register_notifier
========================

.. c:function:: int extcon_register_notifier(struct extcon_dev *edev, unsigned int id, struct notifier_block *nb)

    Register a notifier block to get notified by any state changes from the extcon.

    :param struct extcon_dev \*edev:
        the extcon device

    :param unsigned int id:
        the unique id indicating an external connector

    :param struct notifier_block \*nb:
        a notifier block to be registered

.. _`extcon_register_notifier.description`:

Description
-----------

Note that the second parameter given to the callback of nb (val) is
the current state of an external connector and the third pameter
is the pointer of extcon device.

Returns 0 if success or error number if fail.

.. _`extcon_unregister_notifier`:

extcon_unregister_notifier
==========================

.. c:function:: int extcon_unregister_notifier(struct extcon_dev *edev, unsigned int id, struct notifier_block *nb)

    Unregister a notifier block from the extcon.

    :param struct extcon_dev \*edev:
        the extcon device

    :param unsigned int id:
        the unique id indicating an external connector

    :param struct notifier_block \*nb:
        a notifier block to be registered

.. _`extcon_unregister_notifier.description`:

Description
-----------

Returns 0 if success or error number if fail.

.. _`extcon_register_notifier_all`:

extcon_register_notifier_all
============================

.. c:function:: int extcon_register_notifier_all(struct extcon_dev *edev, struct notifier_block *nb)

    Register a notifier block for all connectors.

    :param struct extcon_dev \*edev:
        the extcon device

    :param struct notifier_block \*nb:
        a notifier block to be registered

.. _`extcon_register_notifier_all.description`:

Description
-----------

Note that this function registers a notifier block in order to receive
the state change of all supported external connectors from extcon device.
And the second parameter given to the callback of nb (val) is
the current state and the third pameter is the pointer of extcon device.

Returns 0 if success or error number if fail.

.. _`extcon_unregister_notifier_all`:

extcon_unregister_notifier_all
==============================

.. c:function:: int extcon_unregister_notifier_all(struct extcon_dev *edev, struct notifier_block *nb)

    Unregister a notifier block from extcon.

    :param struct extcon_dev \*edev:
        the extcon device

    :param struct notifier_block \*nb:
        a notifier block to be registered

.. _`extcon_unregister_notifier_all.description`:

Description
-----------

Returns 0 if success or error number if fail.

.. _`extcon_dev_register`:

extcon_dev_register
===================

.. c:function:: int extcon_dev_register(struct extcon_dev *edev)

    Register an new extcon device

    :param struct extcon_dev \*edev:
        the extcon device to be registered

.. _`extcon_dev_register.description`:

Description
-----------

Among the members of edev struct, please set the "user initializing data"
do not set the values of "internal data", which are initialized by
this function.

Note that before calling this funciton, have to allocate the memory
of an extcon device by using the \ :c:func:`extcon_dev_allocate`\ . And the extcon
dev should include the supported_cable information.

Returns 0 if success or error number if fail.

.. _`extcon_dev_unregister`:

extcon_dev_unregister
=====================

.. c:function:: void extcon_dev_unregister(struct extcon_dev *edev)

    Unregister the extcon device.

    :param struct extcon_dev \*edev:
        the extcon device to be unregistered.

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

