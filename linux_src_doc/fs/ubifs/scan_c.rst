.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ubifs/scan.c

.. _`scan_padding_bytes`:

scan_padding_bytes
==================

.. c:function:: int scan_padding_bytes(void *buf, int len)

    scan for padding bytes.

    :param buf:
        buffer to scan
    :type buf: void \*

    :param len:
        length of buffer
    :type len: int

.. _`scan_padding_bytes.description`:

Description
-----------

This function returns the number of padding bytes on success and
\ ``SCANNED_GARBAGE``\  on failure.

.. _`ubifs_scan_a_node`:

ubifs_scan_a_node
=================

.. c:function:: int ubifs_scan_a_node(const struct ubifs_info *c, void *buf, int len, int lnum, int offs, int quiet)

    scan for a node or padding.

    :param c:
        UBIFS file-system description object
    :type c: const struct ubifs_info \*

    :param buf:
        buffer to scan
    :type buf: void \*

    :param len:
        length of buffer
    :type len: int

    :param lnum:
        logical eraseblock number
    :type lnum: int

    :param offs:
        offset within the logical eraseblock
    :type offs: int

    :param quiet:
        print no messages
    :type quiet: int

.. _`ubifs_scan_a_node.description`:

Description
-----------

This function returns a scanning code to indicate what was scanned.

.. _`ubifs_start_scan`:

ubifs_start_scan
================

.. c:function:: struct ubifs_scan_leb *ubifs_start_scan(const struct ubifs_info *c, int lnum, int offs, void *sbuf)

    create LEB scanning information at start of scan.

    :param c:
        UBIFS file-system description object
    :type c: const struct ubifs_info \*

    :param lnum:
        logical eraseblock number
    :type lnum: int

    :param offs:
        offset to start at (usually zero)
    :type offs: int

    :param sbuf:
        scan buffer (must be c->leb_size)
    :type sbuf: void \*

.. _`ubifs_start_scan.description`:

Description
-----------

This function returns the scanned information on success and a negative error
code on failure.

.. _`ubifs_end_scan`:

ubifs_end_scan
==============

.. c:function:: void ubifs_end_scan(const struct ubifs_info *c, struct ubifs_scan_leb *sleb, int lnum, int offs)

    update LEB scanning information at end of scan.

    :param c:
        UBIFS file-system description object
    :type c: const struct ubifs_info \*

    :param sleb:
        scanning information
    :type sleb: struct ubifs_scan_leb \*

    :param lnum:
        logical eraseblock number
    :type lnum: int

    :param offs:
        offset to start at (usually zero)
    :type offs: int

.. _`ubifs_add_snod`:

ubifs_add_snod
==============

.. c:function:: int ubifs_add_snod(const struct ubifs_info *c, struct ubifs_scan_leb *sleb, void *buf, int offs)

    add a scanned node to LEB scanning information.

    :param c:
        UBIFS file-system description object
    :type c: const struct ubifs_info \*

    :param sleb:
        scanning information
    :type sleb: struct ubifs_scan_leb \*

    :param buf:
        buffer containing node
    :type buf: void \*

    :param offs:
        offset of node on flash
    :type offs: int

.. _`ubifs_add_snod.description`:

Description
-----------

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`ubifs_scanned_corruption`:

ubifs_scanned_corruption
========================

.. c:function:: void ubifs_scanned_corruption(const struct ubifs_info *c, int lnum, int offs, void *buf)

    print information after UBIFS scanned corruption.

    :param c:
        UBIFS file-system description object
    :type c: const struct ubifs_info \*

    :param lnum:
        LEB number of corruption
    :type lnum: int

    :param offs:
        offset of corruption
    :type offs: int

    :param buf:
        buffer containing corruption
    :type buf: void \*

.. _`ubifs_scan`:

ubifs_scan
==========

.. c:function:: struct ubifs_scan_leb *ubifs_scan(const struct ubifs_info *c, int lnum, int offs, void *sbuf, int quiet)

    scan a logical eraseblock.

    :param c:
        UBIFS file-system description object
    :type c: const struct ubifs_info \*

    :param lnum:
        logical eraseblock number
    :type lnum: int

    :param offs:
        offset to start at (usually zero)
    :type offs: int

    :param sbuf:
        scan buffer (must be of \ ``c->leb_size``\  bytes in size)
    :type sbuf: void \*

    :param quiet:
        print no messages
    :type quiet: int

.. _`ubifs_scan.description`:

Description
-----------

This function scans LEB number \ ``lnum``\  and returns complete information about
its contents. Returns the scanned information in case of success and,
\ ``-EUCLEAN``\  if the LEB neads recovery, and other negative error codes in case
of failure.

If \ ``quiet``\  is non-zero, this function does not print large and scary
error messages and flash dumps in case of errors.

.. _`ubifs_scan_destroy`:

ubifs_scan_destroy
==================

.. c:function:: void ubifs_scan_destroy(struct ubifs_scan_leb *sleb)

    destroy LEB scanning information.

    :param sleb:
        scanning information to free
    :type sleb: struct ubifs_scan_leb \*

.. This file was automatic generated / don't edit.

