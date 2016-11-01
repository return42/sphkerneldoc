.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/integrity/ima/ima_main.c

.. _`ima_file_free`:

ima_file_free
=============

.. c:function:: void ima_file_free(struct file *file)

    called on \__fput()

    :param struct file \*file:
        pointer to file structure being freed

.. _`ima_file_free.description`:

Description
-----------

Flag files that changed, based on i_version

.. _`ima_file_mmap`:

ima_file_mmap
=============

.. c:function:: int ima_file_mmap(struct file *file, unsigned long prot)

    based on policy, collect/store measurement.

    :param struct file \*file:
        pointer to the file to be measured (May be NULL)

    :param unsigned long prot:
        contains the protection that will be applied by the kernel.

.. _`ima_file_mmap.description`:

Description
-----------

Measure files being mmapped executable based on the \ :c:func:`ima_must_measure`\ 
policy decision.

On success return 0.  On integrity appraisal error, assuming the file
is in policy and IMA-appraisal is in enforcing mode, return -EACCES.

.. _`ima_bprm_check`:

ima_bprm_check
==============

.. c:function:: int ima_bprm_check(struct linux_binprm *bprm)

    based on policy, collect/store measurement.

    :param struct linux_binprm \*bprm:
        contains the linux_binprm structure

.. _`ima_bprm_check.description`:

Description
-----------

The OS protects against an executable file, already open for write,
from being executed in \ :c:func:`deny_write_access`\  and an executable file,
already open for execute, from being modified in \ :c:func:`get_write_access`\ .
So we can be certain that what we verify and measure here is actually
what is being executed.

On success return 0.  On integrity appraisal error, assuming the file
is in policy and IMA-appraisal is in enforcing mode, return -EACCES.

.. _`ima_file_check`:

ima_file_check
==============

.. c:function:: int ima_file_check(struct file *file, int mask, int opened)

    based on policy, collect/store measurement.

    :param struct file \*file:
        pointer to the file to be measured

    :param int mask:
        contains MAY_READ, MAY_WRITE or MAY_EXECUTE

    :param int opened:
        *undescribed*

.. _`ima_file_check.description`:

Description
-----------

Measure files based on the \ :c:func:`ima_must_measure`\  policy decision.

On success return 0.  On integrity appraisal error, assuming the file
is in policy and IMA-appraisal is in enforcing mode, return -EACCES.

.. _`ima_post_path_mknod`:

ima_post_path_mknod
===================

.. c:function:: void ima_post_path_mknod(struct dentry *dentry)

    mark as a new inode

    :param struct dentry \*dentry:
        newly created dentry

.. _`ima_post_path_mknod.description`:

Description
-----------

Mark files created via the mknodat syscall as new, so that the
file data can be written later.

.. _`ima_read_file`:

ima_read_file
=============

.. c:function:: int ima_read_file(struct file *file, enum kernel_read_file_id read_id)

    pre-measure/appraise hook decision based on policy

    :param struct file \*file:
        pointer to the file to be measured/appraised/audit

    :param enum kernel_read_file_id read_id:
        caller identifier

.. _`ima_read_file.description`:

Description
-----------

Permit reading a file based on policy. The policy rules are written
in terms of the policy identifier.  Appraising the integrity of
a file requires a file descriptor.

For permission return 0, otherwise return -EACCES.

.. _`ima_post_read_file`:

ima_post_read_file
==================

.. c:function:: int ima_post_read_file(struct file *file, void *buf, loff_t size, enum kernel_read_file_id read_id)

    in memory collect/appraise/audit measurement

    :param struct file \*file:
        pointer to the file to be measured/appraised/audit

    :param void \*buf:
        pointer to in memory file contents

    :param loff_t size:
        size of in memory file contents

    :param enum kernel_read_file_id read_id:
        caller identifier

.. _`ima_post_read_file.description`:

Description
-----------

Measure/appraise/audit in memory file based on policy.  Policy rules
are written in terms of a policy identifier.

On success return 0.  On integrity appraisal error, assuming the file
is in policy and IMA-appraisal is in enforcing mode, return -EACCES.

.. This file was automatic generated / don't edit.

