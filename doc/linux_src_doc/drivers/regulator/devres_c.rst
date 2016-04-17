.. -*- coding: utf-8; mode: rst -*-

========
devres.c
========


.. _`devm_regulator_get`:

devm_regulator_get
==================

.. c:function:: struct regulator *devm_regulator_get (struct device *dev, const char *id)

    Resource managed regulator_get()

    :param struct device \*dev:
        device for regulator "consumer"

    :param const char \*id:
        Supply name or regulator ID.



.. _`devm_regulator_get.description`:

Description
-----------

Managed :c:func:`regulator_get`. Regulators returned from this function are
automatically :c:func:`regulator_put` on driver detach. See :c:func:`regulator_get` for more
information.



.. _`devm_regulator_get_exclusive`:

devm_regulator_get_exclusive
============================

.. c:function:: struct regulator *devm_regulator_get_exclusive (struct device *dev, const char *id)

    Resource managed regulator_get_exclusive()

    :param struct device \*dev:
        device for regulator "consumer"

    :param const char \*id:
        Supply name or regulator ID.



.. _`devm_regulator_get_exclusive.description`:

Description
-----------

Managed :c:func:`regulator_get_exclusive`. Regulators returned from this function
are automatically :c:func:`regulator_put` on driver detach. See :c:func:`regulator_get` for
more information.



.. _`devm_regulator_get_optional`:

devm_regulator_get_optional
===========================

.. c:function:: struct regulator *devm_regulator_get_optional (struct device *dev, const char *id)

    Resource managed regulator_get_optional()

    :param struct device \*dev:
        device for regulator "consumer"

    :param const char \*id:
        Supply name or regulator ID.



.. _`devm_regulator_get_optional.description`:

Description
-----------

Managed :c:func:`regulator_get_optional`. Regulators returned from this
function are automatically :c:func:`regulator_put` on driver detach. See
:c:func:`regulator_get_optional` for more information.



.. _`devm_regulator_put`:

devm_regulator_put
==================

.. c:function:: void devm_regulator_put (struct regulator *regulator)

    Resource managed regulator_put()

    :param struct regulator \*regulator:
        regulator to free



.. _`devm_regulator_put.description`:

Description
-----------

Deallocate a regulator allocated with :c:func:`devm_regulator_get`. Normally
this function will not need to be called and the resource management
code will ensure that the resource is freed.



.. _`devm_regulator_bulk_get`:

devm_regulator_bulk_get
=======================

.. c:function:: int devm_regulator_bulk_get (struct device *dev, int num_consumers, struct regulator_bulk_data *consumers)

    managed get multiple regulator consumers

    :param struct device \*dev:
        Device to supply

    :param int num_consumers:
        Number of consumers to register

    :param struct regulator_bulk_data \*consumers:
        Configuration of consumers; clients are stored here.



.. _`devm_regulator_bulk_get.description`:

Description
-----------

``return`` 0 on success, an errno on failure.

This helper function allows drivers to get several regulator
consumers in one operation with management, the regulators will
automatically be freed when the device is unbound.  If any of the
regulators cannot be acquired then any regulators that were
allocated will be freed before returning to the caller.



.. _`devm_regulator_register`:

devm_regulator_register
=======================

.. c:function:: struct regulator_dev *devm_regulator_register (struct device *dev, const struct regulator_desc *regulator_desc, const struct regulator_config *config)

    Resource managed regulator_register()

    :param struct device \*dev:

        *undescribed*

    :param const struct regulator_desc \*regulator_desc:
        regulator to register

    :param const struct regulator_config \*config:
        runtime configuration for regulator



.. _`devm_regulator_register.description`:

Description
-----------

Called by regulator drivers to register a regulator.  Returns a
valid pointer to struct regulator_dev on success or an :c:func:`ERR_PTR` on
error.  The regulator will automatically be released when the device
is unbound.



.. _`devm_regulator_unregister`:

devm_regulator_unregister
=========================

.. c:function:: void devm_regulator_unregister (struct device *dev, struct regulator_dev *rdev)

    Resource managed regulator_unregister()

    :param struct device \*dev:

        *undescribed*

    :param struct regulator_dev \*rdev:

        *undescribed*



.. _`devm_regulator_unregister.description`:

Description
-----------

Unregister a regulator registered with :c:func:`devm_regulator_register`.
Normally this function will not need to be called and the resource
management code will ensure that the resource is freed.



.. _`devm_regulator_register_supply_alias`:

devm_regulator_register_supply_alias
====================================

.. c:function:: int devm_regulator_register_supply_alias (struct device *dev, const char *id, struct device *alias_dev, const char *alias_id)

    Resource managed regulator_register_supply_alias()

    :param struct device \*dev:
        device that will be given as the regulator "consumer"

    :param const char \*id:
        Supply name or regulator ID

    :param struct device \*alias_dev:
        device that should be used to lookup the supply

    :param const char \*alias_id:
        Supply name or regulator ID that should be used to lookup the
        supply



.. _`devm_regulator_register_supply_alias.description`:

Description
-----------

The supply alias will automatically be unregistered when the source
device is unbound.



.. _`devm_regulator_unregister_supply_alias`:

devm_regulator_unregister_supply_alias
======================================

.. c:function:: void devm_regulator_unregister_supply_alias (struct device *dev, const char *id)

    Resource managed regulator_unregister_supply_alias()

    :param struct device \*dev:
        device that will be given as the regulator "consumer"

    :param const char \*id:
        Supply name or regulator ID



.. _`devm_regulator_unregister_supply_alias.description`:

Description
-----------

Unregister an alias registered with
:c:func:`devm_regulator_register_supply_alias`. Normally this function
will not need to be called and the resource management code
will ensure that the resource is freed.



.. _`devm_regulator_bulk_register_supply_alias`:

devm_regulator_bulk_register_supply_alias
=========================================

.. c:function:: int devm_regulator_bulk_register_supply_alias (struct device *dev, const char *const *id, struct device *alias_dev, const char *const *alias_id, int num_id)

    Managed register multiple aliases

    :param struct device \*dev:
        device that will be given as the regulator "consumer"

    :param const \*id:
        List of supply names or regulator IDs

    :param struct device \*alias_dev:
        device that should be used to lookup the supply

    :param const \*alias_id:
        List of supply names or regulator IDs that should be used to
        lookup the supply

    :param int num_id:
        Number of aliases to register



.. _`devm_regulator_bulk_register_supply_alias.description`:

Description
-----------

``return`` 0 on success, an errno on failure.

This helper function allows drivers to register several supply
aliases in one operation, the aliases will be automatically
unregisters when the source device is unbound.  If any of the
aliases cannot be registered any aliases that were registered
will be removed before returning to the caller.



.. _`devm_regulator_bulk_unregister_supply_alias`:

devm_regulator_bulk_unregister_supply_alias
===========================================

.. c:function:: void devm_regulator_bulk_unregister_supply_alias (struct device *dev, const char *const *id, int num_id)

    Managed unregister multiple aliases

    :param struct device \*dev:
        device that will be given as the regulator "consumer"

    :param const \*id:
        List of supply names or regulator IDs

    :param int num_id:
        Number of aliases to unregister



.. _`devm_regulator_bulk_unregister_supply_alias.description`:

Description
-----------

Unregister aliases registered with
:c:func:`devm_regulator_bulk_register_supply_alias`. Normally this function
will not need to be called and the resource management code
will ensure that the resource is freed.



.. _`devm_regulator_register_notifier`:

devm_regulator_register_notifier
================================

.. c:function:: int devm_regulator_register_notifier (struct regulator *regulator, struct notifier_block *nb)

    Resource managed regulator_register_notifier

    :param struct regulator \*regulator:
        regulator source

    :param struct notifier_block \*nb:
        notifier block



.. _`devm_regulator_register_notifier.description`:

Description
-----------

The notifier will be registers under the consumer device and be
automatically be unregistered when the source device is unbound.



.. _`devm_regulator_unregister_notifier`:

devm_regulator_unregister_notifier
==================================

.. c:function:: void devm_regulator_unregister_notifier (struct regulator *regulator, struct notifier_block *nb)

    Resource managed regulator_unregister_notifier()

    :param struct regulator \*regulator:
        regulator source

    :param struct notifier_block \*nb:
        notifier block



.. _`devm_regulator_unregister_notifier.description`:

Description
-----------

Unregister a notifier registered with :c:func:`devm_regulator_register_notifier`.
Normally this function will not need to be called and the resource
management code will ensure that the resource is freed.

