.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/phy/phy-core.c

.. _`phy_create_lookup`:

phy_create_lookup
=================

.. c:function:: int phy_create_lookup(struct phy *phy, const char *con_id, const char *dev_id)

    allocate and register PHY/device association

    :param phy:
        the phy of the association
    :type phy: struct phy \*

    :param con_id:
        connection ID string on device
    :type con_id: const char \*

    :param dev_id:
        the device of the association
    :type dev_id: const char \*

.. _`phy_create_lookup.description`:

Description
-----------

Creates and registers phy_lookup entry.

.. _`phy_remove_lookup`:

phy_remove_lookup
=================

.. c:function:: void phy_remove_lookup(struct phy *phy, const char *con_id, const char *dev_id)

    find and remove PHY/device association

    :param phy:
        the phy of the association
    :type phy: struct phy \*

    :param con_id:
        connection ID string on device
    :type con_id: const char \*

    :param dev_id:
        the device of the association
    :type dev_id: const char \*

.. _`phy_remove_lookup.description`:

Description
-----------

Finds and unregisters phy_lookup entry that was created with
\ :c:func:`phy_create_lookup`\ .

.. _`_of_phy_get`:

\_of_phy_get
============

.. c:function:: struct phy *_of_phy_get(struct device_node *np, int index)

    lookup and obtain a reference to a phy by phandle

    :param np:
        device_node for which to get the phy
    :type np: struct device_node \*

    :param index:
        the index of the phy
    :type index: int

.. _`_of_phy_get.description`:

Description
-----------

Returns the phy associated with the given phandle value,
after getting a refcount to it or -ENODEV if there is no such phy or
-EPROBE_DEFER if there is a phandle to the phy, but the device is
not yet loaded. This function uses of_xlate call back function provided
while registering the phy_provider to find the phy instance.

.. _`of_phy_get`:

of_phy_get
==========

.. c:function:: struct phy *of_phy_get(struct device_node *np, const char *con_id)

    lookup and obtain a reference to a phy using a device_node.

    :param np:
        device_node for which to get the phy
    :type np: struct device_node \*

    :param con_id:
        name of the phy from device's point of view
    :type con_id: const char \*

.. _`of_phy_get.description`:

Description
-----------

Returns the phy driver, after getting a refcount to it; or
-ENODEV if there is no such phy. The caller is responsible for
calling \ :c:func:`phy_put`\  to release that count.

.. _`phy_put`:

phy_put
=======

.. c:function:: void phy_put(struct phy *phy)

    release the PHY

    :param phy:
        the phy returned by \ :c:func:`phy_get`\ 
    :type phy: struct phy \*

.. _`phy_put.description`:

Description
-----------

Releases a refcount the caller received from \ :c:func:`phy_get`\ .

.. _`devm_phy_put`:

devm_phy_put
============

.. c:function:: void devm_phy_put(struct device *dev, struct phy *phy)

    release the PHY

    :param dev:
        device that wants to release this phy
    :type dev: struct device \*

    :param phy:
        the phy returned by \ :c:func:`devm_phy_get`\ 
    :type phy: struct phy \*

.. _`devm_phy_put.description`:

Description
-----------

destroys the devres associated with this phy and invokes phy_put
to release the phy.

.. _`of_phy_simple_xlate`:

of_phy_simple_xlate
===================

.. c:function:: struct phy *of_phy_simple_xlate(struct device *dev, struct of_phandle_args *args)

    returns the phy instance from phy provider

    :param dev:
        the PHY provider device
    :type dev: struct device \*

    :param args:
        of_phandle_args (not used here)
    :type args: struct of_phandle_args \*

.. _`of_phy_simple_xlate.description`:

Description
-----------

Intended to be used by phy provider for the common case where #phy-cells is
0. For other cases where #phy-cells is greater than '0', the phy provider
should provide a custom of_xlate function that reads the \*args\* and returns
the appropriate phy.

.. _`phy_get`:

phy_get
=======

.. c:function:: struct phy *phy_get(struct device *dev, const char *string)

    lookup and obtain a reference to a phy.

    :param dev:
        device that requests this phy
    :type dev: struct device \*

    :param string:
        the phy name as given in the dt data or the name of the controller
        port for non-dt case
    :type string: const char \*

.. _`phy_get.description`:

Description
-----------

Returns the phy driver, after getting a refcount to it; or
-ENODEV if there is no such phy.  The caller is responsible for
calling \ :c:func:`phy_put`\  to release that count.

.. _`phy_optional_get`:

phy_optional_get
================

.. c:function:: struct phy *phy_optional_get(struct device *dev, const char *string)

    lookup and obtain a reference to an optional phy.

    :param dev:
        device that requests this phy
    :type dev: struct device \*

    :param string:
        the phy name as given in the dt data or the name of the controller
        port for non-dt case
    :type string: const char \*

.. _`phy_optional_get.description`:

Description
-----------

Returns the phy driver, after getting a refcount to it; or
NULL if there is no such phy.  The caller is responsible for
calling \ :c:func:`phy_put`\  to release that count.

.. _`devm_phy_get`:

devm_phy_get
============

.. c:function:: struct phy *devm_phy_get(struct device *dev, const char *string)

    lookup and obtain a reference to a phy.

    :param dev:
        device that requests this phy
    :type dev: struct device \*

    :param string:
        the phy name as given in the dt data or phy device name
        for non-dt case
    :type string: const char \*

.. _`devm_phy_get.description`:

Description
-----------

Gets the phy using \ :c:func:`phy_get`\ , and associates a device with it using
devres. On driver detach, release function is invoked on the devres data,
then, devres data is freed.

.. _`devm_phy_optional_get`:

devm_phy_optional_get
=====================

.. c:function:: struct phy *devm_phy_optional_get(struct device *dev, const char *string)

    lookup and obtain a reference to an optional phy.

    :param dev:
        device that requests this phy
    :type dev: struct device \*

    :param string:
        the phy name as given in the dt data or phy device name
        for non-dt case
    :type string: const char \*

.. _`devm_phy_optional_get.description`:

Description
-----------

Gets the phy using \ :c:func:`phy_get`\ , and associates a device with it using
devres. On driver detach, release function is invoked on the devres
data, then, devres data is freed. This differs to \ :c:func:`devm_phy_get`\  in
that if the phy does not exist, it is not considered an error and
-ENODEV will not be returned. Instead the NULL phy is returned,
which can be passed to all other phy consumer calls.

.. _`devm_of_phy_get`:

devm_of_phy_get
===============

.. c:function:: struct phy *devm_of_phy_get(struct device *dev, struct device_node *np, const char *con_id)

    lookup and obtain a reference to a phy.

    :param dev:
        device that requests this phy
    :type dev: struct device \*

    :param np:
        node containing the phy
    :type np: struct device_node \*

    :param con_id:
        name of the phy from device's point of view
    :type con_id: const char \*

.. _`devm_of_phy_get.description`:

Description
-----------

Gets the phy using \ :c:func:`of_phy_get`\ , and associates a device with it using
devres. On driver detach, release function is invoked on the devres data,
then, devres data is freed.

.. _`devm_of_phy_get_by_index`:

devm_of_phy_get_by_index
========================

.. c:function:: struct phy *devm_of_phy_get_by_index(struct device *dev, struct device_node *np, int index)

    lookup and obtain a reference to a phy by index.

    :param dev:
        device that requests this phy
    :type dev: struct device \*

    :param np:
        node containing the phy
    :type np: struct device_node \*

    :param index:
        index of the phy
    :type index: int

.. _`devm_of_phy_get_by_index.description`:

Description
-----------

Gets the phy using \_of_phy_get(), then gets a refcount to it,
and associates a device with it using devres. On driver detach,
release function is invoked on the devres data,
then, devres data is freed.

.. _`phy_create`:

phy_create
==========

.. c:function:: struct phy *phy_create(struct device *dev, struct device_node *node, const struct phy_ops *ops)

    create a new phy

    :param dev:
        device that is creating the new phy
    :type dev: struct device \*

    :param node:
        device node of the phy
    :type node: struct device_node \*

    :param ops:
        function pointers for performing phy operations
    :type ops: const struct phy_ops \*

.. _`phy_create.description`:

Description
-----------

Called to create a phy using phy framework.

.. _`devm_phy_create`:

devm_phy_create
===============

.. c:function:: struct phy *devm_phy_create(struct device *dev, struct device_node *node, const struct phy_ops *ops)

    create a new phy

    :param dev:
        device that is creating the new phy
    :type dev: struct device \*

    :param node:
        device node of the phy
    :type node: struct device_node \*

    :param ops:
        function pointers for performing phy operations
    :type ops: const struct phy_ops \*

.. _`devm_phy_create.description`:

Description
-----------

Creates a new PHY device adding it to the PHY class.
While at that, it also associates the device with the phy using devres.
On driver detach, release function is invoked on the devres data,
then, devres data is freed.

.. _`phy_destroy`:

phy_destroy
===========

.. c:function:: void phy_destroy(struct phy *phy)

    destroy the phy

    :param phy:
        the phy to be destroyed
    :type phy: struct phy \*

.. _`phy_destroy.description`:

Description
-----------

Called to destroy the phy.

.. _`devm_phy_destroy`:

devm_phy_destroy
================

.. c:function:: void devm_phy_destroy(struct device *dev, struct phy *phy)

    destroy the PHY

    :param dev:
        device that wants to release this phy
    :type dev: struct device \*

    :param phy:
        the phy returned by \ :c:func:`devm_phy_get`\ 
    :type phy: struct phy \*

.. _`devm_phy_destroy.description`:

Description
-----------

destroys the devres associated with this phy and invokes phy_destroy
to destroy the phy.

.. _`__of_phy_provider_register`:

\__of_phy_provider_register
===========================

.. c:function:: struct phy_provider *__of_phy_provider_register(struct device *dev, struct device_node *children, struct module *owner, struct phy * (*of_xlate)(struct device *dev, struct of_phandle_args *args))

    create/register phy provider with the framework

    :param dev:
        struct device of the phy provider
    :type dev: struct device \*

    :param children:
        device node containing children (if different from dev->of_node)
    :type children: struct device_node \*

    :param owner:
        the module owner containing of_xlate
    :type owner: struct module \*

    :param struct phy \* (\*of_xlate)(struct device \*dev, struct of_phandle_args \*args):
        function pointer to obtain phy instance from phy provider

.. _`__of_phy_provider_register.description`:

Description
-----------

Creates struct phy_provider from dev and of_xlate function pointer.
This is used in the case of dt boot for finding the phy instance from
phy provider.

If the PHY provider doesn't nest children directly but uses a separate
child node to contain the individual children, the \ ``children``\  parameter
can be used to override the default. If NULL, the default (dev->of_node)
will be used. If non-NULL, the device node must be a child (or further
descendant) of dev->of_node. Otherwise an \ :c:func:`ERR_PTR`\ -encoded -EINVAL
error code is returned.

.. _`__devm_of_phy_provider_register`:

\__devm_of_phy_provider_register
================================

.. c:function:: struct phy_provider *__devm_of_phy_provider_register(struct device *dev, struct device_node *children, struct module *owner, struct phy * (*of_xlate)(struct device *dev, struct of_phandle_args *args))

    create/register phy provider with the framework

    :param dev:
        struct device of the phy provider
    :type dev: struct device \*

    :param children:
        *undescribed*
    :type children: struct device_node \*

    :param owner:
        the module owner containing of_xlate
    :type owner: struct module \*

    :param struct phy \* (\*of_xlate)(struct device \*dev, struct of_phandle_args \*args):
        function pointer to obtain phy instance from phy provider

.. _`__devm_of_phy_provider_register.description`:

Description
-----------

Creates struct phy_provider from dev and of_xlate function pointer.
This is used in the case of dt boot for finding the phy instance from
phy provider. While at that, it also associates the device with the
phy provider using devres. On driver detach, release function is invoked
on the devres data, then, devres data is freed.

.. _`of_phy_provider_unregister`:

of_phy_provider_unregister
==========================

.. c:function:: void of_phy_provider_unregister(struct phy_provider *phy_provider)

    unregister phy provider from the framework

    :param phy_provider:
        phy provider returned by \ :c:func:`of_phy_provider_register`\ 
    :type phy_provider: struct phy_provider \*

.. _`of_phy_provider_unregister.description`:

Description
-----------

Removes the phy_provider created using \ :c:func:`of_phy_provider_register`\ .

.. _`devm_of_phy_provider_unregister`:

devm_of_phy_provider_unregister
===============================

.. c:function:: void devm_of_phy_provider_unregister(struct device *dev, struct phy_provider *phy_provider)

    remove phy provider from the framework

    :param dev:
        struct device of the phy provider
    :type dev: struct device \*

    :param phy_provider:
        *undescribed*
    :type phy_provider: struct phy_provider \*

.. _`devm_of_phy_provider_unregister.description`:

Description
-----------

destroys the devres associated with this phy provider and invokes
of_phy_provider_unregister to unregister the phy provider.

.. _`phy_release`:

phy_release
===========

.. c:function:: void phy_release(struct device *dev)

    release the phy

    :param dev:
        the dev member within phy
    :type dev: struct device \*

.. _`phy_release.description`:

Description
-----------

When the last reference to the device is removed, it is called
from the embedded kobject as release method.

.. This file was automatic generated / don't edit.

