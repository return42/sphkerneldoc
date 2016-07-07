.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/net/qeth_l2_sys.c

.. _`qeth_l2_setup_bridgeport_attrs`:

qeth_l2_setup_bridgeport_attrs
==============================

.. c:function:: void qeth_l2_setup_bridgeport_attrs(struct qeth_card *card)

    set/restore attrs when turning online.

    :param struct qeth_card \*card:
        qeth_card structure pointer

.. _`qeth_l2_setup_bridgeport_attrs.note`:

Note
----

this function is called with conf_mutex held by the caller

.. This file was automatic generated / don't edit.

