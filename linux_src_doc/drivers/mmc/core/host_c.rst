.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mmc/core/host.c

.. _`mmc_of_parse`:

mmc_of_parse
============

.. c:function:: int mmc_of_parse(struct mmc_host *host)

    parse host's device-tree node

    :param struct mmc_host \*host:
        host whose node should be parsed.

.. _`mmc_of_parse.description`:

Description
-----------

To keep the rest of the MMC subsystem unaware of whether DT has been
used to to instantiate and configure this host instance or not, we
parse the properties and set respective generic mmc-host flags and
parameters.

.. _`mmc_alloc_host`:

mmc_alloc_host
==============

.. c:function:: struct mmc_host *mmc_alloc_host(int extra, struct device *dev)

    initialise the per-host structure.

    :param int extra:
        sizeof private data structure

    :param struct device \*dev:
        pointer to host device model structure

.. _`mmc_alloc_host.description`:

Description
-----------

Initialise the per-host structure.

.. _`mmc_add_host`:

mmc_add_host
============

.. c:function:: int mmc_add_host(struct mmc_host *host)

    initialise host hardware

    :param struct mmc_host \*host:
        mmc host

.. _`mmc_add_host.description`:

Description
-----------

Register the host with the driver model. The host must be
prepared to start servicing requests before this function
completes.

.. _`mmc_remove_host`:

mmc_remove_host
===============

.. c:function:: void mmc_remove_host(struct mmc_host *host)

    remove host hardware

    :param struct mmc_host \*host:
        mmc host

.. _`mmc_remove_host.description`:

Description
-----------

Unregister and remove all cards associated with this host,
and power down the MMC bus. No new requests will be issued
after this function has returned.

.. _`mmc_free_host`:

mmc_free_host
=============

.. c:function:: void mmc_free_host(struct mmc_host *host)

    free the host structure

    :param struct mmc_host \*host:
        mmc host

.. _`mmc_free_host.description`:

Description
-----------

Free the host once all references to it have been dropped.

.. This file was automatic generated / don't edit.

