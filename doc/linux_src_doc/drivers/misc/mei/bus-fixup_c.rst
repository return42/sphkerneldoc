.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mei/bus-fixup.c

.. _`number_of_connections`:

number_of_connections
=====================

.. c:function:: void number_of_connections(struct mei_cl_device *cldev)

    determine whether an client be on the bus according number of connections

    :param struct mei_cl_device \*cldev:
        me clients device

.. _`number_of_connections.we-support-only-clients`:

We support only clients
-----------------------

1. with single connection
2. and fixed clients (max_number_of_connections == 0)

.. _`blacklist`:

blacklist
=========

.. c:function:: void blacklist(struct mei_cl_device *cldev)

    blacklist a client from the bus

    :param struct mei_cl_device \*cldev:
        me clients device

.. _`mei_wd`:

mei_wd
======

.. c:function:: void mei_wd(struct mei_cl_device *cldev)

    wd client on the bus, change protocol version as the API has changed.

    :param struct mei_cl_device \*cldev:
        me clients device

.. _`mei_nfc_if_version`:

mei_nfc_if_version
==================

.. c:function:: int mei_nfc_if_version(struct mei_cl *cl, struct mei_nfc_if_version *ver)

    get NFC interface version

    :param struct mei_cl \*cl:
        host client (nfc info)

    :param struct mei_nfc_if_version \*ver:
        NFC interface version to be filled in

.. _`mei_nfc_if_version.return`:

Return
------

0 on success; < 0 otherwise

.. _`mei_nfc_radio_name`:

mei_nfc_radio_name
==================

.. c:function:: const char *mei_nfc_radio_name(struct mei_nfc_if_version *ver)

    derive nfc radio name from the interface version

    :param struct mei_nfc_if_version \*ver:
        NFC radio version

.. _`mei_nfc_radio_name.return`:

Return
------

radio name string

.. _`mei_nfc`:

mei_nfc
=======

.. c:function:: void mei_nfc(struct mei_cl_device *cldev)

    The nfc fixup function. The function retrieves nfc radio name and set is as device attribute so we can load the proper device driver for it

    :param struct mei_cl_device \*cldev:
        me client device (nfc)

.. _`mei_cl_bus_dev_fixup`:

mei_cl_bus_dev_fixup
====================

.. c:function:: void mei_cl_bus_dev_fixup(struct mei_cl_device *cldev)

    run fixup handlers

    :param struct mei_cl_device \*cldev:
        me client device

.. This file was automatic generated / don't edit.

