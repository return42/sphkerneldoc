.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/selinux/ss/ebitmap.c

.. _`ebitmap_netlbl_export`:

ebitmap_netlbl_export
=====================

.. c:function:: int ebitmap_netlbl_export(struct ebitmap *ebmap, struct netlbl_lsm_catmap **catmap)

    Export an ebitmap into a NetLabel category bitmap

    :param ebmap:
        the ebitmap to export
    :type ebmap: struct ebitmap \*

    :param catmap:
        the NetLabel category bitmap
    :type catmap: struct netlbl_lsm_catmap \*\*

.. _`ebitmap_netlbl_export.description`:

Description
-----------

Export a SELinux extensibile bitmap into a NetLabel category bitmap.
Returns zero on success, negative values on error.

.. _`ebitmap_netlbl_import`:

ebitmap_netlbl_import
=====================

.. c:function:: int ebitmap_netlbl_import(struct ebitmap *ebmap, struct netlbl_lsm_catmap *catmap)

    Import a NetLabel category bitmap into an ebitmap

    :param ebmap:
        the ebitmap to import
    :type ebmap: struct ebitmap \*

    :param catmap:
        the NetLabel category bitmap
    :type catmap: struct netlbl_lsm_catmap \*

.. _`ebitmap_netlbl_import.description`:

Description
-----------

Import a NetLabel category bitmap into a SELinux extensibile bitmap.
Returns zero on success, negative values on error.

.. This file was automatic generated / don't edit.

