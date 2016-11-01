.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/lightnvm/gennvm.c

.. _`gen_remove_tgt`:

gen_remove_tgt
==============

.. c:function:: int gen_remove_tgt(struct nvm_dev *dev, struct nvm_ioctl_remove *remove)

    Removes a target from the media manager

    :param struct nvm_dev \*dev:
        device

    :param struct nvm_ioctl_remove \*remove:
        ioctl structure with target name to remove.

.. _`gen_remove_tgt.return`:

Return
------

0: on success
1: on not found
<0: on error

.. This file was automatic generated / don't edit.

