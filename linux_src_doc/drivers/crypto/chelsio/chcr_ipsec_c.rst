.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/chelsio/chcr_ipsec.c

.. _`flits_to_desc`:

flits_to_desc
=============

.. c:function:: unsigned int flits_to_desc(unsigned int n)

    returns the num of Tx descriptors for the given flits

    :param n:
        the number of flits
    :type n: unsigned int

.. _`flits_to_desc.description`:

Description
-----------

Returns the number of Tx descriptors needed for the supplied number
of flits.

.. This file was automatic generated / don't edit.

