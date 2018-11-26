.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/lightnvm/core.c

.. _`nvm_remove_tgt`:

nvm_remove_tgt
==============

.. c:function:: int nvm_remove_tgt(struct nvm_dev *dev, struct nvm_ioctl_remove *remove)

    Removes a target from the media manager

    :param dev:
        device
    :type dev: struct nvm_dev \*

    :param remove:
        ioctl structure with target name to remove.
    :type remove: struct nvm_ioctl_remove \*

.. _`nvm_remove_tgt.return`:

Return
------

0: on success
1: on not found
<0: on error

.. This file was automatic generated / don't edit.

