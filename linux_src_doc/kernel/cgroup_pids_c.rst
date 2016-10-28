.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/cgroup_pids.c

.. _`pids_cancel`:

pids_cancel
===========

.. c:function:: void pids_cancel(struct pids_cgroup *pids, int num)

    uncharge the local pid count

    :param struct pids_cgroup \*pids:
        the pid cgroup state

    :param int num:
        the number of pids to cancel

.. _`pids_cancel.description`:

Description
-----------

This function will WARN if the pid count goes under 0, because such a case is
a bug in the pids controller proper.

.. _`pids_uncharge`:

pids_uncharge
=============

.. c:function:: void pids_uncharge(struct pids_cgroup *pids, int num)

    hierarchically uncharge the pid count

    :param struct pids_cgroup \*pids:
        the pid cgroup state

    :param int num:
        the number of pids to uncharge

.. _`pids_charge`:

pids_charge
===========

.. c:function:: void pids_charge(struct pids_cgroup *pids, int num)

    hierarchically charge the pid count

    :param struct pids_cgroup \*pids:
        the pid cgroup state

    :param int num:
        the number of pids to charge

.. _`pids_charge.description`:

Description
-----------

This function does \*not\* follow the pid limit set. It cannot fail and the new
pid count may exceed the limit. This is only used for reverting failed
attaches, where there is no other way out than violating the limit.

.. _`pids_try_charge`:

pids_try_charge
===============

.. c:function:: int pids_try_charge(struct pids_cgroup *pids, int num)

    hierarchically try to charge the pid count

    :param struct pids_cgroup \*pids:
        the pid cgroup state

    :param int num:
        the number of pids to charge

.. _`pids_try_charge.description`:

Description
-----------

This function follows the set limit. It will fail if the charge would cause
the new value to exceed the hierarchical limit. Returns 0 if the charge
succeeded, otherwise -EAGAIN.

.. This file was automatic generated / don't edit.

