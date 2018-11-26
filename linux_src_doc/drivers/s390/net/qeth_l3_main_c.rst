.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/net/qeth_l3_main.c

.. _`qeth_l3_update_ipato`:

qeth_l3_update_ipato
====================

.. c:function:: void qeth_l3_update_ipato(struct qeth_card *card)

    Update 'takeover' property, for all NORMAL IPs.

    :param card:
        *undescribed*
    :type card: struct qeth_card \*

.. _`qeth_l3_update_ipato.description`:

Description
-----------

Caller must hold ip_lock.

.. This file was automatic generated / don't edit.

