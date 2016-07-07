.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/llc/llc_core.c

.. _`llc_sap_alloc`:

llc_sap_alloc
=============

.. c:function:: struct llc_sap *llc_sap_alloc( void)

    allocates and initializes sap.

    :param  void:
        no arguments

.. _`llc_sap_alloc.description`:

Description
-----------

Allocates and initializes sap.

.. _`llc_sap_find`:

llc_sap_find
============

.. c:function:: struct llc_sap *llc_sap_find(unsigned char sap_value)

    searchs a SAP in station

    :param unsigned char sap_value:
        sap to be found

.. _`llc_sap_find.description`:

Description
-----------

Searchs for a sap in the sap list of the LLC's station upon the sap ID.
If the sap is found it will be refcounted and the user will have to do
a llc_sap_put after use.
Returns the sap or \ ``NULL``\  if not found.

.. _`llc_sap_open`:

llc_sap_open
============

.. c:function:: struct llc_sap *llc_sap_open(unsigned char lsap, int (*) func (struct sk_buff *skb, struct net_device *dev, struct packet_type *pt, struct net_device *orig_dev)

    open interface to the upper layers.

    :param unsigned char lsap:
        SAP number.

    :param (int (\*) func (struct sk_buff \*skb, struct net_device \*dev, struct packet_type \*pt, struct net_device \*orig_dev):
        rcv func for datalink protos

.. _`llc_sap_open.description`:

Description
-----------

Interface function to upper layer. Each one who wants to get a SAP
(for example NetBEUI) should call this function. Returns the opened
SAP for success, NULL for failure.

.. _`llc_sap_close`:

llc_sap_close
=============

.. c:function:: void llc_sap_close(struct llc_sap *sap)

    close interface for upper layers.

    :param struct llc_sap \*sap:
        SAP to be closed.

.. _`llc_sap_close.description`:

Description
-----------

Close interface function to upper layer. Each one who wants to
close an open SAP (for example NetBEUI) should call this function.
Removes this sap from the list of saps in the station and then
frees the memory for this sap.

.. This file was automatic generated / don't edit.

