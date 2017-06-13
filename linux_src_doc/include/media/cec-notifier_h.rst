.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/cec-notifier.h

.. _`cec_notifier_get`:

cec_notifier_get
================

.. c:function:: struct cec_notifier *cec_notifier_get(struct device *dev)

    find or create a new cec_notifier for the given device.

    :param struct device \*dev:
        device that sends the events.

.. _`cec_notifier_get.description`:

Description
-----------

If a notifier for device \ ``dev``\  already exists, then increase the refcount
and return that notifier.

If it doesn't exist, then allocate a new notifier struct and return a
pointer to that new struct.

Return NULL if the memory could not be allocated.

.. _`cec_notifier_put`:

cec_notifier_put
================

.. c:function:: void cec_notifier_put(struct cec_notifier *n)

    decrease refcount and delete when the refcount reaches 0.

    :param struct cec_notifier \*n:
        notifier

.. _`cec_notifier_set_phys_addr`:

cec_notifier_set_phys_addr
==========================

.. c:function:: void cec_notifier_set_phys_addr(struct cec_notifier *n, u16 pa)

    set a new physical address.

    :param struct cec_notifier \*n:
        the CEC notifier

    :param u16 pa:
        the CEC physical address

.. _`cec_notifier_set_phys_addr.description`:

Description
-----------

Set a new CEC physical address.

.. _`cec_notifier_set_phys_addr_from_edid`:

cec_notifier_set_phys_addr_from_edid
====================================

.. c:function:: void cec_notifier_set_phys_addr_from_edid(struct cec_notifier *n, const struct edid *edid)

    set parse the PA from the EDID.

    :param struct cec_notifier \*n:
        the CEC notifier

    :param const struct edid \*edid:
        the struct edid pointer

.. _`cec_notifier_set_phys_addr_from_edid.description`:

Description
-----------

Parses the EDID to obtain the new CEC physical address and set it.

.. _`cec_notifier_register`:

cec_notifier_register
=====================

.. c:function:: void cec_notifier_register(struct cec_notifier *n, struct cec_adapter *adap, void (*callback)(struct cec_adapter *adap, u16 pa))

    register a callback with the notifier

    :param struct cec_notifier \*n:
        the CEC notifier

    :param struct cec_adapter \*adap:
        the CEC adapter, passed as argument to the callback function

    :param void (\*callback)(struct cec_adapter \*adap, u16 pa):
        the callback function

.. _`cec_notifier_unregister`:

cec_notifier_unregister
=======================

.. c:function:: void cec_notifier_unregister(struct cec_notifier *n)

    unregister the callback from the notifier.

    :param struct cec_notifier \*n:
        the CEC notifier

.. This file was automatic generated / don't edit.

