.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/integrity/ima/ima_api.c

.. _`ima_get_action`:

ima_get_action
==============

.. c:function:: int ima_get_action(struct inode *inode, const struct cred *cred, u32 secid, int mask, enum ima_hooks func, int *pcr)

    appraise & measure decision based on policy.

    :param inode:
        pointer to inode to measure
    :type inode: struct inode \*

    :param cred:
        pointer to credentials structure to validate
    :type cred: const struct cred \*

    :param secid:
        secid of the task being validated
    :type secid: u32

    :param mask:
        contains the permission mask (MAY_READ, MAY_WRITE, MAY_EXEC,
        MAY_APPEND)
    :type mask: int

    :param func:
        caller identifier
    :type func: enum ima_hooks

    :param pcr:
        pointer filled in if matched measure policy sets pcr=
    :type pcr: int \*

.. _`ima_get_action.the-policy-is-defined-in-terms-of-keypairs`:

The policy is defined in terms of keypairs
------------------------------------------

subj=, obj=, type=, func=, mask=, fsmagic=
subj,obj, and type: are LSM specific.

.. _`ima_get_action.func`:

func
----

FILE_CHECK \| BPRM_CHECK \| CREDS_CHECK \| MMAP_CHECK \| MODULE_CHECK

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

