.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/csiostor/csio_rnode.c

.. _`csio_rnode_lookup_portid`:

csio_rnode_lookup_portid
========================

.. c:function:: struct csio_rnode *csio_rnode_lookup_portid(struct csio_lnode *ln, uint32_t portid)

    Finds the rnode with the given portid

    :param ln:
        lnode
    :type ln: struct csio_lnode \*

    :param portid:
        port id
    :type portid: uint32_t

.. _`csio_rnode_lookup_portid.description`:

Description
-----------

Lookup the rnode list for a given portid. If no matching entry
found, NULL is returned.

.. _`csio_rnode_fwevt_handler`:

csio_rnode_fwevt_handler
========================

.. c:function:: void csio_rnode_fwevt_handler(struct csio_rnode *rn, uint8_t fwevt)

    Event handler for firmware rnode events.

    :param rn:
        rnode
    :type rn: struct csio_rnode \*

    :param fwevt:
        *undescribed*
    :type fwevt: uint8_t

.. This file was automatic generated / don't edit.

