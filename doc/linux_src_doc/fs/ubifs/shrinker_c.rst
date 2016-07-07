.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ubifs/shrinker.c

.. _`shrink_tnc`:

shrink_tnc
==========

.. c:function:: int shrink_tnc(struct ubifs_info *c, int nr, int age, int *contention)

    shrink TNC tree.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int nr:
        number of znodes to free

    :param int age:
        the age of znodes to free

    :param int \*contention:
        if any contention, this is set to \ ``1``\ 

.. _`shrink_tnc.description`:

Description
-----------

This function traverses TNC tree and frees clean znodes. It does not free
clean znodes which younger then \ ``age``\ . Returns number of freed znodes.

.. _`shrink_tnc_trees`:

shrink_tnc_trees
================

.. c:function:: int shrink_tnc_trees(int nr, int age, int *contention)

    shrink UBIFS TNC trees.

    :param int nr:
        number of znodes to free

    :param int age:
        the age of znodes to free

    :param int \*contention:
        if any contention, this is set to \ ``1``\ 

.. _`shrink_tnc_trees.description`:

Description
-----------

This function walks the list of mounted UBIFS file-systems and frees clean
znodes which are older than \ ``age``\ , until at least \ ``nr``\  znodes are freed.
Returns the number of freed znodes.

.. _`kick_a_thread`:

kick_a_thread
=============

.. c:function:: int kick_a_thread( void)

    kick a background thread to start commit.

    :param  void:
        no arguments

.. _`kick_a_thread.description`:

Description
-----------

This function kicks a background thread to start background commit. Returns
\ ``-1``\  if a thread was kicked or there is another reason to assume the memory
will soon be freed or become freeable. If there are no dirty znodes, returns
\ ``0``\ .

.. This file was automatic generated / don't edit.

