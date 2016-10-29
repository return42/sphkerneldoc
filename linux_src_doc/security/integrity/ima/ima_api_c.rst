.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/integrity/ima/ima_api.c

.. _`ima_get_action`:

ima_get_action
==============

.. c:function:: int ima_get_action(struct inode *inode, int mask, enum ima_hooks func)

    appraise & measure decision based on policy.

    :param struct inode \*inode:
        pointer to inode to measure

    :param int mask:
        contains the permission mask (MAY_READ, MAY_WRITE, MAY_EXECUTE)

    :param enum ima_hooks func:
        caller identifier

.. _`ima_get_action.the-policy-is-defined-in-terms-of-keypairs`:

The policy is defined in terms of keypairs
------------------------------------------

subj=, obj=, type=, func=, mask=, fsmagic=
subj,obj, and type: are LSM specific.

.. _`ima_get_action.func`:

func
----

FILE_CHECK \| BPRM_CHECK \| MMAP_CHECK \| MODULE_CHECK

.. _`ima_get_action.mask`:

mask
----

contains the permission mask

.. _`ima_get_action.fsmagic`:

fsmagic
-------

hex value

Returns IMA_MEASURE, IMA_APPRAISE mask.

.. This file was automatic generated / don't edit.
