.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dca/dca-core.c

.. _`dca_add_requester`:

dca_add_requester
=================

.. c:function:: int dca_add_requester(struct device *dev)

    add a dca client to the list \ ``dev``\  - the device that wants dca service

    :param dev:
        *undescribed*
    :type dev: struct device \*

.. _`dca_remove_requester`:

dca_remove_requester
====================

.. c:function:: int dca_remove_requester(struct device *dev)

    remove a dca client from the list \ ``dev``\  - the device that wants dca service

    :param dev:
        *undescribed*
    :type dev: struct device \*

.. _`dca_common_get_tag`:

dca_common_get_tag
==================

.. c:function:: u8 dca_common_get_tag(struct device *dev, int cpu)

    return the dca tag (serves both new and old api) \ ``dev``\  - the device that wants dca service \ ``cpu``\  - the cpuid as returned by \ :c:func:`get_cpu`\ 

    :param dev:
        *undescribed*
    :type dev: struct device \*

    :param cpu:
        *undescribed*
    :type cpu: int

.. _`dca3_get_tag`:

dca3_get_tag
============

.. c:function:: u8 dca3_get_tag(struct device *dev, int cpu)

    return the dca tag to the requester device for the given cpu (new api) \ ``dev``\  - the device that wants dca service \ ``cpu``\  - the cpuid as returned by \ :c:func:`get_cpu`\ 

    :param dev:
        *undescribed*
    :type dev: struct device \*

    :param cpu:
        *undescribed*
    :type cpu: int

.. _`dca_get_tag`:

dca_get_tag
===========

.. c:function:: u8 dca_get_tag(int cpu)

    return the dca tag for the given cpu (old api) \ ``cpu``\  - the cpuid as returned by \ :c:func:`get_cpu`\ 

    :param cpu:
        *undescribed*
    :type cpu: int

.. _`alloc_dca_provider`:

alloc_dca_provider
==================

.. c:function:: struct dca_provider *alloc_dca_provider(const struct dca_ops *ops, int priv_size)

    get data struct for describing a dca provider \ ``ops``\  - pointer to struct of dca operation function pointers \ ``priv_size``\  - size of extra mem to be added for provider's needs

    :param ops:
        *undescribed*
    :type ops: const struct dca_ops \*

    :param priv_size:
        *undescribed*
    :type priv_size: int

.. _`free_dca_provider`:

free_dca_provider
=================

.. c:function:: void free_dca_provider(struct dca_provider *dca)

    release the dca provider data struct \ ``ops``\  - pointer to struct of dca operation function pointers \ ``priv_size``\  - size of extra mem to be added for provider's needs

    :param dca:
        *undescribed*
    :type dca: struct dca_provider \*

.. _`register_dca_provider`:

register_dca_provider
=====================

.. c:function:: int register_dca_provider(struct dca_provider *dca, struct device *dev)

    register a dca provider \ ``dca``\  - struct created by \ :c:func:`alloc_dca_provider`\  \ ``dev``\  - device providing dca services

    :param dca:
        *undescribed*
    :type dca: struct dca_provider \*

    :param dev:
        *undescribed*
    :type dev: struct device \*

.. _`unregister_dca_provider`:

unregister_dca_provider
=======================

.. c:function:: void unregister_dca_provider(struct dca_provider *dca, struct device *dev)

    remove a dca provider \ ``dca``\  - struct created by \ :c:func:`alloc_dca_provider`\ 

    :param dca:
        *undescribed*
    :type dca: struct dca_provider \*

    :param dev:
        *undescribed*
    :type dev: struct device \*

.. _`dca_register_notify`:

dca_register_notify
===================

.. c:function:: void dca_register_notify(struct notifier_block *nb)

    register a client's notifier callback

    :param nb:
        *undescribed*
    :type nb: struct notifier_block \*

.. _`dca_unregister_notify`:

dca_unregister_notify
=====================

.. c:function:: void dca_unregister_notify(struct notifier_block *nb)

    remove a client's notifier callback

    :param nb:
        *undescribed*
    :type nb: struct notifier_block \*

.. This file was automatic generated / don't edit.

