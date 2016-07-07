.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/kernel/vdso.c

.. _`update_vsyscall`:

update_vsyscall
===============

.. c:function:: void update_vsyscall(struct timekeeper *tk)

    update the vdso data page

    :param struct timekeeper \*tk:
        *undescribed*

.. _`update_vsyscall.description`:

Description
-----------

Increment the sequence counter, making it odd, indicating to
userspace that an update is in progress.  Update the fields used
for coarse clocks and, if the architected system timer is in use,
the fields used for high precision clocks.  Increment the sequence
counter again, making it even, indicating to userspace that the
update is finished.

Userspace is expected to sample seq_count before reading any other
fields from the data page.  If seq_count is odd, userspace is
expected to wait until it becomes even.  After copying data from
the page, userspace must sample seq_count again; if it has changed
from its previous value, userspace must retry the whole sequence.

Calls to update_vsyscall are serialized by the timekeeping core.

.. This file was automatic generated / don't edit.

