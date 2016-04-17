.. -*- coding: utf-8; mode: rst -*-

========
l_lock.c
========


.. _`lock_res_and_lock`:

lock_res_and_lock
=================

.. c:function:: struct ldlm_resource *lock_res_and_lock (struct ldlm_lock *lock)

    :param struct ldlm_lock \*lock:

        *undescribed*



.. _`lock_res_and_lock.description`:

Description
-----------


LDLM locking uses resource to serialize access to locks
but there is a case when we change resource of lock upon
enqueue reply. We rely on lock->l_resource = new_res
being an atomic operation.



.. _`unlock_res_and_lock`:

unlock_res_and_lock
===================

.. c:function:: void unlock_res_and_lock (struct ldlm_lock *lock)

    :param struct ldlm_lock \*lock:

        *undescribed*

