.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/freezer.h

.. _`freezer_do_not_count`:

freezer_do_not_count
====================

.. c:function:: void freezer_do_not_count( void)

    tell freezer to ignore \ ``current``\ 

    :param  void:
        no arguments

.. _`freezer_do_not_count.description`:

Description
-----------

Tell freezers to ignore the current task when determining whether the
target frozen state is reached.  IOW, the current task will be
considered frozen enough by freezers.

The caller shouldn't do anything which isn't allowed for a frozen task
until \ :c:func:`freezer_cont`\  is called.  Usually, freezer[_do_not]_count() pair
wrap a scheduling operation and nothing much else.

.. _`freezer_count`:

freezer_count
=============

.. c:function:: void freezer_count( void)

    tell freezer to stop ignoring \ ``current``\ 

    :param  void:
        no arguments

.. _`freezer_count.description`:

Description
-----------

Undo \ :c:func:`freezer_do_not_count`\ .  It tells freezers that \ ``current``\  should be
considered again and tries to freeze if freezing condition is already in
effect.

.. _`freezer_should_skip`:

freezer_should_skip
===================

.. c:function:: bool freezer_should_skip(struct task_struct *p)

    whether to skip a task when determining frozen state is reached

    :param struct task_struct \*p:
        task in quesion

.. _`freezer_should_skip.description`:

Description
-----------

This function is used by freezers after establishing \ ``true``\  \ :c:func:`freezing`\  to
test whether a task should be skipped when determining the target frozen
state is reached.  IOW, if this function returns \ ``true``\ , \ ``p``\  is considered
frozen enough.

.. This file was automatic generated / don't edit.

