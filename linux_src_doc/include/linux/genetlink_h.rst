.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/genetlink.h

.. _`rcu_dereference_genl`:

rcu_dereference_genl
====================

.. c:function::  rcu_dereference_genl( p)

    rcu_dereference with debug checking

    :param p:
        The pointer to read, prior to dereferencing
    :type p: 

.. _`rcu_dereference_genl.description`:

Description
-----------

Do an rcu_dereference(p), but check caller either holds \ :c:func:`rcu_read_lock`\ 
or genl mutex. Note : Please prefer \ :c:func:`genl_dereference`\  or \ :c:func:`rcu_dereference`\ 

.. _`genl_dereference`:

genl_dereference
================

.. c:function::  genl_dereference( p)

    fetch RCU pointer when updates are prevented by genl mutex

    :param p:
        The pointer to read, prior to dereferencing
    :type p: 

.. _`genl_dereference.description`:

Description
-----------

Return the value of the specified RCU-protected pointer, but omit
the \ :c:func:`READ_ONCE`\ , because caller holds genl mutex.

.. This file was automatic generated / don't edit.

