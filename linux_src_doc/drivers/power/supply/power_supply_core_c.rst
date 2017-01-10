.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/power/supply/power_supply_core.c

.. _`power_supply_get_by_name`:

power_supply_get_by_name
========================

.. c:function:: struct power_supply *power_supply_get_by_name(const char *name)

    Search for a power supply and returns its ref

    :param const char \*name:
        Power supply name to fetch

.. _`power_supply_get_by_name.description`:

Description
-----------

If power supply was found, it increases reference count for the
internal power supply's device. The user should \ :c:func:`power_supply_put`\ 
after usage.

.. _`power_supply_get_by_name.return`:

Return
------

On success returns a reference to a power supply with
matching name equals to \ ``name``\ , a NULL otherwise.

.. _`power_supply_put`:

power_supply_put
================

.. c:function:: void power_supply_put(struct power_supply *psy)

    Drop reference obtained with power_supply_get_by_name

    :param struct power_supply \*psy:
        Reference to put

.. _`power_supply_put.description`:

Description
-----------

The reference to power supply should be put before unregistering
the power supply.

.. _`power_supply_get_by_phandle`:

power_supply_get_by_phandle
===========================

.. c:function:: struct power_supply *power_supply_get_by_phandle(struct device_node *np, const char *property)

    Search for a power supply and returns its ref

    :param struct device_node \*np:
        Pointer to device node holding phandle property

    :param const char \*property:
        Name of property holding a power supply name

.. _`power_supply_get_by_phandle.description`:

Description
-----------

If power supply was found, it increases reference count for the
internal power supply's device. The user should \ :c:func:`power_supply_put`\ 
after usage.

.. _`power_supply_get_by_phandle.return`:

Return
------

On success returns a reference to a power supply with
matching name equals to value under \ ``property``\ , NULL or ERR_PTR otherwise.

.. _`devm_power_supply_get_by_phandle`:

devm_power_supply_get_by_phandle
================================

.. c:function:: struct power_supply *devm_power_supply_get_by_phandle(struct device *dev, const char *property)

    Resource managed version of \ :c:func:`power_supply_get_by_phandle`\ 

    :param struct device \*dev:
        Pointer to device holding phandle property

    :param const char \*property:
        Name of property holding a power supply phandle

.. _`devm_power_supply_get_by_phandle.return`:

Return
------

On success returns a reference to a power supply with
matching name equals to value under \ ``property``\ , NULL or ERR_PTR otherwise.

.. _`power_supply_register`:

power_supply_register
=====================

.. c:function:: struct power_supply *power_supply_register(struct device *parent, const struct power_supply_desc *desc, const struct power_supply_config *cfg)

    Register new power supply

    :param struct device \*parent:
        Device to be a parent of power supply's device, usually
        the device which probe function calls this

    :param const struct power_supply_desc \*desc:
        Description of power supply, must be valid through whole
        lifetime of this power supply

    :param const struct power_supply_config \*cfg:
        Run-time specific configuration accessed during registering,
        may be NULL

.. _`power_supply_register.return`:

Return
------

A pointer to newly allocated power_supply on success
or ERR_PTR otherwise.
Use \ :c:func:`power_supply_unregister`\  on returned power_supply pointer to release
resources.

.. _`power_supply_register_no_ws`:

power_supply_register_no_ws
===========================

.. c:function:: struct power_supply *power_supply_register_no_ws(struct device *parent, const struct power_supply_desc *desc, const struct power_supply_config *cfg)

    Register new non-waking-source power supply

    :param struct device \*parent:
        Device to be a parent of power supply's device, usually
        the device which probe function calls this

    :param const struct power_supply_desc \*desc:
        Description of power supply, must be valid through whole
        lifetime of this power supply

    :param const struct power_supply_config \*cfg:
        Run-time specific configuration accessed during registering,
        may be NULL

.. _`power_supply_register_no_ws.return`:

Return
------

A pointer to newly allocated power_supply on success
or ERR_PTR otherwise.
Use \ :c:func:`power_supply_unregister`\  on returned power_supply pointer to release
resources.

.. _`devm_power_supply_register`:

devm_power_supply_register
==========================

.. c:function:: struct power_supply *devm_power_supply_register(struct device *parent, const struct power_supply_desc *desc, const struct power_supply_config *cfg)

    Register managed power supply

    :param struct device \*parent:
        Device to be a parent of power supply's device, usually
        the device which probe function calls this

    :param const struct power_supply_desc \*desc:
        Description of power supply, must be valid through whole
        lifetime of this power supply

    :param const struct power_supply_config \*cfg:
        Run-time specific configuration accessed during registering,
        may be NULL

.. _`devm_power_supply_register.return`:

Return
------

A pointer to newly allocated power_supply on success
or ERR_PTR otherwise.
The returned power_supply pointer will be automatically unregistered
on driver detach.

.. _`devm_power_supply_register_no_ws`:

devm_power_supply_register_no_ws
================================

.. c:function:: struct power_supply *devm_power_supply_register_no_ws(struct device *parent, const struct power_supply_desc *desc, const struct power_supply_config *cfg)

    Register managed non-waking-source power supply

    :param struct device \*parent:
        Device to be a parent of power supply's device, usually
        the device which probe function calls this

    :param const struct power_supply_desc \*desc:
        Description of power supply, must be valid through whole
        lifetime of this power supply

    :param const struct power_supply_config \*cfg:
        Run-time specific configuration accessed during registering,
        may be NULL

.. _`devm_power_supply_register_no_ws.return`:

Return
------

A pointer to newly allocated power_supply on success
or ERR_PTR otherwise.
The returned power_supply pointer will be automatically unregistered
on driver detach.

.. _`power_supply_unregister`:

power_supply_unregister
=======================

.. c:function:: void power_supply_unregister(struct power_supply *psy)

    Remove this power supply from system

    :param struct power_supply \*psy:
        Pointer to power supply to unregister

.. _`power_supply_unregister.description`:

Description
-----------

Remove this power supply from the system. The resources of power supply
will be freed here or on last \ :c:func:`power_supply_put`\  call.

.. This file was automatic generated / don't edit.

