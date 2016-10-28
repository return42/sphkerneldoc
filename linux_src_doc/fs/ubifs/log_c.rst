.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ubifs/log.c

.. _`ubifs_search_bud`:

ubifs_search_bud
================

.. c:function:: struct ubifs_bud *ubifs_search_bud(struct ubifs_info *c, int lnum)

    search bud LEB.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int lnum:
        logical eraseblock number to search

.. _`ubifs_search_bud.description`:

Description
-----------

This function searches bud LEB \ ``lnum``\ . Returns bud description object in case
of success and \ ``NULL``\  if there is no bud with this LEB number.

.. _`ubifs_get_wbuf`:

ubifs_get_wbuf
==============

.. c:function:: struct ubifs_wbuf *ubifs_get_wbuf(struct ubifs_info *c, int lnum)

    get the wbuf associated with a LEB, if there is one.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int lnum:
        logical eraseblock number to search

.. _`ubifs_get_wbuf.description`:

Description
-----------

This functions returns the wbuf for \ ``lnum``\  or \ ``NULL``\  if there is not one.

.. _`empty_log_bytes`:

empty_log_bytes
===============

.. c:function:: long long empty_log_bytes(const struct ubifs_info *c)

    calculate amount of empty space in the log.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

.. _`ubifs_add_bud`:

ubifs_add_bud
=============

.. c:function:: void ubifs_add_bud(struct ubifs_info *c, struct ubifs_bud *bud)

    add bud LEB to the tree of buds and its journal head list.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_bud \*bud:
        the bud to add

.. _`ubifs_add_bud_to_log`:

ubifs_add_bud_to_log
====================

.. c:function:: int ubifs_add_bud_to_log(struct ubifs_info *c, int jhead, int lnum, int offs)

    add a new bud to the log.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int jhead:
        journal head the bud belongs to

    :param int lnum:
        LEB number of the bud

    :param int offs:
        starting offset of the bud

.. _`ubifs_add_bud_to_log.description`:

Description
-----------

This function writes reference node for the new bud LEB \ ``lnum``\  it to the log,
and adds it to the buds tress. It also makes sure that log size does not
exceed the 'c->max_bud_bytes' limit. Returns zero in case of success,
\ ``-EAGAIN``\  if commit is required, and a negative error codes in case of
failure.

.. _`remove_buds`:

remove_buds
===========

.. c:function:: void remove_buds(struct ubifs_info *c)

    remove used buds.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`remove_buds.description`:

Description
-----------

This function removes use buds from the buds tree. It does not remove the
buds which are pointed to by journal heads.

.. _`ubifs_log_start_commit`:

ubifs_log_start_commit
======================

.. c:function:: int ubifs_log_start_commit(struct ubifs_info *c, int *ltail_lnum)

    start commit.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int \*ltail_lnum:
        return new log tail LEB number

.. _`ubifs_log_start_commit.description`:

Description
-----------

The commit operation starts with writing "commit start" node to the log and
reference nodes for all journal heads which will define new journal after
the commit has been finished. The commit start and reference nodes are
written in one go to the nearest empty log LEB (hence, when commit is
finished UBIFS may safely unmap all the previous log LEBs). This function
returns zero in case of success and a negative error code in case of
failure.

.. _`ubifs_log_end_commit`:

ubifs_log_end_commit
====================

.. c:function:: int ubifs_log_end_commit(struct ubifs_info *c, int ltail_lnum)

    end commit.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int ltail_lnum:
        new log tail LEB number

.. _`ubifs_log_end_commit.description`:

Description
-----------

This function is called on when the commit operation was finished. It
moves log tail to new position and updates the master node so that it stores
the new log tail LEB number. Returns zero in case of success and a negative
error code in case of failure.

.. _`ubifs_log_post_commit`:

ubifs_log_post_commit
=====================

.. c:function:: int ubifs_log_post_commit(struct ubifs_info *c, int old_ltail_lnum)

    things to do after commit is completed.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int old_ltail_lnum:
        old log tail LEB number

.. _`ubifs_log_post_commit.description`:

Description
-----------

Release buds only after commit is completed, because they must be unchanged
if recovery is needed.

Unmap log LEBs only after commit is completed, because they may be needed for
recovery.

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`done_ref`:

struct done_ref
===============

.. c:type:: struct done_ref

    references that have been done.

.. _`done_ref.definition`:

Definition
----------

.. code-block:: c

    struct done_ref {
        struct rb_node rb;
        int lnum;
    }

.. _`done_ref.members`:

Members
-------

rb
    rb-tree node

lnum
    LEB number

.. _`done_already`:

done_already
============

.. c:function:: int done_already(struct rb_root *done_tree, int lnum)

    determine if a reference has been done already.

    :param struct rb_root \*done_tree:
        rb-tree to store references that have been done

    :param int lnum:
        LEB number of reference

.. _`done_already.description`:

Description
-----------

This function returns \ ``1``\  if the reference has been done, \ ``0``\  if not, otherwise
a negative error code is returned.

.. _`destroy_done_tree`:

destroy_done_tree
=================

.. c:function:: void destroy_done_tree(struct rb_root *done_tree)

    destroy the done tree.

    :param struct rb_root \*done_tree:
        done tree to destroy

.. _`add_node`:

add_node
========

.. c:function:: int add_node(struct ubifs_info *c, void *buf, int *lnum, int *offs, void *node)

    add a node to the consolidated log.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param void \*buf:
        buffer to which to add

    :param int \*lnum:
        LEB number to which to write is passed and returned here

    :param int \*offs:
        offset to where to write is passed and returned here

    :param void \*node:
        node to add

.. _`add_node.description`:

Description
-----------

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`ubifs_consolidate_log`:

ubifs_consolidate_log
=====================

.. c:function:: int ubifs_consolidate_log(struct ubifs_info *c)

    consolidate the log.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`ubifs_consolidate_log.description`:

Description
-----------

Repeated failed commits could cause the log to be full, but at least 1 LEB is
needed for commit. This function rewrites the reference nodes in the log
omitting duplicates, and failed CS nodes, and leaving no gaps.

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`dbg_check_bud_bytes`:

dbg_check_bud_bytes
===================

.. c:function:: int dbg_check_bud_bytes(struct ubifs_info *c)

    make sure bud bytes calculation are all right.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`dbg_check_bud_bytes.description`:

Description
-----------

This function makes sure the amount of flash space used by closed buds
('c->bud_bytes' is correct). Returns zero in case of success and \ ``-EINVAL``\  in
case of failure.

.. This file was automatic generated / don't edit.

