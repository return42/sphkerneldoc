.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/cec-notifier.h

.. _`cec_notifier_get_conn`:

cec_notifier_get_conn
=====================

.. c:function:: struct cec_notifier *cec_notifier_get_conn(struct device *dev, const char *conn)

    find or create a new cec_notifier for the given device and connector tuple.

    :param dev:
        device that sends the events.
    :type dev: struct device \*

    :param conn:
        the connector name from which the event occurs
    :type conn: const char \*

.. _`cec_notifier_get_conn.description`:

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

    :param n:
        notifier
    :type n: struct cec_notifier \*

.. _`cec_notifier_set_phys_addr`:

cec_notifier_set_phys_addr
==========================

.. c:function:: void cec_notifier_set_phys_addr(struct cec_notifier *n, u16 pa)

    set a new physical address.

    :param n:
        the CEC notifier
    :type n: struct cec_notifier \*

    :param pa:
        the CEC physical address
    :type pa: u16

.. _`cec_notifier_set_phys_addr.description`:

Description
-----------

Set a new CEC physical address.
Does nothing if \ ``n``\  == NULL.

.. _`cec_notifier_set_phys_addr_from_edid`:

cec_notifier_set_phys_addr_from_edid
====================================

.. c:function:: void cec_notifier_set_phys_addr_from_edid(struct cec_notifier *n, const struct edid *edid)

    set parse the PA from the EDID.

    :param n:
        the CEC notifier
    :type n: struct cec_notifier \*

    :param edid:
        the struct edid pointer
    :type edid: const struct edid \*

.. _`cec_notifier_set_phys_addr_from_edid.description`:

Description
-----------

Parses the EDID to obtain the new CEC physical address and set it.
Does nothing if \ ``n``\  == NULL.

.. _`cec_notifier_register`:

cec_notifier_register
=====================

.. c:function:: void cec_notifier_register(struct cec_notifier *n, struct cec_adapter *adap, void (*callback)(struct cec_adapter *adap, u16 pa))

    register a callback with the notifier

    :param n:
        the CEC notifier
    :type n: struct cec_notifier \*

    :param adap:
        the CEC adapter, passed as argument to the callback function
    :type adap: struct cec_adapter \*

    :param void (\*callback)(struct cec_adapter \*adap, u16 pa):
        the callback function

.. _`cec_notifier_unregister`:

cec_notifier_unregister
=======================

.. c:function:: void cec_notifier_unregister(struct cec_notifier *n)

    unregister the callback from the notifier.

    :param n:
        the CEC notifier
    :type n: struct cec_notifier \*

.. _`cec_register_cec_notifier`:

cec_register_cec_notifier
=========================

.. c:function:: void cec_register_cec_notifier(struct cec_adapter *adap, struct cec_notifier *notifier)

    register the notifier with the cec adapter.

    :param adap:
        the CEC adapter
    :type adap: struct cec_adapter \*

    :param notifier:
        the CEC notifier
    :type notifier: struct cec_notifier \*

.. _`cec_notifier_get`:

cec_notifier_get
================

.. c:function:: struct cec_notifier *cec_notifier_get(struct device *dev)

    find or create a new cec_notifier for the given device.

    :param dev:
        device that sends the events.
    :type dev: struct device \*

.. _`cec_notifier_get.description`:

Description
-----------

If a notifier for device \ ``dev``\  already exists, then increase the refcount
and return that notifier.

If it doesn't exist, then allocate a new notifier struct and return a
pointer to that new struct.

Return NULL if the memory could not be allocated.

.. _`cec_notifier_phys_addr_invalidate`:

cec_notifier_phys_addr_invalidate
=================================

.. c:function:: void cec_notifier_phys_addr_invalidate(struct cec_notifier *n)

    set the physical address to INVALID

    :param n:
        the CEC notifier
    :type n: struct cec_notifier \*

.. _`cec_notifier_phys_addr_invalidate.description`:

Description
-----------

This is a simple helper function to invalidate the physical
address. Does nothing if \ ``n``\  == NULL.

.. This file was automatic generated / don't edit.

