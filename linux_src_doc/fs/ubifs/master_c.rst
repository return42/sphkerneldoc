.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ubifs/master.c

.. _`ubifs_compare_master_node`:

ubifs_compare_master_node
=========================

.. c:function:: int ubifs_compare_master_node(struct ubifs_info *c, void *m1, void *m2)

    compare two UBIFS master nodes

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param m1:
        the first node
    :type m1: void \*

    :param m2:
        the second node
    :type m2: void \*

.. _`ubifs_compare_master_node.description`:

Description
-----------

This function compares two UBIFS master nodes. Returns 0 if they are equal
and nonzero if not.

.. _`scan_for_master`:

scan_for_master
===============

.. c:function:: int scan_for_master(struct ubifs_info *c)

    search the valid master node.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`scan_for_master.description`:

Description
-----------

This function scans the master node LEBs and search for the latest master
node. Returns zero in case of success, \ ``-EUCLEAN``\  if there master area is
corrupted and requires recovery, and a negative error code in case of
failure.

.. _`validate_master`:

validate_master
===============

.. c:function:: int validate_master(const struct ubifs_info *c)

    validate master node.

    :param c:
        UBIFS file-system description object
    :type c: const struct ubifs_info \*

.. _`validate_master.description`:

Description
-----------

This function validates data which was read from master node. Returns zero
if the data is all right and \ ``-EINVAL``\  if not.

.. _`ubifs_read_master`:

ubifs_read_master
=================

.. c:function:: int ubifs_read_master(struct ubifs_info *c)

    read master node.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`ubifs_read_master.description`:

Description
-----------

This function finds and reads the master node during file-system mount. If
the flash is empty, it creates default master node as well. Returns zero in
case of success and a negative error code in case of failure.

.. _`ubifs_write_master`:

ubifs_write_master
==================

.. c:function:: int ubifs_write_master(struct ubifs_info *c)

    write master node.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`ubifs_write_master.description`:

Description
-----------

This function writes the master node. Returns zero in case of success and a
negative error code in case of failure. The master node is written twice to
enable recovery.

.. This file was automatic generated / don't edit.

