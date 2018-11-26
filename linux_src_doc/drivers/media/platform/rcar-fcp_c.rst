.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/rcar-fcp.c

.. _`rcar_fcp_get`:

rcar_fcp_get
============

.. c:function:: struct rcar_fcp_device *rcar_fcp_get(const struct device_node *np)

    Find and acquire a reference to an FCP instance

    :param np:
        Device node of the FCP instance
    :type np: const struct device_node \*

.. _`rcar_fcp_get.description`:

Description
-----------

Search the list of registered FCP instances for the instance corresponding to
the given device node.

Return a pointer to the FCP instance, or an ERR_PTR if the instance can't be
found.

.. _`rcar_fcp_put`:

rcar_fcp_put
============

.. c:function:: void rcar_fcp_put(struct rcar_fcp_device *fcp)

    Release a reference to an FCP instance

    :param fcp:
        The FCP instance
    :type fcp: struct rcar_fcp_device \*

.. _`rcar_fcp_put.description`:

Description
-----------

Release the FCP instance acquired by a call to \ :c:func:`rcar_fcp_get`\ .

.. _`rcar_fcp_enable`:

rcar_fcp_enable
===============

.. c:function:: int rcar_fcp_enable(struct rcar_fcp_device *fcp)

    Enable an FCP

    :param fcp:
        The FCP instance
    :type fcp: struct rcar_fcp_device \*

.. _`rcar_fcp_enable.description`:

Description
-----------

Before any memory access through an FCP is performed by a module, the FCP
must be enabled by a call to this function. The enable calls are reference
counted, each successful call must be followed by one \ :c:func:`rcar_fcp_disable`\ 
call when no more memory transfer can occur through the FCP.

Return 0 on success or a negative error code if an error occurs. The enable
reference count isn't increased when this function returns an error.

.. _`rcar_fcp_disable`:

rcar_fcp_disable
================

.. c:function:: void rcar_fcp_disable(struct rcar_fcp_device *fcp)

    Disable an FCP

    :param fcp:
        The FCP instance
    :type fcp: struct rcar_fcp_device \*

.. _`rcar_fcp_disable.description`:

Description
-----------

This function is the counterpart of \ :c:func:`rcar_fcp_enable`\ . As enable calls are
reference counted a disable call may not disable the FCP synchronously.

.. This file was automatic generated / don't edit.

