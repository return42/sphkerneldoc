.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/cred.h

.. _`get_group_info`:

get_group_info
==============

.. c:function:: struct group_info *get_group_info(struct group_info *gi)

    Get a reference to a group info structure

    :param gi:
        *undescribed*
    :type gi: struct group_info \*

.. _`get_group_info.description`:

Description
-----------

This gets a reference to a set of supplementary groups.

If the caller is accessing a task's credentials, they must hold the RCU read
lock when reading.

.. _`put_group_info`:

put_group_info
==============

.. c:function::  put_group_info( group_info)

    Release a reference to a group info structure

    :param group_info:
        The group info to release
    :type group_info: 

.. _`get_new_cred`:

get_new_cred
============

.. c:function:: struct cred *get_new_cred(struct cred *cred)

    Get a reference on a new set of credentials

    :param cred:
        The new credentials to reference
    :type cred: struct cred \*

.. _`get_new_cred.description`:

Description
-----------

Get a reference on the specified set of new credentials.  The caller must
release the reference.

.. _`get_cred`:

get_cred
========

.. c:function:: const struct cred *get_cred(const struct cred *cred)

    Get a reference on a set of credentials

    :param cred:
        The credentials to reference
    :type cred: const struct cred \*

.. _`get_cred.description`:

Description
-----------

Get a reference on the specified set of credentials.  The caller must
release the reference.

This is used to deal with a committed set of credentials.  Although the
pointer is const, this will temporarily discard the const and increment the
usage count.  The purpose of this is to attempt to catch at compile time the
accidental alteration of a set of credentials that should be considered
immutable.

.. _`put_cred`:

put_cred
========

.. c:function:: void put_cred(const struct cred *_cred)

    Release a reference to a set of credentials

    :param _cred:
        *undescribed*
    :type _cred: const struct cred \*

.. _`put_cred.description`:

Description
-----------

Release a reference to a set of credentials, deleting them when the last ref
is released.

This takes a const pointer to a set of credentials because the credentials
on task_struct are attached by const pointers to prevent accidental
alteration of otherwise immutable credential sets.

.. _`current_cred`:

current_cred
============

.. c:function::  current_cred( void)

    Access the current task's subjective credentials

    :param void:
        no arguments
    :type void: 

.. _`current_cred.description`:

Description
-----------

Access the subjective credentials of the current task.  RCU-safe,
since nobody else can modify it.

.. _`current_real_cred`:

current_real_cred
=================

.. c:function::  current_real_cred( void)

    Access the current task's objective credentials

    :param void:
        no arguments
    :type void: 

.. _`current_real_cred.description`:

Description
-----------

Access the objective credentials of the current task.  RCU-safe,
since nobody else can modify it.

.. _`__task_cred`:

\__task_cred
============

.. c:function::  __task_cred( task)

    Access a task's objective credentials

    :param task:
        The task to query
    :type task: 

.. _`__task_cred.description`:

Description
-----------

Access the objective credentials of a task.  The caller must hold the RCU
readlock.

The result of this function should not be passed directly to \ :c:func:`get_cred`\ ;
rather \ :c:func:`get_task_cred`\  should be used instead.

.. _`get_current_cred`:

get_current_cred
================

.. c:function::  get_current_cred( void)

    Get the current task's subjective credentials

    :param void:
        no arguments
    :type void: 

.. _`get_current_cred.description`:

Description
-----------

Get the subjective credentials of the current task, pinning them so that
they can't go away.  Accessing the current task's credentials directly is
not permitted.

.. _`get_current_user`:

get_current_user
================

.. c:function::  get_current_user( void)

    Get the current task's user_struct

    :param void:
        no arguments
    :type void: 

.. _`get_current_user.description`:

Description
-----------

Get the user record of the current task, pinning it so that it can't go
away.

.. _`get_current_groups`:

get_current_groups
==================

.. c:function::  get_current_groups( void)

    Get the current task's supplementary group list

    :param void:
        no arguments
    :type void: 

.. _`get_current_groups.description`:

Description
-----------

Get the supplementary group list of the current task, pinning it so that it
can't go away.

.. This file was automatic generated / don't edit.

