.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/net/qeth_l3_main.c

.. _`qeth_l3_update_ipato`:

qeth_l3_update_ipato
====================

.. c:function:: void qeth_l3_update_ipato(struct qeth_card *card)

    Update 'takeover' property, for all NORMAL IPs.

    :param struct qeth_card \*card:
        *undescribed*

.. _`qeth_l3_update_ipato.description`:

Description
-----------

Caller must hold ip_lock.

.. _`qeth_l3_get_elements_no_tso`:

qeth_l3_get_elements_no_tso
===========================

.. c:function:: int qeth_l3_get_elements_no_tso(struct qeth_card *card, struct sk_buff *skb, int extra_elems)

    find number of SBALEs for skb data for tso

    :param struct qeth_card \*card:
        qeth card structure, to check max. elems.

    :param struct sk_buff \*skb:
        SKB address

    :param int extra_elems:
        extra elems needed, to check against max.

.. _`qeth_l3_get_elements_no_tso.description`:

Description
-----------

Returns the number of pages, and thus QDIO buffer elements, needed to cover
skb data, including linear part and fragments, but excluding TCP header.
(Exclusion of TCP header distinguishes it from \ :c:func:`qeth_get_elements_no`\ .)
Checks if the result plus extra_elems fits under the limit for the card.
Returns 0 if it does not.

.. _`qeth_l3_get_elements_no_tso.note`:

Note
----

extra_elems is not included in the returned result.

.. This file was automatic generated / don't edit.

