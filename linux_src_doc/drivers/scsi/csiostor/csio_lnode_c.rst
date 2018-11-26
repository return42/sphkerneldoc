.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/csiostor/csio_lnode.c

.. _`csio_lnode_lookup_by_wwpn`:

csio_lnode_lookup_by_wwpn
=========================

.. c:function:: struct csio_lnode *csio_lnode_lookup_by_wwpn(struct csio_hw *hw, uint8_t *wwpn)

    Lookup lnode using given wwpn.

    :param hw:
        HW module.
    :type hw: struct csio_hw \*

    :param wwpn:
        WWPN.
    :type wwpn: uint8_t \*

.. _`csio_lnode_lookup_by_wwpn.description`:

Description
-----------

If found, returns lnode matching given wwpn, returns NULL otherwise.

.. _`csio_ln_fdmi_start`:

csio_ln_fdmi_start
==================

.. c:function:: int csio_ln_fdmi_start(struct csio_lnode *ln, void *context)

    Start an FDMI request.

    :param ln:
        lnode
    :type ln: struct csio_lnode \*

    :param context:
        session context
    :type context: void \*

.. _`csio_ln_fdmi_start.description`:

Description
-----------

Issued with lock held.

.. _`csio_fcoe_fwevt_handler`:

csio_fcoe_fwevt_handler
=======================

.. c:function:: void csio_fcoe_fwevt_handler(struct csio_hw *hw, __u8 cpl_op, __be64 *cmd)

    Event handler for Firmware FCoE events.

    :param hw:
        HW module
    :type hw: struct csio_hw \*

    :param cpl_op:
        CPL opcode
    :type cpl_op: __u8

    :param cmd:
        FW cmd/WR.
    :type cmd: __be64 \*

.. _`csio_fcoe_fwevt_handler.description`:

Description
-----------

Process received FCoE cmd/WR event from FW.

.. _`csio_lnode_start`:

csio_lnode_start
================

.. c:function:: int csio_lnode_start(struct csio_lnode *ln)

    Kickstart lnode discovery.

    :param ln:
        lnode
    :type ln: struct csio_lnode \*

.. _`csio_lnode_start.description`:

Description
-----------

This routine kickstarts the discovery by issuing an FCOE_LINK (up) command.

.. _`csio_lnode_stop`:

csio_lnode_stop
===============

.. c:function:: void csio_lnode_stop(struct csio_lnode *ln)

    Stop the lnode.

    :param ln:
        lnode
    :type ln: struct csio_lnode \*

.. _`csio_lnode_stop.description`:

Description
-----------

This routine is invoked by HW module to stop lnode and its associated NPIV
lnodes.

.. _`csio_lnode_close`:

csio_lnode_close
================

.. c:function:: void csio_lnode_close(struct csio_lnode *ln)

    Close an lnode.

    :param ln:
        lnode
    :type ln: struct csio_lnode \*

.. _`csio_lnode_close.description`:

Description
-----------

This routine is invoked by HW module to close an lnode and its
associated NPIV lnodes. Lnode and its associated NPIV lnodes are
set to uninitialized state.

.. _`csio_lnode_init`:

csio_lnode_init
===============

.. c:function:: int csio_lnode_init(struct csio_lnode *ln, struct csio_hw *hw, struct csio_lnode *pln)

    Initialize the members of an lnode.

    :param ln:
        lnode
    :type ln: struct csio_lnode \*

    :param hw:
        *undescribed*
    :type hw: struct csio_hw \*

    :param pln:
        *undescribed*
    :type pln: struct csio_lnode \*

.. _`csio_lnode_exit`:

csio_lnode_exit
===============

.. c:function:: void csio_lnode_exit(struct csio_lnode *ln)

    De-instantiate an lnode.

    :param ln:
        lnode
    :type ln: struct csio_lnode \*

.. This file was automatic generated / don't edit.

