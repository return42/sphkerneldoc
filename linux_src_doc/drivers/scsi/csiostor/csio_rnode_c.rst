.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/csiostor/csio_rnode.c

.. _`csio_rnode_lookup_portid`:

csio_rnode_lookup_portid
========================

.. c:function:: struct csio_rnode *csio_rnode_lookup_portid(struct csio_lnode *ln, uint32_t portid)

    Finds the rnode with the given portid

    :param struct csio_lnode \*ln:
        lnode

    :param uint32_t portid:
        port id

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

    :param struct csio_rnode \*rn:
        rnode

    :param uint8_t fwevt:
        *undescribed*

.. This file was automatic generated / don't edit.

