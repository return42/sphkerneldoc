.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/rtnetlink.h

.. _`rcu_dereference_rtnl`:

rcu_dereference_rtnl
====================

.. c:function::  rcu_dereference_rtnl( p)

    rcu_dereference with debug checking

    :param p:
        The pointer to read, prior to dereferencing
    :type p: 

.. _`rcu_dereference_rtnl.description`:

Description
-----------

Do an rcu_dereference(p), but check caller either holds \ :c:func:`rcu_read_lock`\ 
or RTNL. Note : Please prefer \ :c:func:`rtnl_dereference`\  or \ :c:func:`rcu_dereference`\ 

.. _`rcu_dereference_bh_rtnl`:

rcu_dereference_bh_rtnl
=======================

.. c:function::  rcu_dereference_bh_rtnl( p)

    rcu_dereference_bh with debug checking

    :param p:
        The pointer to read, prior to dereference
    :type p: 

.. _`rcu_dereference_bh_rtnl.description`:

Description
-----------

Do an rcu_dereference_bh(p), but check caller either holds \ :c:func:`rcu_read_lock_bh`\ 
or RTNL. Note : Please prefer \ :c:func:`rtnl_dereference`\  or \ :c:func:`rcu_dereference_bh`\ 

.. _`rtnl_dereference`:

rtnl_dereference
================

.. c:function::  rtnl_dereference( p)

    fetch RCU pointer when updates are prevented by RTNL

    :param p:
        The pointer to read, prior to dereferencing
    :type p: 

.. _`rtnl_dereference.description`:

Description
-----------

Return the value of the specified RCU-protected pointer, but omit
the \ :c:func:`READ_ONCE`\ , because caller holds RTNL.

.. This file was automatic generated / don't edit.

